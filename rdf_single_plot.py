import matplotlib.pyplot as plt
x = []
y = []
f = open('PCF.dat', 'r')
next(f)
    row = [i for i in f.split()]
    #row = row.split('')
    x.append(float(row[0]))
    y.append(float(row[1]))
plt.title("Radial distribution function", fontsize = 12)
plt.xlabel('r(A)', fontsize = 12)
plt.ylabel('g(r)', fontsize = 12)
plt.plot(x, y, marker = 'o', c = 'g')
plt.legend()
plt.xlim([0, 20])
plt.savefig('rdf.png')
plt.show()

