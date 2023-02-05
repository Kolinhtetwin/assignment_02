import sqlite3

try:
    # is called the grave accent
    db_connection = sqlite3.connect("customer_data.db")
    sql_query = "INSERT INTO customer(account_number,first_name,last_name,list_of_dvd_borrowed)" \
                "VALUES (100,'Erik Tan','Hak','Boss of Manchester');"
    cursor = db_connection.cursor()
    cursor.execute(sql_query)
    db_connection.commit()  # commit to the database
    print("SQLite records inserted")

except sqlite3.Error as error:
    print(f"An error has occurred: Please contact the DB administrator")
finally:
    if db_connection:
        db_connection.close()