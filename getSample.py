f = open('asmc.sample', 'w')
length = int(input())

f.write('ID_1 ID_2 missing\n0 0 0\n')
for i in range(1, length+1):
    f.write('1_' + str(i+1) + ' 1_' + str(i+1) + ' 0\n')

f.close()
