if __name__ == '__main__':
    N = int(input())
    list = []
    for _ in range(N):
        command = input().strip().split()
        if command[0] == "insert":
            i = int(command[1])
            e = int(command[2])
            list.insert(i,e)
        elif command[0] == "print":
            print(list)
        elif command[0] == "remove":
            e = int(command[1])
           
            list.remove(e)
        elif command[0] == "append":
            e = int(command[1])
            list.append(e)     
        elif command [0]== "sort":
            command.sort()
        elif command[0] == "pop":
            command.pop()
        elif command[0] == "reverse":
            command.reverse()
