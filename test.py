with open('datafile', 'r') as f: lines = f.readlines()

print('lines : ', lines)
print('*' * 50)

i = 0
ican = 0
high = 0
seemhigh = 0
s1 = '높으편'
s2 = 'C++'

for line in lines:
    if line.find(s2) > 0: ican += 1
    #elif line.find(s1) >= 0: high += 1
    elif line.find('아주높다') : high += 1
    elif line.find('높으편') : seemhigh += 1
    else: print(i, line)
    print('*' * 50)
    i += 1

print('*' * 50)
print(i, 'lines')
print('C++', ican)
print('아주높다', high)
print('높으편', seemhigh)
