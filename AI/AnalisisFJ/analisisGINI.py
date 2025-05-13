import pandas as pd

def gini_impurity(df, target_col):
    total = len(df)
    if total == 0:
        return 0  # Nodo vacío
    
    proportions = df[target_col].value_counts(normalize=True)
    gini = 1 - sum(proportions ** 2)
    return gini

# Cargar el archivo Excel
def process_gini(file_path):
    df = pd.read_excel(file_path, sheet_name="Respuestas de formulario 1")
    
    # Calcular Gini del nodo raíz
    gini_root = gini_impurity(df, "Desenlace")
    
    # Dividir por "Afinidad de mentalidad"
    MENTALITY_AFFINITY_COL = "Afinidad de mentalidad"
    threshold = df[MENTALITY_AFFINITY_COL].median()
    low_affinity = df[df[MENTALITY_AFFINITY_COL] <= threshold]
    high_affinity = df[df[MENTALITY_AFFINITY_COL] > threshold]
    
    # Calcular Gini de los nodos generados
    gini_low_affinity = gini_impurity(low_affinity, "Desenlace")
    gini_high_affinity = gini_impurity(high_affinity, "Desenlace")
    
    return {
        "Gini Root": gini_root,
        "Gini Low Affinity": gini_low_affinity,
        "Gini High Affinity": gini_high_affinity
    }

# Llamar a la función con el archivo correspondiente
file_path = "AI/AnalisisFJ\Cupido FJ25 (Respuestas).xlsx"
gini_values = process_gini(file_path)
print(gini_values)
