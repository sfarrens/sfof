# Compilers
CLANG      = clang++
CLANG_FLAG = -O3 -std=c++11 -stdlib=libc++ -w
GCC      = /usr/local/bin/g++
GCC_FLAG = -O3 -std=c++11
OMP_FLAG = -fopenmp

# Libraries

FITS_INC = -I/Users/Rowen/Documents/Library/cfitsio/include/
FITS_LIB = -L/Users/Rowen/Documents/Library/cfitsio/lib/ -lcfitsio

# All Objects

each: fof

# New Friends-of-Friends

FOF_OBJ = fof_omp_v2.1.o

fof: $(FOF_OBJ)

$(FOF_OBJ):
	$(GCC) -c $(GCC_FLAG) $(OMP_FLAG) ./$*.cpp -o ./$*.o $(FITS_INC)
	$(GCC) -g $(GCC_FLAG) $(OMP_FLAG) ./$*.o -o ./$* $(FITS_LIB)
	mv ./$* ./bin

clean: 
	-rm -f ./*.o ./*~

