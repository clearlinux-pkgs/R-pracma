#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-pracma
Version  : 2.1.8
Release  : 13
URL      : https://cran.r-project.org/src/contrib/pracma_2.1.8.tar.gz
Source0  : https://cran.r-project.org/src/contrib/pracma_2.1.8.tar.gz
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

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1539741278

%install
export SOURCE_DATE_EPOCH=1539741278
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
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
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library pracma|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


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
