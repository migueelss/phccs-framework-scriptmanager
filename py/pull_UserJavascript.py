db_conn = pyodbc.connect(db_connString)

os.system('cls') 
print("==== Pull Javascript de Utilizador")
print("\n1 - Pull Single File")
print(f"\n2 - Pull All Files from {db_database}")

option = int(input('\n'))

if option == 1:
    scriptTitle = input('\nScript\'s Title:')

try:

    db_cursor = db_conn.cursor()
    if option == 1:
        db_cursor.execute(f"SELECT jsustamp, titulo, javascript FROM jsu WHERE titulo = ? ", (scriptTitle))
    else:
        db_cursor.execute("SELECT jsustamp, titulo, javascript FROM jsu")

    while True:
        queryRow = db_cursor.fetchone()
        
        if not queryRow:
            break
        
        if not os.path.exists(f"../jsUtilizador/{queryRow.titulo}"): 
            os.makedirs(f"../jsUtilizador/{queryRow.titulo}") 
            print(f"Created the directory /jsUtilizador/{queryRow.titulo} from Javascript de Utilizador with STAMP: {queryRow.jsustamp}")

        with open(f"../jsUtilizador/{queryRow.titulo}/{queryRow.jsustamp}.js", 'w') as file:
            file.write(queryRow.javascript)
            print(f"Deployed {queryRow.jsustamp}.js in /jsUtilizador/{queryRow.titulo}")

except pyodbc.Error as e:
    print(f"SQL Server Error: {e}")

finally:
    if db_cursor:
        db_cursor.close()
    if db_conn:
        db_conn.close()
    input('\nPress ENTER to continue...')
