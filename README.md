# Python: Prevention of SQL Injection attacks
![spaceinjection](https://user-images.githubusercontent.com/90658763/183930258-9bf68857-712c-49fa-85ae-b468ca17e2fc.gif)

Steps for the prevention of SQL Injection attacks in an application created with Python and MySQL.

<hr/>

First, create a virtual environment:
### `python -m virtualenv env`

To install the necessary packages:
### `pip install -r requirements.txt`

Create an .env file (in the root of the project) for the environment variables:

### `MYSQL_HOST=host`
### `MYSQL_USER=user`
### `MYSQL_PASSWORD=password`
### `MYSQL_DB=database`

```console
. from decouple import config
import pymysql
import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host=config('MYSQL_HOST'),        
        database=config('MYSQL_DB'),
        user=config('MYSQL_USER'),
        password=config('MYSQL_PASSWORD')
    )
```

![Inyeccionsqldef](https://user-images.githubusercontent.com/90658763/183928503-53df4acb-6de0-486f-b41a-f8a1335374a8.png)

# OPERATION "MySQL data store":

## The code tries to provide the correct values ​​for ```your_username``` , ```your_password```, ```your_host```, and ```your_database```. If the MySQL server is on the same machine as the Python code, you can use 'localhost' as the value for ```your_host```. If the MySQL server is on a remote machine, make sure you provide the correct IP address or domain name.

## The function ```execute_stored_procedure``` takes as arguments the connection to the database, the name of the stored procedure, and the values ​​of the parameters. Inside the function, the ```callproc``` function is used to execute the stored procedure with the given parameters. Placeholders are indicated by %s in the placeholders string that is passed to the join function. The results are retrieved using the cursor's fetchall method and are returned as a list of tuples.

## The usage example shows how you can use the ```execute_stored_procedure``` function to execute a stored procedure called ```sp_myprocedure``` with two parameters ```parameter_value1``` and ```parameter_value2``` . The results are printed to the console using the print function.

<hr/>

<br/><br/>

# Bookstores:

protobuf==3.19.3
pycodestyle==2.8.0

![ciberguarden](https://github.com/DESTHUbb/Defense-against-SQL-injection-attacks-with-Python/assets/90658763/88f2b448-0305-4b55-b94b-acb9365ebb71)


## pymysql:
 [![pymysql ](https://user-images.githubusercontent.com/90658763/232776563-2dfbe1b5-8dd3-4cab-9446-1c2f99bb2049.png)](https://pypi.org/project/pymysql/)

## mysql.connector:
[![mysql.connector](https://user-images.githubusercontent.com/90658763/232777656-87133a22-8239-4796-91b8-ca535c452000.png)](https://www.mysql.com/products/connector/)

## Create_engine:
 [![pymysql ](https://user-images.githubusercontent.com/90658763/236939383-c72bff9e-033e-4116-be80-4c9fc6acd797.png)](https://docs.sqlalchemy.org/en/20/core/engines.html)
 
## Sessionmaker:
 [![pymysql ](https://user-images.githubusercontent.com/90658763/236940458-55217f51-b276-4f63-bd71-a1cc460cb7e4.png)](https://docs.sqlalchemy.org/en/20/orm/session_basics.html)

## Re:

 [![Re](https://user-images.githubusercontent.com/90658763/236941506-7f8d03a1-8743-4238-b24d-9dc6ece7d9b3.png)](https://docs.python.org/3/library/re.html)

## [![Autopep8](Autopep8)](https://pypi.org/project/autopep8/)
![autopep8-banner](https://github.com/DESTHUbb/Defense-against-SQL-injection-attacks-with-Python/assets/90658763/e3d83e43-7520-467d-bb3d-1a493f006202)

## [![Protobuf](protobuf)](https://pypi.org/project/protobuf/)
![image](https://github.com/DESTHUbb/Defense-against-SQL-injection-attacks-with-Python/assets/90658763/e15c0278-ae2d-48e4-9b68-4f30dde53c17)



