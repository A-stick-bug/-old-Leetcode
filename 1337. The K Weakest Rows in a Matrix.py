mat = [[1, 1, 0, 0, 0], [1, 1, 1, 1, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 1, 1, 1]]
k = 3

weakest = {}
index = 0

for i in mat:
    weak = i.count(0)
    weakest[index] = weak

    index += 1

x = sorted(weakest.items(), key=lambda x:x[1], reverse=True)
new = dict(x)

arr = []

for x in new.keys():
    arr.append(x)

print(arr[:k])
