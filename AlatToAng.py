import sys
import numpy as np

lattice_constant = 6.64245 #This is celldm(1)
bohr_to_angstrom = 0.52917721092

if len(sys.argv) == 4:
    arg_list = [float(i) for i in sys.argv[1:]]
    fractional_position = np.array(arg_list)

    print("ATOMIC_POSITION (alat):")
    print(fractional_position)

    cartesian_position = fractional_position*bohr_to_angstrom*lattice_constant

    print("ATOMIC_POSITION (angstrom):")
    print(cartesian_position)
else:
    print("Error: Three atomic position values are needed.")
