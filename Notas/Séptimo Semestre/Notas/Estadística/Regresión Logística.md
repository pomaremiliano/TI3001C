---
Fecha: Invalid date
Tipo: Notas
Clase:
  - Data Science
Status: In progress
---
### 📌 ¿Qué es la regresión logística?

- Técnica de análisis de datos que modela la relación entre variables independientes y una variable dependiente categórica (como **sí/no**, **verdadero/falso**, etc.).
- Ideal para problemas de clasificación binaria.
- Se basa en la probabilidad de que un evento ocurra dado un conjunto de variables.

### 🎯 **Ejemplo práctico**

- Predicción de si un usuario hace clic en un botón de pago:
    - Variables: tiempo en sitio, número de artículos en carrito.
    - Si el usuario pasa >5 minutos y tiene >3 artículos → alta probabilidad de hacer clic.
    - Se entrena con datos históricos para hacer predicciones con nuevos usuarios.

### ✅ **Ventajas de la regresión logística**

- **Simplicidad:** modelo matemáticamente menos complejo.
- **Velocidad:** eficiente con grandes volúmenes de datos, requiere menos recursos.
- **Flexibilidad:** puede adaptarse a variables con 2 o más resultados finitos.
- **Visibilidad:** más interpretable que otros métodos de machine learning.

### 🧠 **Concepto clave: Matriz de Confusión**

- Herramienta para evaluar el rendimiento del modelo.
- Permite calcular:
    - **Accuracy** (precisión global)
    - **Precision** (verdaderos positivos entre todos los positivos predichos)
    - **Recall** (verdaderos positivos entre todos los positivos reales)

---

### 🧪 **Ejercicio en clase (Python + Dataset:** `**diabetes2.csv**`**)**

1. **Selecciona variables relevantes** del dataset (2 o 3).
2. **Normaliza los valores** (para que tengan la misma escala).
3. **Divide el dataset** en datos de entrenamiento y prueba.
4. **Ajusta el modelo** con los datos de entrenamiento.
5. **Evalúa el modelo**:
    - Usa la **matriz de confusión**.
    - Calcula **Accuracy, Precision y Recall**.
6. **Repite el proceso** con un nuevo conjunto de variables.