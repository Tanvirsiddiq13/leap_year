if __name__ == '__main__':
    n = int(input("enter the number of students:"))
    student_marks = {}
    for _ in range(n):
        name, *line = input("enter student name and scores:").split()
        scores = list(map(float, line))
        student_marks[name] = scores
        print( scores)

    query_name = input("enter query name: ")
    average_mark = sum(student_marks[query_name])/len(student_marks[query_name])
    print(f"{average_mark:.2f}")
