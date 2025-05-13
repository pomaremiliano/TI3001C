---
Fecha: Invalid date
Tipo: Notas
Clase:
  - Data Science
Status: In progress
---
## 🧮 ¿Qué es la regresión lineal?

Antes solo teníamos una variable independiente:

```Python
y = mx + b
```

Donde:

- `y` es la variable dependiente.
- `x` es la variable independiente.
- `m` es la pendiente.
- `b` es la intersección (bias).

## 📈 ¿Qué es la regresión lineal múltiple?

Es una extensión del modelo lineal simple que incluye **más de una variable independiente**. El modelo general es:

```Plain
y = b0 + b1*x1 + b2*x2 + ... + bn*xn
```

Donde:

- `y` sigue siendo la variable dependiente.
- `x1, x2, ..., xn` son variables independientes.
- `b0` es el término independiente.
- `b1, b2, ..., bn` son los coeficientes que representan la influencia de cada variable sobre `y`.

---

## 🧪 Ejemplo en Python

Se trabaja con el archivo **Clase7 – regresión lineal Múltiple.IPYNB** para mostrar cómo implementar el modelo en Python.

---

## 🧠 Ejercicio en Clase

Trabajar con el dataset `**unconv_MV_v5.csv**` que contiene información de pozos petroleros:

### 🎯 Objetivo:

Crear **tres modelos de regresión lineal múltiple**.

### 📌 Requisitos:

- Cada modelo debe tener **2 variables independientes distintas**.
- La variable dependiente en todos los casos será: **Producción por día (Prod)**.

### 📊 Análisis previo:

- Realizar un análisis de **correlación** entre variables (de forma numérica y gráfica).
- Elegir las variables independientes en base a los resultados de correlación.

### 📝 Documentación:

Durante el desarrollo del ejercicio, se deben anotar:

- Observaciones relevantes.
- Justificación de las variables seleccionadas.
- Resultados obtenidos en cada modelo.