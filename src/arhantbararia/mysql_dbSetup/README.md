# Script to make a MySql Database

Useful for
- automating project setup
- setting up database for django / flask projects


## Installation
Run
```
pip install requirements.txt
```
Make sure your Mysql Server is running and to connect you will need
- Mysql Server Host address (Eg. 127.0.0.1)
- Authorized Username and Password
- (optional) Mysql Server Listening port (default 3306)

## Usage


```
$ python3 mysql_db_setup.py
Enter Host Address of Mysql User (default = localhost): 127.0.0.1
Enter Mysql Server port (default = 3306):
Enter Username: mysql_user
Password:
connected to server
Enter Database name: test_database
Database Created!

```


