s = "srghaiuhiusfpr"
numRow = 4
answer_list = []
answer = ""

# create rows in list
for i in range(numRow):
    answer_list.append("")

# check if rows == 1
if numRow == 1:
    answer = s
    print(answer)
    exit(0)

temp = 0
temp_2 = 0
temp_3 = numRow - 1

# check the change point to not be 0
if temp_3 == 0:
    temp_3 = 1


# fill answer list
for i in range(len(s)):

    # add char to answer list
    answer_list[temp] += s[i]

    # compute change point
    if i % temp_3 == 0 and i != 0:
        temp_2 += 1

    # check the index we want to add
    if temp_2 % temp_3 == 0:
        temp += 1
    else:
        temp -= 1

# convert answer list to string
for i in answer_list:
    answer += i

print(answer)




