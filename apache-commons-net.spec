Name:		apache-commons-net
Version:	3.13.0
Release:	1
Summary:	Internet protocol clients for Java
Group:		Development/Java
License:	ASL 2.0
URL:		https://commons.apache.org/proper/commons-net/
Source0:	https://archive.apache.org/dist/commons/net/source/commons-net-%{version}-src.tar.gz

BuildArch:	noarch
# The package phase builds a second FTP-only jar with Ant. Ship one jar.
%global sysjar_drops --drop org.apache.maven.plugins:maven-antrun-plugin
BuildRequires:	mvn(org.apache.commons:commons-parent:pom::)
BuildRequires:	mvn(commons-io:commons-io)
# Literal, so the first rpmbuild -bs records them before sysjar is installed.
BuildRequires:	maven
BuildRequires:	java-current-devel
BuildSystem:	maven
BuildOption(install):	--file-name commons-net --link %{name}
Provides:	jakarta-commons-net = %{version}-%{release}
Obsoletes:	jakarta-commons-net < 2.0-3

%description
Apache Commons Net is a client library for FTP, NNTP, SMTP, POP3,
IMAP, Telnet, TFTP, and several smaller protocols. 3.13.0 needs Java 8.

%prep
%setup -q -n commons-net-%{version}-src

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt
