a=int(input())
b=int(input())
for i in range(a, b+1):
    c=str(i)
    d=str(i)[::-1]
    if c == d:
        print(c)
input()
