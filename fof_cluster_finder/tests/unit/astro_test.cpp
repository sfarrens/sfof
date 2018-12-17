/**
 * @file astro_test.cpp
 *
 * @author Samuel Farrens
 *
 * Unit tests for the methods of the Astro class.
 *
 */

#define BOOST_TEST_DYN_LINK
#define BOOST_TEST_MODULE MasterTestSuite
#include <boost/test/unit_test.hpp>
#include <boost/test/parameterized_test.hpp>
#include "../../src/astro.hpp"
#include "../../src/exceptions.hpp"

using namespace boost::unit_test;
Astro astro;

BOOST_AUTO_TEST_SUITE (Master_test_suite)

/**
 * Unit test for Astro::find_bin.
 */
BOOST_AUTO_TEST_CASE( find_bin )
{
  BOOST_CHECK( astro.find_bin(1.0, 1.0, 1.0) == 0 );
  BOOST_CHECK( astro.find_bin(2.0, 1.0, 1.0) == 1.0 );
  BOOST_CHECK_THROW( astro.find_bin(1.0, 2.0, 1.0) == 0, BadArgumentException );
}

/**
 * Unit test for Astro::num_bins.
 */
BOOST_AUTO_TEST_CASE( num_bins )
{
  BOOST_CHECK( astro.num_bins(1.0, 2.0, 1.0) == 1.0 );
  BOOST_CHECK_THROW( astro.num_bins(2.0, 1.0, 1.0) == 0, BadArgumentException );
}

/**
 * Unit test for Astro::within.
 */
BOOST_AUTO_TEST_CASE( within )
{
  BOOST_CHECK( astro.within(1.5, 1.0, 2.0) == 1.0 );
  BOOST_CHECK( astro.within(0.5, 1.0, 2.0) == 0.0 );
  BOOST_CHECK_THROW( astro.within(1.0, 2.0, 1.0) == 0, BadArgumentException );
}

/**
 * Unit test for Astro::angsep.
 */
BOOST_AUTO_TEST_CASE( angsep )
{
  BOOST_CHECK( astro.angsep(0.0, -90.0, 0.0, -90.0) == 0.0 );
  BOOST_CHECK( astro.angsep(360.0, 90.0, 360.0, 90.0) == 0.0 );
  BOOST_CHECK_THROW( astro.angsep( -10.0 , 60.0, 20.0, 60.0) == 0, BadArgumentException );
  BOOST_CHECK_THROW( astro.angsep( 20.0 , 60.0, 400.0, 60.0) == 0, BadArgumentException );
  BOOST_CHECK_THROW( astro.angsep( 20.0 , 100.0, 20.0, 60.0) == 0, BadArgumentException );
  BOOST_CHECK_THROW( astro.angsep( 20.0 , 60.0, 20.0, -100.0) == 0, BadArgumentException );
}

/**
 * Unit test for Astro::mean.
 */
BOOST_AUTO_TEST_CASE( mean )
{
  std::vector<double> test;
  BOOST_CHECK_THROW( astro.mean(test) == 0, BadArgumentException );
  for (int i = 0; i < 10; i++) test.push_back(i);
  BOOST_CHECK( std::abs(astro.mean(test) - 4.5)
	       <= std::numeric_limits<double>::epsilon() );
}

/**
 * Unit test for Astro::median.
 */
BOOST_AUTO_TEST_CASE( median )
{
  std::vector<double> test;
  BOOST_CHECK_THROW( astro.median(test) == 0, BadArgumentException );
  for (int i = 0; i < 10; i++) test.push_back(i);
  BOOST_CHECK( std::abs(astro.median(test) - 4.5)
	       <= std::numeric_limits<double>::epsilon() );
}

/**
 * Unit test for Astro::variance.
 */
BOOST_AUTO_TEST_CASE( variance )
{
  std::vector<double> test;
  BOOST_CHECK_THROW( astro.variance(test) == 0, BadArgumentException );
  for (int i = 0; i < 10; i++) test.push_back(i);
  BOOST_CHECK( std::abs(astro.variance(test) - 8.25)
	       <= std::numeric_limits<double>::epsilon() );

}

/**
 * Unit test for Astro::stdev.
 */
BOOST_AUTO_TEST_CASE( stdev )
{
  std::vector<double> test;
  BOOST_CHECK_THROW( astro.stdev(test) == 0, BadArgumentException );
  for (int i = 0; i < 10; i++) test.push_back(1.0);
  BOOST_CHECK( astro.stdev(test) == 0.0 );
}

/**
 * Unit test for Astro::stderr_mean.
 */
BOOST_AUTO_TEST_CASE( stderr_mean )
{
  std::vector<double> test;
  BOOST_CHECK_THROW( astro.stderr_mean(test) == 0, BadArgumentException );
  for (int i = 0; i < 10; i++) test.push_back(1.0);
  BOOST_CHECK( astro.stderr_mean(test) == 0.0 );
}

/**
 * Unit test for Astro::stderr_median.
 */
BOOST_AUTO_TEST_CASE( stderr_median )
{
  std::vector<double> test;
  BOOST_CHECK_THROW( astro.stderr_median(test) == 0, BadArgumentException );
  for (int i = 0; i < 10; i++) test.push_back(1.0);
  BOOST_CHECK( astro.variance(test) == 0.0 );
}

/**
 * Unit test for Astro::min.
 */
BOOST_AUTO_TEST_CASE( min )
{
  std::vector<double> test;
  BOOST_CHECK_THROW( astro.min(test) == 0, BadArgumentException );
  for (int i = 0; i < 10; i++) test.push_back(i);
  BOOST_CHECK( astro.min(test) == 0 );
}

/**
 * Unit test for Astro::max.
 */
BOOST_AUTO_TEST_CASE( max )
{
  std::vector<double> test;
  BOOST_CHECK_THROW( astro.max(test) == 0, BadArgumentException );
  for (int i = 0; i < 10; i++) test.push_back(i);
  BOOST_CHECK( astro.max(test) == 9 );
}

BOOST_AUTO_TEST_SUITE_END ()
