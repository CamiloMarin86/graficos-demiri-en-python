#%%
import pandas as pd
import numpy as np 
from matplotlib import pyplot as plt
import pandas_bokeh
from bokeh.plotting import output_file, output_notebook
#pd.set_option('plotting.backend', 'pandas_bokeh')


#%%
DataFile = pd.ExcelFile('6Bus.xlsx')
#ComparativeLast.xlsx

# %%
#Para comparar resultados de Formulaciones:

FOb_performance = DataFile.parse(1).set_index("Parametros")
df_despachos = DataFile.parse(2).set_index("tiempo")
df_flujos = DataFile.parse(3).set_index("tiempo")
df_MCs = DataFile.parse(4).set_index("Sims")

#Para comparar resultados para diferentes Errores de incertidumbre:

FOb_performance_Error = DataFile.parse(5).set_index("Parametros")
df_despachos_Error = DataFile.parse(6).set_index("tiempo")
df_MCs_Error = DataFile.parse(7).set_index("Sims")

# %%
FOb_performance.plot_bokeh.bar(
    figsize = (500,400),
    colormap=['#d73027','#fc8d59','#fee08b','#d9ef8b','#91cf60','#1a9850'],
    title = "Desempeño de Modelos",
    xlabel = "Periodos",
    ylabel = "Parametros de desempeño",
        )   
#output_file('Desempeño.HTML')
output_notebook() 


#%%GRAFICAS PARA LOS GENERADORES

for i in df_despachos.generador.unique().tolist()[:]:
    df_despachos.groupby('generador').get_group(i).iloc[:,:7].plot_bokeh.line(
    #df_despachos[df_despachos.generador.isin([(i)])].iloc[:,:7].plot_bokeh.line(
    figsize = (800,500),
    colormap=['#66c2a5','#fc8d62','#8da0cb','#e78ac3','#a6d854','#ffd92f'],
    title = "Despacho del Generador "+ (i) + "[MW]",
    xlabel =" Periodos",
    ylabel = "Potencia [MW]",
    plot_data_points = True,
    marker ="o",
    vertical_xlabel=True,
    hovertool= True
        )
    output_notebook()     
    #output_file(f'{i}.HTML')


# %%
df_MCs=df_MCs.set_index('Porcentaje _de_ Error')
#df_MCsErr.index=100*df_MCsErr.index

df_MCs.plot_bokeh.line(
    figsize = (1500,300),
    #xticks= df['Porcentaje _de_ Error'].tolist(),
    colormap=['#d73027','#fc8d59','#fee08b','#d9ef8b','#91cf60','#1a9850'],
    title = "MonteCarlo Para Modelos ",
    xlabel =" '%' Error",
    ylabel = "Numero de infactibilidades",
    plot_data_points = True,
    marker ="*",
    vertical_xlabel=True,
    hovertool= True
    )
  
#output_file('MCs.HTML') 
output_notebook()    

   
#%%GRAFICAS PARA LOS GENERADORES

for i in df_despachos_Error.generador.unique().tolist()[:]:
    df_despachos_Error.groupby('generador').get_group(i).iloc[:,:8].plot_bokeh.line(
    #df_despachos_Error[df_despachos.generador.isin([(i)])].iloc[:,:7].plot_bokeh.line(
    figsize = (800,500),
    colormap=['#66c2a5','#fc8d62','#8da0cb','#e78ac3','#a6d854','#ffd92f'],
    title = "Despacho del Generador "+ (i) + "[MW]",
    xlabel =" Periodos",
    ylabel = "Potencia [MW]",
    plot_data_points = True,
    marker ="o",
    vertical_xlabel=True,
    hovertool= True
        )
    output_notebook()     
    #output_file(f'{i}.HTML')


# %%
df_MCs_Error.plot_bokeh.line(
    figsize = (1500,300),
    #xticks= df['Porcentaje _de_ Error'].tolist(),
    colormap=['#d73027','#fc8d59','#fee08b','#d9ef8b','#91cf60','#1a9850'],
    title = "MonteCarlo Para Modelos ",
    xlabel =" '%' Error",
    ylabel = "Numero de infactibilidades",
    plot_data_points = True,
    marker ="*",
    vertical_xlabel=True,
    hovertool= True
    )
  
#output_file('MCs.HTML') 
output_notebook() 
# %%
