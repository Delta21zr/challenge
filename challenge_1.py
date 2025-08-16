import pandas as pd
import matplotlib.pyplot as plt

# URLs de las tiendas
urls = [
    "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_1%20.csv",
    "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_2.csv",
    "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_3.csv",
    "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_4.csv"
]

# Cargar los datos
tiendas = [pd.read_csv(url) for url in urls]

# -------------------- Análisis previo --------------------

# Calcular ingreso total de cada tienda y mostrar primeras filas
for i, tienda in enumerate(tiendas, start=1):
    ingreso_total = tienda['Precio'].sum()
    print(f"\n--- Tienda {i} ---")
    print("Primeras filas:")
    print(tienda.head())
    print(f"Ingreso total: {ingreso_total}")

# Mostrar nombres de columnas
for i, tienda in enumerate(tiendas, start=1):
    print(f"Tienda {i} columnas:", tienda.columns.tolist())

# Calcular cantidad de productos vendidos por categoría en cada tienda
for i, tienda in enumerate(tiendas, start=1):
    conteo_categoria = tienda.groupby('Categoría del Producto')['Producto'].count().sort_values(ascending=False)
    print(f"\n--- Tienda {i} ---")
    print("Productos vendidos por categoría:")
    print(conteo_categoria)

# Calcular calificación promedio de cada tienda
for i, tienda in enumerate(tiendas, start=1):
    calificacion_promedio = tienda['Calificación'].mean()
    print(f"Tienda {i} - Calificación promedio: {calificacion_promedio:.2f}")

# Identificar productos más y menos vendidos por tienda
for i, tienda in enumerate(tiendas, start=1):
    conteo_productos = tienda['Producto'].value_counts()
    
    mas_vendido = conteo_productos.idxmax()
    cantidad_mas_vendido = conteo_productos.max()
    
    menos_vendido = conteo_productos.idxmin()
    cantidad_menos_vendido = conteo_productos.min()
    
    print(f"\n--- Tienda {i} ---")
    print("Productos más destacados en ventas:")
    print(f"Más vendido: {mas_vendido} ({cantidad_mas_vendido} ventas)")
    print(f"Menos vendido: {menos_vendido} ({cantidad_menos_vendido} ventas)")

# Calcular costo de envío promedio por tienda
for i, tienda in enumerate(tiendas, start=1):
    costo_envio_promedio = tienda['Costo de envío'].mean()
    print(f"Tienda {i} - Costo de envío promedio: ${costo_envio_promedio:.2f}")

# -------------------- Visualizaciones --------------------

# 1️⃣ Ingreso total por tienda
ingresos = [tienda['Precio'].sum() for tienda in tiendas]

plt.figure(figsize=(8,5))
plt.bar(['Tienda 1','Tienda 2','Tienda 3','Tienda 4'], ingresos, color='skyblue')
plt.title('Ingresos Totales por Tienda')
plt.ylabel('Ingreso Total')
plt.xlabel('Tiendas')
plt.show()

# 2️⃣ Distribución de productos por categoría en la Tienda 1
categorias_tienda1 = tiendas[0]['Categoría del Producto'].value_counts()

plt.figure(figsize=(8,5))
categorias_tienda1.plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Distribución de Productos por Categoría - Tienda 1')
plt.ylabel('')
plt.show()

# 3️⃣ Calificación promedio por tienda
calificaciones = [tienda['Calificación'].mean() for tienda in tiendas]

plt.figure(figsize=(8,5))
plt.plot(['Tienda 1','Tienda 2','Tienda 3','Tienda 4'], calificaciones, marker='o', linestyle='-', color='green')
plt.title('Calificación Promedio por Tienda')
plt.ylabel('Calificación Promedio')
plt.xlabel('Tiendas')
plt.ylim(0,5)  # Suponiendo que la calificación es de 0 a 5
plt.show()

# 4️⃣ Productos más vendidos de cada tienda (barras horizontales)
for i, tienda in enumerate(tiendas, start=1):
    conteo_productos = tienda['Producto'].value_counts().head(10)  # Top 10 productos
    plt.figure(figsize=(8,5))
    conteo_productos.plot(kind='barh', color='orange')
    plt.title(f'Top 10 Productos Más Vendidos - Tienda {i}')
    plt.xlabel('Cantidad de Ventas')
    plt.ylabel('Producto')
    plt.gca().invert_yaxis()  # Para mostrar el más vendido arriba
    plt.show()
