%{?_javapackages_macros:%_javapackages_macros}
%global base_name    net
%global short_name   commons-%{base_name}

Name:           apache-%{short_name}
Version:        3.3
Release:        2.1%{?dist}
Summary:        Internet protocol suite Java library
License:        ASL 2.0
URL:            http://commons.apache.org/%{base_name}/
Source0:        http://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  maven-plugin-build-helper
BuildRequires:  apache-commons-parent
# Test dependency
BuildRequires:  junit

Provides:       jakarta-%{short_name} = 0:%{version}-%{release}
Obsoletes:      jakarta-%{short_name} < 0:2.0-3


%description
This is an Internet protocol suite Java library originally developed by
ORO, Inc.  This version supports Finger, Whois, TFTP, Telnet, POP3, FTP,
NNTP, SMTP, and some miscellaneous protocols like Time and Echo as well
as BSD R command support. The purpose of the library is to provide
fundamental protocol access, not higher-level abstractions.

%package javadoc
Summary:    API documentation for %{name}
Provides:   jakarta-%{short_name}-javadoc = 0:%{version}-%{release}
Obsoletes:  jakarta-%{short_name}-javadoc < 0:2.0-3

%description javadoc
%{summary}.

%prep
%setup -q -n %{short_name}-%{version}-src
sed -i 's/\r//' NOTICE.txt LICENSE.txt README RELEASE-NOTES.txt

# This test fails with "Connection timed out"
rm src/test/java/org/apache/commons/net/time/TimeTCPClientTest.java

%mvn_file  : %{short_name} %{name}
%mvn_alias : org.apache.commons:%{short_name}

%build
%mvn_build

%install
%mvn_install


%files -f .mfiles
%doc LICENSE.txt NOTICE.txt README RELEASE-NOTES.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jun 12 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.3-1
- Update to upstream version 3.3

* Wed Jun 05 2013 Michal Srb <msrb@redhat.com> - 3.2-5
- Enable tests
- Install README, RELEASE-NOTES.txt files
- Fix BR

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 3.2-3
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Jan 16 2013 Michal Srb <msrb@redhat.com> - 3.2-2
- Build with xmvn

* Mon Dec  3 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.2-1
- Update to upstream version 3.2

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 19 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 3.1-1
- Update to upstream 3.1
- Remove RPM bug workaround
- Remove BR on maven-changes-plugin

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 24 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2-3
- Use maven 3 to build
- Packaging fixes according to latest guidelines

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Dec 10 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2-1
- Replace maven plugins with apache-commons-parent for BR
- Versionless jars and javadocs
- Rebase to latest upstream version

* Thu Jul  8 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.0-6
- Add license to javadoc subpackage

* Thu May 20 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.0-5
- Fix maven depmap JPP name to short_name

* Wed May 19 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.0-4
- Ignore test failure

* Wed May 12 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.0-3
- Rename jakarta-commons-net to apache-commons-net and drop EPOCH
- Build with maven
- Clean up whole spec

* Thu Aug 13 2009 Alexander Kurtakov <akurtako@redhat.com> 0:2.0-2
- Set maven.repo.local.

* Thu Aug 13 2009 Alexander Kurtakov <akurtako@redhat.com> 0:2.0-1
- Update to upstream 2.0.

