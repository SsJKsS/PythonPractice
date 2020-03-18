n = int(input())

print('打印直角三角形')
for i in range(n):
    print("* " * (i + 1))

print('打印逆直角三角形')
for i in range(n):
    print(" " * i)
    for j in range(n - i):
        print("*" , end = ' ')  # 使用end不換行

print('')  # 換行

print('打印等腰三角形')
for i in range(n):
	for j in range(0,n - i):
		print(end=' ')  # 使用end不換行
	for k in range(n - i,n):
		print('*',end=' ')  # 使用end不換行
	print('')  # 換行
