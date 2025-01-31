if __name__ == "__main__":
    x = int(input("enter the value of an x:"))
    print(f"please separated each number by a space otherwise it doesn't work")
    print(f"and don't enter more then {x} students number ")
    arr = list(map(int,input("enter the number of the list:").split()))
    res = sorted(set(arr))
    print(f"list",res[0:])
    print("the champion",res[-1])
    print("runner-up",res[-2])