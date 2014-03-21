###########################
# ERROR MESSAGE FUNCTIONS #
###########################

import sys, getopt
import os.path

def file_name_error(file_name):
   '''
   Function that returns an error message for missing files.
   '''
   if file_name=='' or file_name[0][0]=='-':
      print 'ERROR! Input file name not specified.'
      exit(-1)
   elif os.path.isfile(file_name)==False:
      print 'ERROR! Input file name [%s] does not exist.' % file_name
      exit(-1)

