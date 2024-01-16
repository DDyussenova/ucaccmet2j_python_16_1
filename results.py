import json 

file = open('ucaccmet2j_python_16_1\precipitation.json')

precipitation_data = json.load(file)

seattle_values = []

for seattle_station in precipitation_data: 
    if "GHCND:US1WAKG0038" == seattle_station['station']:
        seattle_values.append(seattle_station)


for individual_value in seattle_values: 
    date_string = individual_value['date'] 
    year, month, day = map(int, date_string.split('-'))
    individual_value['year'] = year 
    individual_value['month'] = month
    individual_value['day'] = day


total_monthly_precipitation = []

months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for x in months: 
    sum = 0
    for input in seattle_values:
        if x == input['month']:
            sum += input['value']
    total_monthly_precipitation.append(sum)
    
print(total_monthly_precipitation)

# for inidividual_month_value in seattle_values: 
#     month = inidividual_month_value['month'] 
#     if month in total_monthly_precipitation: 
#         total_monthly_precipitation[month] = total_monthly_precipitation[month]+ inidividual_month_value['value']
#     else: 
#         total_monthly_precipitation[month] = inidividual_month_value['value']

with open('results.json', 'w', encoding='utf-8') as file: 
    json.dump(total_monthly_precipitation, file, indent = 4)
