from dotenv import dotenv_values
import psycopg2

# Cargar variables desde .env
config = dotenv_values("Database/.env")

try:
    conn = psycopg2.connect(
        dbname=config['NOMBRE_BD'],
        user=config['USUARIO'],
        password=config['POSTGRES_PASSWORD'],
        host=config['HOST'],
        port=config['PUERTO']
    )
    cur = conn.cursor()
    cur.execute("SELECT 1;")
    result = cur.fetchone()
    cur.close()
    conn.close()
    print("Conexión exitosa. Resultado de prueba:", result)
except Exception as e:
    print("Error al conectar a la base de datos:", e)
