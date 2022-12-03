s = "-bac"


# check to answer be 32bit
def check_32bit(x):
    if x < -2 ** 31:
        return -2 ** 31
    elif x > 2 ** 31 - 1:
        return 2 ** 31 - 1
    else:
        return x


answer = ""
p_n = 0
s = s.strip()
temp = ""


# find number part of string
def number(x):
    number = ""
    for i in x:
        if not i.isdigit():
            break
        number += i
    return int(number)


# check if s was empty
if len(s) == 0:
    answer = 0
    print(answer)
    exit(0)

for i in range(len(s)):

    # check to start with number
    if not (s[0] == "+" or s[0] == "-"):
        if not s[0].isdigit():
            answer = 0
            print(answer)
            exit(0)

    if temp == "+" or temp == "-":

        # check to be number after + or -
        if not s[i].isdigit():
            answer = 0
            print(answer)
            exit(0)

        # check to noy have to + or -
        if s[i] == "-" or s[i] == "+":
            answer = 0
            print(answer)
            exit(0)

        # check the number be positive or negative
        if temp == "+":
            p_n = 1
        else:
            p_n = -1

        # find number part
        if s[i].isdigit():
            answer = number(s[i:len(s)])
            break
        else:
            continue
    elif s[i].isdigit():
        p_n = 1
        answer = number(s[i:len(s)])
        break
    temp = s[i]

    # check to not have 1 + or -
    if len(s) == 1:
        if not s[i].isdigit():
            answer = 0
            print(answer)
            exit(0)

answer *= p_n
answer = check_32bit(answer)
print(answer)
