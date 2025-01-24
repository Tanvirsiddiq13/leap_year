year = int(input("ENTER THE YEAR"))

while True:
    if year % 4 == 0 and year % 100 == 0 and year % 400 != 0:
        print('False')
    elif year % 4 == 0 :
        print("True")
    elif year % 4 != 0:
        print('False')
    break