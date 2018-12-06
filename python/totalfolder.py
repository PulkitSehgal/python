zoo = open(zoo.csv",'rt')
read_file = zoo.readlines()

water1 = 0
for i in read_file:
    y = i.split(',')
    if(y[0] == str(zebra)):
        water1 = water1 + int(y[2])

water2 = 0
for i in read_file:
    y = i.split(',')
    if(y[0] == str(tiger)):
        water2 = water2 + int(y[2])

water3 = 0
for i in read_file:
    y = i.split(',')
    if(y[0] == str(lion)):
        water3 = water3 + int(y[2])

        
water4 = 0
for i in read_file:
    y = i.split(',')
    if(y[0] == str(elephant)):
        water4 = water4 + int(y[2])


water5 = 0
for i in read_file:
    y = i.split(',')
    if(y[0] == str(kangroo)):
        water5 = water5 + int(y[2])


total_water=water1+water2+water3+water4+water5
print(total_water)

