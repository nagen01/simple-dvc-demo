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


tox commands:
'''bash
tox

for rebuild
tox -r
'''

pytest command
''bash
pytest -v

setup command
'''bash
pip install -e .
'''

build your own package command
'''bash
python setup.py sdist bdist_wheel
'''

create an artifcats folder

mlflow server command -

mlflow server
    --backend-store-uri sqlite:///mlflow.db
    --default-artifact-root ./artifacts
    --host 0.0.0.0 -p 1234

mlflow server --backend-store-uri sqlite:///mlflow.db --default-artifact-root ./artifacts