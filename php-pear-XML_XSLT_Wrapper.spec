%include	/usr/lib/rpm/macros.php
%define         _class          XML
%define         _subclass       XSLT
%define		_pearname	%{_class}_%{_subclass}_Wrapper
Summary:	%{_pearname} - single interface to the different XSLT interface or commands
Summary(pl):	%{_pearname} - jeden interfejs do ró¿nych interfejsów i komend XSLT
Name:		php-pear-%{_pearname}
Version:	0.1
Release:	3
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
URL:		http://pear.php.net/
Patch0:		%{name}-pathfix.patch
BuildRequires:	rpm-php-pearprov
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package was written to provide a simpler, cross-library and cross
commands interface to doing XSL transformations. It provides support
for: DOM XSLT php extension, XSLT php extension, MSXML using COM php
extension, XT command line
(http://www.blnz.com/xt/xt-20020426a-src/index.html), Sablotron
command line
(http://www.gingerall.com/charlie/ga/act/gadoc.act?pg=sablot#i__1940),
XT java interface, xml.apache.org java and C interface
(http://xml.apache.org/), Instant Saxon
(http://users.iclway.co.uk/mhkay/saxon/instant.html). Batch mode: XML:
multiple transformations of a single XML file, XSL: multiple
transformations of multiple XML files using a single XSL.

%description -l pl
Ten pakiet zosta³ napisany, by zapewniæ prosty interfejs do
wykonywania transformacji XSL przy u¿yciu ró¿nych bibliotek i poleceñ.
Ma obs³ugê: rozszerzenia PHP DOM XSLT, rozszerzenia PHP XSLT, MSXML
przy u¿yciu rozszerzenia PHP COM, linii poleceñ XT
(http://www.blnz.com/xt/xt-20020426a-src/index.html), linii poleceñ
Sablotrona
(http://www.gingerall.com/charlie/ga/act/gadoc.act?pg=sablot#i__1940),
interfejsu Javy XT, interfejsu Javy i C xml.apache.org
(http://xml.apache.org/), Instant Saxon
(http://users.iclway.co.uk/mhkay/saxon/instant.html). Tryb wsadowy dla
XML: wiele transformacji jednego pliku XML; dla XSL: wiele
transformacji wielu plików XML przy u¿yciu jednego XSL.

%prep
%setup -q -c
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Wrapper/Backend

install %{_pearname}-%{version}/XSLT_Wrapper.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Wrapper.php
install %{_pearname}-%{version}/Backend/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Wrapper/Backend

# remove windows class:
rm $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Wrapper/Backend/*Com.php

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/{TODO,examples/*}
%dir %{php_pear_dir}/%{_class}/%{_subclass}
%dir %{php_pear_dir}/%{_class}/%{_subclass}/Wrapper
%dir %{php_pear_dir}/%{_class}/%{_subclass}/Wrapper/Backend
%{php_pear_dir}/%{_class}/%{_subclass}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}/Wrapper/Backend/*.php
