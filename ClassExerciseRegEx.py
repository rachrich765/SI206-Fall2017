import re
opened_file = open('mbox-short.txt')
numlist = list()
for line in opened_file:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
# find all values in X-DSPAM-Confidence
# add them to a list of numbers
    if len(stuff) != 1 : continue
    num = float(stuff[0])
    numlist.append(num)
#determine number of values
number_of_values = len(numlist)
max_value = max(numlist)
min_value = min(numlist)
print ('Number of Values:',number_of_values)
print ('Maximum:', max_value)
print ('Minimum:', min_value)
#find average
average_value = sum(numlist)/len(numlist)
# format average to three decimal places
print ('Average:', "{:.3f}".format(average_value))
