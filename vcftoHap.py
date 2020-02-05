filename = input()
f = open(filename, 'r')
k = 1
str = ""

for line in f:
    if k == 10001:
        break
    print(k)
    list = line.split()

    str += list[0]
    str += " " + list[2]
    str += " " + list[1]
    str += " " + list[3]
    str += " " + list[4]

    for i in range(9, 1009):
        vector = list[i].split('|')
        if vector[0] != '1' and vector[0] != '0':
            vector[0] = '1'
        if vector[1] != '1' and vector[1] != '0':
            vector[1] = '1'
        str += " " + vector[0]
        str += " " + vector[1]


    k += 1
    str += '\n'



f.close()

print("writing..")
f = open('asmc.haps', 'w')
f.write(str)
f.close()
