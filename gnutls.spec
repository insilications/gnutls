#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : gnutls
Version  : 3.6.15
Release  : 75
URL      : https://www.gnupg.org/ftp/gcrypt/gnutls/v3.6/gnutls-3.6.15.tar.xz
Source0  : https://www.gnupg.org/ftp/gcrypt/gnutls/v3.6/gnutls-3.6.15.tar.xz
Summary  : Transport Security Layer implementation for the GNU system
Group    : Development/Tools
License  : GPL-3.0+ LGPL-2.0+ LGPL-2.1
Requires: gnutls-bin = %{version}-%{release}
Requires: gnutls-lib = %{version}-%{release}
Requires: gnutls-locales = %{version}-%{release}
BuildRequires : autoconf
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : bison
BuildRequires : buildreq-configure
BuildRequires : ccache
BuildRequires : datefudge
BuildRequires : docbook-xml
BuildRequires : findutils
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : glibc-locale
BuildRequires : gmp-dev
BuildRequires : gmp-dev32
BuildRequires : gmp-lib32
BuildRequires : gmp-staticdev
BuildRequires : gmp-staticdev32
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : intltool-dev
BuildRequires : libidn2-dev
BuildRequires : libidn2-dev32
BuildRequires : libidn2-staticdev
BuildRequires : libidn2-staticdev32
BuildRequires : libseccomp-dev
BuildRequires : libtasn1-dev
BuildRequires : libtasn1-dev32
BuildRequires : libtasn1-staticdev
BuildRequires : libtasn1-staticdev32
BuildRequires : libunistring-dev
BuildRequires : libunistring-dev32
BuildRequires : libunistring-staticdev
BuildRequires : libunistring-staticdev32
BuildRequires : libxslt-bin
BuildRequires : net-tools
BuildRequires : nettle
BuildRequires : nettle-dev
BuildRequires : nettle-dev32
BuildRequires : nettle-lib
BuildRequires : nettle-lib32
BuildRequires : nettle-staticdev
BuildRequires : nettle-staticdev32
BuildRequires : p11-kit
BuildRequires : p11-kit-dev
BuildRequires : p11-kit-dev32
BuildRequires : pkg-config
BuildRequires : pkgconfig(32gmp)
BuildRequires : pkgconfig(32gmpxx)
BuildRequires : pkgconfig(32libidn2)
BuildRequires : pkgconfig(32libtasn1)
BuildRequires : pkgconfig(32libunistring)
BuildRequires : pkgconfig(32p11-kit-1)
BuildRequires : pkgconfig(gmp)
BuildRequires : pkgconfig(gmpxx)
BuildRequires : pkgconfig(hogweed)
BuildRequires : pkgconfig(libidn2)
BuildRequires : pkgconfig(libtasn1)
BuildRequires : pkgconfig(libunistring)
BuildRequires : pkgconfig(nettle)
BuildRequires : pkgconfig(p11-kit-1)
BuildRequires : sed
BuildRequires : texinfo
BuildRequires : util-linux
BuildRequires : util-linux-dev
BuildRequires : util-linux-staticdev
BuildRequires : valgrind-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: noversion.patch
Patch2: 0001-Don-t-run-trust-store-test-as-it-isn-t-in-the-buildr.patch
Patch3: gnutls-3.2.7-rpath.patch
Patch4: gnutls-3.6.7-no-now-guile.patch
Patch5: gnutls-3.6.15-gnulib-perror-tests.patch

%description
ext/         -> Implementation of TLS extensions
auth/        -> Implementation of TLS authentication methods (DHE, SRP etc.)
accelerated/ -> Implementation of cipher acceleration

%package bin
Summary: bin components for the gnutls package.
Group: Binaries

%description bin
bin components for the gnutls package.


%package dev
Summary: dev components for the gnutls package.
Group: Development
Requires: gnutls-lib = %{version}-%{release}
Requires: gnutls-bin = %{version}-%{release}
Provides: gnutls-devel = %{version}-%{release}
Requires: gnutls = %{version}-%{release}

%description dev
dev components for the gnutls package.


%package dev32
Summary: dev32 components for the gnutls package.
Group: Default
Requires: gnutls-lib32 = %{version}-%{release}
Requires: gnutls-bin = %{version}-%{release}
Requires: gnutls-dev = %{version}-%{release}

%description dev32
dev32 components for the gnutls package.


%package extras
Summary: extras components for the gnutls package.
Group: Default

%description extras
extras components for the gnutls package.


%package lib
Summary: lib components for the gnutls package.
Group: Libraries

%description lib
lib components for the gnutls package.


%package lib32
Summary: lib32 components for the gnutls package.
Group: Default

%description lib32
lib32 components for the gnutls package.


%package locales
Summary: locales components for the gnutls package.
Group: Default

%description locales
locales components for the gnutls package.


%package staticdev
Summary: staticdev components for the gnutls package.
Group: Default
Requires: gnutls-dev = %{version}-%{release}

%description staticdev
staticdev components for the gnutls package.


%prep
%setup -q -n gnutls-3.6.15
cd %{_builddir}/gnutls-3.6.15
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
pushd ..
cp -a gnutls-3.6.15 build32
popd

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1610668908
export GCC_IGNORE_WERROR=1
## altflags_pgo content
## pgo generate
export PGO_GEN="-fprofile-generate=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-update=atomic -fprofile-arcs -ftest-coverage --coverage -fprofile-partial-training"
export CFLAGS_GENERATE="-O2 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -fcommon -fPIC -ffat-lto-objects -fPIC $PGO_GEN"
export FCFLAGS_GENERATE="-O2 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -fcommon -fPIC -ffat-lto-objects -ffat-lto-objects -fPIC $PGO_GEN"
export FFLAGS_GENERATE="-O2 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -fcommon -fPIC -ffat-lto-objects -ffat-lto-objects -fPIC $PGO_GEN"
export CXXFLAGS_GENERATE="-O2 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -fvisibility-inlines-hidden -pipe -fcommon -fPIC -ffat-lto-objects -ffat-lto-objects -fPIC $PGO_GEN"
export LDFLAGS_GENERATE="-O2 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -fcommon -fPIC -ffat-lto-objects -ffat-lto-objects -fPIC $PGO_GEN"
## pgo use
## -ffat-lto-objects -fno-PIE -fno-PIE -m64 -no-pie -fpic -fvisibility=hidden
## gcc: -feliminate-unused-debug-types -fipa-pta -flto=16 -Wno-error -Wp,-D_REENTRANT -fno-common
export PGO_USE="-fprofile-use=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-correction -fprofile-partial-training"
export CFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -fcommon -fPIC -ffat-lto-objects $PGO_USE"
export FCFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -fcommon -fPIC -ffat-lto-objects -ffat-lto-objects -fPIC $PGO_USE"
export FFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -fcommon -fPIC -ffat-lto-objects -ffat-lto-objects -fPIC $PGO_USE"
export CXXFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -fcommon -fPIC -ffat-lto-objects -ffat-lto-objects -fPIC $PGO_USE"
export LDFLAGS_USE="-g -O3 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -fcommon -fPIC -ffat-lto-objects -ffat-lto-objects -fPIC $PGO_USE"
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export PATH="/usr/lib64/ccache/bin:$PATH"
export CCACHE_NOHASHDIR=1
export CCACHE_DIRECT=1
export CCACHE_SLOPPINESS=pch_defines,locale,time_macros
# export CCACHE_DISABLE=1
# --disable-full-test-suite
## altflags_pgo end
export CFLAGS="${CFLAGS_GENERATE}"
export CXXFLAGS="${CXXFLAGS_GENERATE}"
export FFLAGS="${FFLAGS_GENERATE}"
export FCFLAGS="${FCFLAGS_GENERATE}"
export LDFLAGS="${LDFLAGS_GENERATE}"
 %configure  --enable-guile=no --with-default-trust-store-dir=/var/cache/ca-certs/anchors --enable-shared --enable-static --disable-rpath --disable-valgrind-tests --disable-gtk-doc-html --disable-gtk-doc-html --disable-gtk-doc-pdf --disable-doc --disable-gcc-warnings
make  %{?_smp_mflags}  V=1 VERBOSE=1 LDFLAGS="${LDFLAGS} -Wl,--whole-archive /usr/lib64/libunistring.a /usr/lib64/libtasn1.a /usr/lib64/libhogweed.a /usr/lib64/libnettle.a /usr/lib64/libgmp.a /usr/lib64/libidn2.a /usr/lib64/libunistring.a -Wl,--no-whole-archive"

make -j16 VERBOSE=1 V=1 LDFLAGS="${LDFLAGS} -Wl,--whole-archive /usr/lib64/libunistring.a /usr/lib64/libtasn1.a /usr/lib64/libhogweed.a /usr/lib64/libnettle.a /usr/lib64/libgmp.a /usr/lib64/libidn2.a /usr/lib64/libunistring.a -Wl,--no-whole-archive" check || :
make clean
export CFLAGS="${CFLAGS_USE}"
export CXXFLAGS="${CXXFLAGS_USE}"
export FFLAGS="${FFLAGS_USE}"
export FCFLAGS="${FCFLAGS_USE}"
export LDFLAGS="${LDFLAGS_USE}"
%configure  --enable-guile=no --with-default-trust-store-dir=/var/cache/ca-certs/anchors --enable-shared --enable-static --disable-rpath --disable-valgrind-tests --disable-gtk-doc-html --disable-gtk-doc-html --disable-gtk-doc-pdf --disable-doc --disable-gcc-warnings
make  %{?_smp_mflags}  V=1 VERBOSE=1 LDFLAGS="${LDFLAGS} -Wl,--whole-archive /usr/lib64/libunistring.a /usr/lib64/libtasn1.a /usr/lib64/libhogweed.a /usr/lib64/libnettle.a /usr/lib64/libgmp.a /usr/lib64/libidn2.a /usr/lib64/libunistring.a -Wl,--no-whole-archive"

pushd ../build32/
export CFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -pipe -fPIC -m32 -mstackrealign -march=native -mtune=native"
export CXXFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -fvisibility-inlines-hidden -pipe -fPIC -m32 -mstackrealign -march=native -mtune=native"
export LDFLAGS="-O2 -ffat-lto-objects -fuse-linker-plugin -pipe -fPIC -m32 -mstackrealign -march=native -mtune=native"
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
unset LD_LIBRARY_PATH
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure  --enable-guile=no --with-default-trust-store-dir=/var/cache/ca-certs/anchors --enable-shared --disable-static --disable-rpath --disable-valgrind-tests --disable-gtk-doc-html --disable-gtk-doc-html --disable-gtk-doc-pdf --disable-doc --disable-gcc-warnings --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}  V=1 VERBOSE=1
popd

%check
export LANG=C.UTF-8
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
make %{?_smp_mflags} check || :
cd ../build32;
make %{?_smp_mflags} check || : || :

%install
export SOURCE_DATE_EPOCH=1610668908
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install
%find_lang gnutls

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/certtool
/usr/bin/gnutls-cli
/usr/bin/gnutls-cli-debug
/usr/bin/gnutls-serv
/usr/bin/ocsptool
/usr/bin/p11tool
/usr/bin/psktool
/usr/bin/srptool

%files dev
%defattr(-,root,root,-)
/usr/include/gnutls/abstract.h
/usr/include/gnutls/compat.h
/usr/include/gnutls/crypto.h
/usr/include/gnutls/dtls.h
/usr/include/gnutls/gnutls.h
/usr/include/gnutls/gnutlsxx.h
/usr/include/gnutls/ocsp.h
/usr/include/gnutls/openpgp.h
/usr/include/gnutls/pkcs11.h
/usr/include/gnutls/pkcs12.h
/usr/include/gnutls/pkcs7.h
/usr/include/gnutls/self-test.h
/usr/include/gnutls/socket.h
/usr/include/gnutls/system-keys.h
/usr/include/gnutls/tpm.h
/usr/include/gnutls/urls.h
/usr/include/gnutls/x509-ext.h
/usr/include/gnutls/x509.h
/usr/lib64/libgnutls.so
/usr/lib64/pkgconfig/gnutls.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libgnutls.so
/usr/lib32/libgnutlsxx.so
/usr/lib32/pkgconfig/32gnutls.pc
/usr/lib32/pkgconfig/gnutls.pc

%files extras
%defattr(-,root,root,-)
/usr/lib64/libgnutlsxx.so
/usr/lib64/libgnutlsxx.so.28
/usr/lib64/libgnutlsxx.so.28.1.0

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgnutls.so.30
/usr/lib64/libgnutls.so.30.28.1

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libgnutls.so.30
/usr/lib32/libgnutls.so.30.28.1
/usr/lib32/libgnutlsxx.so.28
/usr/lib32/libgnutlsxx.so.28.1.0

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libgnutls.a
/usr/lib64/libgnutlsxx.a

%files locales -f gnutls.lang
%defattr(-,root,root,-)

