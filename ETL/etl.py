import mysql.connector
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

def get_connection(section):
    return mysql.connector.connect(
        host=config[section]['host'],
        user=config[section]['user'],
        password=config[section]['password'],
        database=config[section]['database']
    )

source = get_connection('source_db')
target = get_connection('target_db')

cursor_src = source.cursor(dictionary=True)
cursor_tgt = target.cursor()

cursor_src.execute("SELECT * FROM ventas")
ventas = cursor_src.fetchall()

for v in ventas:
    cursor_tgt.execute("""
        INSERT INTO ventas (cliente_id, producto_id, fecha, cantidad)
        VALUES (%s,%s,%s,%s)
    """, (v['cliente_id'], v['producto_id'], v['fecha'], v['cantidad']))

target.commit()
print("ETL ejecutado correctamente")
