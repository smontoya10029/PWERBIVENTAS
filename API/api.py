from fastapi import FastAPI
import mysql.connector

app = FastAPI()

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="prueba_ventas"
)

@app.get("/ventas/categoria")
def ventas_por_categoria():
    cursor = db.cursor(dictionary=True)
    cursor.execute("""
        SELECT p.categoria, SUM(v.cantidad * p.precio) AS total
        FROM ventas v
        JOIN productos p ON v.producto_id = p.id
        GROUP BY p.categoria
    """)
    return cursor.fetchall()
