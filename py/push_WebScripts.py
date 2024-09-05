def push_files(cursor, conn, title):
    def process_file(file_path):
        with open(file_path) as pushScript:
            pushScriptJavascript = pushScript.read()
            pushScriptStamp = os.path.basename(file_path).rstrip('.vb')
            cursor.execute(f"UPDATE ESCR SET expressao = ?, usrdata=DATEADD(DAY, DATEDIFF(DAY, 0, GETDATE()) + 1, 0), usrhora=CONVERT(TIME, GETDATE()) WHERE escrstamp = ?", (pushScriptJavascript, pushScriptStamp))
            conn.commit()
            print(f"Published {file_path}")

    os.system('cls')

    if title:
        folder_path = f'../webScriptsVB/{title}/'
        if os.path.isdir(folder_path):
            print(f'Folder {folder_path} found!')
            files = [item for item in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, item))]
            if len(files) == 1:
                process_file(os.path.join(folder_path, files[0]))
            elif len(files) == 0:
                print("No files found...")
            else:
                print("More than one file found, expecting a single one.")
        else:
            print('Folder not found.')
    else:
        base_folder = '../webScriptsVB/'
        if os.path.isdir(base_folder):
            print(f'Folder {base_folder} found!')
            for folder_name in os.listdir(base_folder):
                folder_path = os.path.join(base_folder, folder_name)
                if os.path.isdir(folder_path):
                    folder_files = [item for item in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, item))]
                    if len(folder_files) == 1:
                        print(f"Found Script Web (VB.NET): '{folder_name}'")
                        process_file(os.path.join(folder_path, folder_files[0]))
                    else:
                        print(f"Expected 1 file in '{folder_name}' but found {len(folder_files)}")
        else:
            print(f"Couldn't find any Script Web (VB.NET)!")

db_conn = pyodbc.connect(db_connString)

os.system('cls') 
print("==== Push Scripts Web (VB.NET)")
print("\n1 - Push Single File")
print(f"\n2 - Push All Files from /webScriptsVB/")
print(f"\n0 - Go Back")

option = int(input('\n'))

if option == 1:
    scriptTitle = input('\nScript\'s Code:')

try:
    db_cursor = db_conn.cursor()

    if option == 1:
        push_files(db_cursor, db_conn, scriptTitle)
    elif option == 2:
        push_files(db_cursor, db_conn, None)
    else:
        pass

except pyodbc.Error as e:
    print(f"SQL Server Error: {e}")

if db_cursor:
    db_cursor.close()
if db_conn:
    db_conn.close()
if option == 1 or option == 2:
    input('\nPress ENTER to continue...')
