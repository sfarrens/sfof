/* UNIT TEST FOR ASTRO */

#include "../../src/astro.hpp"
#include "../../src/exceptions.hpp"

#define BOOST_TEST_DYN_LINK
#define BOOST_TEST_MODULE MasterTestSuite
#include <boost/test/included/unit_test.hpp>
#include <boost/test/parameterized_test.hpp>

using namespace boost::unit_test;

BOOST_AUTO_TEST_SUITE (Master_test_suite)

BOOST_AUTO_TEST_CASE( test_Astro1 )
{
  Astro astro;
  BOOST_CHECK( astro.find_bin(1.0, 1.0, 1.0) == 0 );
  BOOST_CHECK( astro.find_bin(2.0, 1.0, 1.0) == 1.0 );
  BOOST_CHECK_THROW( astro.find_bin(1.0, 2.0, 1.0) == 0, BadArgumentException);
}

BOOST_AUTO_TEST_CASE( test_Astro2 )
{
  Astro astro;
  BOOST_CHECK( astro.num_bins(1.0, 2.0, 1.0) == 1.0 );
  BOOST_CHECK_THROW( astro.num_bins(2.0, 1.0, 1.0) == 0, BadArgumentException);
}

BOOST_AUTO_TEST_SUITE_END ()
