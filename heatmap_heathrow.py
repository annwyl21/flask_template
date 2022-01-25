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

headers = ['Year',
'Month', 'Mean daily maximum temperature', 'Mean daily minimum temperature', 'Days of air frost', 'Total rainfall, mm', 'Total sunshine hours']

#function to create heatmap
def create_heatmap_heathrow(id, start_date, end_date, weather_type):
    #import data
    df = pd.read_csv('heathrow_weather_data1.txt', delim_whitespace=True, skiprows=6, header=0, names=headers)
    df['Total sunshine hours'] = df['Total sunshine hours'].str.replace('#','')
    df["Days of air frost"] = pd.to_numeric(df["Days of air frost"], errors='coerce')
    df["Total sunshine hours"] = pd.to_numeric(df["Total sunshine hours"], errors='coerce')
    #print(df.info())
    #print(df.head())
    #print(df.isnull().head())
    
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
    #manage the figsize based on the number of years requested
    if len(years) > 10:
        fig, ax = plt.subplots(figsize = (9, 3))   
        if weather_type == 1:
            sns.heatmap(mean_temp, cmap="seismic", center=10)
        elif weather_type == 2:
            sns.heatmap(mean_temp, cmap="bwr", center=4)
        elif weather_type == 3:
            sns.heatmap(mean_temp, cmap="coolwarm_r")
        #_r to reverse the colours
        elif weather_type == 4:
            sns.heatmap(mean_temp, cmap="Blues")
        else:
            sns.heatmap(mean_temp, cmap="afmhot")
    else:
        fig, ax = plt.subplots()
        if weather_type == 1:
            sns.heatmap(mean_temp, cmap="seismic", center=10, annot=True, annot_kws={"size": 2})
        elif weather_type == 2:
            sns.heatmap(mean_temp, cmap="bwr", center=4, annot=True)
        elif weather_type == 3:
            sns.heatmap(mean_temp, cmap="coolwarm_r", annot=True)
        elif weather_type == 4:
            sns.heatmap(mean_temp, cmap="Blues", annot=True)
        else:
            sns.heatmap(mean_temp, cmap="afmhot", annot=True)

    #set axes
    #Set the axis labels, rotate, size and alignment of label
    #x-axis
    ax.set_xticklabels(years)
    plt.setp(ax.get_xticklabels(), rotation=45, size=5)
    #y-axis
    months = ['Dec', 'Nov', 'Oct', 'Sep', 'Aug', 'Jul', 'Jun', 'May', 'Apr', 'Mar', 'Feb', 'Jan']
    ax.set_yticklabels(months)
    plt.setp(ax.get_yticklabels(), rotation=0, size=7) 

    the_title = headers[num] #putting the column header into the title
    ax.set_title("Heathrow - {t} {s} and {e}".format(t=the_title, s=start_date, e=end_date))
    ax.set_xlabel('Time Period {s} to {e}'.format(s=start_date, e=end_date))
    ax.set_ylabel('Months')
    
    #generate the image file
    #plt.savefig(f"static/{id}.png")
    plt.show()
    plt.close()

create_heatmap_heathrow(888, 2010, 2020, 5)
