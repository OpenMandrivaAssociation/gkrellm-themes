%define name	gkrellm-themes
%define version	20030129
%define release	%mkrel 11

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Themes for the GKrellM
License:	GPL
Group:		Monitoring
URL:		http://www.muhri.net
Source:		http://www.muhri.net/gkrellm/GKrellM-Skins.tar.bz2
Requires:	gkrellm >= 0.9.0
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This package contains some nice themes for the GKrellM monitoring utility.

%prep
%setup -q -n GKrellM-skins
rm -f Aqua.gkrellm.tgz
rm -f Azteker2k.gkrellm.tar.gz
rm -f BloeStolen.tar.gz
rm -f brushedmetalnew.tar.gz
rm -f Cyroid.tar.gz
rm -f E-Tech_XSlate_GKrellM.tar.gz
rm -f E17.gkrellm.tar.gz
rm -f Eazel.gkrellm.tar.gz
rm -f Plastique.tar.gz
rm -f ShinyMetal2.tar.gz
rm -f TaoMetal.tar.gz
rm -f blueHeart_gkrellm.tar.gz
rm -f brushed.tar.gz
rm -f indiglow_blue-gkrellm.tar.gz
rm -f minE-Gkrellm.tar.gz
for file in *.tar.gz *.tgz; do
	tar xvzf $file;
	rm -f $file
done
# remove hidden files or directories
find . -mindepth 1 -name '.*' | xargs rm -rf
# remove empty files or directories
find . -empty | xargs rm -rf
# remove CVS files
find . -type d -name CVS | xargs rm -rf
# fix perms
find . -type d -exec chmod 755 {} \;
find . -type f -exec chmod 644 {} \;

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/gkrellm2/themes
cp -av * %{buildroot}%{_datadir}/gkrellm2/themes

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/gkrellm2/themes/*

