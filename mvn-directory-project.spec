#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-directory-project
Version  : 31
Release  : 5
URL      : https://github.com/apache/directory-project/archive/31.tar.gz
Source0  : https://github.com/apache/directory-project/archive/31.tar.gz
Source1  : https://repo1.maven.org/maven2/org/apache/directory/project/project/29/project-29.pom
Source2  : https://repo1.maven.org/maven2/org/apache/directory/project/project/31/project-31.pom
Source3  : https://repo1.maven.org/maven2/org/apache/directory/project/project/33/project-33.pom
Source4  : https://repo1.maven.org/maven2/org/apache/directory/project/project/34/project-34.pom
Source5  : https://repo1.maven.org/maven2/org/apache/directory/project/project/35/project-35.pom
Source6  : https://repo1.maven.org/maven2/org/apache/directory/project/project/40/project-40.pom
Source7  : https://repo1.maven.org/maven2/org/apache/directory/project/project/41/project-41.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-directory-project-data = %{version}-%{release}
Requires: mvn-directory-project-license = %{version}-%{release}
BuildRequires : apache-maven
BuildRequires : buildreq-mvn

%description
This is the trunk for all directory projects.
Branches
--------
directory svn repo base.

%package data
Summary: data components for the mvn-directory-project package.
Group: Data

%description data
data components for the mvn-directory-project package.


%package license
Summary: license components for the mvn-directory-project package.
Group: Default

%description license
license components for the mvn-directory-project package.


%prep
%setup -q -n directory-project-31

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-directory-project
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/mvn-directory-project/LICENSE.txt
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/directory/project/project/29
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/directory/project/project/29/project-29.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/directory/project/project/31
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/directory/project/project/31/project-31.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/directory/project/project/33
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/apache/directory/project/project/33/project-33.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/directory/project/project/34
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/apache/directory/project/project/34/project-34.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/directory/project/project/35
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/apache/directory/project/project/35/project-35.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/directory/project/project/40
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/apache/directory/project/project/40/project-40.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/directory/project/project/41
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/apache/directory/project/project/41/project-41.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/directory/project/project/29/project-29.pom
/usr/share/java/.m2/repository/org/apache/directory/project/project/31/project-31.pom
/usr/share/java/.m2/repository/org/apache/directory/project/project/33/project-33.pom
/usr/share/java/.m2/repository/org/apache/directory/project/project/34/project-34.pom
/usr/share/java/.m2/repository/org/apache/directory/project/project/35/project-35.pom
/usr/share/java/.m2/repository/org/apache/directory/project/project/40/project-40.pom
/usr/share/java/.m2/repository/org/apache/directory/project/project/41/project-41.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-directory-project/LICENSE.txt
