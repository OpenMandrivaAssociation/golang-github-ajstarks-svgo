# Run tests in check section
%bcond_without check

%global goipath         github.com/ajstarks/svgo
%global commit          644b8db467afccf19a0692a3e31a1868e4287ab8

%global common_description %{expand:
The library generates SVG as defined by the Scalable Vector Graphics 1.1 
Specification (http://www.w3.org/TR/SVG11/). Output goes to the specified 
io.Writer.}

%gometa

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        Go library for SVG generation
License:        CC-BY
URL:            %{gourl}
Source0:        %{gosource}

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.3.git644b8db
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 03 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.2.20180421git644b8db
- Fix typo in the changelog

* Fri Mar 23 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20180421git644b8db
- First package for Fedora

