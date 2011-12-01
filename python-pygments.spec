%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           python-pygments
Version:        1.1.1
Release:        1%{?dist}
Summary:        A syntax highlighting engine written in Python

Group:          Development/Libraries
License:        BSD
URL:            http://pygments.org/
Source0:        http://cheeseshop.python.org/packages/source/P/Pygments/Pygments-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python-devel, python-setuptools
Requires:       python-setuptools


%description
Pygments is a syntax highlighting engine written in Python. That means, it 
will take source code (or other markup) in a supported language and output 
a processed version (in different formats) containing syntax highlighting 
markup.


%prep
%setup -q -n Pygments-%{version}


%build
%{__python} setup.py build
%{__sed} -i 's/\r//' LICENSE


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1/
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT
mv docs/pygmentize.1 $RPM_BUILD_ROOT%{_mandir}/man1/pygmentize.1


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc AUTHORS CHANGES docs/ LICENSE TODO 
# For noarch packages: sitelib
%{python_sitelib}/*
%{_bindir}/pygmentize
%lang(en) %{_mandir}/man1/pygmentize.1.gz


%changelog
* Tue Sep 29 2009 Steve 'Ashcrow' Milner <me@stevemilner.org> - 1.1.1-1
- Updated for release.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Dec 21 2008 Steve 'Ashcrow' Milner <me@stevemilner.org> - 1.0-3
- Updated for release.

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1.0-2
- Rebuild for Python 2.6

* Fri Nov 27 2008 Steve 'Ashcrow' Milner <me@stevemilner.org> - 1.0-1
- Updated for upstream 1.0.

* Sun Sep 14 2008 Steve 'Ashcrow' Milner <me@stevemilner.org> - 0.11.1-1
- Updated for upstream 0.11.

* Mon Jul 21 2008 Steve 'Ashcrow' Milner <me@stevemilner.org> - 0.10-1
- Updated for upstream 0.10.

* Thu Nov 29 2007 Steve 'Ashcrow' Milner <me@stevemilner.org> - 0.9-2
- Added python-setuptools as a Requires per bz#403601.

* Mon Nov 12 2007 Steve 'Ashcrow' Milner <me@stevemilner.org> - 0.9-1
- Updated for upstream 0.9.

* Thu Aug 17 2007 Steve 'Ashcrow' Milner <me@stevemilner.org> - 0.8.1-2
- Removed the dos2unix build dependency.

* Thu Jun 28 2007 Steve 'Ashcrow' Milner <me@stevemilner.org> - 0.8.1-1
- Initial packaging for Fedora.
