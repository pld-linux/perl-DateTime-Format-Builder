#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define	pdir	DateTime
%define	pnam	Format-Builder
Summary:	DateTime::Format::Builder - Create DateTime parser classes and objects
Summary(pl.UTF-8):	DateTime::Format::Builder - tworzenie klas i obiektów analizatorów DateTime
Name:		perl-DateTime-Format-Builder
Version:	0.83
Release:	1
Epoch:		1
License:	Artistic v2.0
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/DateTime/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	aa41917ca9ad69b3898728ce9c2fb477
URL:		https://metacpan.org/dist/DateTime-Format-Builder
BuildRequires:	perl-ExtUtils-MakeMaker
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl-DateTime >= 1.0.0
BuildRequires:	perl-DateTime-Format-Strptime >= 1.04
BuildRequires:	perl-Params-Validate >= 0.72
BuildRequires:	perl-Scalar-List-Utils
BuildRequires:	perl-Test-Simple >= 0.96
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
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/DateTime/Format/Builder/Tutorial.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README.md
%{perl_vendorlib}/DateTime/Format/Builder.pm
%{perl_vendorlib}/DateTime/Format/Builder
%{_mandir}/man3/DateTime::Format::Builder*.3pm*
%{_examplesdir}/%{name}-%{version}
