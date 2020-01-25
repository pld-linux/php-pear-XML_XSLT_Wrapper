%define		_class		XML
%define		_subclass	XSLT
%define		_pearname	%{_class}_%{_subclass}_Wrapper

Summary:	%{_pearname} - single interface to the different XSLT interface or commands
Summary(pl.UTF-8):	%{_pearname} - jeden interfejs do różnych interfejsów i komend XSLT
Name:		php-pear-%{_pearname}
Version:	0.2.2
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	25e0ee88b56ea4eb87c709c5777b0d7a
URL:		http://pear.php.net/package/XML_XSLT_Wrapper/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package was written to provide a simpler, cross-library and cross
commands interface to doing XSL transformations. It provides support
for: DOM XSLT PHP extension, XSLT PHP extension, MSXML using COM PHP
extension, XT command line
(http://www.blnz.com/xt/xt-20020426a-src/index.html), Sablotron
command line
(http://www.gingerall.com/charlie/ga/act/gadoc.act?pg=sablot#i__1940),
XT java interface, xml.apache.org java and C interface
(http://xml.apache.org/), Instant Saxon
(http://users.iclway.co.uk/mhkay/saxon/instant.html). Batch mode: XML:
multiple transformations of a single XML file, XSL: multiple
transformations of multiple XML files using a single XSL.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Ten pakiet został napisany, by zapewnić prosty interfejs do
wykonywania transformacji XSL przy użyciu różnych bibliotek i poleceń.
Ma obsługę: rozszerzenia PHP DOM XSLT, rozszerzenia PHP XSLT, MSXML
przy użyciu rozszerzenia PHP COM, linii poleceń XT
(http://www.blnz.com/xt/xt-20020426a-src/index.html), linii poleceń
Sablotrona
(http://www.gingerall.com/charlie/ga/act/gadoc.act?pg=sablot#i__1940),
interfejsu Javy XT, interfejsu Javy i C xml.apache.org
(http://xml.apache.org/), Instant Saxon
(http://users.iclway.co.uk/mhkay/saxon/instant.html). Tryb wsadowy dla
XML-a: wiele transformacji jednego pliku XML; dla XSL-a: wiele
transformacji wielu plików XML przy użyciu jednego XSL.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/*
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%dir %{php_pear_dir}/%{_class}/%{_subclass}/Wrapper
%dir %{php_pear_dir}/%{_class}/%{_subclass}/Wrapper/Backend
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/Wrapper/Backend/*.php
