%define upstream_name    Catalyst-Plugin-Unicode
%define upstream_version 0.92

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Unicode aware Catalyst
License:	Artistic/GPL
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Catalyst::Runtime)
BuildRequires:	perl(Test::WWW::Mechanize::Catalyst)
BuildRequires:	perl(Test::use::ok)
BuildRequires:	perl(IO::Scalar)
BuildRequires:	perl(MRO::Compat) >= 0.10
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
On request, decodes all params from UTF-8 octets into a sequence of
logical characters. On response, encodes body into UTF-8 octets.


%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor --skipdeps
%make

%check
%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/*/*
%{perl_vendorlib}/Catalyst
