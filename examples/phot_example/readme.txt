============
Phot Example
============

This example runs the FoF code in photometric mode on 2slaq_phot.dat.

1 - PYCATCUT

Cut 2slaq_phot.dat into two pieces with a 5 degree overlap in RA.

>> python ../../python/pycatcut.py -i 2slaq_phot.dat -r 2 -d 1 --ra_overlap 5

Expected output:

Reading data from 2slaq_phot.dat
Printing data to 2slaq_phot.dat_piece_00.dat (5295)
Printing data to 2slaq_phot.dat_piece_01.dat (7956)

2 - FOF_OMP_V2.1 {part 1}

Run FoF on piece00 with parameters specified in fof_param.ini.

>> ./../../bin/fof_omp_v2.1 -i 2slaq_phot.dat_piece_00.dat

Expected output:

[:::::::::::::::::::::::FRIENDS-OF-FRIENDS INITIATED:::::::::::::::::::::::]
 FoF Mode: [PHOTOMETRIC]
 FoF Linking Parameters: [R(0.5)=0.86] [z0=1] [DYNAMIC]
 Reading ASCII file with 6 columns and 5295 rows:	Done
   - Using only the 5155 objects between z=0.01 and z=1.45 with z_err <= 0.05
 Mean Particle Separation (0.500): 983.045 Mpc/h
 Calculating linking length for redshift range:		Done
   - R_friend at z=0.500:	0.860000 Mpc/h
 Making kdtree:
 Done
Creating Protoclusters:	 z = 0.01  Nprtclt = 000000  Ngalprtclt = 0000000	Time: 0 s
...
Creating Protoclusters:	 z = 0.73	Nprtclt = 000680  Ngalprtclt = 0002236	Time: 0 s
 Merging in Progress...
 Merging protoclusters into clusters:		Done
		- Number of Clusters:			243
		- Number of Galaxies in Clusters:	948
		- Number of Protoclusters:		680
 Determining cluster properties:			Done
 Outputting files:						Done
 Time Elapsed: [0 days | 0 h | 0 m | 2 s]
[:::::::::::::::::::::::FRIENDS-OF-FRIENDS COMPLETE:::::::::::::::::::::::]


3 - FOF_OMP_V2.1 {part 2}

Run FoF on piece01 with parameters specified in fof_param.ini.

>> ./../../bin/fof_omp_v2.1 -i 2slaq_phot.dat_piece_01.dat

Expected output:

[:::::::::::::::::::::::FRIENDS-OF-FRIENDS INITIATED:::::::::::::::::::::::]
 FoF Mode: [PHOTOMETRIC]
 FoF Linking Parameters: [R(0.5)=0.86] [z0=1] [DYNAMIC]
 Reading ASCII file with 6 columns and 7956 rows:	Done
   - Using only the 7762 objects between z=0.01 and z=1.45 with z_err <= 0.05
 Mean Particle Separation (0.500): 1002.461 Mpc/h
 Calculating linking length for redshift range:		Done
   - R_friend at z=0.500:	0.860000 Mpc/h
 Making kdtree:						Done			Done
Creating Protoclusters:	 z = 0.01  Nprtclt = 000000  Ngalprtclt = 0000000	Time: 0 s
...
Creating Protoclusters:	 z = 0.73	Nprtclt = 001129  Ngalprtclt = 0003899	Time: 0 s
 Merging in Progress...
 Merging protoclusters into clusters:			Done
		- Number of Clusters:			392
		- Number of Galaxies in Clusters:	1628
		- Number of Protoclusters:		1129
 Determining cluster properties:			Done
 Outputting files:					Done
 Time Elapsed: [0 days | 0 h | 0 m | 7 s]
[:::::::::::::::::::::::FRIENDS-OF-FRIENDS COMPLETE:::::::::::::::::::::::]

4 - PYMERGE

Merge FoF output using expectation of 30 galaxies per square arcminute.

>> python ../../python/pymerge.py -i 2slaq_phot.dat_piece_00.dat_galaxies_0.86_1.0_phot.dat -i 2slaq_phot.dat_piece_01.dat_galaxies_0.86_1.0_phot.dat -o merged -b 30

Expected output:

Reading:  2slaq_phot.dat_piece_00.dat_galaxies_0.86_1.0_phot.dat
Reading:  2slaq_phot.dat_piece_01.dat_galaxies_0.86_1.0_phot.dat
Original number of clusters: 635
Original number of cluster members: 2576
Finding cluster matches and merging:
 >> Sweep: 1
 >> Sweep: 2
Final number of merged clusters: 629
Final number of merged cluster members: 2548
