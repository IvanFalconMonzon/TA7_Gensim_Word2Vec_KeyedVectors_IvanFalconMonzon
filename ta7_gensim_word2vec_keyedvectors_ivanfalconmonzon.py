# -*- coding: utf-8 -*-
"""TA7_Gensim_Word2Vec_KeyedVectors_IvanFalconMonzon.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1M9rIN34j9dzDmotxVwOcn_70Mrl_KQeu

# *IVÁN FALCÓN MONZÓN*

**Análisis y Aplicación de Gensim y Word2Vec**

Video tutorial de la tarea: https://youtu.be/Z1VsHYcNXDI?si=PxIOcNjWb1HItQqB

# **1. Introducción**

**¿Qué es Gensim?**

Gensim es una biblioteca de **Python** especializada en el p**rocesamiento de texto, aprendizaje automático y modelado de temas**. Se utiliza principalmente en tareas de procesamiento de lenguaje natural (NLP) y análisis semántico.

Es especialmente eficiente para trabajar con grandes volúmenes de texto, ya que está diseñada para manejar datos de forma escalable, sin necesidad de cargar todo en memoria.

Esta diseñada para el modelado de temas y procesamiento de texto en tareas de NLP. Su capacidad para manejar grandes volúmenes de texto sin cargarlos en memoria la hace ideal para entrenar modelos como Word2Vec.

# **2. Instalación de Gensim**

Antes de usar **Gensim**, es necesario instalarlo en el entorno de Google Colab con el siguiente comando:
"""

# IVAN FALCON MONZON
!pip install gensim

"""Si ya está instalado, el sistema confirmará la instalación.

# **3. Entrenamiento de un modelo Word2Vec desde cero**

####***3.1 Descarga del dataset***

Se obtiene un dataset de noticias de Reddit desde Kaggle:
https://www.kaggle.com/datasets/rootuser/worldnews-on-reddit

####***3.2 Carga y preprocesamiento de datos***

Cargar/Importar todas las librerías necesarías:
"""

# IVAN FALCON MONZON
# Importación de librerías necesarias
# Gensim: Librería para modelos de procesamiento de texto
from gensim.models import Word2Vec, keyedvectors

# Pandas: Librería para manipulación de datos en estructuras tipo DataFrame
import pandas as pd

# NLTK: Biblioteca para procesamiento de lenguaje natural
import nltk

# Se importa una librería diferente a la del vídeo
# TreebankWordTokenizer: Tokenizador de NLTK basado en el estándar Penn Treebank
from nltk.tokenize import TreebankWordTokenizer

"""Los datos se cargan en un DataFrame usando Google drive:"""

from google.colab import drive

# Montar Google Drive
drive.mount('/content/drive')

# Especificar la ruta del archivo dentro de Google Drive
file_path = '/content/drive/MyDrive/7PRO/reddit_worldnews_start_to_2016-11-22.csv'

# Cargar el dataset en un DataFrame
df = pd.read_csv(file_path)

# Mostrar las primeras filas para verificar la carga
df.head()

# IVAN FALCON MONZON
# Muestra las primeras 10 filas del DataFrame
df.head(10)

"""Se extraen los títulos de las noticias para su procesamiento posterior:"""

# IVAN FALCON MONZON
# Extraer los títulos de noticias del DataFrame y los almacena en una variable
newsTiles = df['title'].values

# IVAN FALCON MONZON
# Mostrar el contenido de la variable newsTiles
newsTiles

"""####***3.3 Tokenización de textos***

Se usa TreebankWordTokenizer de NLTK para dividir los títulos en palabras:
"""

# IVAN FALCON MONZON
# Librería necesaría (cargada anteriormente):
# from nltk.tokenize import TreebankWordTokenizer

# Inicializa el tokenizador de NLTK basado en el estándar Penn Treebank
tokenizer = TreebankWordTokenizer()

# Tokeniza cada título de noticia en newsTiles usando el tokenizador
newsVec = [tokenizer.tokenize(title) for title in newsTiles]

"""Resultados de **títulos tokenizados**"""

# IVAN FALCON MONZON
# Muestra los títulos tokenizados
newsVec

"""####***3.4 Entrenamiento del modelo Word2Vec***

Se entrena un modelo de Word2Vec con los datos procesados:
"""

# IVAN FALCON MONZON
# Librería necesaría (cargada anteriormente):
# from gensim.models import Word2Vec

# Entrenamiento del modelo Word2Vec con los títulos tokenizados
model = Word2Vec(newsVec, min_count=1, vector_size=32)

"""####***3.5 Búsqueda de palabras similares***

Una vez entrenado el modelo, se pueden encontrar palabras con significados similares:
"""

# Encuentra las palabras más similares a 'man' en el espacio vectorial de Word2Vec
model.wv.most_similar('man')

"""También se pueden realizar operaciones semánticas, como:"""

# Realiza un cálculo de vectores para encontrar la relación entre 'King', 'man' y 'woman'
vec = model.wv['King'] - model.wv['man'] + model.wv['woman']

# Encuentra las palabras más similares al nuevo vector calculado
model.wv.most_similar([vec])

"""Representación vectorial de una palabra:"""

# Muestra el vector correspondiente a la palabra 'man' en el modelo Word2Vec
model.wv['man']

"""# **4. Uso de un modelo preentrenado de Word2Vec**

####***4.1 Descarga del modelo preentrenado***

Descargar el archivo y ponerlo en Google Drive, pesa 1,5GB.

Descargar Pretrain Word2vec model: https://drive.usercontent.google.com/download?id=0B7XkCwpI5KDYNlNUTTlSS21pQmM&export=download&authuser=1

####***4.2 Montaje de Google Drive en Colab***

Para cargar el modelo almacenado en Drive:
"""

# IVAN FALCON MONZON
# Importación de la librería para interactuar con Google Drive en Google Colab
from google.colab import drive

# Montar Google Drive para acceder a los archivos almacenados en él
drive.mount('/content/drive')

"""####***4.3 Carga del modelo preentrenado***

Se utiliza KeyedVectors  cargar el modelo:
"""

# IVAN FALCON MONZON
# Importación de la clase KeyedVectors de gensim para manejar modelos preentrenados
from gensim.models import KeyedVectors  # Importación correcta

# Especificar la ruta completa del archivo del modelo de Word2Vec (se debe cambiar la ruta según dónde se tenga el archivo)
file_path = '/content/drive/MyDrive/7PRO/GoogleNews-vectors-negative300.bin'

# Cargar el modelo preentrenado de Word2Vec desde el archivo binario usando la ruta especificada
# El parámetro 'binary=True' indica que el archivo está en formato binario y 'limit=100000' carga solo las primeras 100,000 palabras.
model = KeyedVectors.load_word2vec_format(file_path, binary=True, limit=100000)

"""Se puede verificar la carga con:"""

# IVAN FALCON MONZON
# Confirmar que el modelo se ha cargado correctamente
print("Modelo cargado correctamente.")

"""####***4.4 Operaciones vectoriales en el espacio semántico***

Se pueden realizar comparaciones semánticas similares a las realizadas con el modelo entrenado:
"""

# IVAN FALCON MONZON
# Realiza una operación vectorial para obtener una relación semántica entre 'King', 'man' y 'woman'
vec = model['King'] - model['man'] + model['woman']

# Encuentra las palabras más similares al vector calculado
model.most_similar([vec])

"""####***4.5 Ejemplos de comparaciones***

Ejemplo, comparando países y capitales:
"""

# IVAN FALCON MONZON
# Realiza una operación vectorial para obtener una relación semántica entre 'Germany', 'Berlin' y 'Madrid'
vec = model['Germany'] - model['Berlin'] + model['Madrid']

# Encuentra las palabras más similares al vector calculado
model.most_similar([vec])

"""Otro ejemplo, comparando fútbol y cricket:"""

# IVAN FALCON MONZON
# Realiza una operación vectorial para obtener una relación semántica entre 'Messi', 'football' y 'cricket'
vec = model['Messi'] - model['football'] + model['cricket']

# Encuentra las palabras más similares al vector calculado
model.most_similar([vec])

"""Otro ejemplo, comparando fútbol y tennis:"""

# IVAN FALCON MONZON
# Realiza una operación vectorial para obtener una relación semántica entre 'Messi', 'football' y 'tennis'
vec = model['Messi'] - model['football'] + model['tennis']

# Encuentra las palabras más similares al vector calculado
model.most_similar([vec])

"""# **5. Referencias y enlaces**

Google Colab: https://colab.research.google.com/drive/1M9rIN34j9dzDmotxVwOcn_70Mrl_KQeu?usp=sharing

 Github: https://github.com/IvanFalconMonzon/TA7_Gensim_Word2Vec_KeyedVectors_IvanFalconMonzon.git
"""