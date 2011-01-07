# Red Hat Documentation Specfile
Name:           Cluster_Administration
Version:        5.0.0
Release:        5
Summary:        Red Hat Cluster Suite
Group:          Documentation
License:        OPL
URL:            http://www.redhat.com/docs
Source0:         %{name}-%{version}-%{release}.tgz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires(post,postun): coreutils

%description

		
			 Clustered systems provide reliability, scalability, and availability to critical production services. Using a Red Hat Cluster, you can create high-availability clusters for file sharing, Web servers, and more. This document describes the configuration and management of Red Hat cluster systems. It does not include information about Red Hat Linux Virtual Servers (LVS). Information about installing and configuring LVS is in a separate document. 
		
	

%package -n Cluster_Administration-en-US
Summary:    Red Hat Cluster Suite
Group:      Documentation
Requires(post,postun): coreutils
%description -n Cluster_Administration-en-US

		
			 Clustered systems provide reliability, scalability, and availability to critical production services. Using a Red Hat Cluster, you can create high-availability clusters for file sharing, Web servers, and more. This document describes the configuration and management of Red Hat cluster systems. It does not include information about Red Hat Linux Virtual Servers (LVS). Information about installing and configuring LVS is in a separate document. 
		
	

%prep
%setup -q -n %{name}-%{version}-%{release}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/share/applications/

cat > $RPM_BUILD_ROOT/usr/share/applications/Cluster_Administration.desktop <<'EOF'
[Desktop Entry]
Name=Red Hat Cluster Suite
Name[en-US]=Red Hat Cluster Suite
Name[as-IN]=Red Hat Cluster Suite
Name[bn-IN]=Red Hat Cluster Suite
Name[de-DE]=Red Hat Cluster Suite
Name[es-ES]=Red Hat Cluster Suite
Name[fr-FR]=Red Hat Cluster Suite
Name[gu-IN]=Red Hat Cluster Suite
Name[hi-IN]=Red Hat Cluster Suite
Name[it-IT]=Red Hat Cluster Suite
Name[ja-JP]=Red Hat Cluster Suite
Name[kn-IN]=Red Hat Cluster Suite
Name[ko-KR]=Red Hat Cluster Suite
Name[ml-IN]=Red Hat Cluster Suite
Name[mr-IN]=Red Hat Cluster Suite
Name[or-IN]=Red Hat Cluster Suite
Name[pa-IN]=Red Hat Cluster Suite
Name[pt-BR]=Red Hat Cluster Suite
Name[ru-RU]=Red Hat Cluster Suite
Name[si-LK]=Red Hat Cluster Suite
Name[ta-IN]=Red Hat Cluster Suite
Name[te-IN]=Red Hat Cluster Suite
Name[zh-CN]=Red Hat Cluster Suite
Name[zh-TW]=Red Hat Cluster Suite
Comment=Configuring and Managing a Red Hat Cluster
Exec=yelp ghelp:Cluster_Administration
Icon=%{_docdir}/%{name}-en-US-%{version}/images/icon.svg
Categories=Documentation;X-Red-Hat-Base;
Type=Application
Encoding=UTF-8
Terminal=false
EOF

mkdir -p $RPM_BUILD_ROOT/usr/share/gnome/help/Cluster_Administration

%clean
rm -rf $RPM_BUILD_ROOT

%post -n Cluster_Administration-en-US
%define _locale %(echo en-US |sed 's/-/_/')
if [ ! -d /usr/share/gnome/help/Cluster_Administration/%{_locale} ]; then
	ln -s %{_docdir}/%{name}-en-US-%{version} /usr/share/gnome/help/Cluster_Administration/%{_locale};
fi
if [ ! -d /usr/share/gnome/help/Cluster_Administration/C ]; then
	ln -s %{_docdir}/%{name}-en-US-%{version} /usr/share/gnome/help/Cluster_Administration/C;
fi

%postun -n Cluster_Administration-en-US
rm -rf /usr/share/gnome/help/Cluster_Administration

%files -n Cluster_Administration-en-US
%defattr(-,root,root,-)
%doc en-US/*.xml
%doc en-US/Common_Config
%doc en-US/Common_Content
%doc en-US/images
/usr/share/applications/Cluster_Administration.desktop
/usr/share/gnome/help/Cluster_Administration



%package -n Cluster_Administration-as-IN
Summary: Red Hat Cluster Suite
Group: Documentation
Requires: Cluster_Administration-en-US = 5.0.0-5
Requires(post,postun): coreutils

%description -n Cluster_Administration-as-IN

		
			 Clustered systems provide reliability, scalability, and availability to critical production services. Using a Red Hat Cluster, you can create high-availability clusters for file sharing, Web servers, and more. This document describes the configuration and management of Red Hat cluster systems. It does not include information about Red Hat Linux Virtual Servers (LVS). Information about installing and configuring LVS is in a separate document. 
		
	

%post -n Cluster_Administration-as-IN
%define _locale %(echo as-IN |sed 's/-/_/')
if [ ! -d /usr/share/gnome/help/Cluster_Administration/%{_locale} ]; then
	ln -s %{_docdir}/Cluster_Administration-as-IN-%{version} /usr/share/gnome/help/Cluster_Administration/%{_locale};
fi

%postun -n Cluster_Administration-as-IN
%define _locale %(echo as-IN |sed 's/-/_/')
rm -f /usr/share/gnome/help/Cluster_Administration/%{_locale}

%files -n Cluster_Administration-as-IN
%defattr(-,root,root,-)
%doc as-IN/*.xml
%doc as-IN/Common_Config
%doc as-IN/Common_Content
%doc as-IN/images


%package -n Cluster_Administration-bn-IN
Summary: Red Hat Cluster Suite
Group: Documentation
Requires: Cluster_Administration-en-US = 5.0.0-5
Requires(post,postun): coreutils

%description -n Cluster_Administration-bn-IN

		
			 Clustered systems provide reliability, scalability, and availability to critical production services. Using a Red Hat Cluster, you can create high-availability clusters for file sharing, Web servers, and more. This document describes the configuration and management of Red Hat cluster systems. It does not include information about Red Hat Linux Virtual Servers (LVS). Information about installing and configuring LVS is in a separate document. 
		
	

%post -n Cluster_Administration-bn-IN
%define _locale %(echo bn-IN |sed 's/-/_/')
if [ ! -d /usr/share/gnome/help/Cluster_Administration/%{_locale} ]; then
	ln -s %{_docdir}/Cluster_Administration-bn-IN-%{version} /usr/share/gnome/help/Cluster_Administration/%{_locale};
fi

%postun -n Cluster_Administration-bn-IN
%define _locale %(echo bn-IN |sed 's/-/_/')
rm -f /usr/share/gnome/help/Cluster_Administration/%{_locale}

%files -n Cluster_Administration-bn-IN
%defattr(-,root,root,-)
%doc bn-IN/*.xml
%doc bn-IN/Common_Config
%doc bn-IN/Common_Content
%doc bn-IN/images


%package -n Cluster_Administration-de-DE
Summary: Red Hat Cluster Suite
Group: Documentation
Requires: Cluster_Administration-en-US = 5.0.0-5
Requires(post,postun): coreutils

%description -n Cluster_Administration-de-DE

		
			 Clustered systems provide reliability, scalability, and availability to critical production services. Using a Red Hat Cluster, you can create high-availability clusters for file sharing, Web servers, and more. This document describes the configuration and management of Red Hat cluster systems. It does not include information about Red Hat Linux Virtual Servers (LVS). Information about installing and configuring LVS is in a separate document. 
		
	

%post -n Cluster_Administration-de-DE
%define _locale %(echo de-DE |sed 's/-/_/')
if [ ! -d /usr/share/gnome/help/Cluster_Administration/%{_locale} ]; then
	ln -s %{_docdir}/Cluster_Administration-de-DE-%{version} /usr/share/gnome/help/Cluster_Administration/%{_locale};
fi

%postun -n Cluster_Administration-de-DE
%define _locale %(echo de-DE |sed 's/-/_/')
rm -f /usr/share/gnome/help/Cluster_Administration/%{_locale}

%files -n Cluster_Administration-de-DE
%defattr(-,root,root,-)
%doc de-DE/*.xml
%doc de-DE/Common_Config
%doc de-DE/Common_Content
%doc de-DE/images


%package -n Cluster_Administration-es-ES
Summary: Red Hat Cluster Suite
Group: Documentation
Requires: Cluster_Administration-en-US = 5.0.0-5
Requires(post,postun): coreutils

%description -n Cluster_Administration-es-ES

		
			 Clustered systems provide reliability, scalability, and availability to critical production services. Using a Red Hat Cluster, you can create high-availability clusters for file sharing, Web servers, and more. This document describes the configuration and management of Red Hat cluster systems. It does not include information about Red Hat Linux Virtual Servers (LVS). Information about installing and configuring LVS is in a separate document. 
		
	

%post -n Cluster_Administration-es-ES
%define _locale %(echo es-ES |sed 's/-/_/')
if [ ! -d /usr/share/gnome/help/Cluster_Administration/%{_locale} ]; then
	ln -s %{_docdir}/Cluster_Administration-es-ES-%{version} /usr/share/gnome/help/Cluster_Administration/%{_locale};
fi

%postun -n Cluster_Administration-es-ES
%define _locale %(echo es-ES |sed 's/-/_/')
rm -f /usr/share/gnome/help/Cluster_Administration/%{_locale}

%files -n Cluster_Administration-es-ES
%defattr(-,root,root,-)
%doc es-ES/*.xml
%doc es-ES/Common_Config
%doc es-ES/Common_Content
%doc es-ES/images


%package -n Cluster_Administration-fr-FR
Summary: Red Hat Cluster Suite
Group: Documentation
Requires: Cluster_Administration-en-US = 5.0.0-5
Requires(post,postun): coreutils

%description -n Cluster_Administration-fr-FR

		
			 Clustered systems provide reliability, scalability, and availability to critical production services. Using a Red Hat Cluster, you can create high-availability clusters for file sharing, Web servers, and more. This document describes the configuration and management of Red Hat cluster systems. It does not include information about Red Hat Linux Virtual Servers (LVS). Information about installing and configuring LVS is in a separate document. 
		
	

%post -n Cluster_Administration-fr-FR
%define _locale %(echo fr-FR |sed 's/-/_/')
if [ ! -d /usr/share/gnome/help/Cluster_Administration/%{_locale} ]; then
	ln -s %{_docdir}/Cluster_Administration-fr-FR-%{version} /usr/share/gnome/help/Cluster_Administration/%{_locale};
fi

%postun -n Cluster_Administration-fr-FR
%define _locale %(echo fr-FR |sed 's/-/_/')
rm -f /usr/share/gnome/help/Cluster_Administration/%{_locale}

%files -n Cluster_Administration-fr-FR
%defattr(-,root,root,-)
%doc fr-FR/*.xml
%doc fr-FR/Common_Config
%doc fr-FR/Common_Content
%doc fr-FR/images


%package -n Cluster_Administration-gu-IN
Summary: Red Hat Cluster Suite
Group: Documentation
Requires: Cluster_Administration-en-US = 5.0.0-5
Requires(post,postun): coreutils

%description -n Cluster_Administration-gu-IN

		
			 Clustered systems provide reliability, scalability, and availability to critical production services. Using a Red Hat Cluster, you can create high-availability clusters for file sharing, Web servers, and more. This document describes the configuration and management of Red Hat cluster systems. It does not include information about Red Hat Linux Virtual Servers (LVS). Information about installing and configuring LVS is in a separate document. 
		
	

%post -n Cluster_Administration-gu-IN
%define _locale %(echo gu-IN |sed 's/-/_/')
if [ ! -d /usr/share/gnome/help/Cluster_Administration/%{_locale} ]; then
	ln -s %{_docdir}/Cluster_Administration-gu-IN-%{version} /usr/share/gnome/help/Cluster_Administration/%{_locale};
fi

%postun -n Cluster_Administration-gu-IN
%define _locale %(echo gu-IN |sed 's/-/_/')
rm -f /usr/share/gnome/help/Cluster_Administration/%{_locale}

%files -n Cluster_Administration-gu-IN
%defattr(-,root,root,-)
%doc gu-IN/*.xml
%doc gu-IN/Common_Config
%doc gu-IN/Common_Content
%doc gu-IN/images


%package -n Cluster_Administration-hi-IN
Summary: Red Hat Cluster Suite
Group: Documentation
Requires: Cluster_Administration-en-US = 5.0.0-5
Requires(post,postun): coreutils

%description -n Cluster_Administration-hi-IN

		
			 Clustered systems provide reliability, scalability, and availability to critical production services. Using a Red Hat Cluster, you can create high-availability clusters for file sharing, Web servers, and more. This document describes the configuration and management of Red Hat cluster systems. It does not include information about Red Hat Linux Virtual Servers (LVS). Information about installing and configuring LVS is in a separate document. 
		
	

%post -n Cluster_Administration-hi-IN
%define _locale %(echo hi-IN |sed 's/-/_/')
if [ ! -d /usr/share/gnome/help/Cluster_Administration/%{_locale} ]; then
	ln -s %{_docdir}/Cluster_Administration-hi-IN-%{version} /usr/share/gnome/help/Cluster_Administration/%{_locale};
fi

%postun -n Cluster_Administration-hi-IN
%define _locale %(echo hi-IN |sed 's/-/_/')
rm -f /usr/share/gnome/help/Cluster_Administration/%{_locale}

%files -n Cluster_Administration-hi-IN
%defattr(-,root,root,-)
%doc hi-IN/*.xml
%doc hi-IN/Common_Config
%doc hi-IN/Common_Content
%doc hi-IN/images


%package -n Cluster_Administration-it-IT
Summary: Red Hat Cluster Suite
Group: Documentation
Requires: Cluster_Administration-en-US = 5.0.0-5
Requires(post,postun): coreutils

%description -n Cluster_Administration-it-IT

		
			 Clustered systems provide reliability, scalability, and availability to critical production services. Using a Red Hat Cluster, you can create high-availability clusters for file sharing, Web servers, and more. This document describes the configuration and management of Red Hat cluster systems. It does not include information about Red Hat Linux Virtual Servers (LVS). Information about installing and configuring LVS is in a separate document. 
		
	

%post -n Cluster_Administration-it-IT
%define _locale %(echo it-IT |sed 's/-/_/')
if [ ! -d /usr/share/gnome/help/Cluster_Administration/%{_locale} ]; then
	ln -s %{_docdir}/Cluster_Administration-it-IT-%{version} /usr/share/gnome/help/Cluster_Administration/%{_locale};
fi

%postun -n Cluster_Administration-it-IT
%define _locale %(echo it-IT |sed 's/-/_/')
rm -f /usr/share/gnome/help/Cluster_Administration/%{_locale}

%files -n Cluster_Administration-it-IT
%defattr(-,root,root,-)
%doc it-IT/*.xml
%doc it-IT/Common_Config
%doc it-IT/Common_Content
%doc it-IT/images


%package -n Cluster_Administration-ja-JP
Summary: Red Hat Cluster Suite
Group: Documentation
Requires: Cluster_Administration-en-US = 5.0.0-5
Requires(post,postun): coreutils

%description -n Cluster_Administration-ja-JP

		
			 Clustered systems provide reliability, scalability, and availability to critical production services. Using a Red Hat Cluster, you can create high-availability clusters for file sharing, Web servers, and more. This document describes the configuration and management of Red Hat cluster systems. It does not include information about Red Hat Linux Virtual Servers (LVS). Information about installing and configuring LVS is in a separate document. 
		
	

%post -n Cluster_Administration-ja-JP
%define _locale %(echo ja-JP |sed 's/-/_/')
if [ ! -d /usr/share/gnome/help/Cluster_Administration/%{_locale} ]; then
	ln -s %{_docdir}/Cluster_Administration-ja-JP-%{version} /usr/share/gnome/help/Cluster_Administration/%{_locale};
fi

%postun -n Cluster_Administration-ja-JP
%define _locale %(echo ja-JP |sed 's/-/_/')
rm -f /usr/share/gnome/help/Cluster_Administration/%{_locale}

%files -n Cluster_Administration-ja-JP
%defattr(-,root,root,-)
%doc ja-JP/*.xml
%doc ja-JP/Common_Config
%doc ja-JP/Common_Content
%doc ja-JP/images


%package -n Cluster_Administration-kn-IN
Summary: Red Hat Cluster Suite
Group: Documentation
Requires: Cluster_Administration-en-US = 5.0.0-5
Requires(post,postun): coreutils

%description -n Cluster_Administration-kn-IN

		
			 Clustered systems provide reliability, scalability, and availability to critical production services. Using a Red Hat Cluster, you can create high-availability clusters for file sharing, Web servers, and more. This document describes the configuration and management of Red Hat cluster systems. It does not include information about Red Hat Linux Virtual Servers (LVS). Information about installing and configuring LVS is in a separate document. 
		
	

%post -n Cluster_Administration-kn-IN
%define _locale %(echo kn-IN |sed 's/-/_/')
if [ ! -d /usr/share/gnome/help/Cluster_Administration/%{_locale} ]; then
	ln -s %{_docdir}/Cluster_Administration-kn-IN-%{version} /usr/share/gnome/help/Cluster_Administration/%{_locale};
fi

%postun -n Cluster_Administration-kn-IN
%define _locale %(echo kn-IN |sed 's/-/_/')
rm -f /usr/share/gnome/help/Cluster_Administration/%{_locale}

%files -n Cluster_Administration-kn-IN
%defattr(-,root,root,-)
%doc kn-IN/*.xml
%doc kn-IN/Common_Config
%doc kn-IN/Common_Content
%doc kn-IN/images


%package -n Cluster_Administration-ko-KR
Summary: Red Hat Cluster Suite
Group: Documentation
Requires: Cluster_Administration-en-US = 5.0.0-5
Requires(post,postun): coreutils

%description -n Cluster_Administration-ko-KR

		
			 Clustered systems provide reliability, scalability, and availability to critical production services. Using a Red Hat Cluster, you can create high-availability clusters for file sharing, Web servers, and more. This document describes the configuration and management of Red Hat cluster systems. It does not include information about Red Hat Linux Virtual Servers (LVS). Information about installing and configuring LVS is in a separate document. 
		
	

%post -n Cluster_Administration-ko-KR
%define _locale %(echo ko-KR |sed 's/-/_/')
if [ ! -d /usr/share/gnome/help/Cluster_Administration/%{_locale} ]; then
	ln -s %{_docdir}/Cluster_Administration-ko-KR-%{version} /usr/share/gnome/help/Cluster_Administration/%{_locale};
fi

%postun -n Cluster_Administration-ko-KR
%define _locale %(echo ko-KR |sed 's/-/_/')
rm -f /usr/share/gnome/help/Cluster_Administration/%{_locale}

%files -n Cluster_Administration-ko-KR
%defattr(-,root,root,-)
%doc ko-KR/*.xml
%doc ko-KR/Common_Config
%doc ko-KR/Common_Content
%doc ko-KR/images


%package -n Cluster_Administration-ml-IN
Summary: Red Hat Cluster Suite
Group: Documentation
Requires: Cluster_Administration-en-US = 5.0.0-5
Requires(post,postun): coreutils

%description -n Cluster_Administration-ml-IN

		
			 Clustered systems provide reliability, scalability, and availability to critical production services. Using a Red Hat Cluster, you can create high-availability clusters for file sharing, Web servers, and more. This document describes the configuration and management of Red Hat cluster systems. It does not include information about Red Hat Linux Virtual Servers (LVS). Information about installing and configuring LVS is in a separate document. 
		
	

%post -n Cluster_Administration-ml-IN
%define _locale %(echo ml-IN |sed 's/-/_/')
if [ ! -d /usr/share/gnome/help/Cluster_Administration/%{_locale} ]; then
	ln -s %{_docdir}/Cluster_Administration-ml-IN-%{version} /usr/share/gnome/help/Cluster_Administration/%{_locale};
fi

%postun -n Cluster_Administration-ml-IN
%define _locale %(echo ml-IN |sed 's/-/_/')
rm -f /usr/share/gnome/help/Cluster_Administration/%{_locale}

%files -n Cluster_Administration-ml-IN
%defattr(-,root,root,-)
%doc ml-IN/*.xml
%doc ml-IN/Common_Config
%doc ml-IN/Common_Content
%doc ml-IN/images


%package -n Cluster_Administration-mr-IN
Summary: Red Hat Cluster Suite
Group: Documentation
Requires: Cluster_Administration-en-US = 5.0.0-5
Requires(post,postun): coreutils

%description -n Cluster_Administration-mr-IN

		
			 Clustered systems provide reliability, scalability, and availability to critical production services. Using a Red Hat Cluster, you can create high-availability clusters for file sharing, Web servers, and more. This document describes the configuration and management of Red Hat cluster systems. It does not include information about Red Hat Linux Virtual Servers (LVS). Information about installing and configuring LVS is in a separate document. 
		
	

%post -n Cluster_Administration-mr-IN
%define _locale %(echo mr-IN |sed 's/-/_/')
if [ ! -d /usr/share/gnome/help/Cluster_Administration/%{_locale} ]; then
	ln -s %{_docdir}/Cluster_Administration-mr-IN-%{version} /usr/share/gnome/help/Cluster_Administration/%{_locale};
fi

%postun -n Cluster_Administration-mr-IN
%define _locale %(echo mr-IN |sed 's/-/_/')
rm -f /usr/share/gnome/help/Cluster_Administration/%{_locale}

%files -n Cluster_Administration-mr-IN
%defattr(-,root,root,-)
%doc mr-IN/*.xml
%doc mr-IN/Common_Config
%doc mr-IN/Common_Content
%doc mr-IN/images


%package -n Cluster_Administration-or-IN
Summary: Red Hat Cluster Suite
Group: Documentation
Requires: Cluster_Administration-en-US = 5.0.0-5
Requires(post,postun): coreutils

%description -n Cluster_Administration-or-IN

		
			 Clustered systems provide reliability, scalability, and availability to critical production services. Using a Red Hat Cluster, you can create high-availability clusters for file sharing, Web servers, and more. This document describes the configuration and management of Red Hat cluster systems. It does not include information about Red Hat Linux Virtual Servers (LVS). Information about installing and configuring LVS is in a separate document. 
		
	

%post -n Cluster_Administration-or-IN
%define _locale %(echo or-IN |sed 's/-/_/')
if [ ! -d /usr/share/gnome/help/Cluster_Administration/%{_locale} ]; then
	ln -s %{_docdir}/Cluster_Administration-or-IN-%{version} /usr/share/gnome/help/Cluster_Administration/%{_locale};
fi

%postun -n Cluster_Administration-or-IN
%define _locale %(echo or-IN |sed 's/-/_/')
rm -f /usr/share/gnome/help/Cluster_Administration/%{_locale}

%files -n Cluster_Administration-or-IN
%defattr(-,root,root,-)
%doc or-IN/*.xml
%doc or-IN/Common_Config
%doc or-IN/Common_Content
%doc or-IN/images


%package -n Cluster_Administration-pa-IN
Summary: Red Hat Cluster Suite
Group: Documentation
Requires: Cluster_Administration-en-US = 5.0.0-5
Requires(post,postun): coreutils

%description -n Cluster_Administration-pa-IN

		
			 Clustered systems provide reliability, scalability, and availability to critical production services. Using a Red Hat Cluster, you can create high-availability clusters for file sharing, Web servers, and more. This document describes the configuration and management of Red Hat cluster systems. It does not include information about Red Hat Linux Virtual Servers (LVS). Information about installing and configuring LVS is in a separate document. 
		
	

%post -n Cluster_Administration-pa-IN
%define _locale %(echo pa-IN |sed 's/-/_/')
if [ ! -d /usr/share/gnome/help/Cluster_Administration/%{_locale} ]; then
	ln -s %{_docdir}/Cluster_Administration-pa-IN-%{version} /usr/share/gnome/help/Cluster_Administration/%{_locale};
fi

%postun -n Cluster_Administration-pa-IN
%define _locale %(echo pa-IN |sed 's/-/_/')
rm -f /usr/share/gnome/help/Cluster_Administration/%{_locale}

%files -n Cluster_Administration-pa-IN
%defattr(-,root,root,-)
%doc pa-IN/*.xml
%doc pa-IN/Common_Config
%doc pa-IN/Common_Content
%doc pa-IN/images


%package -n Cluster_Administration-pt-BR
Summary: Red Hat Cluster Suite
Group: Documentation
Requires: Cluster_Administration-en-US = 5.0.0-5
Requires(post,postun): coreutils

%description -n Cluster_Administration-pt-BR

		
			 Clustered systems provide reliability, scalability, and availability to critical production services. Using a Red Hat Cluster, you can create high-availability clusters for file sharing, Web servers, and more. This document describes the configuration and management of Red Hat cluster systems. It does not include information about Red Hat Linux Virtual Servers (LVS). Information about installing and configuring LVS is in a separate document. 
		
	

%post -n Cluster_Administration-pt-BR
%define _locale %(echo pt-BR |sed 's/-/_/')
if [ ! -d /usr/share/gnome/help/Cluster_Administration/%{_locale} ]; then
	ln -s %{_docdir}/Cluster_Administration-pt-BR-%{version} /usr/share/gnome/help/Cluster_Administration/%{_locale};
fi

%postun -n Cluster_Administration-pt-BR
%define _locale %(echo pt-BR |sed 's/-/_/')
rm -f /usr/share/gnome/help/Cluster_Administration/%{_locale}

%files -n Cluster_Administration-pt-BR
%defattr(-,root,root,-)
%doc pt-BR/*.xml
%doc pt-BR/Common_Config
%doc pt-BR/Common_Content
%doc pt-BR/images


%package -n Cluster_Administration-ru-RU
Summary: Red Hat Cluster Suite
Group: Documentation
Requires: Cluster_Administration-en-US = 5.0.0-5
Requires(post,postun): coreutils

%description -n Cluster_Administration-ru-RU

		
			 Clustered systems provide reliability, scalability, and availability to critical production services. Using a Red Hat Cluster, you can create high-availability clusters for file sharing, Web servers, and more. This document describes the configuration and management of Red Hat cluster systems. It does not include information about Red Hat Linux Virtual Servers (LVS). Information about installing and configuring LVS is in a separate document. 
		
	

%post -n Cluster_Administration-ru-RU
%define _locale %(echo ru-RU |sed 's/-/_/')
if [ ! -d /usr/share/gnome/help/Cluster_Administration/%{_locale} ]; then
	ln -s %{_docdir}/Cluster_Administration-ru-RU-%{version} /usr/share/gnome/help/Cluster_Administration/%{_locale};
fi

%postun -n Cluster_Administration-ru-RU
%define _locale %(echo ru-RU |sed 's/-/_/')
rm -f /usr/share/gnome/help/Cluster_Administration/%{_locale}

%files -n Cluster_Administration-ru-RU
%defattr(-,root,root,-)
%doc ru-RU/*.xml
%doc ru-RU/Common_Config
%doc ru-RU/Common_Content
%doc ru-RU/images


%package -n Cluster_Administration-si-LK
Summary: Red Hat Cluster Suite
Group: Documentation
Requires: Cluster_Administration-en-US = 5.0.0-5
Requires(post,postun): coreutils

%description -n Cluster_Administration-si-LK

		
			 Clustered systems provide reliability, scalability, and availability to critical production services. Using a Red Hat Cluster, you can create high-availability clusters for file sharing, Web servers, and more. This document describes the configuration and management of Red Hat cluster systems. It does not include information about Red Hat Linux Virtual Servers (LVS). Information about installing and configuring LVS is in a separate document. 
		
	

%post -n Cluster_Administration-si-LK
%define _locale %(echo si-LK |sed 's/-/_/')
if [ ! -d /usr/share/gnome/help/Cluster_Administration/%{_locale} ]; then
	ln -s %{_docdir}/Cluster_Administration-si-LK-%{version} /usr/share/gnome/help/Cluster_Administration/%{_locale};
fi

%postun -n Cluster_Administration-si-LK
%define _locale %(echo si-LK |sed 's/-/_/')
rm -f /usr/share/gnome/help/Cluster_Administration/%{_locale}

%files -n Cluster_Administration-si-LK
%defattr(-,root,root,-)
%doc si-LK/*.xml
%doc si-LK/Common_Config
%doc si-LK/Common_Content
%doc si-LK/images


%package -n Cluster_Administration-ta-IN
Summary: Red Hat Cluster Suite
Group: Documentation
Requires: Cluster_Administration-en-US = 5.0.0-5
Requires(post,postun): coreutils

%description -n Cluster_Administration-ta-IN

		
			 Clustered systems provide reliability, scalability, and availability to critical production services. Using a Red Hat Cluster, you can create high-availability clusters for file sharing, Web servers, and more. This document describes the configuration and management of Red Hat cluster systems. It does not include information about Red Hat Linux Virtual Servers (LVS). Information about installing and configuring LVS is in a separate document. 
		
	

%post -n Cluster_Administration-ta-IN
%define _locale %(echo ta-IN |sed 's/-/_/')
if [ ! -d /usr/share/gnome/help/Cluster_Administration/%{_locale} ]; then
	ln -s %{_docdir}/Cluster_Administration-ta-IN-%{version} /usr/share/gnome/help/Cluster_Administration/%{_locale};
fi

%postun -n Cluster_Administration-ta-IN
%define _locale %(echo ta-IN |sed 's/-/_/')
rm -f /usr/share/gnome/help/Cluster_Administration/%{_locale}

%files -n Cluster_Administration-ta-IN
%defattr(-,root,root,-)
%doc ta-IN/*.xml
%doc ta-IN/Common_Config
%doc ta-IN/Common_Content
%doc ta-IN/images


%package -n Cluster_Administration-te-IN
Summary: Red Hat Cluster Suite
Group: Documentation
Requires: Cluster_Administration-en-US = 5.0.0-5
Requires(post,postun): coreutils

%description -n Cluster_Administration-te-IN

		
			 Clustered systems provide reliability, scalability, and availability to critical production services. Using a Red Hat Cluster, you can create high-availability clusters for file sharing, Web servers, and more. This document describes the configuration and management of Red Hat cluster systems. It does not include information about Red Hat Linux Virtual Servers (LVS). Information about installing and configuring LVS is in a separate document. 
		
	

%post -n Cluster_Administration-te-IN
%define _locale %(echo te-IN |sed 's/-/_/')
if [ ! -d /usr/share/gnome/help/Cluster_Administration/%{_locale} ]; then
	ln -s %{_docdir}/Cluster_Administration-te-IN-%{version} /usr/share/gnome/help/Cluster_Administration/%{_locale};
fi

%postun -n Cluster_Administration-te-IN
%define _locale %(echo te-IN |sed 's/-/_/')
rm -f /usr/share/gnome/help/Cluster_Administration/%{_locale}

%files -n Cluster_Administration-te-IN
%defattr(-,root,root,-)
%doc te-IN/*.xml
%doc te-IN/Common_Config
%doc te-IN/Common_Content
%doc te-IN/images


%package -n Cluster_Administration-zh-CN
Summary: Red Hat Cluster Suite
Group: Documentation
Requires: Cluster_Administration-en-US = 5.0.0-5
Requires(post,postun): coreutils

%description -n Cluster_Administration-zh-CN

		
			 Clustered systems provide reliability, scalability, and availability to critical production services. Using a Red Hat Cluster, you can create high-availability clusters for file sharing, Web servers, and more. This document describes the configuration and management of Red Hat cluster systems. It does not include information about Red Hat Linux Virtual Servers (LVS). Information about installing and configuring LVS is in a separate document. 
		
	

%post -n Cluster_Administration-zh-CN
%define _locale %(echo zh-CN |sed 's/-/_/')
if [ ! -d /usr/share/gnome/help/Cluster_Administration/%{_locale} ]; then
	ln -s %{_docdir}/Cluster_Administration-zh-CN-%{version} /usr/share/gnome/help/Cluster_Administration/%{_locale};
fi

%postun -n Cluster_Administration-zh-CN
%define _locale %(echo zh-CN |sed 's/-/_/')
rm -f /usr/share/gnome/help/Cluster_Administration/%{_locale}

%files -n Cluster_Administration-zh-CN
%defattr(-,root,root,-)
%doc zh-CN/*.xml
%doc zh-CN/Common_Config
%doc zh-CN/Common_Content
%doc zh-CN/images


%package -n Cluster_Administration-zh-TW
Summary: Red Hat Cluster Suite
Group: Documentation
Requires: Cluster_Administration-en-US = 5.0.0-5
Requires(post,postun): coreutils

%description -n Cluster_Administration-zh-TW

		
			 Clustered systems provide reliability, scalability, and availability to critical production services. Using a Red Hat Cluster, you can create high-availability clusters for file sharing, Web servers, and more. This document describes the configuration and management of Red Hat cluster systems. It does not include information about Red Hat Linux Virtual Servers (LVS). Information about installing and configuring LVS is in a separate document. 
		
	

%post -n Cluster_Administration-zh-TW
%define _locale %(echo zh-TW |sed 's/-/_/')
if [ ! -d /usr/share/gnome/help/Cluster_Administration/%{_locale} ]; then
	ln -s %{_docdir}/Cluster_Administration-zh-TW-%{version} /usr/share/gnome/help/Cluster_Administration/%{_locale};
fi

%postun -n Cluster_Administration-zh-TW
%define _locale %(echo zh-TW |sed 's/-/_/')
rm -f /usr/share/gnome/help/Cluster_Administration/%{_locale}

%files -n Cluster_Administration-zh-TW
%defattr(-,root,root,-)
%doc zh-TW/*.xml
%doc zh-TW/Common_Config
%doc zh-TW/Common_Content
%doc zh-TW/images

%changelog

* Thu Jan 24 2007 Michael Hideo Smith mhideo@redhat.com 5.0.0-4
- Resolves: #221246
- Fix to broken rpm


* Thu Jan 11 2007 Michael Hideo Smith mhideo@redhat.com 5.0.0-3
- Resolves: #221246
- Fix to broken rpm

