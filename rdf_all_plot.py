import matplotlib.pyplot as plt
x =  []
y =  []
y1 = []
y2 = []
y3 = []
y4 = []
for line in open('PCF3.dat', 'r'):
    lines = [i for i in line.split()]
    x.append(float(lines[0]))
    y.append(float(lines[1]))
    y1.append(float(lines[2]))
    y2.append(float(lines[3]))
    y3.append(float(lines[4]))
    y4.append(float(lines[5]))
plt.title("Radial distribution function", fontsize = 12)
plt.xlabel('r(A)', fontsize = 12)
plt.ylabel('g(r)', fontsize = 12)
plt.plot(x, y, marker = 'o', c = 'g')
plt.plot(x, y1, marker = 'o', c = 'r')
plt.plot(x, y2, marker = 'o', c = 'b')
plt.plot(x, y3, marker = 'o', c = 'm')
plt.plot(x, y4, marker = 'o', c = 'y')
#plt.legend()
plt.xlim([0, 20])
plt.ylim([0, 8])
plt.savefig('rdf.png')
plt.show()

