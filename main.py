from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

date=[]
confirmedCases=[]
deathsTotal=[]
recovered=[]
activeCases=[]
newCases=[]
newDeaths=[]
newRecovered=[]
deathsPer100 =[]
recoveredPer100=[]
deathsPer100recovered=[]
numberCountries=[]

def intializeDataSet():
    from csv import reader
    with open('day_wise.csv','r') as read_obj:
        csv_reader = reader(read_obj)
        next(csv_reader)
        for row in csv_reader:
            date.append(row[0])
            confirmedCases.append(int(row[1]))
            deathsTotal.append(int(row[2]))
            recovered.append(int(row[3]))
            activeCases.append(int(row[4]))
            newCases.append(int(row[5]))
            newDeaths.append(int(row[6]))
            newRecovered.append(int(row[7]))
            deathsPer100.append(float(row[8]))
            recoveredPer100.append(float(row[9]))
            deathsPer100recovered.append(float(row[10]))
            numberCountries.append(int(row[11]))

def scatterPlot():
    loc = np.arange(len(date))
    width=0.01
    fig,ax= plt.subplots()
    plt1 = ax.bar(loc-width, newCases, label="Daily Cases")
    plt2 = ax.bar(loc-width, newDeaths, label="Daily Deaths")
    ax.set_ylabel('People')
    ax.set_xlabel('Days since First Case')
    ax.set_xticks(np.arange(0, len(date), 30))
    ax.legend()
    plt.show()

    deathsPerCase=[]
    for i in range(0, len(date)):
        if newDeaths[i] != 0 and newCases[i] != 0:
            deathsPerCase.append(newDeaths[i] / newCases[i])

    loc = np.arange(len(deathsPerCase))
    width=.5
    fig, ax = plt.subplots()
    plt3 = ax.bar(loc-width, deathsPerCase, label='Deaths per case')
    ax.set_ylabel('Deaths')
    ax.set_xlabel('Days since first case')
    ax.set_xticks(np.arange(0, len(date), 30))
    ax.legend()
    plt.show()


if __name__ == "__main__":
    intializeDataSet()
    scatterPlot()