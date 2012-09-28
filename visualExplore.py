from operator import itemgetter, attrgetter
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

#function to remove rows that have "NULL" values in one of the elements
def removeNulls(l1,l2):
    zipped = zip(l1,l2)
    cleaned = []
    for elem in zipped:
        if 'NULL' not in elem:
            cleaned.append(elem)
    return zip(*cleaned)


data = {}

fh = open("emdata.tsv","r")
first = True
for line in fh:
    if first:
        fieldnames = line.rstrip("\n").split("\t")
        for flname in fieldnames:
            data[flname] = []
        first = False
    else:
        fields = line.rstrip("[\t\n]").split("\t")
        assert len(fields) == len(fieldnames)
        for i in range(len(fieldnames)):
            value = fields[i]
            if value == '':
                value = 'NULL'
            data[fieldnames[i]].append(value)

# Histogram cost
index, cost = removeNulls(range(len(data["Cost"])),data["Cost"])
cost2 = [np.log(float(item)) for item in cost]
fig = plt.figure()
ax = fig.add_subplot(131)
ax.set_xlabel("Log Cost")
ax.set_ylabel("Frequency")
ax.hist(cost2, 50, normed=1, facecolor="green")

#Boxplot Cost

#Scatter
cost, affected = removeNulls(data["Cost"],data["Affected"])
cost3 = [np.log(float(item)) for item in cost]
affected3 = [np.log(float(item)) for item in affected]
ax2 = fig.add_subplot(132)
ax2.set_xlabel("Log Cost")
ax2.set_ylabel("Log Affected")
ax2.scatter(cost3, affected3,s=70,c='b',marker='o',alpha=0.4)

# for categorical
keys, values = removeNulls(data["Country"],data["Killed"])
uniqueCountries = list(set(keys))
countryAvgCost = []
for country in uniqueCountries:
    idx = [item for item in range(len(keys)) if keys[item] == country]
    countryAvgCost.append(np.mean([float(values[k]) for k in idx]))

sortedCountries, sortedCosts = zip(*sorted(zip(uniqueCountries,countryAvgCost),key=itemgetter(1), reverse=True))
ax3 = fig.add_subplot(133)
ax3.set_xlabel("Country")
ax3.set_ylabel("Average Cost")
ax3.bar(np.arange(5),sortedCosts[:5])
plt.show()


#for i in range(len(sortedCountries)):
#    print sortedCountries[i] + ": " + str(sortedCosts[i])

