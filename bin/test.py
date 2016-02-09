import sqlite3
import sys
import time
                            ### START Of SQLITE SETUP ### Need to place this into the sqlite functions as a peramerter..... so that it can be moduale
                            
conn = sqlite3.connect('database.db')
c = conn.cursor()
                            ### END OF SQLITE SETUP ###
loop_toggle = True    
#user_input = input(":")
        #user input starting resquest create this into user request function
def User_input(text):
    user_input = input(text)
    print(user_input)
    return(user_input)
    
def input_check(the_input,text):
    if str(the_input) == text:
        return True
        #print("True")
    else:
        return False
        #print("Returned false")

def delete_table():
    new_input = input("Name of Table? ")
    c.execute(" drop table if exists %s" %new_input)
    print("droped table")
def create_table():
    sqlite_column_data = ''
    new_input = input("table name? ")
    AMT_column = int(input("Amount of Columns? "))
    for i in range(AMT_column):
        if i == AMT_column-1:
            sqlite_column_data += input("Column %d data "%i)
        else:
            sqlite_column_data += input("Column %d data "%i) + ' , '
    #column_data = input("Column data? ")
    print(sqlite_column_data)
    #print(column_data)
    cmd = "CREATE TABLE IF NOT EXISTS %s (%s) " % (new_input,sqlite_column_data)
    print(cmd)
    c.execute(cmd)
    print("Created Table called %s" % (new_input))

def print_table():
    tableListQuery = "SELECT name FROM sqlite_master WHERE type='table' ORDER BY Name"
    c.execute(tableListQuery)
    for tables in c:
        print(tables)

def updateDb(file_name,table_name):
    file = open(file_name, 'r')
    for name in file: 
        fixed_name = name.rstrip()
        c.execute("select word from ? where word=?", (table_name,fixed_name,))
        data = c.fetchone()
        if data == None:
            print ('not found')
            c.execute('insert into %s values("%s")'%table_name %fixed_name)
            print('Added word named %s' %name)
        else:
            print ('found')
    file.close()

def add_row():
    table=User_input("Table name? ")
    data = str(User_input("Data? "))
    #print(data)
    #print(raw(data))
    cmd = "insert into %s values(%s)" %(table , data)
    print(cmd)
    c.execute(cmd)
def print_rows():
    table = input("Table name? ")
    cmd = 'SELECT * FROM %s' %table
    for row in c.execute(cmd):
        print(row)
        
def test_data(row_name,db_name):
    for row in c.execute("select word from %s where word='%s'" %(db_name,row_name)):
        return True
        print("found")

def call_data(table_name,row_name,search_cloumn,column_name):
    c.execute("select * from %s" %(table_name))
    table = c.fetchall()
    for column in table:
        if str(column[3]) == column_name and str(column[search_cloumn]) == row_name:
            return(column)
            '''print("found row with data:",row[0])
            print("Prams need are: ",row[1])
            print("Prams are: ",row[2])
            print("Tags are: ",row[3])
            print("layout is: ",row[4])'''

def analize(Input):
    string_list = Input.split()
    print(string_list)
    action = []
    pram = []
    for word in string_list:
        if word.lower() == 'corona':
            string_list.remove(word)
        elif test_data(word.lower(),'actions'):
            got_row = call_data('actions',word.lower(),0,'action')
            for item in got_row:
                action.append(item)
            for number in range(action[1]):
                print("this is action[2]",str(action[2]))
                row =call_data('actions',str(action[2]),3,"object")
                print(row)

            
            
def user_input_cmd(Input):
    the_input = Input

    if input_check(the_input,"table check"):
        new_input=User_input("What is the name of the table to test? ")
        stmt = "SELECT name FROM sqlite_master WHERE type='table' AND name='%s'" %new_input
        c.execute(stmt)
        result = c.fetchone()
        if result:
            print("YES")# there is a table named "tableName"
        else:
            print("NO")# there are no tables named "tableName"
    elif input_check(the_input,"update"):
        file_name = input("Name of file? ")
        table_name = input("Name of Table? ")
        
        updateDb(file_name,table_name)
    elif input_check(the_input,"create table"):
        create_table()
        
    elif input_check(the_input,"delete table"):
        delete_table()
        
    elif input_check(the_input,"list tables"):
        print_table()
    
    elif input_check(the_input,"quit"):
        print("quiting....")
        conn.commit() # these need to be in the functions....
        conn.close()
        sys.exit() 
    elif input_check(the_input,"get time"):
        print(time.localtime())
        
    elif input_check(the_input,"add row"):
        add_row()
        
    elif input_check(the_input,"print rows"):
        print_rows()
    elif input_check(the_input,"get row"):
        call_data("hat","Nouns")
    else:
        analize(the_input)
        
while True:
    the_input = input(":")
    #(the_input)
    user_input_cmd(the_input)
    
        
        
        #testing if the rows reseaved the date correctly
    


                        ### SQLITE REFRANCE CODE ###

    # Create table
#c.execute('''CREATE TABLE words
             #(word text, is_noun text, is_verb text, adverbs text, adjectives text)''')

    # Insert a row of data
#c.execute("INSERT INTO words VALUES ('time','Yes','No','No','No')")
    #remoe a row of data
#c.execute("DELETE FROM words WHERE word=?", ("time",))
    #removes table
#c.execute("DROP TABLE words" )
    # Save (commit) the changes
#conn.commit()
#cur.execute("UPDATE Cars SET Price=? WHERE Id=?", (uPrice, uId)) change data in row
    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
#c.execute("alter table table_name add column '%s' 'float'" % author)

'''con = lite.connect('test.db')    

with con:
    
    con.row_factory = lite.Row
       
    cur = con.cursor() 
    cur.execute("SELECT * FROM Cars")

    rows = cur.fetchall()

    for row in rows:
        print "%s %s %s" % (row["Id"], row["Name"], row["Price"])'''