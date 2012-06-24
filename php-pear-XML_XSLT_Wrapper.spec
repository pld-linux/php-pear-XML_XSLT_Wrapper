%include	/usr/lib/rpm/macros.php
%define		_class		XML
%define		_subclass	XSLT
%define		_pearname	%{_class}_%{_subclass}_Wrapper

Summary:	%{_pearname} - single interface to the different XSLT interface or commands
Summary(pl):	%{_pearname} - jeden interfejs do r�nych interfejs�w i komend XSLT
Name:		php-pear-%{_pearname}
Version:	0.2.1
Release:	4
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	a8d29c179ddbe62f1215bfcc7f9e95e5
URL:		http://pear.php.net/package/XML_XSLT_Wrapper/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
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

%description -l pl
Ten pakiet zosta� napisany, by zapewni� prosty interfejs do
wykonywania transformacji XSL przy u�yciu r�nych bibliotek i polece�.
Ma obs�ug�: rozszerzenia PHP DOM XSLT, rozszerzenia PHP XSLT, MSXML
przy u�yciu rozszerzenia PHP COM, linii polece� XT
(http://www.blnz.com/xt/xt-20020426a-src/index.html), linii polece�
Sablotrona
(http://www.gingerall.com/charlie/ga/act/gadoc.act?pg=sablot#i__1940),
interfejsu Javy XT, interfejsu Javy i C xml.apache.org
(http://xml.apache.org/), Instant Saxon
(http://users.iclway.co.uk/mhkay/saxon/instant.html). Tryb wsadowy dla
XML-a: wiele transformacji jednego pliku XML; dla XSL-a: wiele
transformacji wielu plik�w XML przy u�yciu jednego XSL.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

install -d docs/%{_pearname}/examples
mv ./%{php_pear_dir}/data/%{_pearname}/examples/* docs/%{_pearname}/examples
rmdir ./%{php_pear_dir}/data/%{_pearname}/examples

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
