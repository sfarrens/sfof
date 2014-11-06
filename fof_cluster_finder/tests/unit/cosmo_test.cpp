/**
 * @file cosmo_test.cpp
 *
 * @author Samuel Farrens
 *
 * Unit tests for the methods of the Cosmo class.
 *
 */

#define BOOST_TEST_DYN_LINK
#define BOOST_TEST_MODULE MasterTestSuite
#include <boost/test/included/unit_test.hpp>
#include <boost/test/parameterized_test.hpp>
#include <limits>
#include "../../src/cosmo.hpp"
#include "../../src/exceptions.hpp"

using namespace boost::unit_test;
Cosmo cosmo;

BOOST_AUTO_TEST_SUITE (Master_test_suite)

/**
 * Unit test for Cosmo::set_up.
 */
BOOST_AUTO_TEST_CASE( set_up )
{
  BOOST_CHECK_THROW( cosmo.set_up(1.1, 0.7), BadArgumentException );
  BOOST_CHECK_THROW( cosmo.set_up(-0.1, 0.7), BadArgumentException );
  BOOST_CHECK_THROW( cosmo.set_up(0.3, 1.1), BadArgumentException );
  BOOST_CHECK_THROW( cosmo.set_up(0.3, -0.1), BadArgumentException );
  BOOST_CHECK_THROW( cosmo.set_up(0.5, 0.4), DomainException );
}

/**
 * Unit test for Cosmo::angdidis.
 */
BOOST_AUTO_TEST_CASE( angdidis )
{
  BOOST_CHECK( cosmo.angdidis(0.0) == 0.0 );
  BOOST_CHECK( std::abs(cosmo.angdidis(1.0) - 0.375) 
	       <= std::numeric_limits<double>::epsilon() );
}

/**
 * Unit test for Cosmo::angdidis2.
 */
BOOST_AUTO_TEST_CASE( angdidis2 )
{
  BOOST_CHECK( std::abs(cosmo.angdidis2(0.0, 1.0) - 0.375) 
	       <= std::numeric_limits<double>::epsilon() );
  BOOST_CHECK_THROW( cosmo.angdidis2(1.0, 0.0), BadArgumentException );
}

/**
 * Unit test for Cosmo::comdis.
 */
BOOST_AUTO_TEST_CASE( comdis )
{
  BOOST_CHECK( cosmo.comdis(0.0) == 0.0 );
  BOOST_CHECK_THROW( cosmo.comdis(-1.0), BadArgumentException );
}

/**
 * Unit test for Cosmo::comvol.
 */
BOOST_AUTO_TEST_CASE( comvol )
{
  BOOST_CHECK( cosmo.comvol(0.0) == 0.0 );
}

/**
 * Unit test for Cosmo::dcomdisdz.
 */
BOOST_AUTO_TEST_CASE( dcomdisdz )
{
  BOOST_CHECK( cosmo.dcomdisdz(0.0) == 1.0 );
}

/**
 * Unit test for Cosmo::dcomvoldz.
 */
BOOST_AUTO_TEST_CASE( dcomvoldz )
{
  BOOST_CHECK( cosmo.dcomvoldz(0.0) == 0.0 );
}

/**
 * Unit test for Cosmo::dlookbackdz.
 */
BOOST_AUTO_TEST_CASE( dlookbackdz )
{
  BOOST_CHECK( cosmo.dlookbackdz(0.0) == 1.0 );
  BOOST_CHECK_THROW( cosmo.dlookbackdz(-1.0), BadArgumentException );
}

/**
 * Unit test for Cosmo::doptdepthdz.
 */
BOOST_AUTO_TEST_CASE( doptdepthdz )
{
  BOOST_CHECK( cosmo.doptdepthdz(0.0) == 1.0 );
  BOOST_CHECK_THROW( cosmo.doptdepthdz(-1.0), BadArgumentException );
}

/**
 * Unit test for Cosmo::dpropmotdisdz.
 */
BOOST_AUTO_TEST_CASE( dpropmotdisdz )
{
  BOOST_CHECK( cosmo.dpropmotdisdz(0.0) == 1.0 );
}

/**
 * Unit test for Cosmo::intcomvol.
 */
BOOST_AUTO_TEST_CASE( intcomvol )
{
  BOOST_CHECK( cosmo.intcomvol(0.0) == 0.0 );
}

/**
 * Unit test for Cosmo::lookback.
 */
BOOST_AUTO_TEST_CASE( lookback )
{
  BOOST_CHECK( cosmo.lookback(0.0) == 0.0 );
}

/**
 * Unit test for Cosmo::lumdis.
 */
BOOST_AUTO_TEST_CASE( lumdis )
{
  BOOST_CHECK( cosmo.lumdis(0.0) == 0.0 );
}

/**
 * Unit test for Cosmo::optdepth.
 */
BOOST_AUTO_TEST_CASE( optdepth )
{
  BOOST_CHECK( cosmo.optdepth(0.0) == 0.0 );
}

BOOST_AUTO_TEST_SUITE_END ()

/**
 * Unit test for Cosmo::propmotdis.
 */
BOOST_AUTO_TEST_CASE( propmotdis )
{
  BOOST_CHECK( cosmo.propmotdis(0.0) == 0.0 );
  BOOST_CHECK_THROW( cosmo.propmotdis(-1.0), BadArgumentException );
}
