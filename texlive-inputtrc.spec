Name:		texlive-inputtrc
Version:	0.2d
Release:	1
Summary:	Trace which file loads which
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/inputtrc
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/inputtrc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/inputtrc.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/inputtrc.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package produces screen/log messages of the form '<current>
INPUTTING <next>' reporting LaTeX input commands (<current> and
<next> being file names). The message is indented to reflect
the level of input nesting. Tracing may be turned on and off,
and the unit of indentation may be adjusted. The implementation
somewhat resembles those of packages FiNK and inputfile.

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
%{_texmfdistdir}/tex/latex/inputtrc/inputtrc.sty
%doc %{_texmfdistdir}/doc/latex/inputtrc/FileList.txt
%doc %{_texmfdistdir}/doc/latex/inputtrc/README
%doc %{_texmfdistdir}/doc/latex/inputtrc/README.pdf
%doc %{_texmfdistdir}/doc/latex/inputtrc/README.txt
%doc %{_texmfdistdir}/doc/latex/inputtrc/RELEASE.txt
%doc %{_texmfdistdir}/doc/latex/inputtrc/inputtrc.pdf
#- source
%doc %{_texmfdistdir}/source/latex/inputtrc/README.tex
%doc %{_texmfdistdir}/source/latex/inputtrc/gather.tex
%doc %{_texmfdistdir}/source/latex/inputtrc/inputtrc.tex
%doc %{_texmfdistdir}/source/latex/inputtrc/makedoc.cfg

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}