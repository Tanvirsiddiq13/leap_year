def calculator():
    print("welcome to our calculator")
    print("this calculator can perform 4 calculation ")
    print("1.addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.division")
    while True:
        try:
            choise = input("choice one option 1/2/3/4:")
            if choise not in ["1","2","3","4"]:
                print("invalid option")
                continue
            first_number = int(input("first number: "))
            second_number = int(input("second number: "))
            if choise == "1":
                print(f'the addition of this two number is {first_number}+{second_number} = {first_number+second_number}')

            elif choise == "2":
                print(f"the subtraction of this two number is {first_number}-{second_number}= {first_number-second_number}")
            elif choise == "3":
                print(f'the multiplication of this two number is {first_number}*{second_number}= {first_number*second_number}')
            elif choise == "4":
                if second_number == 0:
                    print(f"Error:divide something by 0 isn't allowed")
                else:
                    print(f"the division of this two number is {first_number}/{second_number}= {first_number/second_number}")
            else:
                print("invalid choice")
                print(f'please chose option in between 1/2/3/4')
            furture_calculation =str((input("do you want to calculate another number?(yes/no)")))
            if furture_calculation == "no":
                print(f"thank you for using our calculator")
                break
            elif furture_calculation == "yes":
                print("okay,here again")
            else:
                print("invalid input please enter yos or no")
                break

        except ValueError:
            print("invalid input please enter yos or no")


if __name__ == "__main__":
    calculator()