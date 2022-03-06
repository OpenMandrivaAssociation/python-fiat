%define	omodule FIAT
%define	module %(echo %omodule | tr [:upper:] [:lower:])

Summary:	FInite element Automatic Tabulator for Python
Name:		python-%{module}
Version:	2019.1.0
Release:	1
License:	LGPLv3+
Group:		Development/Python
URL:		http://fenicsproject.org
Source0:	https://bitbucket.org/fenics-project/%{module}/downloads/%{module}-%{version}.tar.gz

BuildRequires:	pkgconfig(python3)
BuildRequires:	python3dist(numpy)
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(sympy)

BuildArch:	noarch
%description
The FInite element Automatic Tabulator FIAT supports generation of arbitrary
order instances of the Lagrange elements on lines, triangles, and
tetrahedra. It is also capable of generating arbitrary order instances of
Jacobi-type quadrature rules on the same element shapes. Further, H(div) and 
H(curl) conforming finite element spaces such as the families of
Raviart-Thomas, Brezzi-Douglas-Marini and Nedelec are supported on triangles
and tetrahedra. Upcoming versions will also support Hermite and
nonconforming elements.

Instant is part of the FEniCS Project.

%files
%license COPYING
%license COPYING.LESSER
%doc README.rst
%doc AUTHORS
%{py_sitedir}/%{omodule}/
%{py_sitedir}/fenics_%{module}-%{version}-py%{python_version}.egg-info/

#----------------------------------------------------------------------------

%prep
%autosetup -n %{module}-%{version}

%build
%py_build

%install
%py_install

