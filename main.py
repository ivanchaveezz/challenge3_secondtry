# PYBANK
import csv

with open("/Users/ivanchavez/Desktop/BOOTCAMP TEC DATA /CHALLENGES/Starter_Code-8/PyBank/Resources/budget_data.csv", mode = "r") as file:
    csvFile = csv.reader(file, delimiter=",")
    csvFile2 = list(csvFile)

header  = csvFile2.pop(0)

print("FINANCIAL ANALYSIS")
print("------------------------")

#TOTAL NUMBER OF MONTHS INCLUDED IN DATASET
tot_months = len(csvFile2) - 1
print("Total de meses" , tot_months)

#NET TOTAL AMOUNT OF "PROFIT/LOSSES"
prof_loss = [row[1] for row in csvFile2]
prof_loss.pop(0)
int_prof_loss = list(map(int, prof_loss))
prof_loss_sum = sum(int_prof_loss)
print("Total : $" , prof_loss_sum)

#CHANGES IN "PROFIT/LOSSES" OVER PERIOD AND AVERAGE
avg_change = [0]*(len(csvFile2)-2)
j = list(range(len(csvFile2)-2))

for x in j:
    avg_change[x] = int_prof_loss[x+1] - int_prof_loss[x]

avg_change_val = (sum(avg_change)/(len(csvFile2)-2))
print("Average Change: $" , avg_change_val)

#BIGGEST CHANGE AND DATE
dates = [row[0] for row in csvFile2]
dates.pop(0)
dates.pop(0)
new_list = [item for sublist in zip(dates, avg_change) for item in sublist]
new_list = [new_list[i: i + 2] for i in range(0, len(new_list), 2)]
#print(new_list)

def Sort(List):
    List.sort(key = lambda l: l[1])
    return List

avg_change_sort = Sort(new_list)
print("Greatest Increase in Profits:" , avg_change_sort.pop(-1))

#BIGGEST DECREASE AND DATE
print("Greatest Decrease in Profits:" , avg_change_sort.pop(0))



