#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-pracma
Version  : 2.2.9
Release  : 34
URL      : https://cran.r-project.org/src/contrib/pracma_2.2.9.tar.gz
Source0  : https://cran.r-project.org/src/contrib/pracma_2.2.9.tar.gz
Summary  : Practical Numerical Math Functions
Group    : Development/Tools
License  : GPL-3.0
BuildRequires : buildreq-R

%description
Provides a large number of functions from numerical analysis and
    linear algebra, numerical optimization, differential equations,
    time series, plus some well-known special mathematical functions.
    Uses 'MATLAB' function names where appropriate to simplify porting.

%prep
%setup -q -c -n pracma
cd %{_builddir}/pracma

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589525559

%install
export SOURCE_DATE_EPOCH=1589525559
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pracma
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pracma
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pracma
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc pracma || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/pracma/DESCRIPTION
/usr/lib64/R/library/pracma/INDEX
/usr/lib64/R/library/pracma/Meta/Rd.rds
/usr/lib64/R/library/pracma/Meta/data.rds
/usr/lib64/R/library/pracma/Meta/demo.rds
/usr/lib64/R/library/pracma/Meta/features.rds
/usr/lib64/R/library/pracma/Meta/hsearch.rds
/usr/lib64/R/library/pracma/Meta/links.rds
/usr/lib64/R/library/pracma/Meta/nsInfo.rds
/usr/lib64/R/library/pracma/Meta/package.rds
/usr/lib64/R/library/pracma/NAMESPACE
/usr/lib64/R/library/pracma/NEWS
/usr/lib64/R/library/pracma/NEWS.md
/usr/lib64/R/library/pracma/R/pracma
/usr/lib64/R/library/pracma/R/pracma.rdb
/usr/lib64/R/library/pracma/R/pracma.rdx
/usr/lib64/R/library/pracma/data/Rdata.rdb
/usr/lib64/R/library/pracma/data/Rdata.rds
/usr/lib64/R/library/pracma/data/Rdata.rdx
/usr/lib64/R/library/pracma/demo/pracma.R
/usr/lib64/R/library/pracma/help/AnIndex
/usr/lib64/R/library/pracma/help/aliases.rds
/usr/lib64/R/library/pracma/help/paths.rds
/usr/lib64/R/library/pracma/help/pracma.rdb
/usr/lib64/R/library/pracma/help/pracma.rdx
/usr/lib64/R/library/pracma/html/00Index.html
/usr/lib64/R/library/pracma/html/R.css
/usr/lib64/R/library/pracma/tests/blkdiag.R
/usr/lib64/R/library/pracma/tests/ceil.R
/usr/lib64/R/library/pracma/tests/chebyshev.R
/usr/lib64/R/library/pracma/tests/combs.R
/usr/lib64/R/library/pracma/tests/compan.R
/usr/lib64/R/library/pracma/tests/cond.R
/usr/lib64/R/library/pracma/tests/conv.R
/usr/lib64/R/library/pracma/tests/cross.R
/usr/lib64/R/library/pracma/tests/crossn.R
/usr/lib64/R/library/pracma/tests/deval.R
/usr/lib64/R/library/pracma/tests/diag.R
/usr/lib64/R/library/pracma/tests/distmat.R
/usr/lib64/R/library/pracma/tests/dot.R
/usr/lib64/R/library/pracma/tests/eig.R
/usr/lib64/R/library/pracma/tests/factors.R
/usr/lib64/R/library/pracma/tests/find.R
/usr/lib64/R/library/pracma/tests/findintervals.R
/usr/lib64/R/library/pracma/tests/findpeaks.R
/usr/lib64/R/library/pracma/tests/flipdim.R
/usr/lib64/R/library/pracma/tests/fnorm.R
/usr/lib64/R/library/pracma/tests/gamma.R
/usr/lib64/R/library/pracma/tests/gradient.R
/usr/lib64/R/library/pracma/tests/hadamard.R
/usr/lib64/R/library/pracma/tests/hankel.R
/usr/lib64/R/library/pracma/tests/hilb.R
/usr/lib64/R/library/pracma/tests/horner.R
/usr/lib64/R/library/pracma/tests/hypot.R
/usr/lib64/R/library/pracma/tests/interp1.R
/usr/lib64/R/library/pracma/tests/interp2.R
/usr/lib64/R/library/pracma/tests/inv.R
/usr/lib64/R/library/pracma/tests/isprime.R
/usr/lib64/R/library/pracma/tests/lambertW.R
/usr/lib64/R/library/pracma/tests/linspace.R
/usr/lib64/R/library/pracma/tests/magic.R
/usr/lib64/R/library/pracma/tests/meshgrid.R
/usr/lib64/R/library/pracma/tests/mldivide.R
/usr/lib64/R/library/pracma/tests/mod.R
/usr/lib64/R/library/pracma/tests/mode.R
/usr/lib64/R/library/pracma/tests/nextpow2.R
/usr/lib64/R/library/pracma/tests/norm.R
/usr/lib64/R/library/pracma/tests/nthroot.R
/usr/lib64/R/library/pracma/tests/pascal.R
/usr/lib64/R/library/pracma/tests/pchip.R
/usr/lib64/R/library/pracma/tests/perms.R
/usr/lib64/R/library/pracma/tests/piecewise.R
/usr/lib64/R/library/pracma/tests/poly.R
/usr/lib64/R/library/pracma/tests/polyadd.R
/usr/lib64/R/library/pracma/tests/polyarea.R
/usr/lib64/R/library/pracma/tests/polyder.R
/usr/lib64/R/library/pracma/tests/polyfit.R
/usr/lib64/R/library/pracma/tests/polyint.R
/usr/lib64/R/library/pracma/tests/polymul.R
/usr/lib64/R/library/pracma/tests/polyval.R
/usr/lib64/R/library/pracma/tests/pow2.R
/usr/lib64/R/library/pracma/tests/primes.R
/usr/lib64/R/library/pracma/tests/quad.R
/usr/lib64/R/library/pracma/tests/quadrature.R
/usr/lib64/R/library/pracma/tests/rank.R
/usr/lib64/R/library/pracma/tests/rectint.R
/usr/lib64/R/library/pracma/tests/regexp.R
/usr/lib64/R/library/pracma/tests/roots.R
/usr/lib64/R/library/pracma/tests/size.R
/usr/lib64/R/library/pracma/tests/std.R
/usr/lib64/R/library/pracma/tests/strfind.R
/usr/lib64/R/library/pracma/tests/strings.R
/usr/lib64/R/library/pracma/tests/subspace.R
/usr/lib64/R/library/pracma/tests/trace.R
/usr/lib64/R/library/pracma/tests/trapz.R
/usr/lib64/R/library/pracma/tests/vander.R
/usr/lib64/R/library/pracma/tests/wilkinson.R
