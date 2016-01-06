%{?scl:%scl_package glassfish-annotation-api}
%{!?scl:%global pkg_name %{name}}
%{?java_common_find_provides_and_requires}

%global namedreltag %{nil}
%global namedversion %{version}%{?namedreltag}
%global oname javax.annotation-api
Name:          %{?scl_prefix}glassfish-annotation-api
Version:       1.2
Release:       9.1%{?dist}
Summary:       Common Annotations API Specification (JSR 250)
License:       CDDL or GPLv2 with exceptions
# http://jcp.org/en/jsr/detail?id=250
URL:           http://glassfish.java.net/
# svn export https://svn.java.net/svn/glassfish~svn/tags/javax.annotation-api-1.2/ glassfish-annotation-api-1.2
# tar czf glassfish-annotation-api-1.2-src-svn.tar.gz glassfish-annotation-api-1.2
Source0:       %{pkg_name}-%{namedversion}-src-svn.tar.gz

BuildRequires: %{?scl_prefix_maven}jvnet-parent

BuildRequires: %{?scl_prefix_java_common}maven-local
BuildRequires: %{?scl_prefix_maven}maven-plugin-bundle
BuildRequires: %{?scl_prefix_maven}maven-remote-resources-plugin
BuildRequires: %{?scl_prefix_maven}maven-source-plugin

BuildArch:     noarch

%description
Common Annotations APIs for the Java Platform (JSR 250).

%package javadoc
Summary:       Javadoc for %{pkg_name}

%description javadoc
This package contains javadoc for %{pkg_name}.

%prep
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%setup -q -n %{pkg_name}-%{namedversion}

%pom_remove_plugin :maven-remote-resources-plugin
%pom_remove_plugin org.glassfish.build:spec-version-maven-plugin
%pom_remove_plugin org.codehaus.mojo:findbugs-maven-plugin
%mvn_file :%{oname} %{pkg_name}
%{?scl:EOF}


%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}

%mvn_build -- \
  -Dspec.implementation.version=%{version} \
  -Dspec.specification.version=%{version} \
  -Dspec.bundle.symbolic-name=javax.annotation-api \
  -Dspec.bundle.spec.version=%{version} \
  -Dspec.extension.name=javax.annotation \
  -Dspec.bundle.version=%{version}

%{?scl:EOF}


%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_install
%{?scl:EOF}


%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
* Mon Jun 29 2015 Mat Booth <mat.booth@redhat.com> - 1.2-9.1
- Import latest from Fedora

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
