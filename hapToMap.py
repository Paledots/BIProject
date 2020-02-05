filename = input()  # name of .hap/.haps files
sites = int(input())  # number of sites
f = open(filename, 'r')
k = 1
strr = ""
for line in f:
    if k == sites+1:
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
f = open('asmc.map', 'w')
f.write(strr)
f.close()
