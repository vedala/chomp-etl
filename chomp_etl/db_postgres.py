import sys
import psycopg2

def fetch_and_print_data(table, columns, connect_string):
    conn = psycopg2.connect(connect_string)
    cursor = conn.cursor()
    sql_str = construct_sql(table, columns)
    cursor.execute(sql_str)

    for row in cursor:
        print(row)

def construct_sql(table, columns):
    col_str = ", ".join(columns)
    sql_str = f"SELECT {col_str} FROM {table}"
    return sql_str
