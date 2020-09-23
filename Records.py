import sqlite3

db = ('filmon.sqlite')

def main():
    creating_table()
    insert_data()
    add_new_row_to_records()
    search_by_id_from_records()
    update_by_name_num_of_catches()
    delete_by_record_holder_name()


def creating_table():# creating table if not exists
  
    conn = sqlite3.connect(db)
    conn.execute('CREATE TABLE IF NOT EXISTS records(name text , country text, catches int)')
    conn.commit()
    conn.close()

def insert_data():# inserting data to records table
    conn = sqlite3.connect(db)
    
    conn.execute('INSERT INTO records values(" Janne Mustonen ", "Finland", 98)')
    conn.execute('INSERT INTO records values("Ian Stewart  ", "Canada", 94)')
    conn.execute('INSERT INTO records values("Aaron Gregg ", "Canada", 88)')
    conn.execute('INSERT INTO records values("Chad Taylor", "USA", 78 \n)')
    conn.commit()
    conn.close()


    
def add_new_row_to_records():#adding new row to records table
    conn = sqlite3.connect(db)
    new_participant = input('Enter new name: ')
    new_country = input('Enter country: ')
    new_catch = int(input('Enter the number of catches: '))

    conn.execute('INSERT INTO records VALUES(?,?,?)', (new_participant, new_country, new_catch))
    conn.commit()
    conn.close()

def search_by_id_from_records():#searching by id from the recorda table
    conn = sqlite3.connect(db)
    serach_by_id = input("Enter the I.D you want to search")
    search = conn.execute('select * from records  WHERE  rowid = ? ', ( serach_by_id ,))
    countsearch = search.rowcount
    freshserach =search.fetchone()
    if countsearch == 0:
        print("no search was made at this time")
    else:
        print(freshserach)
    conn.commit()
    conn.close()


def update_by_name_num_of_catches():
    conn = sqlite3.connect(db)
    name_to_update = input("Enter the name you want to update")
    update_catches = int(input("enter the number of catches"))
    update = conn.execute('UPDATE records SET  catches = ? WHERE  name = ? ', ( update_catches, name_to_update))
    countupdate = update.rowcount
    #freshupdate = update.fetchone()
    if countupdate == 0:
        print("no update was made at this time")
    else:
        print("updated successfully")
    conn.commit()
    conn.close()


def delete_by_record_holder_name():
    conn = sqlite3.connect(db)
    delete_by_name = input("Enter the name you want to delete")
    
    delete = conn.execute('delete  from records  WHERE name = ? ', (  delete_by_name ,))
    countdelete = delete.rowcount
   # freshdelete=delete.fetchone()
    if countdelete == 0:
        print("no deletion  was made at this time")
    else:
        print("DELETED SUCCESsFULLY")
    conn.commit()
    conn.close()
    


  
    
if __name__ == '__main__':
    main()


