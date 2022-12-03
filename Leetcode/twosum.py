# getting list and target
num = [2, 5, 5, 11]
target = 10

# define list
answer = []

# define new list
num = list(enumerate(num))


# find items of list that sum of them equal target
for i in range(len(num)):
    for j in range(i + 1, len(num)):

        # checking the condition of program
        if num[i][1] + num[j][1] == target:

            # adding items to answer list
            answer.append(num[i][0])
            answer.append(num[j][0])

            # print answer and exit program
            print(answer)
            exit(0)



