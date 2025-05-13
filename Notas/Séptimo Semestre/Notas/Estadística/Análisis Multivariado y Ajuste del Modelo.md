---
Fecha: Invalid date
Tipo: Notas
Clase:
  - Data Science
Status: Done
---
## 🧪 Análisis Multivariado

### ¿Qué es?

- Estudio simultáneo de múltiples variables para entender relaciones complejas.
- Se utilizan cuando hay varias variables dependientes e independientes involucradas.

### Ejemplo:

- Evaluación de productos químicos para limpiar derrames de aceite.
    - **Variables independientes:** tipos de sustancias químicas.
    - **Variables dependientes:** dispersión, desintoxicación, toxicidad, impacto ambiental.

### Ventajas:

- Permite un análisis más completo y realista.
- Considera interacciones entre variables.
- Mejora la precisión y validez de las conclusiones.

### Herramientas Visuales:

- **Pairplot:** muestra relaciones bivariadas entre variables numéricas.
- **Joinplot:** compara dos variables con gráficos combinados (dispersión y distribución).
- **Matriz de calor (heatmap):** identifica correlaciones entre variables.

---

## 🧩 Ejercicio en Clase

Usar el dataset `mpg` para:

- Crear un **pairplot** con las variables numéricas.
- Generar una **matriz de calor** sintetizada.
- Realizar **joinplots** de `mpg` contra las demás variables numéricas.

---

## 📈 Ajuste del Modelo

### Punto de Partida

- Se plantea como una función matemática que representa la relación entre variables.

### Función Lineal

- Relación directa entre variable dependiente (Y) e independiente (X):

```Plain
Y = aX + b
```

### Tipos de Pendientes:

- **Pendiente = 0:** recta horizontal.
- **Pendiente positiva:** correlación positiva.
- **Pendiente negativa:** correlación negativa.
- **Pendiente infinita:** recta vertical.

## ⚠️ Consideraciones del Ajuste

- Se deben revisar supuestos como:
    - Linealidad
    - Homocedasticidad
    - Normalidad de errores
    - Independencia de errores

---

## 🎥 Actividad en Clase

Revisar los siguientes videos para entender el ajuste por mínimos cuadrados:

- [🔗 Video 1](https://www.youtube.com/watch?v=k964_uNn3l0)
- [🔗 Video 2](https://www.youtube.com/watch?v=gUdU6BgnJ2c)