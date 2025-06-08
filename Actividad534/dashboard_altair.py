# Dashboard de Altair con Streamlit Actividad 5.3.4
# Jorge Emiliano Pomar
# A01709338
# Fecha: 07 de junio de 2025

import streamlit as st
import altair as alt
import pandas as pd

# Cargar datos
df = pd.read_csv("2016-1.csv")

# Definir paleta de colores
colors = ["#1c64b4", "#f9cb22", "#8c946c", "#8aacdc", "#8cb4dc"]  # colores de Cinépolis
st.image(
    "https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Cin%C3%A9polis_logo.svg/3000px-Cin%C3%A9polis_logo.svg.png",
    caption="Logo de Cinépolis",
    use_column_width=True,
)
st.title("Altair Chart Dashboard Actividad 5.3.4.")
st.write("Jorge Emiliano Pomar A01709338")



componentes = [
    "Economy (GDP per Capita)",
    "Family",
    "Health (Life Expectancy)",
    "Freedom",
    "Trust (Government Corruption)",
    "Generosity",
]

region_avg = df.groupby("Region")[componentes].mean().reset_index()
region_avg_melt = region_avg.melt(
    id_vars="Region", var_name="Componente", value_name="Valor"
)

graph1 = (
    alt.Chart(region_avg_melt)
    .mark_rect()
    .encode(
        x=alt.X("Componente:N", title="Componente"),
        y=alt.Y("Region:N", title="Región"),
        color=alt.Color("Valor:Q", scale=alt.Scale(scheme="blues")),
        tooltip=["Region", "Componente", "Valor"],
    )
    .properties(title="Promedio de Componentes del Bienestar por Región")
)
st.title("1. Heatmap de componentes del bienestar por región")
st.altair_chart(graph1, use_container_width=True)
st.info(
    """
    - Este heatmap muestra que el componente que más peso tiene en la sensación de bienestar es la economía GDP en la mayoría de las regiones. Igualmente, para muchas regiones, la familia parece ser más importante que los demás componentes, incluso la Salud. Y además, lo que menos tiene peso en cualquiera de los países es la confianza en el gobierno por su corrupción. Probablemente esto lo vemos claro en México y otros países tercermundistas donde hay mucha corrupción que es parte de la cultura y la gente no confía en el gobierno. Pero eso no significa que la gente no sea feliz, sino que la gente se adapta a las circunstancias y busca su bienestar en otros aspectos como la familia, la economía y la salud. Aquí utilicé la escala de azules de la paleta de cinépolis porque creo que se puede jugar más fácilmente con los tonos de azul para mostrar diferentes niveles de valores.
    """
)

graph2 = (
    alt.Chart(df)
    .mark_circle()
    .encode(
        x=alt.X("Freedom:Q", title="Libertad"),
        y=alt.Y("Trust (Government Corruption):Q", title="Confianza en el Gobierno"),
        size=alt.Size("Happiness Score", title="Puntaje de Felicidad"),
        color=alt.Color("Region:N", scale=alt.Scale(range=colors)),
        tooltip=[
            "Country",
            "Region",
            "Happiness Score",
            "Freedom",
            "Trust (Government Corruption)",
        ],
    )
    .properties(title="Confianza vs Libertad con Tamaño según Felicidad")
)
st.title("2. Bubble chart de la Libertad contra la corrupción y la confianza con el gobierno")
st.altair_chart(graph2, use_container_width=True)
st.info(
    "- Esta gráfica de burbujas muestra que hay una relación positiva entre la libertad y la confianza en el gobierno, así como un tamaño de burbuja que indica el puntaje de felicidad de cada país. Los países con mayor libertad tienden a tener una mayor confianza en el gobierno y, en general, un mayor puntaje de felicidad. Aquí debo admitir que me faltaron más colores, porque en esta gráfica si se presta a que cada region tenga un color diferente de burbuja. Aún así creo que se ve bien con los colores de la paleta de cinépolis, ya que el azul es un color que transmite confianza y seguridad, lo cual es importante en este tipo de gráficas. Además, el amarillo resalta las burbujas más grandes, lo que ayuda a identificar los países con mayor puntaje de felicidad."
)

graph3 = (
    alt.Chart(df)
    .mark_circle(color=colors[1], size=60)
    .encode(x=f"Happiness Rank:Q", y=f"Happiness Score:Q")
    .properties(title=f"Dispersión entre Happiness Rank y Happiness Score")
)
st.title("3. Gráfica de dispersión entre Happiness Rank y Happiness Score")
st.altair_chart(graph3, use_container_width=True)
st.info(
    """- Este mapa de dispersión es muy obvio. La relación entre el ranking y el score se ve gradualmente. Pero fue interesante ver si había alguna caída abrupta entre algun país a otro, pero la verdad es que no. Se ve muy consistente la relación entre el ranking y el score. Los países con un puntaje más alto tienden a tener un ranking más bajo, lo que indica que son considerados más felices. Por otro lado, los países con un puntaje más bajo tienden a tener un ranking más alto, lo que indica que son considerados menos felices. Esta gráfica se presta a que solo tenga un color, en este cado utilicé el amarillo de la paleta de cinépolis, ya que es un color que resalta y ayuda a identificar los puntos en la gráfica. Además, el amarillo es un color que transmite felicidad y optimismo, lo cual es apropiado para esta gráfica que trata sobre la felicidad de los países.
    """
)

graph4 = (
    alt.Chart(df)
    .mark_line(color=colors[4], point=True)
    .encode(
        x="Country:O", y="Happiness Score:Q", tooltip=["Country", "Happiness Score"]
    )
    .properties(title="Happiness Score vs. Happiness Rank")
)
st.title("4. Gráfica de línea de happiness score por país")
st.altair_chart(graph4, use_container_width=True)
st.info(
    """- Este gráfico de líneas muestra que de manera visual que tan alto es el índice de felicidad en cada país. Poco se puede conlcuír de esto más que la tendencia general de que los países más desarrollados tienden a tener un mayor índice de felicidad. Utilicé el azul claro para las líneas y los puntos de azul obscuro. En este caso creo que no se necesita más que un color suave a la vista para que no distraiga de la tendencia general de la gráfica. """
)

# Definir los umbrales para alto, medio y bajo
bins = [df["Trust (Government Corruption)"].min(), 0.2, 0.4, df["Trust (Government Corruption)"].max()]
labels = ["Bajo", "Medio", "Alto"]

df["Corrupción Nivel"] = pd.cut(df["Trust (Government Corruption)"], bins=bins, labels=labels, include_lowest=True)

color_map = {"Bajo": colors[2], "Medio": colors[0], "Alto": colors[1]}

graph5 = (
    alt.Chart(df)
    .mark_bar()
    .encode(
        x=alt.X("Country:N", sort="-y", title="País"),
        y=alt.Y("Trust (Government Corruption):Q", title="Corrupción de Gobierno"),
        color=alt.Color("Corrupción Nivel:N", scale=alt.Scale(domain=list(color_map.keys()), range=list(color_map.values())), title="Nivel de Corrupción"),
        tooltip=["Country", "Region", "Trust (Government Corruption)", "Corrupción Nivel"],
    )
    .properties(title="Corrupción de Gobierno por País (Alto, Medio, Bajo)")
)
st.title("5. Gráfica de la corrupción de cada país")
st.altair_chart(graph5, use_container_width=True)
st.info(
    """- Este gráfico de barras igual tiene a todos los países y muestra el índice de corrupción de cada uno. El tooltip igual indica la región a la que pertenece el país. En este caso, el índice de corrupción no tiene una tendencia clara hacia países desarrollados o subdesarrollados. Están ambas categorías muy dispersas. Lo que sí es que es interesante ver países muy autoritarios como China y Rusia con un índice de corrupción muy bajo. Aquí decidí definir umbrales de alto medio y bajo nivel de corrupción. Y gracias a eso, elegí el verde oliva para los países con bajo nivel de corrupción, el azul para los países con medio nivel de corrupción y el amarillo para los países con alto nivel de corrupción. Esto ayuda a identificar rápidamente los niveles de corrupción en cada país y a comparar entre ellos. Además, el verde oliva es un color que transmite estabilidad y confianza, lo cual es apropiado para este tipo de gráficas que tratan sobre la corrupción en los gobiernos."""
)

graph6 = (
    alt.Chart(df)
    .mark_circle(size=60)
    .encode(
        x="Economy (GDP per Capita)",
        y="Happiness Score",
        color=alt.Color("Region", scale=alt.Scale(range=colors)),
        tooltip=["Country", "Region", "Happiness Score", "Economy (GDP per Capita)"],
    )
    .properties(title="Relación entre Economía y Felicidad")
)
st.title("6. Gráfico de dispersión entre la felicidad y la economía GDP per cápita")
st.altair_chart(graph6, use_container_width=True)
st.info(
    """- Lo que se puede observar en el gráfico de dispersión es que simplemente los países con mayor puntaje de felicidad también son los países más prósperos en cuanto a la economía. Más adelante podremos ver cómo se relacionan estos dos factores de manera más detallada. Elegí todos los colores de la paleta de cinépolis para los puntos, ya que creo que se ve bien y ayuda a identificar los puntos en la gráfica."""
)

componentes = ['Economy (GDP per Capita)', 'Family', 'Health (Life Expectancy)', 
               'Freedom', 'Trust (Government Corruption)', 'Generosity']

top5 = df.nlargest(5, "Happiness Score").melt(id_vars=["Country"], value_vars=componentes)

graph7 = (
    alt.Chart(top5)
    .mark_bar()
    .encode(
        x=alt.X("value:Q", stack="zero", title="Suma de Componentes"),
        y=alt.Y("Country:N", title="País"),
        color=alt.Color("variable:N", scale=alt.Scale(range=colors)),
        tooltip=["Country", "variable", "value"]
    )
    .properties(title="Componentes del Bienestar en los 5 Países más Felices")
)

st.title("7. Gráfico de pilas de componentes que dan felicidad a los 5 países más felices")
st.altair_chart(graph7, use_container_width=True)
st.info(
    """- Aquí se concentran los 5 países más felices, y podemos ver que la economía es el componente más importante en todos los casos. Sin embargo, la familia y la salud también juegan un papel importante en la felicidad de estos países. Es interesante ver que, a pesar de que la economía es el componente más importante, no es el único factor que contribuye a la felicidad de las personas en estos países. La familia y la salud también son componentes importantes que deben ser considerados al analizar el bienestar de las personas. Utilicé los diferentes colores de la paleta de cinépolis para cada componente, lo que ayuda a identificar rápidamente los diferentes componentes que contribuyen a la felicidad en cada país. Además, el uso de colores contrastantes ayuda a resaltar las diferencias entre los componentes y a hacer que la gráfica sea más fácil de entender. """
)
# Graph 8 combinada
# Agregamos un selection point de regiones
selection = alt.selection_point(fields=['Region'], bind='legend', name='Región')

# Primera grafica de regiones y cantidad de países
graph_selector = alt.Chart(df).mark_bar().encode(
    y=alt.Y('Region:N', sort='-x'),
    x=alt.X('count():Q', title='Cantidad de Países'),
    color=alt.Color('Region:N', scale=alt.Scale(range=colors)),
    opacity=alt.condition(selection, alt.value(1), alt.value(0.2))
).add_params(selection).properties(title="Selecciona una Región")

# Gráfica secundaria, se marca la region seleccionada y se muestra la info
graph_detail = alt.Chart(df).mark_circle(size=100).encode(
    x=alt.X('Economy (GDP per Capita):Q', title='Economía (PIB per cápita)'),
    y=alt.Y('Happiness Score:Q', title='Puntaje de Felicidad'),
    color=alt.Color('Region:N', scale=alt.Scale(range=colors)),
    tooltip=['Country', 'Region', 'Happiness Score', 'Economy (GDP per Capita)'],
    opacity=alt.condition(selection, alt.value(1), alt.value(0))
).transform_filter(selection).properties(title="Economía vs Felicidad por País (según Región seleccionada)")

st.title("8. Economía vs Felicidad por País (según Región seleccionada)")
st.altair_chart((graph_selector & graph_detail).resolve_scale(color='independent'), use_container_width=True)
st.info(
    """- Complementando la gráfica de barras de felicidad por país, aquí hay una distribución de los puntajes de felicidad por región. Se puede ver que la región de América del Norte tiene el puntaje más alto, seguida por Europa Occidental y América Latina. Por otro lado, África subsahara y Asia del Sur tienen los puntajes más bajos. Aquí si se puede ver claramente que las regiones más desarrolladas tienden a tener un mayor puntaje de felicidad, mientras que las regiones menos desarrolladas tienden a tener un menor puntaje de felicidad. Si faltaron colores porque en ocasiones se repiten para las regiones y los países, pero creo que si se logran identificar en ambas gráficas. A parte cuando das click en una región, se resalta la región seleccionada en ambas gráficas, lo que ayuda a identificar rápidamente los puntajes de felicidad por región."""
)

st.title("Conclusiones")
st.markdown(
    """
- ¿Cuál es la importancia de una buena elección de color para la representación de datos?
    - La elección de colores puede mejorar la legibilidad y comprensión de los datos, además de hacer las gráficas más atractivas visualmente. 
    - Los colores contrastantes ayudan a distinguir categorías y facilitan la interpretación.
    - En este caso, se me hace buena paleta de colores la de cinépolis, pero para gráficas más extensas como las de barras, se quedan cortos los colores, y intentando prolongarlos, solo pude poner escala de azules que no se distinguen tanto. 

- ¿Altair es una buena librería para realizar gráficas? Comenta ventajas y desventajas
    - Yo la verdad prefiero plotly, creo que es más fácil la modificación de los estilos y tamaños que en altair. Ahorita tuve problemas para modificar los tamaños porque son muy cerrados los gráficos. Probablemente tenga que ver que son gráficas interpretadas que se pasan a Java Script.
    - Ventajas: 
      - Tienen muchos gráficos y algunos no están en plotly. 
      - Es más fácil la declaración de los comandos y creo que en general se hacen gráficos igual de complejos con menos comandos. 
    - Desventajas:
      - Es muy cerrado y no hay tanto control de costumización.
      - Hay cosas que no entiendo porque vienen de Vega Lite y pues es una curva de aprendizaje adicional. Plotly es más nativo de python a mi gusto. 

"""
)
