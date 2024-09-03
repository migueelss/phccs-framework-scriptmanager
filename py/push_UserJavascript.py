db_conn = pyodbc.connect(db_connString)

os.system('cls') 
print("==== Push Javascript de Utilizador")
print("\n1 - Push Single File")
print(f"\n2 - Push All Files from /jsUtilizador/")

option = int(input('\n'))

if option == 1:
    scriptTitle = input('\nScript\'s Title:')

try:
    db_cursor = db_conn.cursor()

    if option == 1:
        if os.path.isdir(f'../jsUtilizador/{scriptTitle}/'):
            print(f'Folder /jsUtilizador/{scriptTitle}/ found!')

            files = [item for item in os.listdir(f'../jsUtilizador/{scriptTitle}')
                     if os.path.isfile(os.path.join(f'../jsUtilizador/{scriptTitle}', item))]

            if len(files) == 1:
                with open(f"../jsUtilizador/{scriptTitle}/{files[0]}") as pushScript:
                    pushScriptJavascript = pushScript.read()
                    db_cursor.execute(f"UPDATE JSU SET JAVASCRIPT = ? WHERE jsustamp = ?", (pushScriptJavascript, files[0].rstrip('.js')))
                    db_conn.commit()
                   
            elif len(files) == 0:
                print("No files found...")
            else:
                print("More than one file found, expecting a single one.")

        else:
            print('Folder not found.')

except pyodbc.Error as e:
    print(f"SQL Server Error: {e}")

finally:
    if db_cursor:
        db_cursor.close()
    if db_conn:
        db_conn.close()
    input('\nPress ENTER to continue...')
