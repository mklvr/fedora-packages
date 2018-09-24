Name:           perl-Mojolicious-Plugin-OAuth2
Version:        1.57
Release:        1%{?dist}
Summary:        A Mojolicious plugin that allows OAuth2 authentication

License:        Artistic 2.0
URL:            https://github.com/marcusramberg/Mojolicious-Plugin-OAuth2
Source0:        https://github.com/marcusramberg/Mojolicious-Plugin-OAuth2/archive/%{version}/Mojolicious-Plugin-OAuth2-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(IO::Socket::SSL)
BuildRequires:  perl(Mojolicious) >= 7.53
BuildRequires:  perl(lib)
BuildRequires:  perl(Mojo::Base)
BuildRequires:  perl(Mojo::Util)
BuildRequires:  perl(Mojolicious::Lite)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Mojo)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Output) >= 1
BuildRequires:  perl(warnings)

Requires:  perl(IO::Socket::SSL)
Requires:  perl(Mojolicious) >= 7.53

%{?perl_default_filter}

%description
This Mojolicious plugin allows you to easily authenticate against a OAuth2
provider. It includes configurations for a few popular providers, but you can
add your own easily as well.

%prep
%setup -q -n Mojolicious-Plugin-OAuth2-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 OPTIMIZE="$RPM_OPT_FLAGS"
%{__make} %{?_smp_mflags}

%install
%{__make} pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
%{__make} test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Mon Sep 24 2018 Mike Oliver <mike@mklvr.io> - 1.57-1
- Initial package creation
