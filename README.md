# Mahindra_Test_Project

# Basic webpage using Django

  1. file uploader to upload the given Input.xlsx
  2. Create a button which will upload the following file and store it in the database. (Use
  Django’s default database SQLite)
  3. On the same click the data should be retrieved from the database and transform it to the
  given format (refer the given Output.xlsx) and save the Output.xlsx in Output Folder.



## Documentation
1. Goals:
```bash
    1. file uploader to upload the given Input.xlsx
    2. Create a button which will upload the following file and store it in the database. (Use
    Django’s default database SQLite)
    3. On the same click the data should be retrieved from the database and transform it to the
    given format (refer the given Output.xlsx) and save the Output.xlsx in Output Folder.
```
2. Database design:
```bash
Database structure 
  1. Category
  2. X
  3. Y
```

## Deployment

To run amulated server 

```windwos powershell
 python manage.py runserver
```
To map with the templates please add template path to DIRS as smention below

```
 TEMPLATES = [
     'DIRS': [os.path.join(BASE_DIR,'templates')],
 ]
```


## Environment Variables


`SECRET_KEY`

`DEBUG`

Find admin login details in .env file

url = 'localhost/admin'

## Installation

Install Django Framework for creating Ecommerce project

```bash
  python -m pip install Django 
  ```
Install decouple for enviornment variables
```bash
  pip install python-decouple
```
    
