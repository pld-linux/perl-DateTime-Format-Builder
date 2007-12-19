#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	DateTime
%define	pnam	Format-Builder
Summary:	DateTime::Format::Builder - Create DateTime parser classes and objects
Summary(pl.UTF-8):	DateTime::Format::Builder - tworzenie klas i obiektów analizatorów DateTime
Name:		perl-DateTime-Format-Builder
Version:	0.7901
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/D/DR/DROLSKY/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	43407285237cdc3cdd2c08b936229198
URL:		http://search.cpan.org/dist/DateTime-Format-Builder/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-Factory-Util >= 1.6
BuildRequires:	perl-DateTime >= 0.12
BuildRequires:	perl-DateTime-Format-Strptime >= 1.04
BuildRequires:	perl-Params-Validate >= 0.72
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DateTime::Format::Builder creates DateTime parsers. Many string
formats of dates and times are simple and just require a basic
regular expression to extract the relevant information. Builder
provides a simple way to do this without writing reams of structural
code.

Builder provides a number of methods, most of which you'll never need,
or at least rarely need. They're provided more for exposing of the
module's innards to any subclasses, or for when you need to do
something slightly beyond what I expected.

%description -l pl.UTF-8
DateTime::Format::Builder tworzy analizatory DateTime. Wiele formatów
łańcuchów dat i czasu jest prostych i do wyciągnięcia istotnych
informacji wymaga jedynie prostego wyrażenia regularnego. Builder
udostępnia prosty sposób wykonania tego bez pisania większego kodu
strukturalnego.

Builder udostępnia wiele metod, z których większości się nie używa lub
używa bardzo rzadko. Są udostępnione bardziej dla ukazania wnętrzności
modułu dla podklas albo w razie potrzeby zrobienia czegoś więcej niż
oczekiwał autor.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS Changes CREDITS INSTALL README
%{perl_vendorlib}/DateTime/Format/*.pm
%{perl_vendorlib}/DateTime/Format/Builder
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
