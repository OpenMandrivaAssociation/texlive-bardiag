%global tl_name bardiag
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.4a
Release:	%{tl_revision}.1
Summary:	LaTeX package for drawing bar diagrams
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/bardiag
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bardiag.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bardiag.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The main purpose of the package is to make the drawing of bar diagrams
possible and easy in LaTeX. The BarDiag package is inspired by and based
on PSTricks.

