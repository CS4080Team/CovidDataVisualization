from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import datetime

#day of the week (yyyy-mm-dd) of data
date=[]

#total confirmed cases
confirmedCases=[]

#running total of number of deaths caused by covid
deathsTotal=[]

#running total of people that recovered from covid
recovered=[]

#total active cases
activeCases=[]

#new cases for that day
newCases=[]

#new deaths for that day
newDeaths=[]

#number of people who recovered that day
newRecovered=[]

#Deaths per 100 people
deathsPer100 =[]

#Recovered per 100 cases
recoveredPer100=[]

#Deaths per 100 people that recovered
deathsPer100recovered=[]

#Number of countries with an active case of covid
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

def DailyCasesVsDeaths():
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

def CovidAnalysisByDaysOftheWeek():
    weekdaysCases = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    weekdaysDeaths = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    totalDays = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    for i in range(len(date)):
        components = date[i].split('-')
        year, month, day = int(components[0]), int(components[1]), int(components[2])
        my_date = datetime.date(year, month, day)
        day_of_week = my_date.weekday()
        weekdaysCases[day_of_week] += newCases[i]
        weekdaysDeaths[day_of_week] += newDeaths[i]
        totalDays[day_of_week] +=1
    avgPerDayCases = {"Monday":0, "Tuesday":0, "Wednesday:":0, "Thursday":0, "Friday":0, "Saturday":0,"Sunday":0}
    avgPerDayDeaths = {"Monday": 0, "Tuesday": 0, "Wednesday:": 0, "Thursday": 0, "Friday": 0, "Saturday": 0,
                      "Sunday": 0}
    i=0
    for day in avgPerDayDeaths:
        avgPerDayDeaths[day] = int(weekdaysDeaths[i]/totalDays[i])
        i+=1
    i = 0
    for day in avgPerDayCases:
        avgPerDayCases[day] = int(weekdaysCases[i] / totalDays[i])
        i += 1
    daysCases = list(avgPerDayCases.keys())
    avgCases = list(avgPerDayCases.values())
    avgDeaths = list(avgPerDayDeaths.values())

    fig = plt.figure(figsize=(10,10))
    plt.bar(daysCases,avgCases, color="Green", width=0.8, edgecolor='Black', linewidth=1)
    plt.bar(daysCases,avgDeaths, color="Red", width=0.8, edgecolor='Black', linewidth=2)
    plt.ylabel("Covid Cases")
    plt.xlabel("Days of the week")
    plt.legend(["Cases", "Deaths"])
    plt.title("Avg cases by day of the week (Jan 21, 2020 - July 26, 2020)")
    plt.show()


if __name__ == "__main__":
    intializeDataSet()
    DailyCasesVsDeaths()
    CovidAnalysisByDaysOftheWeek()