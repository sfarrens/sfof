#######################
#   PYCATCUT V.1.0    #
#######################
# Samuel Farrens 2014 #
#######################

import sys, getopt, math, errors, pycatcut_help as pch
import numpy as np

def main(argv):

    #Set Defaults
    
    file_name = ''
    output = ''
    ra_col = -1
    dec_col = -1
    ra_lower = -1
    ra_upper = -1
    dec_lower = -1
    dec_upper = -1
    n_ra_bins = -1
    n_dec_bins = -1
    ra_overlap = 1.0 #(deg)
    dec_overlap = 1.0 #(deg)

    try:
      opts, args = getopt.getopt(argv,"f:o:r:d:i:j:k:l:s:e:q:p:h",["file=", "output=", "ra_col=", "dec_col=", "ra_lower=", "ra_upper=",
                                                                 "dec_lower=", "dec_upper=", "ra_bin=", "dec_bin=", "ra_overlap=",
                                                                 "dec_overlap=", "help"])
    except getopt.GetoptError:
        pch.print_help()
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            pch.print_help()
        elif opt in ("-f", "--file"):                                                      
            file_name = arg
        elif opt in ("-o", "--output"):                                                      
            output = arg
        elif opt in ("-r", "--ra_col"):
            ra_col = int(arg) - 1
        elif opt in ("-d", "--dec_col"):                                                   
            dec_col = int(arg) - 1
        elif opt in ("-i", "--ra_lower"):
            ra_lower = float(arg)
        elif opt in ("-j", "--ra_upper"):
            ra_upper = float(arg)
        elif opt in ("-k", "--dec_lower"):
            dec_lower = float(arg)
        elif opt in ("-l", "--dec_upper"):
            dec_upper = float(arg)
        elif opt in ("-s", "--ra_bin"):
            n_ra_bins = int(arg)
        elif opt in ("-e", "--dec_bin"):                                                   
            n_dec_bins = int(arg)
        elif opt in ("-q", "--ra_overlap"):
            ra_overlap = float(arg)
        elif opt in ("-p", "--dec_overlap"):                                                   
            dec_overlap = float(arg)
        else:
            print 'Something is wrong!'
            exit()

    #Check for errors
    
    errors.file_name_error(file_name)                                                       
    pch.check_errors(ra_col, dec_col, n_ra_bins, n_dec_bins)
            
    #Read catalogue
    
    print 'Reading data from ' + file_name
    catalogue = np.genfromtxt(file_name, dtype="S", unpack = True)

    ra = np.array(catalogue[ra_col, :], dtype="f")
    dec = np.array(catalogue[dec_col, :], dtype="f")

    #Set bin sizes

    if ra_lower == -1: ra_lower = min(ra)
    if ra_upper == -1: ra_upper = max(ra)
    if dec_lower == -1: dec_lower = min(dec)
    if dec_upper == -1: dec_upper = max(dec)
        
    ra_bin_size = ((ra_upper - ra_lower) / n_ra_bins)
    dec_bin_size = ((dec_upper - dec_lower) / n_dec_bins)
    
    #Cut-up catalogue and print pieces
    
    piece_num = 0
    
    for i in range(n_ra_bins):
        ra_bin_limit_lower = (ra_bin_size * i) + ra_lower - ra_overlap
        ra_bin_limit_upper = (ra_bin_size * (i + 1)) + ra_lower + ra_overlap
        ra_index_1 = ((ra >= ra_bin_limit_lower) | ((ra + 360) < ra_bin_limit_upper))
        ra_index_2 = ((ra < ra_bin_limit_upper) | ((ra - 360) >= ra_bin_limit_lower))
        for j in range(n_dec_bins):
            dec_bin_limit_lower = (dec_bin_size * j) + dec_lower - dec_overlap
            dec_bin_limit_upper = (dec_bin_size * (j + 1)) + dec_lower + dec_overlap
            dec_index_1 = (dec >= dec_bin_limit_lower)
            dec_index_2 = (dec < dec_bin_limit_upper)
            index = (ra_index_1 & ra_index_2 & dec_index_1 & dec_index_2)
            if output == '':
                out_file_name = file_name + '_piece_' + ('%02d' % piece_num) + '.dat'
                out_file = open(out_file_name, 'w')
            else:
                out_file_name = output + '_piece_' + ('%02d' % piece_num) + '.dat'
                out_file = open(out_file_name, 'a')
            print 'Printing data to ' + out_file_name + ' (' + str(np.sum(index)) + ')'
            for k in np.transpose(catalogue[:, index]):
                print>> out_file, ' '.join(k)
            piece_num += 1

if __name__ == "__main__":
    main(sys.argv[1:])
