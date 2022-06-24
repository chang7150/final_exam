from cmath import e


num = int(input())
for i in range(1, num-1, 2):
    print(" "*(num//2)+str(i))
for i in range(1, num+1, 2):
    print(i, end='')
for i in range(num-2, 0, -2):
    print(i, end='')
print()
for i in range(num-2, 0, -2):
    print(" "*(num//2)+str(i))