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


# for categorical
keys, values = removeNulls(data["Country"],data["Killed"])
uniqueCountries = list(set(keys))
countryAvgCost = []
for country in uniqueCountries:
    idx = [item for item in range(len(keys)) if keys[item] == country]
    countryAvgCost.append(np.mean([float(values[k]) for k in idx]))

sortedCountries, sortedCosts = zip(*sorted(zip(uniqueCountries,countryAvgCost),key=itemgetter(1), reverse=True))
for i in range(5):
    print sortedCountries[i] + ": " + str(sortedCosts[i])

