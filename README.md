# 🧠 Entorno de Ciencia de Datos y Machine Learning con Python

Bienvenido a este entorno base de **Ciencia de Datos** y **Machine Learning**, preparado con las principales librerías del ecosistema Python.  
Aquí encontrarás todo lo necesario para el análisis, visualización y modelado de datos.

---

## 📋 Contenido

- [🔧 Requisitos previos](#-requisitos-previos)
- [💻 Instalación del entorno virtual](#-instalación-del-entorno-virtual)
- [📦 Instalación de librerías](#-instalación-de-librerías)
- [📚 Descripción de librerías](#-descripción-de-librerías)
- [🧪 Verificación de instalación](#-verificación-de-instalación)
- [💡 Ejemplo rápido de uso](#-ejemplo-rápido-de-uso)
- [🧰 Recomendaciones](#-recomendaciones)
- [📄 Licencia](#-licencia)

---

## 🔧 Requisitos previos

Antes de comenzar, asegúrate de tener instalado:

- **Python 3.12
- **pip** (gestor de paquetes de Python)
- **Git** (opcional, para clonar el repositorio)

Verifica tus versiones ejecutando:

```bash
python --version
pip --version

💻 Instalación del entorno virtual

Crea un entorno virtual para mantener las dependencias aisladas del sistema:

# Crear entorno virtual
python -m venv venv

# Activar el entorno
# En Windows
venv\Scripts\activate

# En Linux o macOS
source venv/bin/activate

🧮 Instalar NumPy

NumPy es la librería base para realizar cálculos matemáticos, álgebra lineal y manejo de matrices.

pip install numpy

🐼 Instalar Pandas

Pandas permite manejar, limpiar y analizar datos de forma sencilla usando estructuras tipo DataFrame.

pip install pandas
📊 Instalar Matplotlib

Matplotlib es la librería estándar de visualización en Python. Permite crear gráficos de líneas, dispersión, barras, etc.

pip install matplotlib

🌈 Instalar Seaborn

Seaborn está construida sobre Matplotlib y facilita la creación de gráficos estadísticos más elegantes y complejos.

pip install seaborn

🤖 Instalar Scikit-learn

Scikit-learn ofrece herramientas para machine learning clásico, como clasificación, regresión y clustering.

pip install scikit-learn

🔥 Instalar TensorFlow

TensorFlow es un framework de Deep Learning desarrollado por Google.
Permite crear y entrenar redes neuronales y modelos de inteligencia artificial.

pip install tensorflow

🚀 Instalar todas las librerías a la vez

Si quieres instalar todas las dependencias en un solo paso, ejecuta:

pip install numpy pandas matplotlib seaborn scikit-learn tensorflow