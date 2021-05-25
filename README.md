create env
'''bash

conda create -n wineq python=3.7 -y

activate env
'''bash

conda activate wineq

create requirement.txt file

install the requirements
'''bash

pip install -r requirements.txt

download the dataset and put in data_given folder

git init

dvc init

dvc add data_given/winequality.csv

git add .

git commit -m 'first commit' 






