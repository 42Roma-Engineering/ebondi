Progetto ROBOT 42Roma / Engineering

Gruppo dripanuc, marimatt, ebondi

Il progetto consiste nel predire gli stati di malfunzionamento di un braccio meccanico a 6 snodi con vari dataset che contengono cicli in stato di funzionamento normale e non (dryBearing, noPayload e oil leakage) più uno di test di cui non si conosce gli stati...
Per risolvere il problema abbiamo scelto di utilizzare un K-Means clustering

# to start

# create conda enviroment
conda create --name robot_env --file robot_env.txt

# activate enviroment
conda activate robot_env

# unzip Datasets
python3.9 Datasets/exec_once_to_unzip.py

# exec program
python3.9 robot.py