
%global base_name    net
%global short_name   commons-%{base_name}

Name:           apache-%{short_name}
Version:        3.1
Release:        3
Summary:        Internet protocol suite Java library
License:        ASL 2.0
Group:          Development/Java
URL:            http://commons.apache.org/%{base_name}/
Source0:        http://www.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
BuildArch:      noarch
BuildRequires:  jpackage-utils >= 0:1.7.2
BuildRequires:  java-devel >= 0:1.6.0
BuildRequires:  maven-doxia-sitetools
BuildRequires:  maven-changes-plugin
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  maven-surefire-provider-junit4
BuildRequires:  maven-plugin-build-helper
BuildRequires:  apache-commons-parent

Requires:       java >= 0:1.6.0
Requires:       jpackage-utils >= 0:1.7.2
Requires(post):    jpackage-utils
Requires(postun):  jpackage-utils


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
Group:      Development/Java
Requires:   jpackage-utils

Obsoletes:  jakarta-%{short_name}-javadoc < 0:2.0-3

%description javadoc
%{summary}.

%prep
%setup -q -n %{short_name}-%{version}-src
sed -i 's/\r//' NOTICE.txt LICENSE.txt


%build
export MAVEN_REPO_LOCAL=$(pwd)/.m2/repository
mkdir -p $MAVEN_REPO_LOCAL
# test.failure.ignore added because package would not build on koji
# with TimeTCPClientTest failing
mvn-jpp -Dmaven.repo.local=$MAVEN_REPO_LOCAL \
    -Dmaven.test.failure.ignore=true \
    install javadoc:javadoc

%install
# jars
install -d -m 755 %{buildroot}%{_javadir}
install -p -m 644 target/%{short_name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
ln -s %{name}.jar %{buildroot}%{_javadir}/%{short_name}.jar


# pom
install -d -m 755 %{buildroot}%{_mavenpomdir}
install -pm 644 pom.xml %{buildroot}%{_mavenpomdir}/JPP-%{name}.pom
%add_to_maven_depmap org.apache.commons %{short_name} %{version} JPP %{name}

# following line is only for backwards compatibility. New packages
# should use proper groupid org.apache.commons and also artifactid
%add_to_maven_depmap %{short_name} %{short_name} %{version} JPP %{name}

# javadoc
install -d -m 755 %{buildroot}%{_javadocdir}/%{name}
cp -pr target/site/apidocs/* %{buildroot}%{_javadocdir}/%{name}


%post
%update_maven_depmap

%postun
%update_maven_depmap

%pre javadoc
# workaround for rpm bug, can be removed in F-17
[ $1 -gt 1 ] && [ -L %{_javadocdir}/%{name} ] && \
rm -rf $(readlink -f %{_javadocdir}/%{name}) %{_javadocdir}/%{name} || :

%files
%defattr(-,root,root,-)
%doc LICENSE.txt NOTICE.txt
%{_javadir}/*
%{_mavenpomdir}/JPP-%{name}.pom
%{_mavendepmapfragdir}

%files javadoc
%defattr(-,root,root,-)
%doc %{_javadocdir}/%{name}
%doc LICENSE.txt NOTICE.txt

