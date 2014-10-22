cmake_minimum_required(VERSION 2.6)
project(fof_cluster_finder)


message ("BUILDING TYPE = ${CMAKE_BUILD_TYPE} ")

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_CURRENT_SOURCE_DIR}/aux/")

find_package(CFITSIO REQUIRED)
find_package(OpenMP REQUIRED)
find_package(Boost COMPONENTS system filesystem unit_test_framework
program_options REQUIRED)

set(CMAKE_CXX_FLAGS_DEBUG "-std=c++0x -O0 ${OpenMP_CXX_FLAGS} -fprofile-arcs -ftest-coverage")
set(CMAKE_C_FLAGS_DEBUG "-O0 ${OpenMP_C_FLAGS} -fprofile-arcs -ftest-coverage ")

set(CMAKE_CXX_FLAGS_RELEASE "-std=c++0x -O3 ${OpenMP_CXX_FLAGS}")
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
)

include_directories(BEFORE SYSTEM ${CFITSIO_INCLUDE_DIRS} ${Boost_INCLUDE_DIRS})

add_executable(main ${CPP_SRC} ${CPP_SOURCE_DIR}/main.cpp)
add_executable(cat_split ${CPP_SRC} ${CPP_SOURCE_DIR}/cat_split.cpp)
add_executable(cat_merge ${CPP_SRC} ${CPP_SOURCE_DIR}/cat_merge.cpp)
add_executable(test_code ${CPP_SRC} ${CPP_SOURCE_DIR}/test_code.cpp)
add_executable(unit_test ${CPP_SRC} ${CPP_UNITTEST_SOURCE_DIR}/unit_tests.cpp)
add_executable(astro_test ${CPP_SRC} ${CPP_UNITTEST_SOURCE_DIR}/astro_test.cpp)
add_executable(cosmo_test ${CPP_SRC} ${CPP_UNITTEST_SOURCE_DIR}/cosmo_test.cpp)

if (CMAKE_BUILD_TYPE STREQUAL "Debug")
  target_link_libraries(cosmo_test ${CFITSIO_LIBRARIES}  ${Boost_PROGRAM_OPTIONS_LIBRARY_DEBUG})
  target_link_libraries(main ${CFITSIO_LIBRARIES} ${Boost_PROGRAM_OPTIONS_LIBRARY_DEBUG})
  target_link_libraries(cat_split ${CFITSIO_LIBRARIES} ${Boost_PROGRAM_OPTIONS_LIBRARY_DEBUG})
  target_link_libraries(cat_merge ${CFITSIO_LIBRARIES} ${Boost_PROGRAM_OPTIONS_LIBRARY_DEBUG})
  target_link_libraries(test_code ${CFITSIO_LIBRARIES}  ${Boost_PROGRAM_OPTIONS_LIBRARY_DEBUG})
  target_link_libraries(unit_test ${CFITSIO_LIBRARIES} ${Boost_PROGRAM_OPTIONS_LIBRARY_DEBUG})
  target_link_libraries(astro_test ${CFITSIO_LIBRARIES}  ${Boost_PROGRAM_OPTIONS_LIBRARY_DEBUG})
else()
  target_link_libraries(cosmo_test ${CFITSIO_LIBRARIES}  ${Boost_PROGRAM_OPTIONS_LIBRARY_RELEASE})
  target_link_libraries(main ${CFITSIO_LIBRARIES} ${Boost_PROGRAM_OPTIONS_LIBRARY_RELEASE})
  target_link_libraries(cat_split ${CFITSIO_LIBRARIES} ${Boost_PROGRAM_OPTIONS_LIBRARY_RELEASE})
  target_link_libraries(cat_merge ${CFITSIO_LIBRARIES} ${Boost_PROGRAM_OPTIONS_LIBRARY_RELEASE})
  target_link_libraries(test_code ${CFITSIO_LIBRARIES}  ${Boost_PROGRAM_OPTIONS_LIBRARY_RELEASE})
  target_link_libraries(unit_test ${CFITSIO_LIBRARIES} ${Boost_PROGRAM_OPTIONS_LIBRARY_RELEASE})
  target_link_libraries(astro_test ${CFITSIO_LIBRARIES}  ${Boost_PROGRAM_OPTIONS_LIBRARY_RELEASE})
endif()

add_test(unit_test unit_test "--config ../examples/param_file.unit_test.ini")
add_test(astro_test astro_test "--log_level=test_suite")
add_test(cosmo_test cosmo_test "--log_level=test_suite")
