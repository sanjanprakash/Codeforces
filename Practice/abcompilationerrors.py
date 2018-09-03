n = input()
a = map(int,raw_input().split())
b = map(int,raw_input().split())
c = map(int,raw_input().split())
a.sort()
b.sort()
c.sort()
flag = False
for i in range(0,n - 1) :
	if (a[i] != b[i]) :
		print a[i]
		flag = True
		break
if (flag == False) :
	print a[n - 1]
flag = False
for i in range(0,n - 2) :
	if (b[i] != c[i]) :
		print b[i]
		flag = True
		break
if (flag == False) :
	print b[n - 2]
