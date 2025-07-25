import psycopg2

def teste_conexao():
    try:
        conn = psycopg2.connect(
            dbname="tooltrack",
            user="postgres",
            password="55948",
            host="localhost",
            port=5432
        )
        cur = conn.cursor()
        cur.execute("SELECT 1")
        print("Conexão OK:", cur.fetchone())
        cur.close()
        conn.close()
    except Exception as e:
        print("Erro na conexão:", e)

if __name__ == "__main__":
    teste_conexao()
