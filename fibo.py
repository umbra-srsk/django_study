# finonacci
# 0 1 1 2 3 5 8 13 ....

n = int(input('출력할 피보나츠 수열의 갯수는 :'))

a, b = 0, 1

i = 0
while i < n :
    print(a, end=' ')
    a, b = b, a + b
    i += 1