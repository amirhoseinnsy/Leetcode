x = -15342


# check to be 32 bit
def check_p_n(x):
    if x < (-2 ** 31) or x > (2 ** 31 - 1):
        return 0
    else:
        return x


# reverse string of x
temp = x
x = str(abs(x))
x = x[::-1]
x = int(x)

# check to being positive or negative
if temp < 0:
    x *= -1
    x = check_p_n(x)
    print(x)
else:
    x = check_p_n(x)
    print(x)
