# 8- if- else or Conditional statements  excersise

weight = float(input("Weight pounds: "))
unit = (input("(K)g  or  (L)bs: "))

if unit.upper == 'K':
    convert = weight/0.45
    print("Weight in Lbs: ", convert)
else:
    convert = weight * 0.45
    print("Weight in Kgs: ", convert)

