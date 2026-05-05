# Sistema de Recomendación basado en Machine Learning
# Tendencias emergentes en IA: Sistemas de Recomendación Inteligentes
# Autor: Estudiante INACAP
# Fecha: Mayo 2026

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.neighbors import NearestNeighbors

# Ejemplo de datos de productos
data = pd.read_csv('products.csv', error_bad_lines=False) if False else None

# Si no hay archivo CSV, crear datos de ejemplo
if data is None:
    data = pd.DataFrame({
        'product_id': [1, 2, 3, 4, 5, 6, 7, 8],
        'category': ['Tecnología', 'Tecnología', 'Hogar', 'Hogar', 'Moda', 'Moda', 'Deportes', 'Deportes'],
        'price': [500, 1200, 150, 300, 50, 120, 200, 80],
        'rating': [4.5, 4.8, 3.9, 4.2, 4.1, 3.8, 4.6, 4.3],
        'features': [[1, 0, 1], [1, 1, 0], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [0, 1, 1], [1, 0, 1]]
    })

print("=== Sistema de Recomendación Inteligente ===\n")
print(f"Total de productos: {len(data)}")
print(f"\nDatos de productos:\n{data}\n")

# Función de recomendación basada en características similares
def recommend_products(product_id, data, n_recommendations=3):
    """
    Recomienda productos similares al producto seleccionado
    
    Args:
        product_id: ID del producto de referencia
        data: DataFrame con los datos de productos
        n_recommendations: Número de productos a recomendar
    
    Returns:
        Lista de productos recomendados
    """
    
    # Convertir características a matriz
    features_matrix = np.array([feat for feat in data['features']])
    
    # Usar NearestNeighbors para encontrar productos similares
    knn = NearestNeighbors(n_neighbors=n_recommendations + 1, algorithm='ball_tree')
    knn.fit(features_matrix)
    
    # Obtener características del producto
    product_features = np.array(data[data['product_id'] == product_id]['features'].values[0]).reshape(1, -1)
    
    # Encontrar vecinos más cercanos
    distances, indices = knn.kneighbors(product_features)
    
    # Obtener IDs de productos recomendados (excluir el producto actual)
    recommended_ids = [data.iloc[i]['product_id'] for i in indices[0] if data.iloc[i]['product_id'] != product_id]
    
    return recommended_ids[:n_recommendations]

# Ejemplo de uso de la función de recomendación
print("=== Ejemplo de Recomendaciones ===\n")
product_to_recommend = 1
recommended = recommend_products(product_to_recommend, data, n_recommendations=3)

print(f"Para el producto {product_to_recommend}:")
print(f"Productos recomendados: {recommended}\n")

# Mostrar detalles de los productos recomendados
print("Detalles de productos recomendados:")
for prod_id in recommended:
    product_info = data[data['product_id'] == prod_id].iloc[0]
    print(f"  - Producto {prod_id}: {product_info['category']} (${product_info['price']}, Rating: {product_info['rating']})")

# Función para calcular puntuación de similitud
def similarity_score(product_id1, product_id2, data):
    """
    Calcula la similitud entre dos productos
    """
    feat1 = np.array(data[data['product_id'] == product_id1]['features'].values[0])
    feat2 = np.array(data[data['product_id'] == product_id2]['features'].values[0])
    
    # Similitud de coseno
    similarity = np.dot(feat1, feat2) / (np.linalg.norm(feat1) * np.linalg.norm(feat2) + 1e-10)
    return similarity

print("\n=== Matriz de Similitud ===\n")
print("Similitud entre productos:")
for i in range(1, 4):
    for j in range(1, 4):
        if i != j:
            sim = similarity_score(i, j, data)
            print(f"  Producto {i} vs Producto {j}: {sim:.3f}")

# Función para obtener mejores productos
def get_top_products(data, n_top=5):
    """
    Obtiene los productos mejor valorados
    """
    top_products = data.nlargest(n_top, 'rating')
    return top_products

print("\n=== Top 5 Productos Mejor Valorados ===\n")
top_products = get_top_products(data, n_top=5)
for idx, row in top_products.iterrows():
    print(f"Producto {row['product_id']}: {row['category']} - Rating: {row['rating']} - Precio: ${row['price']}")

print("\n=== Sistema de Recomendación Completado ===")
print("Este sistema demuestra tendencias emergentes en IA como:")
print("- Machine Learning para análisis de similitud")
print("- Algoritmos de recomendación personalizados")
print("- Procesamiento inteligente de datos")
