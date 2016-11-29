%{?scl:%scl_package glassfish-annotation-api}
%{!?scl:%global pkg_name %{name}}
%{?java_common_find_provides_and_requires}

%global baserelease 1

%global namedreltag %{nil}
%global namedversion %{version}%{?namedreltag}
%global oname javax.annotation-api
Name:          %{?scl_prefix}glassfish-annotation-api
Version:       1.2
Release:       10.%{baserelease}%{?dist}
Summary:       Common Annotations API Specification (JSR 250)
License:       CDDL or GPLv2 with exceptions
# http://jcp.org/en/jsr/detail?id=250
URL:           http://glassfish.java.net/
# svn export https://svn.java.net/svn/glassfish~svn/tags/javax.annotation-api-1.2/ glassfish-annotation-api-1.2
# tar czf glassfish-annotation-api-1.2-src-svn.tar.gz glassfish-annotation-api-1.2
Source0:       %{pkg_name}-%{namedversion}-src-svn.tar.gz

BuildRequires: %{?scl_prefix_maven}jvnet-parent
BuildRequires: %{?scl_prefix_maven}glassfish-legal

BuildRequires: %{?scl_prefix_maven}maven-local
BuildRequires: %{?scl_prefix_maven}maven-plugin-bundle
BuildRequires: %{?scl_prefix_maven}maven-remote-resources-plugin
BuildRequires: %{?scl_prefix_maven}maven-source-plugin
BuildRequires: %{?scl_prefix_maven}spec-version-maven-plugin

BuildArch:     noarch

%description
Common Annotations APIs for the Java Platform (JSR 250).

%package javadoc
Summary:       Javadoc for %{pkg_name}

%description javadoc
This package contains javadoc for %{pkg_name}.

%prep
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
set -e -x
%setup -q -n %{pkg_name}-%{namedversion}

%pom_remove_plugin org.codehaus.mojo:findbugs-maven-plugin
%mvn_file :%{oname} %{pkg_name}
%{?scl:EOF}


%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
set -e -x

%mvn_build

sed -i 's/\r//' target/classes/META-INF/LICENSE.txt
cp -p target/classes/META-INF/LICENSE.txt .
%{?scl:EOF}


%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
set -e -x
%mvn_install
%{?scl:EOF}


%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Sat Jul 23 2016 Mat Booth <mat.booth@redhat.com> - 1.2-10.1
- Auto SCL-ise package for rh-eclipse46 collection

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 03 2015 gil cattaneo <puntogil@libero.it> 1.2-8
- introduce license macro

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.2-6
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 08 2013 gil cattaneo <puntogil@libero.it> 1.2-4
- switch to XMvn
- minor changes to adapt to current guideline

* Sun May 26 2013 gil cattaneo <puntogil@libero.it> 1.2-3
- rebuilt with spec-version-maven-plugin support

* Wed May 22 2013 gil cattaneo <puntogil@libero.it> 1.2-2
- fixed manifest

* Tue May 07 2013 gil cattaneo <puntogil@libero.it> 1.2-1
- update to 1.2

* Tue Apr 02 2013 gil cattaneo <puntogil@libero.it> 1.2-0.1.b04
- initial rpm