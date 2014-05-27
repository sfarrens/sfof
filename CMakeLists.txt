cmake_minimum_required(VERSION 2.6)
project(fof_cluster_finder)

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_SOURCE_DIR}/aux/")

find_package(CFITSIO REQUIRED)

set(CPP_SOURCE_DIR ${CMAKE_SOURCE_DIR}/src)

set(CPP_SRC
	astro.cpp          
	cluster_class.cpp  
	fileio_class.cpp   
	fof_class.cpp     
	galaxy_class.cpp  
	kdtree_class.cpp  
	merge_class.cpp   
	option_class.cpp
	zbin_class.cpp
)

add_executable(main ${CPP_SRC} main.cpp)
target_link_libraries(main CFITSIO_LIBRARIES)

add_executable(test_code ${CPP_SRC} test_code.cpp)
target_link_libraries(test_code CFITSIO_LIBRARIES)
