Name:		texlive-inputtrc
Version:	28019
Release:	2
Summary:	Trace which file loads which
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/inputtrc
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/inputtrc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/inputtrc.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/inputtrc.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package produces screen/log messages of the form '<current>
INPUTTING <next>' reporting LaTeX input commands (<current> and
<next> being file names). The message is indented to reflect
the level of input nesting. Tracing may be turned on and off,
and the unit of indentation may be adjusted. The implementation
somewhat resembles those of packages FiNK and inputfile.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/inputtrc/inputtrc.RLS
%{_texmfdistdir}/tex/latex/inputtrc/inputtrc.sty
%doc %{_texmfdistdir}/doc/latex/inputtrc/README
%doc %{_texmfdistdir}/doc/latex/inputtrc/README.pdf
%doc %{_texmfdistdir}/doc/latex/inputtrc/RELEASE.txt
%doc %{_texmfdistdir}/doc/latex/inputtrc/SrcFILEs.txt
%doc %{_texmfdistdir}/doc/latex/inputtrc/inputtrc.pdf
#- source
%doc %{_texmfdistdir}/source/latex/inputtrc/README.tex
%doc %{_texmfdistdir}/source/latex/inputtrc/inputtrc.tex
%doc %{_texmfdistdir}/source/latex/inputtrc/srcfiles.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
