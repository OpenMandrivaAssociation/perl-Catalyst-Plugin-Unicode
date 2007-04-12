%define realname Catalyst-Plugin-Unicode
%define name	perl-%{realname}
%define version	0.2
%define release	%mkrel 2

Summary:	Unicode aware Catalyst
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	Artistic/GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{realname}/
Source:		http://search.cpan.org/CPAN/authors/id/M/MR/MRAMBERG/%{realname}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%else
BuildRequires:	perl
%endif
BuildRequires:  perl-Module-Build

BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-root

%description
On request, decodes all params from UTF-8 octets into a sequence of
logical characters. On response, encodes body into UTF-8 octets.


%prep
%setup -q -n %{realname}-%{version}

%build
%__perl Build.PL installdirs=vendor
./Build

%check
./Build test

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/*/*
%{perl_vendorlib}/Catalyst/Plugin/*

%clean
rm -rf $RPM_BUILD_ROOT

