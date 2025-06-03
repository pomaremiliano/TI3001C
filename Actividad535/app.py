from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# Cargar datos y transformar los que necesitamos
df = pd.read_csv("HRDataset_v14.csv")


# Primero tengo que calcular la edad a partir de la fecha de nacimiento
df["DOB"] = pd.to_datetime(df["DOB"], errors="coerce", format=None)
today = pd.to_datetime("today")
df["Edad"] = (today - df["DOB"]).dt.days // 365

# Asegurarse que DOB no tiene nan
df = df[df["DOB"].notna() & (df["DOB"] < today)]

# Calcular edad
df["Edad"] = ((today - df["DOB"]).dt.days // 365).astype(int)

# Filtrar edades razonables porque hay errores en los datos
df = df[(df["Edad"] > 17) & (df["Edad"] < 100)]  # por ejemplo: 18 a 99 años

# Diagrama de dispersión Edad vs Salario
fig1 = px.scatter(
    df,
    x="Edad",
    y="Salary",
    color="Sex",
    title="Diagrama de dispersión: Edad vs Salario",
    hover_data=["Employee_Name", "Department", "Position"],
    labels={"Edad": "Edad", "Salary": "Salario"},
)

fig2 = px.box(
    df,
    x="Department",
    y="Salary",
    color="Department",
    points="all",
    title="Distribución de salarios por departamento",
)
fig2.update_layout(showlegend=False)

fig3 = px.histogram(
    df,
    x="DOB",
    color="Sex",
    nbins=30,
    title="Distribución de edades por género",
    labels={"DOB": "Fecha de nacimiento"},
    marginal="rug",
    hover_data=df.columns,
)
fig3.update_layout(bargap=0.1)

fig4 = px.box(
    df,
    x="Sex",
    y="Absences",
    color="Sex",
    points="all",
    title="Distribución de ausencias por género",
    labels={"Sex": "Género", "Absences": "Ausencias"},
)

satisfaccion_promedio = (
    df.groupby("RecruitmentSource")["EmpSatisfaction"].mean().reset_index()
)
fig5 = px.bar(
    satisfaccion_promedio,
    x="RecruitmentSource",
    y="EmpSatisfaction",
    color="EmpSatisfaction",  # el tono del color va a depender de la satisfacción
    color_continuous_scale="Blues",  # azul porque es como melancólico
    title="Nivel de satisfacción promedio por fuente de reclutamiento",
    labels={
        "RecruitmentSource": "Fuente de Reclutamiento",
        "EmpSatisfaction": "Satisfacción Promedio",
    },
    hover_data={"EmpSatisfaction": ":.2f"},
)
fig5.update_layout(xaxis_tickangle=-45)

fig6 = px.histogram(
    df,
    x="Salary",
    nbins=30,
    title="Histograma de distribución de salarios por departamento",
    labels={"Salary": "Salario"},
)
fig6.update_layout(bargap=0.1)

fig7 = px.pie(
    df,
    names="PerformanceScore",
    title="Distribución de puntajes de desempeño",
    color="PerformanceScore",
    hole=0.3,
)
fig7.update_traces(
    textinfo="percent+label", pull=[0.05] * df["PerformanceScore"].nunique()
)

despedidos = df[df["Termd"] == 1]


despedidos_por_departamento = despedidos["Department"].value_counts().reset_index()
despedidos_por_departamento.columns = ["Department", "NumDespedidos"]

fig8 = px.bar(
    despedidos_por_departamento,
    x="Department",
    y="NumDespedidos",
    color="NumDespedidos",
    color_continuous_scale="Reds",  # Escala de colores en tonos rojos porque es asociado a despidos y es grave
    title="Departamentos con mayor número de empleados despedidos",
    labels={"Department": "Departamento", "NumDespedidos": "Empleados Despedidos"},
    hover_data={"NumDespedidos": True},
)
fig8.update_layout(xaxis_tickangle=-45)

df["DateofHire"] = pd.to_datetime(df["DateofHire"])
df["Antiguedad_Anios"] = (pd.to_datetime("today") - df["DateofHire"]).dt.days / 365

fig9 = px.scatter(
    df,
    x="Antiguedad_Anios",
    y="Salary",
    trendline="ols",
    labels={"Antiguedad_Anios": "Antigüedad (Años)", "Salary": "Salario"},
    title="Relación entre Antigüedad y Salario",
)

fig10 = px.histogram(
    df,
    x="Position",
    color="Sex",
    barmode="group",
    title="Distribución de puestos por género",
    labels={"Position": "Puesto", "Sex": "Género"},
)
fig10.update_layout(xaxis_tickangle=-45)

# Crear la app
app = Dash(__name__)

# Layout de la app
app.layout = html.Div(
    [
        html.H1(
            "Dashboard de HRDataset",
            style={"textAlign": "center", "marginBottom": "40px", "fontFamily": "Arial, sans-serif"},
        ),
        html.Div(
            [
                html.Div(
                    [
                        dcc.Graph(figure=fig1, style={"height": "350px"}),
                        dcc.Graph(figure=fig2, style={"height": "350px"}),
                    ],
                    style={"flex": "1", "padding": "10px"},
                ),
                html.Div(
                    [
                        dcc.Graph(figure=fig3, style={"height": "350px"}),
                        dcc.Graph(figure=fig4, style={"height": "350px"}),
                    ],
                    style={"flex": "1", "padding": "10px"},
                ),
            ],
            style={
                "display": "flex",
                "gap": "20px",
                "marginBottom": "30px",
                "background": "#f9f9f9",
                "borderRadius": "10px",
                "boxShadow": "0 2px 8px #ccc",
                "overflowY": "scroll",
                "maxHeight": "100vh",
            },
        ),
        html.Div(
            [
                html.Div(
                    [
                        dcc.Graph(figure=fig5, style={"height": "350px"}),
                        dcc.Graph(figure=fig6, style={"height": "350px"}),
                    ],
                    style={"flex": "1", "padding": "10px"},
                ),
                html.Div(
                    [
                        dcc.Graph(figure=fig7, style={"height": "350px"}),
                        dcc.Graph(figure=fig8, style={"height": "350px"}),
                    ],
                    style={"flex": "1", "padding": "10px"},
                ),
            ],
            style={
                "display": "flex",
                "gap": "20px",
                "marginBottom": "30px",
                "background": "#f9f9f9",
                "borderRadius": "10px",
                "boxShadow": "0 2px 8px #ccc",
            },
        ),
        html.Div(
            [
                dcc.Graph(
                    figure=fig9,
                    style={
                        "height": "350px",
                        "width": "48%",
                        "display": "inline-block",
                        "marginRight": "2%",
                    },
                ),
                dcc.Graph(
                    figure=fig10,
                    style={
                        "height": "350px",
                        "width": "48%",
                        "display": "inline-block",
                    },
                ),
            ],
            style={
                "display": "flex",
                "gap": "20px",
                "background": "#f9f9f9",
                "borderRadius": "10px",
                "boxShadow": "0 2px 8px #ccc",
            },
        ),
    ],
    style={"padding": "40px", "background": "#eaeaea", "minHeight": "100vh"},
)

# Ejecutar
if __name__ == "__main__":
    app.run(debug=True)
