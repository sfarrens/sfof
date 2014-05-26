# Compilers
GPP      = clang++
GPP_FLAG = -O3 -stdlib=libstdc++

# Libraries

FITS_INC = -I/Users/Rowen/Documents/Library/cfitsio/include/
FITS_LIB = -L/Users/Rowen/Documents/Library/cfitsio/lib/ -lcfitsio

# All Objects

each: fof

# Cluster Tools

FOF_OBJ = main.o test_code.o

fof: $(FOF_OBJ)

$(FOF_OBJ):
	$(GPP) -c $(GPP_FLAG) ./src/$*.cpp -o ./src/$*.o $(FITS_INC)
	$(GPP) -g $(GPP_FLAG) ./src/$*.o -o ./src/$* $(FITS_LIB)
	mv ./src/$* ./bin

clean: 
	-rm -f ./src/*.o ./src/*~
