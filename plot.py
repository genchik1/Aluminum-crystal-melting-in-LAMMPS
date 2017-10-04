#coding:UTF-8
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

rdf_1 = ploting('/home/scala/Документы/my_CODE/lammps/aluminiy/return/RDF/RDF_50.rdf')
rdf_2 = ploting('/home/scala/Документы/my_CODE/lammps/aluminiy/return/RDF/RDF_550.rdf')
rdf_3 = ploting('/home/scala/Документы/my_CODE/lammps/aluminiy/return/RDF/RDF_1050.rdf')

plt.plot(rdf_1[0],rdf_1[1], 'g-')
plt.plot(rdf_2[0],rdf_2[1], 'r-')
plt.plot(rdf_3[0],rdf_3[1], 'b-')

plt.title("RDF")
plt.legend(['rdf_50K', 'rdf_550K', 'rdf_1050K'], loc=0)
plt.grid()
plt.savefig('rdf.png')
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

plots_1 = plots('/home/scala/Документы/my_CODE/lammps/aluminiy/return/pe-temp.txt')
plots_2 = plots('/home/scala/Документы/my_CODE/lammps/aluminiy/return/vol-temp.txt')

plt.title("Temp/PE")
plt.xlabel(u'Tемпература, К')
plt.ylabel(u'Пот.энергия')
plt.plot(plots_1[1], plots_1[0])
plt.grid()
plt.savefig('plot_pe-temp.png')
plt.show()

plt.title("Temp/Vol")
plt.xlabel(u'Tемпература, К')
plt.ylabel(u'Объем')
plt.plot(plots_2[1], plots_2[0])
plt.grid()
plt.savefig('plot_vol-temp.png')
plt.show()
