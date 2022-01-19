import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd

#arrays to hold data in order to create numpy array
temperature_array = []
january = []
february = []
march = []
april = []
may = []
june = []
july = []
august = []
september = []
october = []
november = []
december = []

#function to create heatmap
def create_heatmap_heathrow(id, start_date, end_date, weather_type):
    #weather_type max, min, frost, rainfall, sunshine
    #import data
    df = pd.read_csv('heathrow_weather_data1.txt', delim_whitespace=True, skiprows=6, header=0, names=['Year',
'Month', 'Mean daily maximum temperature', 'Mean daily minimum temperature', 'Days of air frost', 'Total rainfall, mm', 'Total sunshine hours'])
    df['Total sunshine hours'] = df['Total sunshine hours'].str.replace('#','')
    
    #use user input to generate x-axis
    years=[]
    for year in range(start_date, end_date):
        years.append(year)
    
    #generate numpy array
    num = weather_type +1
    for year in years:
        for item in range(1,13):
            dataframe_row = df[(df.Year == year) & (df.Month == item)]
            if item == 1:
                january.append(dataframe_row.iat[0,num])
            elif item == 2:
                february.append(dataframe_row.iat[0,num])
            elif item == 3:
                march.append(dataframe_row.iat[0,num])
            elif item == 4:
                april.append(dataframe_row.iat[0,num])
            elif item == 5:
                may.append(dataframe_row.iat[0,num])
            elif item == 6:
                june.append(dataframe_row.iat[0,num])
            elif item == 7:
                july.append(dataframe_row.iat[0,num])
            elif item == 8:
                august.append(dataframe_row.iat[0,num])
            elif item == 9:
                september.append(dataframe_row.iat[0,num])
            elif item == 10:
                october.append(dataframe_row.iat[0,num])
            elif item == 11:
                november.append(dataframe_row.iat[0,num])
            else:
                december.append(dataframe_row.iat[0,num])
        temperature_array.append(december)
        temperature_array.append(november)
        temperature_array.append(october)
        temperature_array.append(september)
        temperature_array.append(august)
        temperature_array.append(july)
        temperature_array.append(june)
        temperature_array.append(may)
        temperature_array.append(april)
        temperature_array.append(march)
        temperature_array.append(february)
        temperature_array.append(january)
    mean_temp = np.asarray(temperature_array)

    #choose which heatmap to create
    sns.heatmap(mean_temp, cmap="seismic", center=10)
    
    #generate the image file
    plt.savefig(f"static/{id}.png")
    plt.close()
