def pushSingle(title, cursor, conn):
    if os.path.isdir(f'../jsUtilizador/{title}/'):
        print(f'Folder /jsUtilizador/{title}/ found!')

        files = [item for item in os.listdir(f'../jsUtilizador/{title}')
                 if os.path.isfile(os.path.join(f'../jsUtilizador/{title}', item))]

        if len(files) == 1:
            with open(f"../jsUtilizador/{title}/{files[0]}") as pushScript:
                pushScriptJavascript = pushScript.read()
                cursor.execute(f"UPDATE JSU SET JAVASCRIPT = ?, usrdata=DATEADD(DAY, DATEDIFF(DAY, 0, GETDATE()) + 1, 0), usrhora=CONVERT(TIME, GETDATE()) WHERE jsustamp = ?", (pushScriptJavascript, files[0].rstrip('.js')))
                conn.commit()
                   
        elif len(files) == 0:
            print("No files found...")
        else:
            print("More than one file found, expecting a single one.")

    else:
        print('Folder not found.')

def pushAll(cursor, conn):
    filesToPush = []
    os.system('cls') 
    if os.path.isdir(f'../jsUtilizador/'):
        print(f'Folder /jsUtilizador/ found!')
        
        for folder_name in os.listdir('../jsUtilizador'):
            folder_path = os.path.join('../jsUtilizador', folder_name)

            if os.path.isdir(folder_path):
                folder_files = os.listdir(folder_path)

                if len(folder_files) == 1:
                    print(f"Found Javascript de Utilizador: '{folder_name}'")
                    file_path = os.path.join(folder_path, folder_files[0])
                    filesToPush.append(file_path)
                else:
                    print(f"Expected 1 file in '{folder_name}' but found {len(folder_files)}")

        for pushFile in filesToPush:
            with open(pushFile) as pushScript:
                pushScriptJavascript = pushScript.read()
                pushScriptStamp = os.path.basename(pushFile).rstrip('.js')
                cursor.execute(f"UPDATE JSU SET JAVASCRIPT = ?, usrdata=DATEADD(DAY, DATEDIFF(DAY, 0, GETDATE()) + 1, 0), usrhora=CONVERT(TIME, GETDATE()) WHERE jsustamp = ?", (pushScriptJavascript, pushScriptStamp))
                conn.commit()
                  
    else:
        print(f"Couldn't find any Javascript de Utilizador!")

db_conn = pyodbc.connect(db_connString)

phc_updateScriptRoute = f"http://{web_host}/Intranet/ws/wsgeral.asmx/js"


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
        pushSingle(scriptTitle, db_cursor, db_conn)
    elif option == 2:
        pushAll(db_cursor, db_conn)
    else:
        pass

except pyodbc.Error as e:
    print(f"SQL Server Error: {e}")

finally:
    if db_cursor:
        db_cursor.close()
    if db_conn:
        db_conn.close()
    input('\nPress ENTER to continue...')
