# ======================================================================
# Atomistica - Interatomic potential library
# https://github.com/pastewka/atomistica
# Lars Pastewka, lars.pastewka@iwm.fraunhofer.de, and others.
# See the AUTHORS file in the top-level Atomistica directory.
#
# Copyright (2005-2013) Fraunhofer IWM
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# ======================================================================

import ase.io

from ase.calculators.lammps import write_lammps_data
from atomistica.netcdf_trajectory import NetCDFTrajectory

###

def read(fn, **kwargs):
    """
    Convenience function: Detect file extension and read via Atomistica or ASE.
    If reading a NetCDF files, frame numbers can be appended via '@'.
    e.g., a = read('traj.nc@5')
    """
    ext = fn[fn.rfind('.'):].split('@')
    if len(ext) == 1:
        if ext[0] == '.nc':
            traj = NetCDFTrajectory(fn, **kwargs)
            return traj[-1]
        else:
            return ase.io.read(fn, **kwargs)
    elif len(ext) == 2:
        if ext[0] == '.nc':
            frame = int(ext[1])
            fn = fn[:fn.rfind('@')]
            traj = NetCDFTrajectory(fn)
            return traj[frame]
        else:
            return ase.io.read(fn, **kwargs)
    else:
        return ase.io.read(fn, **kwargs)


def write(fn, a, **kwargs):
    """
    Convenience function: Detect file extension and write via Atomistica or ASE.
    Has support for writing LAMMPS data files.
    """
    ext = fn[fn.rfind('.'):].split('@')
    if ext[0] == '.lammps':
        return write_lammps_data(fn, a, **kwargs)
    else:
        return ase.io.write(fn, a, **kwargs)
