Name:           perl-WWW-xkcd
Version:        0.009
Release:        1%{?dist}
Summary:        Synchronous and asynchronous interfaces to xkcd comics

License:        GPL+ or Artistic
URL:            https://metacpan.org/release/WWW-xkcd
Source0:        https://cpan.metacpan.org/authors/id/X/XS/XSAWYERX/WWW-xkcd-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(JSON::MaybeXS)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Fatal)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

Recommends:     perl(AnyEvent)
Recommends:     perl(AnyEvent::HTTP)

%{?perl_default_filter}

%description
This module allows you to access xkcd comics (http://www.xkcd.com/) using
the official API in synchronous mode (what people are used to) or in
asynchronous mode.

The asynchronous mode requires you have AnyEvent and AnyEvent::HTTP
available. However, since it's just supported and not necessary, it is not
declared as a prerequisite.

%prep
%setup -q -n WWW-xkcd-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{__make} %{?_smp_mflags}

%install
%{__make} pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
# This test requires network access. Disable for Koji builds.
%{?!_with_network_tests: rm t/sync.t }
%{__make} test

%files
%doc Changes
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Sep 24 2018 Mike Oliver <mike@mklvr.io> - 0.009-1
- Initial package creation
