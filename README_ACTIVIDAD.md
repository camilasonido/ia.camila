# Actividad Formativa: GitHub Copilot - Sistema de Recomendación Inteligente

## 📋 Descripción del Proyecto

Este proyecto es parte de la actividad formativa de **INACAP** sobre **GitHub Copilot y tendencias emergentes en Inteligencia Artificial**. El objetivo es explorar las capacidades de GitHub Copilot para generar código inteligente en un sistema de recomendación basado en machine learning.

---

## 🎯 Objetivos

1. ✅ Explorar tendencias emergentes en inteligencia artificial
2. ✅ Utilizar GitHub Copilot como herramienta práctica de desarrollo
3. ✅ Crear un sistema de recomendación inteligente
4. ✅ Documentar el proceso de desarrollo
5. ✅ Publicar el proyecto en GitHub

---

## 📦 Contenido del Repositorio

```
ia.camila/
├── recommendation_system.py    # Sistema de recomendación con Machine Learning
├── README.md                   # Documentación completa (este archivo)
├── index.html                  # Página web de registro y login
├── menu.html                   # Menú principal de la aplicación
├── diario.html                 # Página de diario de vida
├── carrito.html                # Página de carrito de compras
├── videos.html                 # Página de visualización de videos
├── app.py                      # Backend Flask para persistencia
├── requirements.txt            # Dependencias del proyecto
└── .git/                        # Repositorio Git
```

---

## 🚀 Tecnologías Utilizadas

### Frontend
- **HTML5** - Estructura de la aplicación web
- **CSS3** - Estilos modernos y responsivos
- **JavaScript** - Interactividad y consumo de APIs

### Backend
- **Python 3.14+** - Lenguaje principal
- **Flask 3.1.3** - Framework web ligero
- **Scikit-learn** - Machine Learning y análisis de datos
- **Pandas** - Manipulación de datos
- **NumPy** - Cálculos numéricos

### DevOps
- **GitHub** - Control de versiones y repositorio
- **GitHub Copilot** - Asistente de codificación con IA
- **Git** - Sistema de versionado

---

## 📖 Sistema de Recomendación

### Características Principales

El sistema de recomendación inteligente implementa:

1. **Análisis de Similitud**
   - Calcula similitud entre productos
   - Utiliza algoritmo de coseno para comparación
   - Identifica productos afines

2. **Machine Learning**
   - Algoritmo KNN (K-Nearest Neighbors)
   - Búsqueda de vecinos más cercanos
   - Recomendaciones personalizadas

3. **Procesamiento de Datos**
   - Manejo de características de productos
   - Cálculo de ratings y precios
   - Categorización inteligente

### Ejemplo de Uso

```python
# Recomendar productos similares
recommended = recommend_products(product_id=1, data=data, n_recommendations=3)

# Calcular similitud entre productos
similarity = similarity_score(product_id1=1, product_id2=2, data=data)

# Obtener productos mejor valorados
top_products = get_top_products(data, n_top=5)
```

---

## 🔧 Instalación y Configuración

### Requisitos Previos
- Python 3.10+
- pip (gestor de paquetes)
- Git
- Visual Studio Code (opcional pero recomendado)
- GitHub Copilot (acceso de estudiante)

### Pasos de Instalación

1. **Clonar el Repositorio**
   ```bash
   git clone https://github.com/tu_usuario/ia.camila.git
   cd ia.camila
   ```

2. **Crear Entorno Virtual**
   ```bash
   python -m venv venv
   
   # En Windows
   venv\Scripts\activate
   
   # En macOS/Linux
   source venv/bin/activate
   ```

3. **Instalar Dependencias**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ejecutar la Aplicación**
   ```bash
   # Backend Flask
   python app.py
   
   # La aplicación estará disponible en http://127.0.0.1:5000
   ```

---

## 📊 Datos de Ejemplo

El sistema utiliza los siguientes datos de ejemplo:

| ID | Categoría | Precio | Rating | Características |
|----|-----------|--------|--------|-----------------|
| 1 | Tecnología | $500 | 4.5 | [1,0,1] |
| 2 | Tecnología | $1200 | 4.8 | [1,1,0] |
| 3 | Hogar | $150 | 3.9 | [0,1,0] |
| 4 | Hogar | $300 | 4.2 | [0,1,1] |
| 5 | Moda | $50 | 4.1 | [1,0,0] |
| 6 | Moda | $120 | 3.8 | [1,0,1] |
| 7 | Deportes | $200 | 4.6 | [0,1,1] |
| 8 | Deportes | $80 | 4.3 | [1,0,1] |

---

## 🤖 GitHub Copilot - Uso en el Proyecto

### Cómo se Utilizó Copilot

1. **Generación de Código**
   - Creación de funciones de machine learning
   - Implementación de algoritmos de similitud
   - Optimización de funciones de recomendación

2. **Documentación**
   - Generación de docstrings
   - Creación de comentarios explicativos
   - Documentación automática

3. **Debugging**
   - Identificación de errores potenciales
   - Sugerencias de mejoras
   - Optimización de performance

### Comandos Copilot Usados

```python
# Copilot sugirió esta función
def similarity_score(product_id1, product_id2, data):
    """Calcula la similitud entre dos productos usando similitud de coseno"""
    # ... implementación generada por Copilot

# Copilot optimizó esta búsqueda
def recommend_products(product_id, data, n_recommendations=3):
    """Recomienda productos similares usando KNN"""
    # ... implementación mejorada
```

---

## 🌐 Aplicación Web

La aplicación web incluye:

### Páginas Disponibles

1. **index.html** - Registro e inicio de sesión
   - Formulario de registro de nuevos usuarios
   - Login seguro con contraseña
   - Validación de datos

2. **menu.html** - Menú principal
   - Acceso a todas las funcionalidades
   - Información del usuario autenticado
   - Botón de cerrar sesión

3. **diario.html** - Diario de vida
   - Crear nuevas entradas
   - Ver historial de entradas
   - Persistencia en backend

4. **carrito.html** - Carrito de compras
   - Seleccionar productos
   - Ver total de compra
   - Enviar orden por WhatsApp

5. **videos.html** - Visualización de videos
   - Reproducción de videos YouTube
   - Interfaz limpia y ordenada

---

## 💾 Backend Flask

### Rutas Disponibles

- `GET /` - Página principal (index.html)
- `POST /api/register` - Registrar nuevo usuario
- `POST /api/login` - Iniciar sesión
- `GET /api/entries?rut=...` - Obtener entradas del diario
- `POST /api/entries` - Guardar nueva entrada del diario
- `GET /<filename>` - Servir archivos estáticos

### Estructura de Datos

```json
{
  "users": [
    {
      "nombre": "Camila",
      "rut": "12345678-9",
      "telefono": "+56912345678",
      "correo": "camila@email.com",
      "password": "secure_password",
      "direccion": "Calle Principal 123",
      "fechaNacimiento": "2005-01-15",
      "opcion": "Profesional"
    }
  ],
  "entries": {
    "12345678-9": [
      {
        "titulo": "Mi primer día",
        "fecha": "2026-05-05",
        "contenido": "Hoy fue un día especial...",
        "timestamp": "2026-05-05T10:30:00Z"
      }
    ]
  }
}
```

---

## 📈 Tendencias Emergentes en IA Exploradas

### 1. Machine Learning Aplicado
- Algoritmos de recomendación personalizados
- Procesamiento inteligente de datos
- Análisis predictivo

### 2. IA Generativa
- GitHub Copilot para código
- Autocompletado inteligente
- Sugerencias de mejora

### 3. Full-Stack IA
- Backend con capacidades inteligentes
- Frontend responsivo y moderno
- Persistencia de datos segura

---

## 📝 Proceso de Desarrollo Documentado

### Paso 1: Creación del Repositorio
- ✅ Crear repositorio en GitHub
- ✅ Configurar estructura del proyecto
- ✅ Inicializar Git

### Paso 2: Desarrollo con GitHub Copilot
- ✅ Crear archivo `recommendation_system.py`
- ✅ Usar Copilot para generar funciones ML
- ✅ Optimizar código sugerido

### Paso 3: Interfaz Web
- ✅ Crear páginas HTML/CSS/JavaScript
- ✅ Implementar estilos modernos
- ✅ Agregar animaciones e iconos

### Paso 4: Backend
- ✅ Crear aplicación Flask
- ✅ Implementar rutas API
- ✅ Configurar persistencia de datos

### Paso 5: Documentación
- ✅ Crear README.md completo
- ✅ Agregar comentarios al código
- ✅ Documentar todas las funciones

### Paso 6: Versionado y Deploy
- ✅ Hacer commit de cambios
- ✅ Push al repositorio remoto
- ✅ Publicar en GitHub Pages (opcional)

---

## 🔗 Enlaces Importantes

- **Repositorio GitHub**: https://github.com/tu_usuario/ia.camila
- **Documentación Copilot**: https://docs.github.com/en/copilot
- **Guía Rápida**: https://docs.github.com/en/copilot/getting-started-with-github-copilot
- **Aplicación Web Local**: http://127.0.0.1:5000

---

## 🎓 Conclusión

Este proyecto demuestra cómo GitHub Copilot puede acelerar el desarrollo de sistemas inteligentes, permitiendo a los estudiantes enfocarse en la lógica empresarial mientras que la IA genera código de calidad y bien documentado.

Las tendencias emergentes exploradas incluyen:
- Machine Learning aplicado
- IA Generativa (Copilot)
- Desarrollo Full-Stack
- Persistencia inteligente de datos
- Recomendaciones personalizadas

---

## 👤 Autor

**Estudiante**: Camila  
**Institución**: INACAP  
**Asignatura**: Tendencias Emergentes en IA  
**Fecha**: Mayo 2026  
**Estado**: ✅ Completado

---

## 📜 Licencia

Este proyecto está bajo licencia MIT. Ver `LICENSE` para más detalles.

---

## 🙏 Agradecimientos

- GitHub Copilot por las sugerencias inteligentes
- INACAP por la oportunidad de aprender IA
- Comunidad de desarrolladores

---

**Última actualización**: 5 de mayo de 2026

