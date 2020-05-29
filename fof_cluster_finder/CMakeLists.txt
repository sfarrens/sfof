cmake_minimum_required(VERSION 2.6)
project(fof_cluster_finder)

if(CMAKE_BUILD_TYPE STREQUAL "")
	set(CMAKE_BUILD_TYPE "Release")
endif()
message(STATUS "CMake Build Type: ${CMAKE_BUILD_TYPE}")

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_CURRENT_SOURCE_DIR}/aux/")

find_package(CFITSIO REQUIRED)

if("${CMAKE_CXX_COMPILER_ID}" MATCHES "Clang")
	if(EXISTS "/usr/local/Cellar/libomp")
		message(STATUS "Found Homebrew package libomp")
	else()
		message(FATAL_ERROR "Could not find Homebrew package libomp")
	endif()
	set(OpenMP_INCLUDE_PATH "/usr/local/include")
	set(OpenMP_LIB_PATH "/usr/local/lib")
	set(OpenMP_CXX_FLAGS "-Xpreprocessor -fopenmp -lomp")
	set(OpenMP_CXX_LIB_NAMES "omp")
	set(OpenMP_CXX_LIBRARIES "${OpenMP_LIB_PATH}/libomp.dylib")
	include_directories(${OpenMP_INCLUDE_PATH})
	link_directories(${OpenMP_LIB_PATH})
else()
	message(STATUS "Searching for OpenMP ${CMAKE_CXX_COMPILER_ID}")
	find_package(OpenMP REQUIRED)
endif()

find_package(Boost COMPONENTS system filesystem unit_test_framework
program_options REQUIRED)

set(CMAKE_CXX_FLAGS_DEBUG "-std=c++11 -g ${OpenMP_CXX_FLAGS} -fprofile-arcs -ftest-coverage")
set(CMAKE_C_FLAGS_DEBUG "-g ${OpenMP_C_FLAGS} -fprofile-arcs -ftest-coverage ")

set(CMAKE_CXX_FLAGS_RELEASE "-std=c++11 -O3 ${OpenMP_CXX_FLAGS}")
set(CMAKE_C_FLAGS_RELEASE "-O3 ${OpenMP_C_FLAGS}")

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_CURRENT_SOURCE_DIR}/aux/")

set(CPP_SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/src)
set(CPP_UNITTEST_SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/tests/unit)

set(CPP_SRC
	${CPP_SOURCE_DIR}/astro.cpp
	${CPP_SOURCE_DIR}/cluster_class.cpp
	${CPP_SOURCE_DIR}/comp.cpp
	${CPP_SOURCE_DIR}/cosmo.cpp
	${CPP_SOURCE_DIR}/fileio_class.cpp
	${CPP_SOURCE_DIR}/fof_class.cpp
	${CPP_SOURCE_DIR}/galaxy_class.cpp
	${CPP_SOURCE_DIR}/kdtree_class.cpp
	${CPP_SOURCE_DIR}/merge_class.cpp
	${CPP_SOURCE_DIR}/option_class.cpp
	${CPP_SOURCE_DIR}/zbin_class.cpp
	${CPP_SOURCE_DIR}/cat_merge_fileio.cpp
  ${CPP_SOURCE_DIR}/exceptions.cpp
	${CPP_SOURCE_DIR}/point_class.cpp
	${CPP_SOURCE_DIR}/band_matrix.cpp
	${CPP_SOURCE_DIR}/spline.cpp
)

include_directories(BEFORE SYSTEM ${CFITSIO_INCLUDE_DIRS} ${Boost_INCLUDE_DIRS})

set(SOURCE_LIST sfof cat_split cat_merge)

foreach(program ${SOURCE_LIST})
	add_executable(${program} ${CPP_SRC} ${CPP_SOURCE_DIR}/${program}.cpp)
	target_link_libraries(${program} ${CFITSIO_LIBRARIES} ${Boost_LIBRARIES})
endforeach(program)

set(TEST_LIST unit_tests astro_test cosmo_test)

foreach(program ${TEST_LIST})
	add_executable(${program} ${CPP_SRC} ${CPP_UNITTEST_SOURCE_DIR}/${program}.cpp)
	target_link_libraries(${program} ${CFITSIO_LIBRARIES} ${Boost_LIBRARIES})
endforeach(program)

enable_testing()

# add_test(unit_tests unit_tests "--config ${CMAKE_CURRENT_SOURCE_DIR}/../examples/unit_test/param_file.unit_test.ini")
add_test(astro_test astro_test "--log_level=test_suite")
add_test(cosmo_test cosmo_test "--log_level=test_suite")

INSTALL(TARGETS ${SOURCE_LIST} DESTINATION bin)
