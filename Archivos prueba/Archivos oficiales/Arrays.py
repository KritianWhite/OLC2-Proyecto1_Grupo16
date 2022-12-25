a = [1,2,3,4,5]
b = [[1,2,3,4],[5,6,7,8]]
c = [[[1,2],[3,4]],[[5,6],[7,8]]]

for i in range(2):
    for j in range(2):
        for k in range(2):
            print(c[i][j][k])

print('')

for i in range(2):
    for j in range(4):
        print(b[i][j])

print('')

for element in a:
    print(element)