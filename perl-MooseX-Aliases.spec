#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	MooseX
%define		pnam	Aliases
%include	/usr/lib/rpm/macros.perl
Summary:	MooseX::Aliases - easy aliasing of methods and attributes in Moose
Name:		perl-MooseX-Aliases
Version:	0.10
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/MooseX/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	148876a7f538881a81597669932c49bc
URL:		http://search.cpan.org/dist/MooseX-Aliases/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Moose >= 1.09
BuildRequires:	perl-Test-Fatal >= 0.003
BuildRequires:	perl-Test-Requires
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The MooseX::Aliases module will allow you to quickly alias methods in
Moose. It provides an alias parameter for has() to generate aliased
accessors as well as the standard ones. Attributes can also be
initialized in the constructor via their aliased names.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/MooseX/Aliases.pm
%{perl_vendorlib}/MooseX/Aliases
%{_mandir}/man3/*
