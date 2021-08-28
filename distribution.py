import csv
import numpy as np
import matplotlib.pyplot as plt
#------------Which file----------------------#
ddir = "C:\\Users\\Salber\\Documents\\Project\\Probability_dist"

type_sim = "MISA_Vor"
file_name = "pdist_voronoi_250_bins.csv"

path = ddir + "\\" + type_sim + "\\" + file_name

#----------------Averager---------------------#
with open(path,'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    averages = []
    boolean = 1
    rows = 0
    #---------------Summing----------------#
    for row in csv_reader:
        rows += 1
        columns = len(row)
        for index in range(0,columns):    
            if boolean<1+len(row):
                averages.append(float(row[index]))
                #print("hi")
                boolean += 1
            else:
                averages[index] += float(row[index])
                
    #------------------Average--------------#
    for index in range(0,len(averages)):
        averages[index] = averages[index] / rows
    

#----------------Histogram Plotter-----------------#
plt.subplot(2,1,1)
plt.bar(idk,averages)
plt.ylabel('Bin weights')
plt.title('Probability Distribution of the 2-gene MISA model')
print(plt.xlim())

plt.subplot(2,1,2)
plt.hist(data,300)
plt.xlabel('Bins')
plt.ylabel('Frequency')
plt.xlim(-51.56,1230)

plt.show()
