x = 673


# check to be 32 bit
def check_32_bit(x):
    if x < (-2 ** 31) or x > (2 ** 31 - 1):
        return 0
    else:
        return x


temp = abs(x)
temp_2 = 0
answer = 0

# compute number of digit
while temp > 0:
    temp_2 += 1
    temp = int(temp / 10)

temp = abs(x)

# compute reverse of number
while temp > 0:
    answer += (temp % 10) * 10 ** (temp_2 - 1)
    temp_2 -= 1
    temp = int(temp / 10)

# check to being positive or negative and being 32 bit
if x < 0:
    answer *= -1
    answer = check_32_bit(answer)
    print(answer)
else:
    answer = check_32_bit(answer)
    print(answer)
