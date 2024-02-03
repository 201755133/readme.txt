# Import the necessary tools for making a Wulff shape
from pymatgen.analysis.wulff import WulffShape
import numpy as np
from surfinpy import p_vs_t as pt
from surfinpy import wulff
from surfinpy import utils as ut
# Import the necessary tools to generate surfaces
from pymatgen.core.surface import Lattice, SlabGenerator, Structure, generate_all_slabs
lattice = Lattice.monoclinic(4.28, 5.64, 4.45, beta=90.0)
Cu2O = Structure(lattice,
    ["Cu","Cu", "Cu", "Cu","Cu","Cu", "Cu", "Cu", "O", "O", "O", "O"],
   [[0.83, 0.25, 0.30], [0.83, 0.75, 0.30], [0.17, 0.25, 0.71], [0.17, 0.75, 0.71], [0.33, 0.00, 0.30], [0.33, 0.50, 0.29], [0.66, 0.00, 0.71], [0.66, 0.50, 0.71], [-0.00, 0.00, 0.99], 
   [0.00, 0.50, 0.99], [0.50, 0.25, 0.00], [0.50, 0.75, 0.00]])
slabgen = SlabGenerator(Cu2O, (1, 1, 1), 10, 10)
surface_energies_Cu2O = {
    (0, 1, 1): 0.05,
    (1, 1, 1): 0.28,
    (0, 1, 0): 0.10,
    (1, 1, 0): 0.04,
    (1, 0, 1): 0.10,
    (1, 0, 0): 0.11,   
}
miller_list = surface_energies_Cu2O.keys()
e_surf_list = surface_energies_Cu2O.values()
# We can now construct a Wulff shape with an accuracy up to a max Miller index of 3
wulffshape = WulffShape(Cu2O.lattice, miller_list, e_surf_list)
wulffshape.show(color_set="RdBu", direction=(1.00, 0.25, 0.25))
# Let's get some useful information from our wulffshape object
print(
    "shape factor: %.3f, anisotropy: \
%.3f, weighted surface energy: %.3f eV/A^2"
    % (
        wulffshape.shape_factor,
        wulffshape.anisotropy,
        wulffshape.weighted_surface_energy,
    )
)
# If we want to see what our Wulff shape looks like
wulffshape.show()
#all_slabs = slabgen.get_slabs()
#print("The Ni(111) slab only has %s termination." % (len(all_slabs)))
