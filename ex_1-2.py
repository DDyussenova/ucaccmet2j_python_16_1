import json 

#3
# I did not have time to do the third part of the assignment. But I was planning on opening the csv file. 

# file_ = open('ucaccmet2j_python_16_1/stations.csv')
# station_codes = file_.read()

#Then, I would figure out how I can match the codes from the csv file to the json file. 
#Afterwards, I would modify the existing code so that it calculates the relative precipitation values for all of the stations. 
#Then I would compare the realtive yearly precipitation among all of the locations and calculate which percentage of these fell in Seattle. 


#1 
#Loading the data from the JSON file 
file = open('ucaccmet2j_python_16_1\precipitation.json')
precipitation_data = json.load(file)

#Opening a list that would contain the precipitation values from Seattle station.  
seattle_values = []

for seattle_station in precipitation_data: 
    if "GHCND:US1WAKG0038" == seattle_station['station']:
        seattle_values.append(seattle_station)

#Splitting the dates into months, so that total precipiation values for each month can be accessed. 
for individual_value in seattle_values: 
    date_string = individual_value['date'] 
    year, month, day = map(int, date_string.split('-'))
    individual_value['year'] = year 
    individual_value['month'] = month
    individual_value['day'] = day

#Opening a list with total monthly percipitations that can store the correspoding information. 
total_monthly_precipitation = []

#Introducing a list of months. 
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

#Calculating the total monthly percipitation for each of the months in Seattle in 2010 and appending them to the list. 
for x in months: 
    sum_ = 0
    for input in seattle_values:
        if x == input['month']:
            sum_ += input['value']
    total_monthly_precipitation.append(sum_)
    
print(total_monthly_precipitation)

#Opening a result.json file and transferring the total monthly precipitation data into it. 
with open('results.json', 'w', encoding='utf-8') as file: 
    json.dump(total_monthly_precipitation, file, indent = 4)

#2

#Calculating the total yearly precipitation by summing all the values in the total_monthly_precipitation list. 
total_yearly_precipitation = sum(total_monthly_precipitation)
print(total_yearly_precipitation)

#Opening a list where the relative monthly precipitation for each month can be stored. 
relative_monthly_precipitation = []

#Calculating teh relative monthly precipitation and appnding the values to the list. 
for part_month in total_monthly_precipitation: 
    relative = part_month/ total_yearly_precipitation
    relative_monthly_precipitation.append(relative) 

print(relative_monthly_precipitation) 

#Transferring the relative monthly precipiation data into the existing results.json file. The previous values would be overridden. 
with open('results.json', 'w', encoding='utf-8') as file: 
    json.dump(relative_monthly_precipitation, file, indent = 4)

