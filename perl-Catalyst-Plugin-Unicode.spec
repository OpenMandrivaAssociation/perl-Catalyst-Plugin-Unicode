%define upstream_name    Catalyst-Plugin-Unicode
%define upstream_version 0.93

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Unicode aware Catalyst
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Catalyst/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Catalyst::Runtime)
BuildRequires:	perl(Test::WWW::Mechanize::Catalyst)
BuildRequires:	perl(Test::use::ok)
BuildRequires:	perl(IO::Scalar)
BuildRequires:	perl(MRO::Compat) >= 0.10
BuildArch:	noarch

%description
On request, decodes all params from UTF-8 octets into a sequence of
logical characters. On response, encodes body into UTF-8 octets.


%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor --skipdeps
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/*/*
%{perl_vendorlib}/Catalyst


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.930.0-2mdv2011.0
+ Revision: 680766
- mass rebuild

* Mon Mar 22 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.930.0-1mdv2011.0
+ Revision: 526427
- update to 0.93

* Fri Nov 06 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.920.0-1mdv2010.1
+ Revision: 461725
- update to 0.92

* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.910.0-1mdv2010.0
+ Revision: 406309
- rebuild using %%perl_convert_version

* Mon May 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.91-1mdv2010.0
+ Revision: 371666
- update to new version 0.91

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.8-3mdv2009.0
+ Revision: 255579
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Oct 13 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.8-1mdv2008.1
+ Revision: 98029
- new version

* Wed Aug 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.5-1mdv2008.0
+ Revision: 69239
- new version


* Tue Apr 04 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.2-2mdk
- Add Buildrequires

* Sun Mar 12 2006 Scott Karns <scott@karnstech.com> 0.2-1mdk
- First Mandriva release

