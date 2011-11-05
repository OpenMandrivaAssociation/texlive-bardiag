# revision 22013
# category Package
# catalog-ctan /graphics/bardiag
# catalog-date 2006-12-21 16:38:41 +0100
# catalog-license lppl
# catalog-version 0.4a
Name:		texlive-bardiag
Version:	0.4a
Release:	1
Summary:	LateX package for drawing bar diagrams
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/bardiag
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bardiag.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bardiag.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The main purpose of the package is to make the drawing of bar
diagrams possible and easy in LaTeX. The BarDiag package is
inspired by and based on PSTricks.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/bardiag/barddoc.sty
%{_texmfdistdir}/tex/latex/bardiag/bardiag.bar
%{_texmfdistdir}/tex/latex/bardiag/bardiag.cfg
%{_texmfdistdir}/tex/latex/bardiag/bardiag.sty
%{_texmfdistdir}/tex/latex/bardiag/pstfp.sty
%doc %{_texmfdistdir}/doc/latex/bardiag/README
%doc %{_texmfdistdir}/doc/latex/bardiag/bardiag.pdf
%doc %{_texmfdistdir}/doc/latex/bardiag/bardiag.tex
%doc %{_texmfdistdir}/doc/latex/bardiag/bardiag1.pdf
%doc %{_texmfdistdir}/doc/latex/bardiag/bardiag1.tex
%doc %{_texmfdistdir}/doc/latex/bardiag/bardiag2.pdf
%doc %{_texmfdistdir}/doc/latex/bardiag/bardiag2.tex
%doc %{_texmfdistdir}/doc/latex/bardiag/example/altdiags.ps
%doc %{_texmfdistdir}/doc/latex/bardiag/example/altdiags.tex
%doc %{_texmfdistdir}/doc/latex/bardiag/example/compile.all
%doc %{_texmfdistdir}/doc/latex/bardiag/example/diagrams.dvi
%doc %{_texmfdistdir}/doc/latex/bardiag/example/diagrams.ps
%doc %{_texmfdistdir}/doc/latex/bardiag/example/diagrams.tex
%doc %{_texmfdistdir}/doc/latex/bardiag/example/diagramsbw.ps
%doc %{_texmfdistdir}/doc/latex/bardiag/example/diagramsbw.tex
%doc %{_texmfdistdir}/doc/latex/bardiag/example/src/10.tex
%doc %{_texmfdistdir}/doc/latex/bardiag/example/src/1a.tex
%doc %{_texmfdistdir}/doc/latex/bardiag/example/src/1b.tex
%doc %{_texmfdistdir}/doc/latex/bardiag/example/src/2a.tex
%doc %{_texmfdistdir}/doc/latex/bardiag/example/src/2b.tex
%doc %{_texmfdistdir}/doc/latex/bardiag/example/src/3.tex
%doc %{_texmfdistdir}/doc/latex/bardiag/example/src/4.tex
%doc %{_texmfdistdir}/doc/latex/bardiag/example/src/5.tex
%doc %{_texmfdistdir}/doc/latex/bardiag/example/src/6.tex
%doc %{_texmfdistdir}/doc/latex/bardiag/example/src/7.tex
%doc %{_texmfdistdir}/doc/latex/bardiag/example/src/8.tex
%doc %{_texmfdistdir}/doc/latex/bardiag/example/src/9.tex
%doc %{_texmfdistdir}/doc/latex/bardiag/figs/diag.eps
%doc %{_texmfdistdir}/doc/latex/bardiag/figs/diagleg.eps
%doc %{_texmfdistdir}/doc/latex/bardiag/figs/examp1.tex
%doc %{_texmfdistdir}/doc/latex/bardiag/figs/examp1a.tex
%doc %{_texmfdistdir}/doc/latex/bardiag/figs/examp1b.tex
%doc %{_texmfdistdir}/doc/latex/bardiag/figs/examp2.tex
%doc %{_texmfdistdir}/doc/latex/bardiag/figs/examp2er.tex
%doc %{_texmfdistdir}/doc/latex/bardiag/figs/examp3.tex
%doc %{_texmfdistdir}/doc/latex/bardiag/figs/examp4.tex
%doc %{_texmfdistdir}/doc/latex/bardiag/figs/examp5.tex
%doc %{_texmfdistdir}/doc/latex/bardiag/figs/examp6.tex
%doc %{_texmfdistdir}/doc/latex/bardiag/figs/exampcr.tex
%doc %{_texmfdistdir}/doc/latex/bardiag/figs/tddiag.eps
%doc %{_texmfdistdir}/doc/latex/bardiag/src/10.tex
%doc %{_texmfdistdir}/doc/latex/bardiag/src/1a.tex
%doc %{_texmfdistdir}/doc/latex/bardiag/src/1b.tex
%doc %{_texmfdistdir}/doc/latex/bardiag/src/2a.tex
%doc %{_texmfdistdir}/doc/latex/bardiag/src/2b.tex
%doc %{_texmfdistdir}/doc/latex/bardiag/src/3.tex
%doc %{_texmfdistdir}/doc/latex/bardiag/src/4.tex
%doc %{_texmfdistdir}/doc/latex/bardiag/src/5.tex
%doc %{_texmfdistdir}/doc/latex/bardiag/src/6.tex
%doc %{_texmfdistdir}/doc/latex/bardiag/src/7.tex
%doc %{_texmfdistdir}/doc/latex/bardiag/src/8.tex
%doc %{_texmfdistdir}/doc/latex/bardiag/src/9.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
