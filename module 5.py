months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
rainfall = []
no_of_months = 0
total_inches = 0
years = int(input('How many years do you want for the average rainfall calculation: '))
for i in range(0, years):
    for month in months:
        rainfall.append(input(f'What is the rainfall for {month} (in inches): '))
        no_of_months +=1
for rain in rainfall:
    total_inches += int(rain)
avg_inches = total_inches/len(rainfall)
print(f'Number of years: {years}')
print(f'Number of months: {no_of_months}')
print(f'Total Rainfall over {years} year(s): {total_inches}')
print(f'Average Rainfall over {years} year(s): {avg_inches}')
    