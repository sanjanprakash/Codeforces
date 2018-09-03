a = int(raw_input())
b = int(raw_input())
c = int(raw_input())
arr = [(a + b) * c,a + (b * c),a * (b + c),(a * b) + c,a * b * c,a + b + c]
print max(arr)
