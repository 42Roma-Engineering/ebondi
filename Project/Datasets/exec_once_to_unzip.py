import zipfile
import os
import shutil

if 'Datasets' in os.listdir():
    os.chdir('Datasets')
with zipfile.ZipFile('./zip/robot.zip', 'r') as zip_ref:
    zip_ref.extractall('./zip/')

shutil.move('./zip/robot/rawData/test', './rawData/test')

base = './zip/robot/rawData/'
for f in os.listdir(base):
    with zipfile.ZipFile(base + f, 'r') as zip_ref:
    	zip_ref.extractall('./rawData/')
        
shutil.rmtree('./zip/robot/')