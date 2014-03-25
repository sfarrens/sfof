#######################
# INTERFACE FUNCTIONS #
#######################

import sys

def progress_bar(i, size):
    """
    Function that prints progress bar to terminal.
    """
    sys.stdout.write('\r')
    x = float(i)/float(size) * 100.0 + 1.0
    sys.stdout.write("[%-50s] %3d%%" % ('=' * int(x * 0.5), x))
    sys.stdout.flush()
