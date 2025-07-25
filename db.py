import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="tooltrack",
        user="postgres",
        password="55948",
        host="localhost",
        port=5432
    )
