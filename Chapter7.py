def sumNegativeInts(userList):
    userList = []
    sum = 0
    for i in userList:
            if i < 0:
                sum = sum + i
            return sum

userList = input("Enter a list of +/- integers: ")
print(sumNegativeInts(userList))