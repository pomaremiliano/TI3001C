---
Fecha: Invalid date
Tipo: Notas
Clase:
  - Data Science
Status: Done
---
## 🧠 ¿Qué es la regresión no lineal?

La **regresión no lineal** es una técnica estadística utilizada para modelar relaciones no lineales entre una variable dependiente y una o más variables independientes. A diferencia de la regresión lineal, esta técnica **no se restringe a relaciones lineales**, lo que permite capturar patrones más complejos en los datos.

- Utiliza **algoritmos iterativos** para estimar los parámetros del modelo.
- Puede adaptarse a relaciones **curvas, exponenciales, logísticas, etc.**

![[image 2.png|image 2.png]]

---

## 📈 Ejemplo de aplicación

**Predicción de población** en función del tiempo:

- Un gráfico de dispersión muestra una relación **no lineal** entre población y tiempo.
- Se puede utilizar un **modelo logístico de crecimiento poblacional** para hacer estimaciones más precisas de la población futura.

---

## 🔢 Tipos de variables

- Las variables **dependientes e independientes deben ser cuantitativas**.
- Las variables **categóricas deben recodificarse** como variables binarias o de contraste.

---

## 🔧 Parámetros del modelo

Los **parámetros** son los valores que el algoritmo estima, y pueden incluir:

- Constantes aditivas
- Coeficientes multiplicativos
- Exponentes
- Parámetros para evaluar funciones

Estos parámetros se definen con valores iniciales en el proceso de ajuste.

---

## 📊 Modelos comunes

Algunos ejemplos de modelos de regresión no lineal incluyen:

- **Curva Cuadrática**
- **Regresión Cúbica**
- **Regresión Exponencial**

---

## ✅ Ventajas

- Capturan **relaciones más complejas** que los modelos lineales.
- Ofrecen **mejores predicciones** cuando la relación entre variables no es lineal.

---

## ❌ Desventajas

- Estimación más **difícil y costosa computacionalmente**.
- Pueden ser **difíciles de interpretar**.
- Mayor riesgo de **sobreajuste**, especialmente con muestras pequeñas.

---

## ☑️ Tabla de modelos

|   |   |   |   |
|---|---|---|---|
|Modelo|Ecuación general|Parámetro `a` (significado típico)|Parámetro `b` (significado típico)|
|**Cuadrático**|y = a·x² + b·x + c|Coeficiente cuadrático|Coeficiente lineal|
|**Cúbico**|y = a·x³ + b·x² + c·x + d|Coeficiente cúbico|Coeficiente cuadrático|
|**Exponencial**|y = a·e^(b·x)|Valor inicial (escala)|Tasa de crecimiento|
|**Logarítmico**|y = a + b·ln(x)|Valor base o desplazamiento vertical|Tasa de crecimiento logarítmico|
|**Potencial**|y = a·x^b|Constante de proporcionalidad|Exponente de potencia|
|**Logístico**|y = a / (1 + e^(-b·(x - c)))|Límite superior (valor máximo)|Tasa de crecimiento|
|**Senoidal**|y = a·sin(b·x + c) + d|Amplitud de la oscilación|Frecuencia angular|

  

## 🧪 Ejercicio en clase

### Actividad:

- Revisa el notebook: `MachineLearningRegNonLinearRegression`
- Dataset: `china_gdp.csv`
    - Se puede descargar desde el notebook o está disponible en la carpeta compartida de la clase 8.
- Enfócate en:
    - Sección “Building the Model”
    - Sección “Practice”
- Al final, **agrega tus observaciones y conclusiones** del código y del proceso.

https://drive.google.com/file/d/1nu3vTjCcqZpKwvXmrss7F-pHDyeejTg1/view?usp=drive_link