f = open('myHap.haps', 'r')
k = 1
strr = ""
for line in f:
    if k == 10001:
        break

    list = line.split()

    strr += list[0]
    strr += " " + list[1]
    strr += " 0"
    strr += " " + list[2]
    strr += '\n'
    k += 1

f.close()

print("writing..")
f = open('myHap.map', 'w')
f.write(strr)
f.close()
