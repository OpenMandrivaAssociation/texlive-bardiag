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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The main purpose of the package is to make the drawing of bar diagrams
possible and easy in LaTeX. The BarDiag package is inspired by and based
on PSTricks.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/bardiag
%dir %{_datadir}/texmf-dist/tex/latex/bardiag
%dir %{_datadir}/texmf-dist/doc/latex/bardiag/example
%dir %{_datadir}/texmf-dist/doc/latex/bardiag/figs
%dir %{_datadir}/texmf-dist/doc/latex/bardiag/src
%dir %{_datadir}/texmf-dist/doc/latex/bardiag/example/src
%doc %{_datadir}/texmf-dist/doc/latex/bardiag/README
%doc %{_datadir}/texmf-dist/doc/latex/bardiag/bardiag.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bardiag/bardiag.tex
%doc %{_datadir}/texmf-dist/doc/latex/bardiag/bardiag1.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bardiag/bardiag1.tex
%doc %{_datadir}/texmf-dist/doc/latex/bardiag/bardiag2.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bardiag/bardiag2.tex
%doc %{_datadir}/texmf-dist/doc/latex/bardiag/example/altdiags.ps
%doc %{_datadir}/texmf-dist/doc/latex/bardiag/example/altdiags.tex
%doc %{_datadir}/texmf-dist/doc/latex/bardiag/example/compile.all
%doc %{_datadir}/texmf-dist/doc/latex/bardiag/example/diagrams.dvi
%doc %{_datadir}/texmf-dist/doc/latex/bardiag/example/diagrams.ps
%doc %{_datadir}/texmf-dist/doc/latex/bardiag/example/diagrams.tex
%doc %{_datadir}/texmf-dist/doc/latex/bardiag/example/diagramsbw.ps
%doc %{_datadir}/texmf-dist/doc/latex/bardiag/example/diagramsbw.tex
%doc %{_datadir}/texmf-dist/doc/latex/bardiag/example/src/10.tex
%doc %{_datadir}/texmf-dist/doc/latex/bardiag/example/src/1a.tex
%doc %{_datadir}/texmf-dist/doc/latex/bardiag/example/src/1b.tex
%doc %{_datadir}/texmf-dist/doc/latex/bardiag/example/src/2a.tex
%doc %{_datadir}/texmf-dist/doc/latex/bardiag/example/src/2b.tex
%doc %{_datadir}/texmf-dist/doc/latex/bardiag/example/src/3.tex
%doc %{_datadir}/texmf-dist/doc/latex/bardiag/example/src/4.tex
%doc %{_datadir}/texmf-dist/doc/latex/bardiag/example/src/5.tex
%doc %{_datadir}/texmf-dist/doc/latex/bardiag/example/src/6.tex
%doc %{_datadir}/texmf-dist/doc/latex/bardiag/example/src/7.tex
%doc %{_datadir}/texmf-dist/doc/latex/bardiag/example/src/8.tex
%doc %{_datadir}/texmf-dist/doc/latex/bardiag/example/src/9.tex
%doc %{_datadir}/texmf-dist/doc/latex/bardiag/figs/diag.eps
%doc %{_datadir}/texmf-dist/doc/latex/bardiag/figs/diagleg.eps
%doc %{_datadir}/texmf-dist/doc/latex/bardiag/figs/examp1.tex
%doc %{_datadir}/texmf-dist/doc/latex/bardiag/figs/examp1a.tex
%doc %{_datadir}/texmf-dist/doc/latex/bardiag/figs/examp1b.tex
%doc %{_datadir}/texmf-dist/doc/latex/bardiag/figs/examp2.tex
%doc %{_datadir}/texmf-dist/doc/latex/bardiag/figs/examp2er.tex
%doc %{_datadir}/texmf-dist/doc/latex/bardiag/figs/examp3.tex
%doc %{_datadir}/texmf-dist/doc/latex/bardiag/figs/examp4.tex
%doc %{_datadir}/texmf-dist/doc/latex/bardiag/figs/examp5.tex
%doc %{_datadir}/texmf-dist/doc/latex/bardiag/figs/examp6.tex
%doc %{_datadir}/texmf-dist/doc/latex/bardiag/figs/exampcr.tex
%doc %{_datadir}/texmf-dist/doc/latex/bardiag/figs/tddiag.eps
%doc %{_datadir}/texmf-dist/doc/latex/bardiag/src/10.tex
%doc %{_datadir}/texmf-dist/doc/latex/bardiag/src/1a.tex
%doc %{_datadir}/texmf-dist/doc/latex/bardiag/src/1b.tex
%doc %{_datadir}/texmf-dist/doc/latex/bardiag/src/2a.tex
%doc %{_datadir}/texmf-dist/doc/latex/bardiag/src/2b.tex
%doc %{_datadir}/texmf-dist/doc/latex/bardiag/src/3.tex
%doc %{_datadir}/texmf-dist/doc/latex/bardiag/src/4.tex
%doc %{_datadir}/texmf-dist/doc/latex/bardiag/src/5.tex
%doc %{_datadir}/texmf-dist/doc/latex/bardiag/src/6.tex
%doc %{_datadir}/texmf-dist/doc/latex/bardiag/src/7.tex
%doc %{_datadir}/texmf-dist/doc/latex/bardiag/src/8.tex
%doc %{_datadir}/texmf-dist/doc/latex/bardiag/src/9.tex
%{_datadir}/texmf-dist/tex/latex/bardiag/barddoc.sty
%{_datadir}/texmf-dist/tex/latex/bardiag/bardiag.bar
%{_datadir}/texmf-dist/tex/latex/bardiag/bardiag.cfg
%{_datadir}/texmf-dist/tex/latex/bardiag/bardiag.sty
%{_datadir}/texmf-dist/tex/latex/bardiag/pstfp.sty
