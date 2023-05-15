import sqlite3


conn = sqlite3.connect('files.db')

# Database connection and create table
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_filename TEXT \
        )")
    conn.commit()


conn = sqlite3.connect('files.db')

# List of file names
fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')
# Looping each item in fileList ending with '.txt'
for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
        # Inserts items that end with '.txt' to table and prints to console
            cur.execute("INSERT INTO tbl_files(col_filename) VALUES (?)",(x,))
            print(x)
            
conn.close()

    



