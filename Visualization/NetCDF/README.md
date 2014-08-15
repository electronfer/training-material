Visualization of NetCDF files
=============================

NetCDF is a very versatile data format that shares many characteristics
with HDF5.  The 4.x APIs (for Fortran, C, C++,...) support groups and
annotations,  In contrast to HDF5, no XDMF metadata files are needed
to work with NetCDF data in ParaView.

Examples
--------
This directory contains a number of example data files (.nc), as well
as some ParaView state files (.pvsm) that illustrate how they can be
imported and vidualized in ParaView.

Scalar field
* `data.nc`: the value of a field is computed on each point
  of a rectilinear (non-uniform) grid (10 x 10 x 10) using the function
 `exp(-(x^2 + y^2 + z^2))`.  The file contains four data sets, i.e.,
  the three coordinates and the computed value.
* `data_netcdf.pvsm`: the NetCDF data is imported, and ParaView
  recognizes the grid coordinates automatically (switch to rectilinear).
  To illustrate, the grid is shown as well.

Notes
-----
* The ParaView state files were generated by ParaView 4.0 and may not work
  with other versions.
* The data was generated using C code that can be found in the top-level
  NetCDF directory.