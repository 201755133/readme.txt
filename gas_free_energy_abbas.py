import sys
from ase.thermochemistry import IdealGasThermo
from numpy import array
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import QuasiNewton
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo
from ase.io import read, write

name = 'CO'
potentialenergy = -.14403613E+02  # Total ground state energy after FeNC-CO adsorbate optimization in units of eV
vib_energies = [193.165785,  6.120672, 5.232957, 0.005894, 6.120672 , 5.232957 ]  #  list of vibrational modes in units of meV
#convert from meV to eV for each mode
vib_energies[:] = [ve/1000. for ve in vib_energies]
#list of temperatures
temperatures = [298.15]
#operating pressure
pressures = [101325]
# coordinates from POSCAR
atoms = read('POSCAR')
# file to write free energy and enthalpy
f = open(name+'_thermo.properties','w')

for temperature in temperatures:
    for pressure in pressures:
        thermo = IdealGasThermo(vib_energies=vib_energies, potentialenergy=potentialenergy
                                ,atoms=atoms, geometry='linear', symmetrynumber=2, spin=0)
        helmholtz = thermo.get_gibbs_energy(temperature, pressure)
        entropy = thermo.get_entropy(temperature, pressure)
        enthalpy = helmholtz + temperature*entropy
        f.write('Temperature: {} K\tPressure: {} Pa\tHelmholtz energy: {:.3f} eV\tEnthalpy: {:.3f} eV\n'.format(temperature, pressure, helmholtz, enthalpy))

f.close()

