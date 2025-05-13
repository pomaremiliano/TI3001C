---
Fecha: Invalid date
Tipo: Notas
Clase:
  - Data Science
Status: In progress
---
## 🔁 Regresión Lineal - Recapitulación

- El análisis de regresión lineal busca ajustar una recta `y = mx + b` a un conjunto de datos.
- El **ajuste del modelo** se hace determinando los coeficientes `m` (pendiente) y `b` (intersección).
- Se utiliza el **método de mínimos cuadrados** para minimizar el error entre los valores reales y los predichos por el modelo.
- El **coeficiente de determinación R²** (entre 0 y 1) indica qué tan bien se ajusta el modelo. Un valor más cercano a 1 representa mejor ajuste.
- Las fórmulas vistas en clase se usan para estimar la recta óptima usando mínimos cuadrados.

### 📎 Ejercicio en Clase

- Ubicación: Carpeta `Clase6`.
- Archivos: `Ejercicio_Regresión_Lineal_Clase.ipynb` y `data.csv`.
- Objetivo: Completar el código y análisis en el notebook.

---

## 📈 ANOVA (Análisis de Varianza)

### 🧠 ¿Qué es?

- Método estadístico para probar **diferencias significativas entre medias** de dos o más grupos.
- Utiliza el **valor F** para medir el tamaño del efecto.
    - Si **F es grande**, hay diferencia.
    - Si **F es pequeño**, no hay efecto → se acepta la hipótesis nula (H₀).

### 📌 Hipótesis

- **H₀:** No existe diferencia significativa entre grupos.
- **H₁:** Existe diferencia significativa entre los grupos.

### 🧮 Fórmulas clave

- **F = MST / MSE**
- **MST = SST / (p - 1)**
- **MSE = SSE / (N - p)**
- **SSE = ∑ (n - 1) * s²**
- **SST = ∑ n(x - X̄)²**

Donde:

- `p`: número de grupos
- `n`: observaciones por grupo
- `N`: total de observaciones
- `X̄`: media global

### 🐾 Ejemplo: Mascotas

|   |   |   |   |   |
|---|---|---|---|---|
|Grupo|Observaciones|Media|Desviación estándar|Varianza|
|Perros|5|12|2|4|
|Gatos|5|16|1|1|
|Hamsters|5|20|4|16|

Cálculo:

- SST = 160
- MST = 80
- SSE = 84
- MSE = 7
- **F calculada = 11.42**

> Si F calculada > F tabular, se rechaza H₀
> 
> Si **F calculada ≤ F tabular**, se acepta H₀

Referencia tabla F: [Tabla de distribución F (UAAN)](http://www.uaaan.mx/~jmelbos/tablas/distf.pdf)

### 📉 p-value y confianza

- Intervalo de confianza típico: **95%**
- **p-value ≥ 0.05** → se acepta H₀
- **p-value < 0.05** → se rechaza H₀, se acepta H₁

---