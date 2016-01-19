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
def string_analize(string):
    splited_list = string.split()
    print(splited_list)
def User_input(text):
    user_input = input(text)
    print(user_input)
    return(user_input)
    
def input_check(the_input,text):
    if str(the_input) == text:
        return True
        print("True")
    else:
        return False
        print("Returned false")

def delete_table():
    new_input = input("Name of Table? ")
    c.execute(" drop table if exists %s" %new_input)
    print("droped table")

def create_table():
    new_input = input("table name? ")
    cmd = '''CREATE TABLE IF NOT EXISTS %s (word text) ''' % (new_input)
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

def user_input_cmd(Input):
    the_input = Input
    user_input = the_input
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
        new_input = input("table name? ")
        if input_check(new_input,"quit") == False:
            cmd = '''CREATE TABLE IF NOT EXISTS %s (word text) ''' % (new_input)
            print(cmd)
            c.execute(cmd)
            print("Created Table called %s" % (new_input))
        
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