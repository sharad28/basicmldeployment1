# Basic ML/AI app (Flask) deployment on heroku


Creating virtual enviroment using venv package (for windows) and activate it

1. install venv using following code, if not exist  
```
py -m pip install --user virtualenv
```

2. Creating virtual local enviroment using venv in the folder "env"
```
py -m venv ./env
```

#here, py (python) is creating enviroment using venv package, 
# ./ represent the current folder and env is a folder name 

3. To activate just created enviroment
```
.\env\Scripts\activate
```
![](readme%20pic.bmp)
credit:https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/

Required python package by :
```
pip freeze > requirements.txt
```
#this will create a requirements.txt file which will be used by container to install required depedency
