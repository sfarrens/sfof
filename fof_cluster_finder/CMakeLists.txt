cmake_minimum_required(VERSION 2.6)
project(fof_cluster_finder)


set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_CURRENT_SOURCE_DIR}/aux/")

find_package(CFITSIO REQUIRED)
find_package(OpenMP REQUIRED)

set(CMAKE_CXX_FLAGS "-O3 ${OpenMP_CXX_FLAGS}")
set(CMAKE_C_FLAGS "-O3 ${OpenMP_C_FLAGS}")

set(CPP_SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/src)

set(CPP_SRC
	${CPP_SOURCE_DIR}/dh.c
	${CPP_SOURCE_DIR}/astro.cpp          
	${CPP_SOURCE_DIR}/cluster_class.cpp  
	${CPP_SOURCE_DIR}/fileio_class.cpp   
	${CPP_SOURCE_DIR}/fof_class.cpp     
	${CPP_SOURCE_DIR}/galaxy_class.cpp  
	${CPP_SOURCE_DIR}/kdtree_class.cpp  
	${CPP_SOURCE_DIR}/merge_class.cpp   
	${CPP_SOURCE_DIR}/option_class.cpp
	${CPP_SOURCE_DIR}/zbin_class.cpp
)

include_directories(BEFORE SYSTEM ${CFITSIO_INCLUDE_DIRS})

add_executable(main ${CPP_SRC} ${CPP_SOURCE_DIR}/main.cpp)
target_link_libraries(main ${CFITSIO_LIBRARIES})

add_executable(test_code ${CPP_SRC} ${CPP_SOURCE_DIR}/test_code.cpp)
target_link_libraries(test_code ${CFITSIO_LIBRARIES})

