///////////////////////////////////////////////////////////////////////////////

#include <string>
#include <cmath>
#include <complex>
#include <sstream>
#include <fstream>
#include <iostream>
#include <map>

///////////////////////////////////////////////////////////////////////////////

#include "./cpgplot.h"
#include "./fftw3.h"

///////////////////////////////////////////////////////////////////////////////

#include "./gsl/gsl_math.h"
#include "./gsl/gsl_eigen.h"
#include "./gsl/gsl_multifit_nlin.h"
#include "./gsl/gsl_blas.h"

///////////////////////////////////////////////////////////////////////////////

#include "../tools/nrutil.hpp"
#include "../tools/tools.hpp"

#include "../tools/anchor.hpp"
#include "../tools/cleanvector.hpp"
#include "../tools/safevector.hpp"
#include "../tools/math_object.hpp"

///////////////////////////////////////////////////////////////////////////////

#include "../camb/camb.hpp"
#include "../spline/spline.hpp"
#include "../spline/spline_web.hpp"
#include "../spec_fct/spec_fct.hpp"
#include "../data/data.hpp"
#include "../data/data_vector.hpp"
#include "../data/data_3d.hpp"
#include "../statistic/statistic.hpp"
#include "../fourrier/fourrier.hpp"
#include "../misc_math/misc_math.hpp"
#include "../matrix/matrix.hpp"
#include "../statistic/multi_gaussian.hpp"
#include "../mcmc/mcmc.hpp"
#include "../catalogue/catalogue.hpp"
#include "../rpn/rpn.hpp"

#include "../cosmology/cosmology.hpp"

//////////////////////////////////////////////////////////////////////////////


//#include "../tools/nrutil.cpp"
//#include "../tools/tools.cpp"

#include "../spline/spline_def.cpp"
#include "../spline/spline_fct.cpp"
#include "../spline/spline_math.cpp"
#include "../spline/spline_lst.cpp"

#include "../spline/spline_web_def.cpp"

#include "../spec_fct/spec_fct_prob.cpp"
#include "../spec_fct/spec_fct_bess.cpp"
#include "../spec_fct/spec_fct_int.cpp"
#include "../spec_fct/spec_fct_hyp.cpp"

#include "../data/data_def.cpp"
#include "../data/data_prob.cpp"
#include "../data/data_fisher.cpp"
#include "../data/data_vector_def.cpp"
#include "../data/data_vector_prob.cpp"
#include "../data/data_vector_filter.cpp"

#include "../data/data_3d.cpp"

#include "../statistic/statistic_rnd.cpp"
#include "../statistic/statistic_prob.cpp"
#include "../statistic/statistic_corr.cpp"

#include "../statistic/multi_gaussian.cpp"

#include "../fourrier/fourrier_smooth.cpp"

#include "../misc_math/misc_math_def.cpp"
#include "../misc_math/misc_math_integral.cpp"
#include "../misc_math/misc_math_open_integral.cpp"
#include "../misc_math/misc_math_quadrature.cpp"
#include "../misc_math/misc_math_derivative.cpp"
#include "../misc_math/misc_math_cheb.cpp"
#include "../misc_math/misc_math_ode.cpp"
#include "../misc_math/misc_math_root.cpp"
#include "../misc_math/misc_math_root_nl.cpp"

#include "../matrix/matrix_two.cpp"
#include "../matrix/matrix_def.cpp"
#include "../matrix/matrix_decomp.cpp"
#include "../matrix/matrix_eigen.cpp"

#include "../mcmc/mcmc_def.cpp"

#include "../catalogue/catalogue_def.cpp"
#include "../catalogue/catalogue_lc.cpp"       
#include "../catalogue/catalogue_lmodel.cpp"
#include "../catalogue/catalogue.hpp"       
#include "../catalogue/catalogue_lc_main.cpp"  
#include "../catalogue/catalogue_init.cpp"

#include "../rpn/rpn_def.cpp"  
#include "../rpn/rpn_stack.cpp"
#include "../rpn/rpn_operator_var.cpp"
#include "../rpn/rpn_getop.cpp"  
#include "../rpn/rpn_operator.cpp"  

///////////////////////////////////////////////////////////////////////////////

///////////////////////////////////////////////////////////////////////////////

// Jo's stuff

//#include "../jxd_prog/mc_var.h"
//#include "../jxd_prog/mc_var.c"
#include "../cosmology/jxd_progs.c"
//#include "../jxd_prog/chi_mps.c"
//#include "../jxd_prog/chi_hi.c"
//#include "../jxd_prog/map_subs.h"
//#include "../jxd_prog/map_subs.c"
//#include "../kavi_prog/expt.h"
//#include "../kavi_prog/expt.c"
//#include "../kavi_prog/theor.h"
//#include "../kavi_prog/theor.c"

///////////////////////////////////////////////////////////////////////////////

#include "../cosmology/cosmology_init.cpp"
#include "../cosmology/cosmology_def.cpp"
#include "../cosmology/cosmology_first.cpp"
#include "../cosmology/cosmology_second.cpp"
#include "../cosmology/cosmology_spher_col.cpp"
#include "../cosmology/cosmology_eps.cpp"
#include "../cosmology/cosmology_halo.cpp"
#include "../cosmology/cosmology_transf.cpp"
#include "../cosmology/cosmology_pk.cpp"
#include "../cosmology/cosmology_pk_dm_halo.cpp"
#include "../cosmology/cosmology_pk_dm_z_halo.cpp"
#include "../cosmology/cosmology_pk_g_halo.cpp"
#include "../cosmology/cosmology_pk_g_z_halo.cpp"
#include "../cosmology/cosmology_galaxy_expt.cpp"
#include "../cosmology/cosmology_galaxy_surveys.cpp"
#include "../cosmology/cosmology_galaxy_2dF.cpp"
#include "../cosmology/cosmology_lensing_expt.cpp"
#include "../cosmology/cosmology_lensing_theory.cpp"
#include "../cosmology/cosmology_cmb_expt.cpp"
#include "../cosmology/cosmology_cmb_theory.cpp"
#include "../cosmology/cosmology_cmb_wmap.cpp"
#include "../cosmology/cosmology_cmb_hi.cpp"
#include "../cosmology/cosmology_spline.cpp"

///////////////////////////////////////////////////////////////////////////////

//Crap but need from other paper...

//#include </users/fba/dphil/level0_SKA/prog_paper_dndz_2/fil_lib/gauleg.c>
//#include </users/fba/dphil/level0_SKA/prog_paper_dndz_2/fil_lib/qgausleg.c>
//#include </users/fba/dphil/level0_SKA/prog_paper_dndz_2/fil_lib/qgausleg_int1_fct2.cpp>


//#include "../old_prog/cosmo_define.hpp"
//#include "../old_prog/cosmo_first.hpp"
//#include "../old_prog/prog_paper_dndz.hpp"
//#include "../old_prog/prog_paper_dndz.cpp"

//#include "../jxd_prog/chain.h"
//#include "../jxd_prog/chain.c"
