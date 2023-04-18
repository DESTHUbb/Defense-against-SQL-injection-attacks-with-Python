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

<hr/>

<br/><br/>

# Bookstores:

 [![Sys.h](https://user-images.githubusercontent.com/90658763/230771212-7be7f549-17c4-49e2-95bf-3f9674b57a89.png)](https://docs.python.org/3/library/sys.html)
![image](https://user-images.githubusercontent.com/90658763/232776563-2dfbe1b5-8dd3-4cab-9446-1c2f99bb2049.png)
