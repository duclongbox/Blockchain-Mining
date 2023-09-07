**Set up the the virtual environment for the project**
```
python3 -m venv "environment name"
for windows:
    cd "environment file"/Scripts/.activate.ps1
for unix:
    source "environment file"/bin/activate
```
**Install all the packages**
```
pip3 install -r requirements.txt
```


**Activate the virtual environment**
**create __init__.py for each directories to run the module**
```
python3 -m backend.blockchain.block
python3 -m pytest backend/tests
```