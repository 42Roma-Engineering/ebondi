from utils import *

def init_data():
	dataset_path = "./Datasets/rawData"
	dataset_names = list(os.listdir(dataset_path))
	print('--- datasets states ---')
	print(dataset_names, end='\n\n')


	## opening files
	datasets = dict()

	columns = ["E1", "E2", "E3", "E4", "E5", "E6", "P1", "P2", "P3", "P4", "P5", "P6", "LOG", "TIMESTAMP", "CICLO"]

	for dataset_name in dataset_names:

		path = dataset_path + "/" + dataset_name + "/"

		datasets[dataset_name] = [ pd.read_csv(path + d, sep=";", names=columns)   for d in os.listdir(path) if d.endswith(".csv") ]
	
	print('--- checking datasets len ---')
	for k, v in datasets.items():
		print(f"dataset: {k}, num files: {len(v)}, tot_len: {sum(len(ds) for ds in v)}")
	print('')

	## changing names...
	datasets["oil"] = datasets.pop("Oil leakage")
	datasets["dry"] = datasets.pop("dryBearing")
	datasets["nop"] = datasets.pop("noPayload")

	print('--- datasets with new names ---')
	print(datasets.keys(), end='\n\n')


	## transform to datetime
	for k, df_list in datasets.items():
		for df in df_list:
			df["TIMESTAMP"] = pd.to_datetime(df["TIMESTAMP"])
	
	## concat dataset + FILL missing TIMESTAMP
	dt = pd.Timedelta(milliseconds=2)

	print ('--- len before and after resample to 2 ms frequency ---')
	for k, v in datasets.items():

		if k == "test":
			continue ## ram crash

		datasets[k] = pd.concat(datasets[k], ignore_index = True)

		datasets[k].index = datasets[k]["TIMESTAMP"]

		print(k, "initially ", len(datasets[k]))

		## resample to 2 ms frequency
		datasets[k] = datasets[k].asfreq(dt, method="pad")

		print(k, "finally", len(datasets[k]))
	print('')
	return datasets

def preparing_plotting_and_training():
	os.chdir(".//Datasets/rawData")
	dirs = os.listdir()

	all_list = {}
	for directory in dirs:
		if "." in directory:
			continue

		if "test" in directory:
			os.chdir(directory)
			l = []
			for d in os.listdir():
				if ".csv" in d:
					csv = pd.read_csv(d, sep=";", names=columns)
					l.append(csv)
			all_list[directory] = l
			os.chdir("..")
			continue
		os.chdir(directory)
		columns = ["E1", "E2", "E3", "E4", "E5", "E6", "P1", "P2", "P3", "P4", "P5", "P6", "LOG", "TIMESTAMP", "CICLO"]
		l = []
		for d in os.listdir():
			if ".csv" in d:
				csv = pd.read_csv(d, sep=";", names=columns)
				l.append(csv)
				csv["labels"] = directory
				csv["encoded_labels"] = csv["labels"].apply(lambda x: 0 if x == "Oil leakage" else 1 if x == "nominal" else 2 if x == "noPayload" else 3 if x == "dryBearing" else 4)
		os.chdir("..")
		if len(l):
			all_list[directory] = l
	return all_list


def prepare_data(all_list, remove_outliers=False):
	df_list = []
	df_val = []
	tmp = []
	df_labels = []
	lof = LocalOutlierFactor(n_neighbors=5)  # Adjust the contamination parameter as needed
	for k, v in all_list.items():
		tmp = []
		if k != "test":
			for df in v:
				f = extract_features(df)
				df_list.append(f)
				df_labels.append(df["encoded_labels"][0])
				tmp.append(f)
			if remove_outliers:
				reduced_tmp = pd.DataFrame(tmp)
				outliers = lof.fit_predict(tmp)
				outliers = np.where(outliers == -1)[0]
				ix_list = [len(df_list) - len(tmp) + e for e in outliers]
				df_list = [v for i, v in enumerate(df_list) if i not in ix_list]
				df_labels = [v for i, v in enumerate(df_labels) if i not in ix_list]

	for df in all_list["test"]:
		df_val.append(extract_features(df))

	df_val = pd.DataFrame(df_val)

	return df_val, df_labels, df_list


def split_train_test(df_list, df_labels, perc):
	indices = list(range(len(df_list)))
	random.seed(42)
	random.shuffle(indices)
	train_indices = indices[:int(perc * len(df_list))]
	test_indices = indices[int(perc * len(df_list)):]
	train_x = [df_list[i] for i in train_indices]
	test_x = [df_list[i] for i in test_indices]
	train_y = [df_labels[i] for i in train_indices]
	test_y = [df_labels[i] for i in test_indices]
	test_lab = [k for k, v in zip(test_x, test_y) if  v==0]
	test_lab_y = [ v for k, v in zip(test_x, test_y) if  v==0]
	return pd.DataFrame(train_x), pd.DataFrame(test_x), train_y, test_y, pd.DataFrame(test_lab), test_lab_y

def train(train_x, train_y, test_lab, test_lab_y):
	np.random.seed(42)

	kmeans = KMeans(n_init="auto" ,n_clusters=5, random_state=42)
	scaler = StandardScaler()
	scaled_features = scaler.fit_transform(train_x)

	labels = kmeans.fit_predict(scaled_features)

	labels, map_int = map_labels(labels, train_y)


	plotting_features = train_x.copy()
	plotting_features["cluster"] = labels



	id2label_y={0:"Oil leakage", 1:"Nominal", 2: "noPayload", 3:"dryBearing"}
	id2color = {1:"red", 0:"green", 2: "blue", 3:"yellow"}


	# Plotting using reduced features
	pca = PCA(n_components=2)
	reduced_features = pca.fit_transform(scaled_features)
	# Plot Real Labels
	c = [id2color[l] for l in train_y]
	plt.scatter(reduced_features[:, 0], reduced_features[:, 1], c=c)
	plt.title('Testing Real Labels')
	plt.legend(handles=[mpatches.Patch(color=id2color[i], label=id2label_y[i]) for i in id2label_y.keys()])
	plt.show()
	c = [id2color[l] for l in plotting_features["cluster"].values]
	plt.scatter(reduced_features[:, 0], reduced_features[:, 1], c=c)
	plt.title('Testing K-Means Clustering')
	plt.legend(handles=[mpatches.Patch(color=id2color[i], label=id2label_y[i]) for i in id2label_y.keys()])
	plt.show()


	errors = 0
	accuracy = 0
	for i in range(len(train_x)):
		if id2label_y[plotting_features["cluster"].values[i]] != id2label_y[train_y[i]]:
			print("Error", id2label_y[plotting_features["cluster"].values[i]],id2label_y[train_y[i]])
			errors += 1

	accuracy = 1 - errors/len(train_x)
	print("Accuracy on train set: ", accuracy)

	# metrics from sklearn

	from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

	print(accuracy_score(train_y, plotting_features["cluster"].values))
	print(confusion_matrix(train_y, plotting_features["cluster"].values))
	print(classification_report(train_y, plotting_features["cluster"].values))
	
	return scaler, kmeans, map_int, pca

def testing_datasets(scaler, kmeans, map_int, pca, test_x, test_y):
	id2label_y={0:"Oil leakage", 1:"Nominal", 2: "noPayload", 3:"dryBearing"}
	id2color = {1:"red", 0:"green", 2: "blue", 3:"yellow"}
	scaled_test_features = scaler.transform(test_x)
	test_labels = kmeans.predict(scaled_test_features)
	
	test_labels = [map_int[l] for l in test_labels]
	
	plotting_test_features = test_x.copy()
	plotting_test_features["cluster"] = test_labels
	plotting_test_features["encoded_labels"] = test_y
	
	reduced_test_features = pca.transform(scaled_test_features)
	c = [id2color[l] for l in test_y]
	plt.scatter(reduced_test_features[:, 0], reduced_test_features[:, 1], c=c)
	plt.title('Validation real Labels')
	plt.legend(handles=[mpatches.Patch(color=id2color[i], label=id2label_y[i]) for i in id2label_y.keys()])
	plt.show()
	
	c = [id2color[l] for l in plotting_test_features["cluster"].values]
	plt.scatter(reduced_test_features[:, 0], reduced_test_features[:, 1], c=c)
	plt.title('Validation K-Means Clustering')
	plt.legend(handles=[mpatches.Patch(color=id2color[i], label=id2label_y[i]) for i in id2label_y.keys()])
	plt.show()
	
	
	errors = 0
	accuracy = 0
	for i in range(len(test_x)):
		if id2label_y[plotting_test_features["cluster"].values[i]] != id2label_y[test_y[i]]:
			print("Error", id2label_y[plotting_test_features["cluster"].values[i]],id2label_y[test_y[i]])
			errors += 1
	
	accuracy = 1 - errors/len(test_x)
	print("Accuracy on test set: ", accuracy)

def results(scaler, kmeans, map_int, pca, df_val, train_x):
	id2label_y={0:"Oil leakage", 1:"Nominal", 2: "noPayload", 3:"dryBearing"}
	id2color = {1:"red", 0:"green", 2: "blue", 3:"yellow"}
	scaled_test_features = scaler.transform(df_val)
	val_labels = kmeans.predict(scaled_test_features)

	val_labels = [map_int[l] for l in val_labels]

	plotting_val_features = df_val.copy()
	plotting_val_features["cluster"] = val_labels
	reduced_val_features = pca.transform(scaled_test_features)
	c = [id2color[l] for l in plotting_val_features["cluster"].values]
	plt.scatter(reduced_val_features[:, 0], reduced_val_features[:, 1], c=c)
	plt.title('K-Means Clustering of test dataset')
	plt.legend(handles=[mpatches.Patch(color=id2color[i], label=id2label_y[i]) for i in id2label_y.keys()])
	plt.show()

	total_df = pd.concat([df_val, train_x])
	scaled_total_features = scaler.transform(total_df)
	total_labels = kmeans.predict(scaled_total_features)

	total_labels = [map_int[l] for l in total_labels]

	plotting_total_features = total_df.copy()
	plotting_total_features["cluster"] = total_labels
	reduced_total_features = pca.transform(scaled_total_features)

	c = [id2color[l] for l in plotting_total_features["cluster"].values]

	plt.scatter(reduced_total_features[:, 0], reduced_total_features[:, 1], c=c)
	plt.title('K-Means Clustering of all datasets (test included)')
	plt.legend(handles=[mpatches.Patch(color=id2color[i], label=id2label_y[i]) for i in id2label_y.keys()])
	plt.show()


def inference_on_new_cycle(cycle, kmeans, scaler, pca, map_int, one_cycle_df):
	id2label_y={0:"Oil leakage", 1:"Nominal", 2: "noPayload", 3:"dryBearing"}
	features = extract_features(one_cycle_df)
	scaled_features = scaler.transform([features])
	reduced_features = pca.transform(scaled_features)
	label = kmeans.predict(scaled_features)
	label = map_int[label[0]]
	print(f"Cycle {cycle} is predicted as {id2label_y[label]}")
	return reduced_features



def robot():
	datasets = init_data()
	study_datasets(datasets)
	all_list = preparing_plotting_and_training()
	plotting(all_list)
	df_val, df_labels, df_list = prepare_data(all_list, remove_outliers=False)
	train_x, test_x, train_y, test_y, test_lab, test_lab_y = split_train_test(df_list, df_labels, 0.9)
	scaler, kmeans, map_int, pca = train(train_x, train_y, test_lab, test_lab_y)
	testing_datasets(scaler, kmeans, map_int, pca, test_x, test_y)
	results(scaler, kmeans, map_int, pca, df_val, train_x)
	inference_on_new_cycle(1, kmeans, scaler, pca, map_int, all_list["test"][4])

if __name__=="__main__":
	robot()