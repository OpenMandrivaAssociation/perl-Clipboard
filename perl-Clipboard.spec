%define module   Clipboard
%define version    0.09
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Copy and paste with any OS
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module//%{module}-%{version}.tar.gz
BuildRequires: perl(Spiffy)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Who doesn't remember the first time they learned to copy and paste, and
generated an exponentially growing text document? Yes, that's right,
clipboards are magical.

With Clipboard.pm, this magic is now trivial to access, cross-platformly,
from your Perl code.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/Clipboard.pm
%{perl_vendorlib}/Clipboard
%{_bindir}/*
%{_mandir}/man1/*

