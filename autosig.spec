Summary:	Autosig - tool for generating .signature and .plan files
Summary(pl):	Autosig - narzêdzie do tworzenia plików .signature, .plan
Name:		autosig
Version:	2.3
Release:	0.2
License:	GPL v2
Group:		Applications/Console
Source0:	http://www.irendi.com/~msharpe/%{name}-%{version}.tar.gz
# Source0-md5:	b13ddbef5051b2b2249d5faef61374be
URL:		http://www.irendi.com/~msharpe
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Autosig is a small utility for generating .signature files for email
and .plan files for finger.

%description -l pl
Autosig jest prostym narzêdziem generuj±cym pliki .signature oraz
.plan.

%prep
%setup -q

%build
%{__make} \
	DEFINES="%{rpmcflags} -DNEED_BASENAME" \
	CC="%{__cc}"

%{__sed} -i 's/quotes/\/usr\/share\/autosig\/quotes/' chplan
%{__sed} -i 's/dotplannc/\/usr\/share\/autosig\/dotplannc/' chplan
%{__sed} -i 's/planFile=dotplan/planFile=$quoteFile/' chplan
%{__sed} -i 's/quotes/\/usr\/share\/autosig\/quotes/' selm
%{__sed} -i 's/dotsignc/\/usr\/share\/autosig\/dotsignc/' selm
%{__sed} -i 's/quotes/\/usr\/share\/autosig\/quotes/' chsig
%{__sed} -i 's/dotsignc/\/usr\/share\/autosig\/dotsignc/' chsig

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}

install autosig autosigd chplan chsig selm smutt $RPM_BUILD_ROOT%{_bindir}
install dotplannc dotsignc quotes $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
