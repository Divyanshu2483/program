d = {}
n = int(input())
for _ in range(n):
    k, v = input().split()
    d[k] = int(v)

key_max = max(d, key=d.get)
print(key_max)
#Output:
#Enter number of entries: 3
#Enter key and value: c 3
#Enter key and value: a 1
#Enter key and value: b 2
#c
#Enter number of entries: 2
#Enter key and value: x 10
#Enter key and value: y 20
#y

    