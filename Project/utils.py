import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
import matplotlib.patches as mpatches

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

from sklearn.neighbors import LocalOutlierFactor

def study_datasets(datasets):
	power_columns = ["E1", "E2", "E3", "E4", "E5", "E6"]
	##UNCOMMENT FOR PLOTTING OF ALL ENERGY COMPARISON BY TYPE
	#for k, df in datasets.items():
#
	#	if k == "test":
	#		continue
	#	plt.figure(figsize=(12, 6))
	#	df[power_columns].plot(title = k)
	#	plt.show()

	print('--- Comparison of states energy columns with normal mean ---')
	for k, df in datasets.items():
		if k == "test":
			continue
		## normal mean
		print(k, df[power_columns].mean().sum(), df[power_columns].mean().values)
	print('')


	print('--- Comparison of states energy columns with absolute mean ---')
	for k, df in datasets.items():
		if k == "test":
			continue
		## asbolute mean
		print(k, df[power_columns].abs().mean().sum(), df[power_columns].abs().mean().values)
	print('')

	print('--- describe of nominal ---')
	print(datasets["nominal"].iloc[:, :-3].describe(), end='\n\n')
	print('--- describe of noPayload ---')
	print(datasets["nop"].iloc[:, :-3].describe(), end='\n\n')
	print('--- describe of dryBearing ---')
	print(datasets["dry"].iloc[:, :-3].describe(), end='\n\n')
	print('--- describe of oilLeakage ---')
	print(datasets["oil"].iloc[:, :-3].describe(), end='\n\n')

def plotting(datasets):
	nominal = pd.concat(datasets['nominal'], ignore_index=True)
	for key in datasets.keys():
		if key == 'nominal' or key == 'test':
			continue
		other = pd.concat(datasets[key], ignore_index=True)
		tab, oil_leak = plt.subplots(6, 2)

		tab.suptitle('Energy & position, nominal(b) vs ' + key + '(r)')
		#plt.subplots_adjust(bottom=0, right=1.5, top=2)
		if key == 'dryBearing':
			plt.tight_layout()
		for i in range(6):
			oil_leak[i, 0].set_title('E' + str(i+1))
			oil_leak[i, 0].plot(nominal['E' + str(i+1)], c='b')
			oil_leak[i, 0].plot(other['E' + str(i+1)], c='r')

			oil_leak[i, 1].set_title('P' + str(i+1))
			oil_leak[i, 1].plot(nominal['P' + str(i+1)], c='b')
			oil_leak[i, 1].plot(other['P' + str(i+1)], c='r')
		plt.show()

def extract_features(df):
	df = df[["E1","E2", "E3", "E5", "E4", "E6"]]

	return df.std().tolist() + df.mean().tolist()

def map_labels(labels, train_y):
	train_y = np.array(train_y)
	map_int = {}
	for i in range(max(labels) + 1):
		idx = np.argwhere(labels == i)
		if len(idx) == 0:
			continue
		vals, counts = np.unique(train_y[idx], return_counts=True)
		idx_max = np.argmax(counts)
		map_int[i] = vals[idx_max] 
	return [map_int[l] for l in labels], map_int

