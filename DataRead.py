file = open("diabetic_data_initial.csv",'r')

header = file.readline().split(",")
data = []

for line in file:
    line.split(',')
    data.append(line.split(','))