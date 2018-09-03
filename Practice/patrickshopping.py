d1,d2,d3 = map(int,raw_input().split())
arr = [d1 + d2 + d3,(2 * d1) + (2 * d2),(2 * d1) + (2 * d3),(2 * d2) + (2 * d3),(3 * d1) + d2 + d3,d1 + (3 * d2) + d3]
print min(arr)
