# =================================================================
# == INSTITUTO TECNOLOGICO Y DE ESTUDIOS SUPERIORES DE OCCIDENTE ==
# ==         ITESO, UNIVERSIDAD JESUITA DE GUADALAJARA           ==
# ==                                                             ==
# ==            MAESTRÍA EN SISTEMAS COMPUTACIONALES             ==
# ==             PROGRAMACIÓN PARA ANÁLISIS DE DATOS             ==
# ==                 IMPLEMENTACIÓN EN STREAMLIT                 ==
# =================================================================

#----- Importación de Librerías -----------------------------------
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import random
from skimage import io


#------------------------------------------------------------------
#----- Configuración Inicial del Panel Central --------------------
#------------------------------------------------------------------

#----- Lectura de la Imagen ---------------------------------------
Logo = io.imread(r"./Imagenes/ITESO_Logo.png")

#----- Renderizado de la Imagen -----------------------------------
st.image(Logo, width = 500)

#----- Renderizado del Texto --------------------------------------
st.title("Uso Básico de Streamlit")
st.subheader(":blue[Streamlit es un *framework* para la creación de aplicaciones web "
             "interactivas y basadas en datos.]")


#------------------------------------------------------------------
#----- Configuración de los Elementos del DashBoard ---------------
#------------------------------------------------------------------

#----- Renderizado de la Imagen y el Título en el Dashboard -------
st.sidebar.image(Logo, width = 200)
st.sidebar.markdown("## MENÚ DE CONFIGURACIÓN")
st.sidebar.divider()

#----- HISTOGRAMA POR MES -----------------------------------------
#----- Selector del Mes -------------------------------------------
vars_mes = ['ENE','FEB','MAR','ABR','MAY','JUN','JUL','AGO','SEP','OCT','NOV','DIC']
default_hist = vars_mes.index('ENE')
histo_selected = st.sidebar.selectbox('Elección del Mes para el Histograma:', vars_mes, index = default_hist)
st.sidebar.divider()

#----- GRÁFICO DE LÍNEAS PARA LAS GANANCIAS -----------------------
#----- Selector de las Personas -----------------------------------
vars_per = ['Iñaki González','María Cázares','José García','Jérémie Muñoz','Agnès Villalón','Bérénice Pitkämäki',
            'Geneviève Rukajärvi','Hélène Ñuñoz','Ñaguí Grönholm','Iván Földváry']
default_pers = vars_per.index('Iñaki González')
ganan_selected = st.sidebar.selectbox('Elección de Persona para Mostrar las Ganancias Personales:', vars_per, index = default_pers)
st.sidebar.divider()

#----- GRÁFICO DE CORRELACIÓN DE LOS MESES ------------------------
#----- Selector del Mapa de Color ---------------------------------
vars_cmap = ['viridis', 'plasma', 'inferno', 'magma', 'cividis', 'Greys', 'Purples', 'Blues', 'Greens', 'Oranges',
             'Reds', 'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu', 'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn',
             'YlGn', 'binary', 'gist_yarg', 'gist_gray', 'gray', 'bone', 'pink', 'spring', 'summer', 'autumn', 'winter',
             'cool', 'Wistia', 'hot', 'afmhot', 'gist_heat', 'copper', 'PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu',
             'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic', 'twilight', 'twilight_shifted', 'hsv',
             'Pastel1', 'Pastel2', 'Paired', 'Accent', 'Dark2', 'Set1', 'Set2', 'Set3', 'tab10', 'tab20', 'tab20b',
             'tab20c', 'flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern', 'gnuplot', 'gnuplot2', 'CMRmap',
             'cubehelix', 'brg', 'gist_rainbow', 'rainbow', 'jet', 'turbo', 'nipy_spectral', 'gist_ncar']
color_selected = st.sidebar.selectbox('Paleta de Color para la Matriz de Correlación:', vars_cmap)
if st.sidebar.button('Color Aleatorio') == True:
    color_selected = random.choice(vars_cmap)

#----- Selector de Valores de Correlación para el Gráfico ---------
selec_val_corr = st.sidebar.radio("Valores de Correlación:", options = ['Activo', 'Inactivo'])
if selec_val_corr == 'Activo':
    anotacion = True
elif selec_val_corr == 'Inactivo':
    anotacion = False

#----- Selector de los Meses para el Histograma -------------------
mes_multi_selected = st.sidebar.multiselect('Elementos de la Matriz de Correlación:', vars_mes, default = vars_mes)


#------------------------------------------------------------------
#----- Configuración de Texto y Elementos del Panel Central -------
#------------------------------------------------------------------

#----- Lectura de los Datos Desde el Archivo CSV ------------------
datos_df = pd.read_csv('Datos_DF.csv')

#----- Renderizado del Texto --------------------------------------
st.markdown(":violet[**DATAFRAME PARA EL MANEJO DE INFORMACIÓN DE CLIENTES**]")
st.markdown(":blue[Este **DataFrame** contiene información de varias personas, "
            "las ciudades donde viven, así como sus ganancias a lo largo de un año. "
            "En esta aplicación se generan los siguientes gráficos:]")
st.markdown(":blue[*- **Histograma** para cada uno de los Meses del **DataFrame**.*]")
st.markdown(":blue[*- **Ganancias** para cada persona del **DataFrame**.*]")
st.markdown(":blue[*- **Matriz de Correlación** para los Meses Seleccionados del **DataFrame**.*]")
st.markdown(":violet[El **DataFrame** es el siguiente:]")

#----- Renderizado del DataFrame ----------------------------------
st.dataframe(datos_df)
st.divider()


#------------------------------------------------------------------
#----- Configuración de los Elementos del Panel Central -----------
#------------------------------------------------------------------

#Definición de las columnas
colum_izq, colum_der = st.columns(2)

#----- HISTOGRAMA POR MES -----------------------------------------
#Título para el gráfico
colum_izq.subheader('Histograma')

#Inicialización del gráfico
fig1, ax1 = plt.subplots()

#Generación del gráfico
sns.set(style = "darkgrid")
sns.histplot(data = datos_df[histo_selected])
ax1.set_title('Histograma de Valores')
ax1.set_xlabel(histo_selected)
ax1.set_ylabel('Frecuencia')

#Renderización del gráfico
colum_izq.pyplot(fig1)

#----- GRÁFICO DE LÍNEAS PARA LAS GANANCIAS -----------------------
#Título para el gráfico
colum_der.subheader('Ganancias')

#Inicialización del gráfico
fig2, ax2 = plt.subplots()

#Generación del gráfico
if ganan_selected == 'Iñaki González':
    periodo_df = datos_df.iloc[0]
elif ganan_selected == 'María Cázares':
    periodo_df = datos_df.iloc[1]
elif ganan_selected == 'José García':
    periodo_df = datos_df.iloc[2]
elif ganan_selected == 'Jérémie Muñoz':
    periodo_df = datos_df.iloc[3]
elif ganan_selected == 'Agnès Villalón':
    periodo_df = datos_df.iloc[4]
elif ganan_selected == 'Bérénice Pitkämäki':
    periodo_df = datos_df.iloc[5]
elif ganan_selected == 'Geneviève Rukajärvi':
    periodo_df = datos_df.iloc[6]
elif ganan_selected == 'Hélène Ñuñoz':
    periodo_df = datos_df.iloc[7]
elif ganan_selected == 'Ñaguí Grönholm':
    periodo_df = datos_df.iloc[8]
elif ganan_selected == 'Iván Földváry':
    periodo_df = datos_df.iloc[9]
else:
    periodo_df = datos_df
periodo_df = periodo_df.transpose()
periodo_df = periodo_df.to_frame()
periodo_df = periodo_df.rename(columns = {1: 'MES'})
periodo_df = periodo_df.drop(['NOMBRE','APELLIDO','CIUDAD'])
plt.plot(periodo_df)
ax2.set_title('Ganancias Mensuales por Persona')
ax2.set_xlabel(ganan_selected)
ax2.set_ylabel('Ganancias')

#Renderización del gráfico
colum_der.pyplot(fig2)
st.divider()

#----- GRÁFICO DE CORRELACIÓN DE LOS MESES ------------------------
#Título para el gráfico
st.subheader('Matriz de Correlación')

#Inicialización del gráfico
fig3, ax3 = plt.subplots()

#Generación del gráfico
df_corr = datos_df[mes_multi_selected].corr()
sns.heatmap(df_corr, annot = anotacion, fmt='.2f', cmap = color_selected)

#Renderización del gráfico
st.pyplot(fig3)
st.divider()