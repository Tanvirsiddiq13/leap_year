if __name__ == '__main__':
    x = int(input("enter the value of x:"))
    y = int(input("enter the value of y:"))
    z = int(input("enter the value of z:"))
    n = int(input("enter the value of n:"))
    result = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n]
    print(result)
if __name__ == '__main__':
    n = int(input("enter the value of n:"))
    print("please give the integers each separated by a space otherwise it doesn't work")
    arr = list(map(int, input("enter the value of the participant:").split()))
    max_num = max(arr)
    res = sorted(set(arr))
    print(f"the campion is",max_num)
    print(f"runner-up is",res[-2])

if __name__ == '__main__':
    students = []

    n = int(input("number of students:"))

    for _ in range(n):
        name = input("name")
        score = float(input("score"))
        students.append([name, score])

    unique_scores = sorted(set(score for _, score in students))

    second_lowest_score = unique_scores[1]

    second_lowest_students = [name for name, score in students if score == second_lowest_score]

    second_lowest_students.sort()

    for student in second_lowest_students:
        print(student)