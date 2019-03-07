#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-mvnormtest
Version  : 0.1.9
Release  : 5
URL      : https://cran.r-project.org/src/contrib/mvnormtest_0.1-9.tar.gz
Source0  : https://cran.r-project.org/src/contrib/mvnormtest_0.1-9.tar.gz
Summary  : Normality test for multivariate variables
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : clr-R-helpers

%description
variables.

%prep
%setup -q -c -n mvnormtest

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530342067

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1530342067
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mvnormtest
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mvnormtest
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mvnormtest
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library mvnormtest|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/mvnormtest/COPYING
/usr/lib64/R/library/mvnormtest/ChangeLog
/usr/lib64/R/library/mvnormtest/DESCRIPTION
/usr/lib64/R/library/mvnormtest/INDEX
/usr/lib64/R/library/mvnormtest/Meta/Rd.rds
/usr/lib64/R/library/mvnormtest/Meta/features.rds
/usr/lib64/R/library/mvnormtest/Meta/hsearch.rds
/usr/lib64/R/library/mvnormtest/Meta/links.rds
/usr/lib64/R/library/mvnormtest/Meta/nsInfo.rds
/usr/lib64/R/library/mvnormtest/Meta/package.rds
/usr/lib64/R/library/mvnormtest/NAMESPACE
/usr/lib64/R/library/mvnormtest/R/mvnormtest
/usr/lib64/R/library/mvnormtest/R/mvnormtest.rdb
/usr/lib64/R/library/mvnormtest/R/mvnormtest.rdx
/usr/lib64/R/library/mvnormtest/help/AnIndex
/usr/lib64/R/library/mvnormtest/help/aliases.rds
/usr/lib64/R/library/mvnormtest/help/mvnormtest.rdb
/usr/lib64/R/library/mvnormtest/help/mvnormtest.rdx
/usr/lib64/R/library/mvnormtest/help/paths.rds
/usr/lib64/R/library/mvnormtest/html/00Index.html
/usr/lib64/R/library/mvnormtest/html/R.css
