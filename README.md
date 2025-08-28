# 🦠 Detector de Virus mediante Autómatas Finitos

## 📌 Introducción
El presente proyecto tiene como finalidad la implementación de un **analizador de virus** desarrollado en **Python**, basado en el uso de **Autómatas Finitos Deterministas (AFD)** diseñados en la herramienta **JFLAP**.  
El sistema recorre los archivos en formato digital y determina, a partir de la lectura de su contenido en bytes, si se encuentra presente alguna de las secuencias definidas como virus.  

---

## 🎯 Objetivo
Implementar un programa que recorra un archivo una sola vez, identificando si contiene alguna secuencia de bytes correspondiente a un virus predefinido.  

### Objetivos específicos
1. Diseñar autómatas finitos en JFLAP que representen las secuencias de los virus a analizar.  
2. Implementar un sistema en Python que realice la detección de virus mediante la lectura de archivos en bytes.  
3. Validar el funcionamiento del analizador con archivos de prueba que simulen infecciones.  

---

## 📚 Fundamentación Teórica
La detección de patrones en archivos digitales puede modelarse mediante el uso de **Autómatas Finitos**, los cuales son estructuras matemáticas capaces de reconocer lenguajes formales y patrones específicos.  

En este caso, cada virus se modela como una **secuencia finita de 4 bytes en orden exacto**. El autómata diseñado en JFLAP permite simular el reconocimiento de dichas secuencias, y posteriormente su lógica es trasladada al código en Python.  

De esta manera, el sistema implementa un **reconocimiento determinista**, recorriendo el archivo una única vez y estableciendo el estado final en el que se detiene la máquina.

---

## 🧬 Virus considerados
El programa identifica los siguientes virus a partir de su secuencia característica de cuatro bytes:

| Virus       | Secuencia (Bytes decimales) |
|-------------|------------------------------|
| Usama       | 15 – 30 – 15 – 49 |
| Amtrax      | 72 – 72 – 15 – 29 |
| Ébola       | 29 – 32 – 53 – 29 |
| Ah1N1       | 72 – 32 – 32 – 20 |
| Covid19     | 30 – 25 – 20 – 19 |

Un archivo se considera infectado si contiene, en cualquier parte de su contenido, alguna de las secuencias anteriores.  

---

## ⚙️ Metodología de Implementación

1. **Diseño del autómata**: Creación de los AFD en JFLAP para cada virus.  
2. **Definición de patrones**: Representación de las secuencias de virus como listas de bytes en Python.  
3. **Lectura del archivo**: Conversión del contenido a un vector de bytes para su análisis.  
4. **Análisis**: Recorrido del archivo con la máquina de estados, determinando si el archivo contiene un virus.  
5. **Salida de resultados**:  
   - Nombre del archivo analizado.  
   - Contenido del archivo en bytes.  
   - Virus detectado o mensaje *“No encontrado”*.  
   - Estado en el cual se detuvo el autómata.  

---

## 📂 Estructura del Proyecto

```plaintext
TComp-AnalizadorVirus/
│── archivosJFLAP/       # Autómatas diseñados en JFLAP
│── archivosPrueba/      # Archivos de prueba
│── controladores/       # Lógica del analizador
│   │── admin_archivo.py # Lectura de archivos
│   │── analizador.py    # Implementación del autómata
│── modelos/             # Espacio reservado para clases adicionales
│── vistas/              # Interfaz gráfica (Tkinter)
│   │── ventana.py
│── main.py              # Punto de entrada del programa
│── README.md            # Documento de referencia (este archivo)
```


## 🚀 Ejecución del Programa
Para iniciar el sistema, desde la carpeta raíz del proyecto ejecutar:

```bash
python main.py
```

## 👩‍💻 Autores

Proyecto desarrollado por Nicolás Buitrago Paredes y Maria Alejandra Vargas como parte de la asignatura **Teoría de la Computación**.

