#MEASURING BMI

#STORING HEIGHT
HeightInFoot = input (" ENTER YOUR HEIGHT [FOOT] > ")

HeightInInch = input (" ENTER YOUR HEIGHT [INCH] > ")

#VALUE OF
oneFoot = 0.3048
oneInch = 0.0254

#calculating proper heigt
Height = (HeightInFoot)*(oneFoot) + (HeightInInch)*(oneInch)

#STORING WEIGHT
WeightInKG = input("ENTER YOUR WEIGHT [KG] > ")

#CALCULATING BMI
BMI = (WeightInKG)/(Height**2)

print(BMI)

