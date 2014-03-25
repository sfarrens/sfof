============
Spec Example
============

This example runs the FoF code in spectroscopic mode on 2slaq_spec.dat.

1 - PYCATCUT

Cut 2slaq_spec.dat into two pieces with a 5 degree overlap in RA.

>> python ../../python/pycatcut.py -i 2slaq_spec.dat -r 2 -d 1 --ra_overlap 5

Expected output:

Reading data from 2slaq_spec.dat
Printing data to 2slaq_spec.dat_piece_00.dat (5295)
Printing data to 2slaq_spec.dat_piece_01.dat (7956)

2 - FOF_OMP_V2.1 {part 1}

Run FoF on piece00 with parameters specified in fof_param.ini.

>> ./../../bin/fof_omp_v2.1 -i 2slaq_spec.dat_piece_00.dat

Expected output:

[:::::::::::::::::::::::FRIENDS-OF-FRIENDS INITIATED:::::::::::::::::::::::]
 FoF Mode: [SPECTROSCOPIC]
 FoF Linking Parameters: [R(0.5)=0.86] [z0=0.009] [DYNAMIC]
 Reading ASCII file with 6 columns and 5295 rows:	Done
   - Using only the 5295 objects between z=0.01 and z=1.45
 Mean Particle Separation (0.500): 1004.154 Mpc/h
 Calculating linking length for redshift range:		Done
   - R_friend at z=0.500:	0.860000 Mpc/h
   - v at z=0.500:		1798.740016 km/s
 Making kdtree:						Done
 Merging in Progress...
 Merging protoclusters into clusters:			Done
		- Number of Clusters:			137
		- Number of Galaxies in Clusters:	526
		- Number of Protoclusters:		137
 Determining cluster properties:			Done
 Outputting files:					Done
 Time Elapsed: [0 days | 0 h | 0 m | 0 s]
[:::::::::::::::::::::::FRIENDS-OF-FRIENDS COMPLETE:::::::::::::::::::::::]

3 - FOF_OMP_V2.1 {part 2}

Run FoF on piece01 with parameters specified in fof_param.ini.

>> ./../../bin/fof_omp_v2.1 -i 2slaq_spec.dat_piece_00.dat

Expected output:

[:::::::::::::::::::::::FRIENDS-OF-FRIENDS INITIATED:::::::::::::::::::::::]
 FoF Mode: [SPECTROSCOPIC]
 FoF Linking Parameters: [R(0.5)=0.86] [z0=0.009] [DYNAMIC]
 Reading ASCII file with 6 columns and 7956 rows:	Done
   - Using only the 7956 objects between z=0.01 and z=1.45
 Mean Particle Separation (0.500): 1016.005 Mpc/h
 Calculating linking length for redshift range:		Done
   - R_friend at z=0.500:	0.860000 Mpc/h
   - v at z=0.500:		1798.740016 km/s
 Making kdtree:						Done
 Merging in Progress...
 Merging protoclusters into clusters:			Done
		- Number of Clusters:			250
		- Number of Galaxies in Clusters:	946
		- Number of Protoclusters:		250
 Determining cluster properties:			Done
 Outputting files:					Done
 Time Elapsed: [0 days | 0 h | 0 m | 1 s]
[:::::::::::::::::::::::FRIENDS-OF-FRIENDS COMPLETE:::::::::::::::::::::::]

4 - PYMERGE

Merge FoF output using expectation of 30 galaxies per square arcminute.

>> python ../../python/pymerge.py -i 2slaq_spec.dat_piece_00.dat_galaxies_0.86_0.0090_spec.dat -i 2slaq_spec.dat_piece_01.dat_galaxies_0.86_0.0090_spec.dat -o merged -b 30

Expected output:

Reading:  2slaq_spec.dat_piece_00.dat_galaxies_0.86_0.0090_spec.dat
Reading:  2slaq_spec.dat_piece_01.dat_galaxies_0.86_0.0090_spec.dat
Original number of clusters: 387
Original number of cluster members: 1472
Finding cluster matches and merging:
 >> Sweep: 1
 >> Sweep: 2
Final number of merged clusters: 380
Final number of merged cluster members: 1449
