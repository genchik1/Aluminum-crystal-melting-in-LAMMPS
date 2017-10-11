# Aluminum-crystal-melting-in-LAMMPS

To run the Lummps file, you need to enter it in the console:

$ Lammps -in in.aluminium
To run on multiple processors:
$ mpirun -np (n-processors) Lammps -in in.aluminium

File "plot.py" - script for building graphs, for this to be installed: python and the matplotlib library:
$ python plot.py
