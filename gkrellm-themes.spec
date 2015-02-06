%define name	gkrellm-themes
%define version	20030129
%define release	12

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



%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 20030129-11mdv2011.0
+ Revision: 618954
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 20030129-10mdv2010.0
+ Revision: 429208
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 20030129-9mdv2009.0
+ Revision: 246164
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 18 2007 Guillaume Rousse <guillomovitch@mandriva.org> 20030129-7mdv2008.1
+ Revision: 132436
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import gkrellm-themes


* Tue Jul 11 2006 Guillaume Rousse <guillomovitch@mandriva.org> 20030129-6mdv2007.0
- %%mkrel

* Wed Jun 15 2005 Guillaume Rousse <guillomovitch@mandriva.org> 20030129-5mdk 
- really really remove all themes already included in gkrellm

* Mon Jun 13 2005 Guillaume Rousse <guillomovitch@mandriva.org> 20030129-4mdk 
- really remove all themes already included in gkrellm
- fix additional themes shipped in .tgz

* Sat Jun 11 2005 Guillaume Rousse <guillomovitch@mandriva.org> 20030129-3mdk 
- removed all themes already included in gkrellm

* Tue Jun 07 2005 Guillaume Rousse <guillomovitch@mandriva.org> 20030129-2mdk 
- drop BloeStolen, it's already included in gkrellm

* Tue Jun 07 2005 Guillaume Rousse <guillomovitch@mandriva.org> 20030129-1mdk 
- new versionning scheme, more adapted to follow upstream changes
- spec cleanup
- don't own parent directory

* Mon Apr 28 2003 Guillaume Rousse <g.rousse@linux-mandrake.com> 0.2-5mdk
- fixed dir ownership (Olivier Thauvin <thauvin@aerov.jussieu.fr>)

* Sun Mar 23 2003 Guillaume Rousse <g.rousse@linux-mandrake.com> 0.2-4mdk
- s/Copyright/License
- removed lurking .xvpics directories

* Thu Jan 02 2003 Vincent Danen <vdanen@mandrakesoft.com> 0.2-3mdk
- a bot told me to rebuild so here we go
- fix some rpmlint errors while we're at it

* Fri Oct 11 2002 Vincent Danen <vdanen@mandrakesoft.com> 0.2-2mdk
- build for gkrellm2

* Thu Jan 31 2002 Vincent Danen <vdanen@mandrakesoft.com> 0.2-1mdk
- a lot more themes

* Thu Apr 05 2001 Vincent Danen <vdanen@mandrakesoft.com> 0.1-2mdk
- spec cleanups
- more themes

* Tue May 16 2000 Vincent Danen <vdanen@linux-mandrake.com> 0.1-1mdk
- initial specfile
- Added 26 different themes
