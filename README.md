1.punto
1. Escribe una consulta para obtener las ventas totales por mes y 
categoría de producto. 
2. Obtén el TOP 5 de clientes con mayores compras en el último 
año. 
3. Crea una vista que muestre: cliente, ciudad, total de compras, 
última fecha de compra.

R: esta se encuentra en el carpeta de mysql donde se encuentras los querys.

2.punto

Construir un ETL en Python, el cual debe conectarse a la base de datos 
creada en la Sección A, y extraer la información de las tablas 
construidas, esta información debe ser cargada en otra base de datos 
nueva. 
El ETL debe contar con un archivo de configuración de conexiones. 

R: en este se encuentra un etl con dos archivos donde en uno se encuentra la construccion a la base de datos y el otro el codigo de la construccion de los datos para ejecutar este proceso se corre el siguiente comando.
puyhon etl.py

tambien en la carpeta de mysql se encuentra un query para crear la base de datos y la tabla para la ejecucion del ETL

3.punto

Crear un api sencillo con Python el cual debe tener un endpoint que 
devuelva un JSON del total de las ventas por categoría. 

R: en la carpeta de API se debe correr el siguiente comando 
pip install fastapi uvicorn mysql-connector-python // este comando se utiliza para la instaalacion del fastapi el cual es la libreria para poder correr el api
pip install uvicorn //despues se corre este para poder correr el proceso correctamente 
python -m uvicorn api:app --reload // despues se corre este proceso el cual me devuelve lo siguiente http://127.0.0.1:8000
dentro del codigo del api yo tengo un apartado construido de la siguiente manera @app.get("/ventas/categoria") el cual para poder ver el json se debe agregar la siguiente  url http://127.0.0.1:8000/ventas/categoria 

4.punto
Usando Power BI crea lo siguiente: 
• Grafico de ventas por categoria 
• Gráfico de categorías por mes 
• Cliente que más compra  

R: existe una carpeta llamda POWERBI donde se encuentra el archivo con las graficas






