f = float(input())
s = float(input())
z = input()
if z == '+':
    print(f+s)
elif z == '-':
    print(f-s)
elif z == '*':
    print(f*s)
elif z == '/':
    if s != 0:
        print(f/s)