from __future__ import division
from count import Count
import math
from entropy import entropy

data = [
    {"Outlook": "Sunny", "Temperature": "Hot", "Humidity": "High", "Wind": "Weak", "PlayTennis": "No"},
    {"Outlook": "Sunny", "Temperature": "Hot", "Humidity": "High", "Wind": "Strong", "PlayTennis": "No"},
    {"Outlook": "Overcast", "Temperature": "Hot", "Humidity": "High", "Wind": "Weak", "PlayTennis": "Yes"},
    {"Outlook": "Rain", "Temperature": "Mild", "Humidity": "High", "Wind": "Weak", "PlayTennis": "Yes"},
    {"Outlook": "Rain", "Temperature": "Cool", "Humidity": "Normal", "Wind": "Weak", "PlayTennis": "Yes"},
    {"Outlook": "Rain", "Temperature": "Cool", "Humidity": "Normal", "Wind": "Strong", "PlayTennis": "No"},
    {"Outlook": "Overcast", "Temperature": "Cool", "Humidity": "Normal", "Wind": "Strong", "PlayTennis": "Yes"},
    {"Outlook": "Sunny", "Temperature": "Mild", "Humidity": "High", "Wind": "Weak", "PlayTennis": "No"},
    {"Outlook": "Sunny", "Temperature": "Cool", "Humidity": "Normal", "Wind": "Weak", "PlayTennis": "Yes"},
    {"Outlook": "Rain", "Temperature": "Mild", "Humidity": "Normal", "Wind": "Weak", "PlayTennis": "Yes"},
    {"Outlook": "Sunny", "Temperature": "Mild", "Humidity": "Normal", "Wind": "Strong", "PlayTennis": "Yes"},
    {"Outlook": "Overcast", "Temperature": "Mild", "Humidity": "High", "Wind": "Strong", "PlayTennis": "Yes"},
    {"Outlook": "Overcast", "Temperature": "Hot", "Humidity": "Normal", "Wind": "Weak", "PlayTennis": "Yes"},
]
attributeNames = ['Outlook', 'Temperature', 'Humidity', 'Wind']
dependencyAttribute = 'PlayTennis'


def selectAttribute(selectedAttribute, data):
    dd = {}
    for attrName in attributeNames:
        if attrName not in selectedAttribute:
            d = {}
            for item in data:
                d.setdefault(item[attrName], Count(0, 0))
                if item[dependencyAttribute] == 'Yes':
                    d[item[attrName]].addYes()
                else:
                    d[item[attrName]].addNo()
            totalEntropy = 0.0
            for key, value in d.iteritems():
                totalEntropy += (value.totalYesAndNo() / len(data)) * value.calculateEntropy()
            dd[attrName] = totalEntropy
    selected = min(dd, key=lambda k: dd[k])
    selectedAttribute.append(selected)
    return selected


def createTree(selectedAttribute, data, test):
    selectedAttribute = list(selectedAttribute)
    selected = selectAttribute(selectedAttribute, data)
    data2 = list(data)
    value = test[selected]
    count = Count(0, 0)
    for item in data2:
        if item[selected] == value and item[dependencyAttribute] == 'Yes':
            count.addYes()
        elif item[selected] == value and item[dependencyAttribute] == 'No':
            count.addNo()
    if count.yes == count.totalYesAndNo():
        return 'Yes'
    elif count.no == count.totalYesAndNo():
        return 'No'

    data3 = []
    for item in data2:
        if item[selected] == value:
            data3.append(item)

    return createTree(selectedAttribute, data3, test)


selectedAttribute = []
test1 = {"Outlook": "Rain", "Temperature": "Mild", "Humidity": "High", "Wind": "Strong"}
test2 = {"Outlook": "Overcast", "Temperature": "Mild", "Humidity": "High", "Wind": "Strong"}
print createTree(selectedAttribute, data, test1)
print createTree(selectedAttribute, data, test2)

