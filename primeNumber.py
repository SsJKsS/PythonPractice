tmp = 0

for num in range(2, 101):
    for i in range(2, num):
        if num % i == 0:
            tmp += 1

    if tmp > 0:
        tmp = 0
    else:
        print(num, "是質數")

