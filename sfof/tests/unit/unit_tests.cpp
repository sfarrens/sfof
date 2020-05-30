
/*
 *
 *
 *
 *
 *
 */

#include <vector>
#include "../../src/sfof.hpp"
#include "../../src/exceptions.hpp"

#define BOOST_TEST_DYN_LINK
#define BOOST_TEST_MODULE MasterTestSuite
#include <boost/test/unit_test.hpp>
#include <boost/test/parameterized_test.hpp>

#include <iostream>

using namespace boost::unit_test;

BOOST_AUTO_TEST_SUITE (Master_test_suite)

/*
 * set up basic test for elementary methods and routines
 */

/*
 * ASTRO class
 */

//void test_Astro()
BOOST_AUTO_TEST_CASE( test_Astro )
{
  Astro astro;
  BOOST_TEST_MESSAGE("entering case for Astro");
  BOOST_CHECK( astro.find_bin(1.0, 1.0, 1.0) == 0 );
  BOOST_CHECK_THROW( astro.find_bin(1.0, 2.0, 1.0) == 0, BadArgumentException);   // out-of-range values should be handled

  /* .. */

}

//void test_Options_and_Galaxies()
BOOST_AUTO_TEST_CASE( test_Options_and_Galaxies )
{
  int i;
  Option opt;
  std::vector<Galaxy> gals;

  double version_number = 1.0;

  BOOST_TEST_MESSAGE("entering case for Options and Galaxy");

  opt.read_opts(framework::master_test_suite().argc, framework::master_test_suite().argv, version_number);

  BOOST_CHECK( opt.link_r != 0);
  BOOST_CHECK( opt.fof_mode == "phot");
  BOOST_CHECK( opt.z_bin_size > 0);
  BOOST_CHECK_MESSAGE( opt.input_file.length() != 0, opt.input_file);

  /* .. */

  Fileio fileio;
  if (opt.fof_mode == "spec")
    fileio.set_up(1, 2, 3, 4);
  else
    fileio.set_up(1, 2, 3, 4, 5);
  if(opt.input_mode == "ascii")
    fileio.read_ascii(opt.input_file, opt.fof_mode, opt.z_min, opt.z_max, opt.z_err_max, gals);
  else if(opt.input_mode == "fits")
    fileio.read_fits(opt.input_file, opt.fof_mode, opt.z_min, opt.z_max, opt.z_err_max, gals);

  BOOST_CHECK( gals.size() > 0);

  std::vector<int> nums;
  for (int i = 0; i < gals.size(); i++)
  nums.push_back(gals[i].num);

  sort(nums.begin(), nums.end());

  for (i = 0; (nums[i]!= nums[i+1]) && (i < nums.size()-1); i++)
    ;

  BOOST_CHECK( i == nums.size()-1 );

}


BOOST_AUTO_TEST_SUITE_END ()

// test_suite* init_unit_test_suite(int argc, char *argv[])
// {

//   // test_suite* ts1 = BOOST_TEST_SUITE( "simple functions" );
//   // ts1->add( BOOST_TEST_CASE( &test_Astro ) );
//   // ts1->add( BOOST_TEST_CASE( &test_Options_and_Galaxies ) );

//   framework::master_test_suite().p_name.value = "Master Unit test";
//   framework::master_test_suite().add( BOOST_TEST_CASE( &test_Astro ) );
//   framework::master_test_suite().add( BOOST_TEST_CASE( &test_Options_and_Galaxies ) );

// }
