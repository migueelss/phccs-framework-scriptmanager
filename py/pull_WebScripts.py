def pullScripts(cursor, title):
    try:
        if title is not None:
            cursor.execute(f"SELECT escrstamp, codigo, expressao FROM escr WHERE codigo = ? ", (title))
        else:
            cursor.execute("SELECT escrstamp, codigo, expressao FROM escr")

        while True:
            queryRow = cursor.fetchone()
            
            if not queryRow:
                break
            
            if not os.path.exists(f"../webScriptsVB/{queryRow.codigo}"): 
                os.makedirs(f"../webScriptsVB/{queryRow.codigo}") 
                print(f"Created the directory /webScriptsVB/{queryRow.codigo} from Web Script (VB.NET) with STAMP: {queryRow.escrstamp}")

            with open(f"../webScriptsVB/{queryRow.codigo}/{queryRow.escrstamp}.vb", 'w') as file:
                file.write(queryRow.expressao)
                print(f"Deployed {queryRow.escrstamp}.vb in /webScriptsVB/{queryRow.codigo}")

    except pyodbc.Error as e:
        print(f"SQL Server Error: {e}")

db_conn = pyodbc.connect(db_connString)

os.system('cls') 
print("==== Pull Scripts Web (VB.NET)")
print("\n1 - Pull Single File")
print(f"\n2 - Pull All Files from {db_database}")
print(f"\n0 - Go Back")

option = int(input('\n'))

if option == 1:
    db_cursor = db_conn.cursor()
    scriptTitle = input('\nScript\'s Code:')
    pullScripts(db_cursor, scriptTitle)
    if db_cursor:
        db_cursor.close()
    if db_conn:
        db_conn.close()
    input('\nPress ENTER to continue...')
if option == 2:
    db_cursor = db_conn.cursor()
    pullScripts(db_cursor, None)
    if db_cursor:
        db_cursor.close()
    if db_conn:
        db_conn.close()
    input('\nPress ENTER to continue...')
else:
    pass

    


