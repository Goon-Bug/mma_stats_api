import mysql.connector
import pandas as pd
import database_config as dc  # change to 'database_config_example'

cnx = mysql.connector.connect(user=dc.USERNAME,
                              password=dc.PASSWORD,
                              host=dc.HOST,
                              database=dc.DB_NAME)

mycursor = cnx.cursor()

# Uncomment and run this piece of code to create the necessary database to store the MMA stats

# mycursor.execute("CREATE DATABASE mma_stats")
# mycursor.execute("CREATE TABLE stats ("
#                  "name VARCHAR(255),"
#                  "age VARCHAR(255),"
#                  "nationality VARCHAR(255),"
#                  "organization VARCHAR(255),"
#                  "height VARCHAR(255),"
#                  "weight VARCHAR(255),"
#                  "wins VARCHAR(255),"
#                  "losses VARCHAR(255),"
#                  "kos VARCHAR(255),"
#                  "submissions VARCHAR(255),"
#                  "decisions VARCHAR(255))")

# mycursor.close()


def print_table(table):
    """
    Given the database and table name, prints table to console

    :param table: table name (str)
    """
    try:
        print(pd.read_sql(f'SELECT * FROM {table}', cnx))
    except pd.errors.DatabaseError as e:
        print(str(e))


def export_to_excel(table, filename):
    """
    Export table to xlsx file

    :param table: table name (str)
    :param filename: name of the file exported (str)
    """
    df = pd.read_sql(f'SELECT * FROM {table}', cnx)
    df.to_excel(f"{filename}.xlsx")


def insert_row(table, **kwargs):
    """
    Inserts row into given table

    :param table: table name (str)
    :param kwargs: dict {column_name: value}
    """
    d = kwargs
    keys = ''
    placeholders = ''
    for i, key in enumerate(d.keys()):
        keys += key
        placeholders += '%s'
        if not i == len(d) - 1:
            keys += ', '
            placeholders += ', '
    query = f"INSERT INTO {table} ({keys}) VALUES ({placeholders})"
    val = tuple(val for val in d.values())
    mycursor.execute(query, val)
    cnx.commit()
    print(f"Row added with values: {val}")


def delete_row(table, column, value):
    """
    Deletes row from table

    :param table: table name (str)
    :param column: column name (str)
    :param value: tuple ('value', )
    """
    sql = f"DELETE FROM {table} WHERE {column} = %s"
    mycursor.execute(sql, value)
    cnx.commit()
    print(f"{mycursor.rowcount} record(s) deleted from {table}")


def delete_all_records(table):
    """
    Deletes all records from given table

    :param table: table name (str)
    """
    sql = f"DELETE FROM {table}"
    mycursor.execute(sql)
    cnx.commit()
    print("All records deleted")


def delete_records_where(table, column, value):
    """
    Deletes all records where 'column' = 'value'

    :param table: table name (str)
    :param column: column name (str)
    :param value: str
    """
    sql = f"DELETE FROM {table} WHERE {column} = %s"
    val = [value]
    mycursor.execute(sql, val)
    cnx.commit()
    print(f"Deleted all rows where {column} = {value}")


def update_row(table, column, value, where, val_id):
    """
    Updates row using the given arguments

    :param table: table name (str)
    :param column: column to change (str)
    :param value: value to change to (str)
    :param where: column to identify row (str)
    :param val_id: value to identify row (str)
    """
    sql = f"UPDATE {table} SET {column} = %s WHERE {where} = %s"
    val = (value, val_id)
    mycursor.execute(sql, val)
    cnx.commit()
    print(mycursor.rowcount, "record(s) affected")
