%define module   Clipboard

%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Mac::Pasteboard\\)|perl\\(Win32::Clipboard\\)'
%endif

Name:		perl-%{module}
Version:	0.13
Release:	5
Summary:	Copy and paste with any OS
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/%{module}-%{version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	perl(Spiffy)
BuildArch:	noarch

%description
Who doesn't remember the first time they learned to copy and paste, and
generated an exponentially growing text document? Yes, that's right,
clipboards are magical.

With Clipboard.pm, this magic is now trivial to access, cross-platformly,
from your Perl code.

%prep
%setup -q -n %{module}-%{version} 

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/Clipboard.pm
%{perl_vendorlib}/Clipboard
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.13-2mdv2011.0
+ Revision: 680832
- mass rebuild

* Tue Oct 19 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.13-1mdv2011.0
+ Revision: 586766
- new version

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 0.09-2mdv2011.0
+ Revision: 440540
- rebuild

* Fri Jan 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.09-1mdv2009.1
+ Revision: 327454
- import perl-Clipboard


* Fri Jan 09 2009 cpan2dist 0.09-1mdv
- initial mdv release, generated with cpan2dist

