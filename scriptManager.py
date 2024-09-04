import os
import pyodbc # type: ignore
import configparser
import requests
from requests.auth import HTTPBasicAuth

config = configparser.ConfigParser()
config.read('config.cfg')

web_host = config['web']['host']

# Database Connection Data
db_database = config['database']['db']
db_host = config['database']['dbhost']
db_port = config.getint('database', 'port')
db_user = config['database']['user']
db_userPassword = config['database']['password']


db_connString = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER="+db_host+";" 
    "DATABASE="+db_database+";" 
    "UID="+db_user+";"
    "PWD="+db_userPassword+";"
)

def scriptManager():
    while True:
        os.system('cls')
        print("=== Script Manager PHC Framework 0.1.0")
        print("\n1 - Pull Javascript de Utilizador")
        print("\n2 - Push Javascript de Utilizador")

        option = int(input('\n'))

        if option == 1:
            with open('./py/pull_UserJavascript.py') as script:
                exec(script.read())
        elif option == 2:
            with open('./py/push_UserJavascript.py') as script:
                exec(script.read())
        elif option == 0:
            break

scriptManager()