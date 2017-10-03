import matplotlib.pyplot as plt

def ploting(filename):
    infile = open(filename,'r')
    infile.readline()
    infile.readline()
    infile.readline()
    infile.readline()

    rdf_x = []
    rdf_y = []
    for line in infile:
        words = line.split()
        den_x = float(words[1])
        rdf_x.append(den_x)
        den_y = float(words[2])
        rdf_y.append(den_y)
    infile.close()
    return rdf_x, rdf_y

rdf_1 = ploting('return/RDF/RDF_50.rdf')
rdf_2 = ploting('return/RDF/RDF_550.rdf')
rdf_3 = ploting('return/RDF/RDF_1050.rdf')

plt.plot(rdf_1[0],rdf_1[1], 'g-')
plt.plot(rdf_2[0],rdf_2[1], 'r-')
plt.plot(rdf_3[0],rdf_3[1], 'b-')

plt.legend(['rdf_50K', 'rdf_500K', 'rdf_1250K'], loc=0)
plt.savefig('rdf_2.png')
plt.grid()
plt.show()

def plots(filename):
    infile = open(filename,'r')
    plot_x = []
    plot_y = []
    for line in infile:
        words = line.split()
        den_x = float(words[0])
        plot_x.append(den_x)
        den_y = float(words[1])
        plot_y.append(den_y)
    infile.close()
    return plot_x, plot_y

plots_1 = plots('return/pe-temp.txt')
plots_2 = plots('return/vol-temp.txt')

plt.plot(plots_1[1], plots_1[0])
plt.savefig('plot_pe-temp_2.png')
plt.grid()
plt.show()

plt.plot(plots_2[1], plots_2[0])
plt.savefig('plot_vol-temp_2.png')
plt.grid()
plt.show()
