# Compilers
GPP      = clang++
GCC      = gcc
GPP_FLAG = -O3 -std=c++11 -stdlib=libc++ -w
GFLAGS   = -O3 -c

# Libraries

FITS_INC = -I/Users/Rowen/Documents/Library/cfitsio/include/
FITS_LIB = -L/Users/Rowen/Documents/Library/cfitsio/lib/ -lcfitsio

# All Objects

each: fof

# New Friends-of-Friends

FOF_OBJ = fof_v2.1.o

fof: $(FOF_OBJ)

$(FOF_OBJ):
	$(GPP) -c $(GPP_FLAG) ./$*.cpp -o ./$*.o $(FITS_INC)
	$(GPP) -g $(GPP_FLAG) ./$*.o -o ./$* $(FITS_LIB)

clean: 
	-rm -f ./*.o ./*~

