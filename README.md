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

## The function ```execute_stored_procedure``` takes as arguments the connection to the database, the name of the stored procedure, and the values ​​of the parameters. Inside the function, the callproc function is used to execute the stored procedure with the given parameters. Placeholders are indicated by %s in the placeholders string that is passed to the join function. The results are retrieved using the cursor's fetchall method and are returned as a list of tuples.
<hr/>

<br/><br/>

# Bookstores:
## pymysql:
 [![pymysql ](https://user-images.githubusercontent.com/90658763/232776563-2dfbe1b5-8dd3-4cab-9446-1c2f99bb2049.png)](https://pypi.org/project/pymysql/)

## mysql.connector:
[![mysql.connector](https://user-images.githubusercontent.com/90658763/232777656-87133a22-8239-4796-91b8-ca535c452000.png)](https://www.mysql.com/products/connector/)

