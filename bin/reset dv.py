import sqlite3
                            ### START Of SQLITE SETUP ###
conn = sqlite3.connect('parts_of_speach.db')
c = conn.cursor()
                            ### END OF SQLITE SETUP ###
c.execute("DROP TABLE Nouns" )
print("doped table")