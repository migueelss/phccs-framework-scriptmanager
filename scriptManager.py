import os
import pyodbc # type: ignore
import configparser

config = configparser.ConfigParser()
config.read('config.cfg')

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
        print("\n\n3 - Pull Scripts Web (VB.NET)")
        print("\n4 - Push Scripts Web (VB.NET)")
        print("\n0 - Quit")

        option = int(input('\n'))

        if option == 1:
            with open('./py/pull_UserJavascript.py') as script:
                exec(script.read())
        elif option == 2:
            with open('./py/push_UserJavascript.py') as script:
                exec(script.read())
        elif option == 3:
            with open ('./py/pull_WebScripts.py') as script:
                exec(script.read())
        elif option == 4:
            with open ('./py/push_WebScripts.py') as script:
                exec(script.read())
        elif option == 0:
            break

scriptManager()