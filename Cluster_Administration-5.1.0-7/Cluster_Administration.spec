# Red Hat Documentation Specfile
Name:           Cluster_Administration
Version:        5.1.0
Release:        7
Summary:        Cluster Administration Suite
Group:          Documentation
License:        OPL + Restrictions
URL:            http://www.redhat.com/docs
Source0:         %{name}-%{version}-%{release}.tgz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires(post,postun): coreutils

%description
Clustered systems provide reliability, scalability, and
availability to critical production services. Using the Red Hat Cluster Manager,
administrators can create high availability clusters for
filesharing, Web servers, and more. This book discusses the
installation and configuration of cluster systems.

%package -n %{name}-en-US
Summary:    Cluster Administration Suite
Group:      Documentation
Requires(post,postun): coreutils

%description -n %{name}-en-US


%prep
%setup -q -n %{name}-%{version}-%{release}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/share/applications/

cat > $RPM_BUILD_ROOT/usr/share/applications/%{name}.desktop <<'EOF'
[Desktop Entry]
Name=Cluster Administration Suite
Name[en-US]=Cluster Administration Suite
Name[as-IN]=Cluster Administration Suite
Name[bn-IN]=Cluster Administration Suite
Name[de-DE]=Cluster Administration Suite
Name[es-ES]=Cluster Administration Suite
Name[fr-FR]=Cluster Administration Suite
Name[gu-IN]=Cluster Administration Suite
Name[hi-IN]=Cluster Administration Suite
Name[it-IT]=Cluster Administration Suite
Name[ja-JP]=Cluster Administration Suite
Name[kn-IN]=Cluster Administration Suite
Name[ko-KR]=Cluster Administration Suite
Name[ml-IN]=Cluster Administration Suite
Name[mr-IN]=Cluster Administration Suite
Name[or-IN]=Cluster Administration Suite
Name[pa-IN]=Cluster Administration Suite
Name[pt-BR]=Cluster Administration Suite
Name[ru-RU]=Cluster Administration Suite
Name[si-LK]=Cluster Administration Suite
Name[ta-IN]=Cluster Administration Suite
Name[te-IN]=Cluster Administration Suite
Name[zh-CN]=Cluster Administration Suite
Name[zh-TW]=Cluster Administration Suite
Comment=Configuring and Managing a Cluster
Exec=yelp ghelp:%{name}
#Exec=yelp %{_docdir}/%{name}-en-US-%{version}/Cluster_Administration.xml
Icon=%{_docdir}/%{name}-en-US-%{version}/images/icon.svg
Categories=Documentation;X-Red-Hat-Base;
Type=Application
Encoding=UTF-8
Terminal=false
EOF

mkdir -p $RPM_BUILD_ROOT/usr/share/gnome/help/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{name}-en-US
%define _locale %(echo en-US |sed 's/-/_/')
if [ -d /usr/share/gnome/help/%{name}/%{_locale} ]; then
	rm -rf /usr/share/gnome/help/%{name}/%{_locale}
fi
ln -sf %{_docdir}/%{name}-en-US-%{version} /usr/share/gnome/help/%{name}/%{_locale};
if [ -d /usr/share/gnome/help/%{name}/C ]; then
	rm -rf /usr/share/gnome/help/%{name}/C
fi
ln -sf %{_docdir}/%{name}-en-US-%{version} /usr/share/gnome/help/%{name}/C;


%postun -n %{name}-en-US
if [ "$1" -eq "0" ]; then
	rm -rf /usr/share/gnome/help/%{name}
fi

%posttrans -n %{name}-en-US
%define _locale %(echo en-US |sed 's/-/_/')
if [ -d %{_docdir}/%{name}-en-US-%{version} ]; then
	mkdir -p /usr/share/gnome/help/%{name}
	if [ -d /usr/share/gnome/help/%{name}/%{_locale} ]; then
		rm -rf /usr/share/gnome/help/%{name}/%{_locale}
	fi
	ln -sf %{_docdir}/%{name}-en-US-%{version} /usr/share/gnome/help/%{name}/%{_locale};
	if [ -d /usr/share/gnome/help/%{name}/C ]; then
		rm -rf /usr/share/gnome/help/%{name}/C
	fi
	ln -sf %{_docdir}/%{name}-en-US-%{version} /usr/share/gnome/help/%{name}/C;
fi

%files -n %{name}-en-US
%defattr(-,root,root,-)
%doc en-US/*.*
%doc en-US/Common_Content
%doc en-US/images
/usr/share/applications/%{name}.desktop
/usr/share/gnome/help/%{name}
%doc en-US/images
%doc en-US/Common_Content
%doc en-US/Virtual_Server_Administration
%doc en-US/Cluster_Administration
%doc en-US/Cluster_Suite_Overview


%package -n %{name}-as-IN
Summary: Cluster Administration Suite
Group: Documentation
Requires: %{name}-en-US = 5.1.0-7
Requires(post,postun): coreutils

%description -n %{name}-as-IN
Clustered systems provide reliability, scalability, and
availability to critical production services. Using the Red Hat Cluster Manager,
administrators can create high availability clusters for
filesharing, Web servers, and more. This book discusses the
installation and configuration of cluster systems.

%post -n %{name}-as-IN
%define _locale %(echo as-IN |sed 's/-/_/')
if [ -d /usr/share/gnome/help/%{name}/%{_locale} ]; then
	rm -rf /usr/share/gnome/help/%{name}/%{_locale}
fi
ln -sf %{_docdir}/%{name}-as-IN-%{version} /usr/share/gnome/help/%{name}/%{_locale};


%postun -n %{name}-as-IN
%define _locale %(echo as-IN |sed 's/-/_/')
if [ "$1" = 0 ]; then
	rm -f /usr/share/gnome/help/%{name}/%{_locale}
fi

%posttrans -n %{name}-as-IN
%define _locale %(echo as-IN |sed 's/-/_/')
if [ -d %{_docdir}/%{name}-as-IN-%{version} ]; then
	if [ -d /usr/share/gnome/help/%{name}/%{_locale} ]; then
		rm -rf /usr/share/gnome/help/%{name}/%{_locale}
	fi
	ln -sf %{_docdir}/%{name}-as-IN-%{version} /usr/share/gnome/help/%{name}/%{_locale};
fi

%files -n %{name}-as-IN
%defattr(-,root,root,-)
%doc as-IN/*.xml
%doc as-IN/images
%doc as-IN/Common_Content
%doc as-IN/Virtual_Server_Administration
%doc as-IN/Cluster_Administration
%doc as-IN/Cluster_Suite_Overview

%package -n %{name}-bn-IN
Summary: Cluster Administration Suite
Group: Documentation
Requires: %{name}-en-US = 5.1.0-7
Requires(post,postun): coreutils

%description -n %{name}-bn-IN
Clustered systems provide reliability, scalability, and
availability to critical production services. Using the Red Hat Cluster Manager,
administrators can create high availability clusters for
filesharing, Web servers, and more. This book discusses the
installation and configuration of cluster systems.

%post -n %{name}-bn-IN
%define _locale %(echo bn-IN |sed 's/-/_/')
if [ -d /usr/share/gnome/help/%{name}/%{_locale} ]; then
	rm -rf /usr/share/gnome/help/%{name}/%{_locale}
fi
ln -sf %{_docdir}/%{name}-bn-IN-%{version} /usr/share/gnome/help/%{name}/%{_locale};


%postun -n %{name}-bn-IN
%define _locale %(echo bn-IN |sed 's/-/_/')
if [ "$1" = 0 ]; then
	rm -f /usr/share/gnome/help/%{name}/%{_locale}
fi

%posttrans -n %{name}-bn-IN
%define _locale %(echo bn-IN |sed 's/-/_/')
if [ -d %{_docdir}/%{name}-bn-IN-%{version} ]; then
	if [ -d /usr/share/gnome/help/%{name}/%{_locale} ]; then
		rm -rf /usr/share/gnome/help/%{name}/%{_locale}
	fi
	ln -sf %{_docdir}/%{name}-bn-IN-%{version} /usr/share/gnome/help/%{name}/%{_locale};
fi

%files -n %{name}-bn-IN
%defattr(-,root,root,-)
%doc bn-IN/*.xml
%doc bn-IN/images
%doc bn-IN/Common_Content
%doc bn-IN/Virtual_Server_Administration
%doc bn-IN/Cluster_Administration
%doc bn-IN/Cluster_Suite_Overview

%package -n %{name}-de-DE
Summary: Cluster Administration Suite
Group: Documentation
Requires: %{name}-en-US = 5.1.0-7
Requires(post,postun): coreutils

%description -n %{name}-de-DE
Clustered systems provide reliability, scalability, and
availability to critical production services. Using the Red Hat Cluster Manager,
administrators can create high availability clusters for
filesharing, Web servers, and more. This book discusses the
installation and configuration of cluster systems.

%post -n %{name}-de-DE
%define _locale %(echo de-DE |sed 's/-/_/')
if [ -d /usr/share/gnome/help/%{name}/%{_locale} ]; then
	rm -rf /usr/share/gnome/help/%{name}/%{_locale}
fi
ln -sf %{_docdir}/%{name}-de-DE-%{version} /usr/share/gnome/help/%{name}/%{_locale};


%postun -n %{name}-de-DE
%define _locale %(echo de-DE |sed 's/-/_/')
if [ "$1" = 0 ]; then
	rm -f /usr/share/gnome/help/%{name}/%{_locale}
fi

%posttrans -n %{name}-de-DE
%define _locale %(echo de-DE |sed 's/-/_/')
if [ -d %{_docdir}/%{name}-de-DE-%{version} ]; then
	if [ -d /usr/share/gnome/help/%{name}/%{_locale} ]; then
		rm -rf /usr/share/gnome/help/%{name}/%{_locale}
	fi
	ln -sf %{_docdir}/%{name}-de-DE-%{version} /usr/share/gnome/help/%{name}/%{_locale};
fi

%files -n %{name}-de-DE
%defattr(-,root,root,-)
%doc de-DE/*.xml
%doc de-DE/images
%doc de-DE/Common_Content
%doc de-DE/Virtual_Server_Administration
%doc de-DE/Cluster_Administration
%doc de-DE/Cluster_Suite_Overview

%package -n %{name}-es-ES
Summary: Cluster Administration Suite
Group: Documentation
Requires: %{name}-en-US = 5.1.0-7
Requires(post,postun): coreutils

%description -n %{name}-es-ES
Clustered systems provide reliability, scalability, and
availability to critical production services. Using the Red Hat Cluster Manager,
administrators can create high availability clusters for
filesharing, Web servers, and more. This book discusses the
installation and configuration of cluster systems.

%post -n %{name}-es-ES
%define _locale %(echo es-ES |sed 's/-/_/')
if [ -d /usr/share/gnome/help/%{name}/%{_locale} ]; then
	rm -rf /usr/share/gnome/help/%{name}/%{_locale}
fi
ln -sf %{_docdir}/%{name}-es-ES-%{version} /usr/share/gnome/help/%{name}/%{_locale};


%postun -n %{name}-es-ES
%define _locale %(echo es-ES |sed 's/-/_/')
if [ "$1" = 0 ]; then
	rm -f /usr/share/gnome/help/%{name}/%{_locale}
fi

%posttrans -n %{name}-es-ES
%define _locale %(echo es-ES |sed 's/-/_/')
if [ -d %{_docdir}/%{name}-es-ES-%{version} ]; then
	if [ -d /usr/share/gnome/help/%{name}/%{_locale} ]; then
		rm -rf /usr/share/gnome/help/%{name}/%{_locale}
	fi
	ln -sf %{_docdir}/%{name}-es-ES-%{version} /usr/share/gnome/help/%{name}/%{_locale};
fi

%files -n %{name}-es-ES
%defattr(-,root,root,-)
%doc es-ES/*.xml
%doc es-ES/images
%doc es-ES/Common_Content
%doc es-ES/Virtual_Server_Administration
%doc es-ES/Cluster_Administration
%doc es-ES/Cluster_Suite_Overview

%package -n %{name}-fr-FR
Summary: Cluster Administration Suite
Group: Documentation
Requires: %{name}-en-US = 5.1.0-7
Requires(post,postun): coreutils

%description -n %{name}-fr-FR
Clustered systems provide reliability, scalability, and
availability to critical production services. Using the Red Hat Cluster Manager,
administrators can create high availability clusters for
filesharing, Web servers, and more. This book discusses the
installation and configuration of cluster systems.

%post -n %{name}-fr-FR
%define _locale %(echo fr-FR |sed 's/-/_/')
if [ -d /usr/share/gnome/help/%{name}/%{_locale} ]; then
	rm -rf /usr/share/gnome/help/%{name}/%{_locale}
fi
ln -sf %{_docdir}/%{name}-fr-FR-%{version} /usr/share/gnome/help/%{name}/%{_locale};


%postun -n %{name}-fr-FR
%define _locale %(echo fr-FR |sed 's/-/_/')
if [ "$1" = 0 ]; then
	rm -f /usr/share/gnome/help/%{name}/%{_locale}
fi

%posttrans -n %{name}-fr-FR
%define _locale %(echo fr-FR |sed 's/-/_/')
if [ -d %{_docdir}/%{name}-fr-FR-%{version} ]; then
	if [ -d /usr/share/gnome/help/%{name}/%{_locale} ]; then
		rm -rf /usr/share/gnome/help/%{name}/%{_locale}
	fi
	ln -sf %{_docdir}/%{name}-fr-FR-%{version} /usr/share/gnome/help/%{name}/%{_locale};
fi

%files -n %{name}-fr-FR
%defattr(-,root,root,-)
%doc fr-FR/*.xml
%doc fr-FR/images
%doc fr-FR/Common_Content
%doc fr-FR/Virtual_Server_Administration
%doc fr-FR/Cluster_Administration
%doc fr-FR/Cluster_Suite_Overview

%package -n %{name}-gu-IN
Summary: Cluster Administration Suite
Group: Documentation
Requires: %{name}-en-US = 5.1.0-7
Requires(post,postun): coreutils

%description -n %{name}-gu-IN
Clustered systems provide reliability, scalability, and
availability to critical production services. Using the Red Hat Cluster Manager,
administrators can create high availability clusters for
filesharing, Web servers, and more. This book discusses the
installation and configuration of cluster systems.

%post -n %{name}-gu-IN
%define _locale %(echo gu-IN |sed 's/-/_/')
if [ -d /usr/share/gnome/help/%{name}/%{_locale} ]; then
	rm -rf /usr/share/gnome/help/%{name}/%{_locale}
fi
ln -sf %{_docdir}/%{name}-gu-IN-%{version} /usr/share/gnome/help/%{name}/%{_locale};


%postun -n %{name}-gu-IN
%define _locale %(echo gu-IN |sed 's/-/_/')
if [ "$1" = 0 ]; then
	rm -f /usr/share/gnome/help/%{name}/%{_locale}
fi

%posttrans -n %{name}-gu-IN
%define _locale %(echo gu-IN |sed 's/-/_/')
if [ -d %{_docdir}/%{name}-gu-IN-%{version} ]; then
	if [ -d /usr/share/gnome/help/%{name}/%{_locale} ]; then
		rm -rf /usr/share/gnome/help/%{name}/%{_locale}
	fi
	ln -sf %{_docdir}/%{name}-gu-IN-%{version} /usr/share/gnome/help/%{name}/%{_locale};
fi

%files -n %{name}-gu-IN
%defattr(-,root,root,-)
%doc gu-IN/*.xml
%doc gu-IN/images
%doc gu-IN/Common_Content
%doc gu-IN/Virtual_Server_Administration
%doc gu-IN/Cluster_Administration
%doc gu-IN/Cluster_Suite_Overview

%package -n %{name}-hi-IN
Summary: Cluster Administration Suite
Group: Documentation
Requires: %{name}-en-US = 5.1.0-7
Requires(post,postun): coreutils

%description -n %{name}-hi-IN
Clustered systems provide reliability, scalability, and
availability to critical production services. Using the Red Hat Cluster Manager,
administrators can create high availability clusters for
filesharing, Web servers, and more. This book discusses the
installation and configuration of cluster systems.

%post -n %{name}-hi-IN
%define _locale %(echo hi-IN |sed 's/-/_/')
if [ -d /usr/share/gnome/help/%{name}/%{_locale} ]; then
	rm -rf /usr/share/gnome/help/%{name}/%{_locale}
fi
ln -sf %{_docdir}/%{name}-hi-IN-%{version} /usr/share/gnome/help/%{name}/%{_locale};


%postun -n %{name}-hi-IN
%define _locale %(echo hi-IN |sed 's/-/_/')
if [ "$1" = 0 ]; then
	rm -f /usr/share/gnome/help/%{name}/%{_locale}
fi

%posttrans -n %{name}-hi-IN
%define _locale %(echo hi-IN |sed 's/-/_/')
if [ -d %{_docdir}/%{name}-hi-IN-%{version} ]; then
	if [ -d /usr/share/gnome/help/%{name}/%{_locale} ]; then
		rm -rf /usr/share/gnome/help/%{name}/%{_locale}
	fi
	ln -sf %{_docdir}/%{name}-hi-IN-%{version} /usr/share/gnome/help/%{name}/%{_locale};
fi

%files -n %{name}-hi-IN
%defattr(-,root,root,-)
%doc hi-IN/*.xml
%doc hi-IN/images
%doc hi-IN/Common_Content
%doc hi-IN/Virtual_Server_Administration
%doc hi-IN/Cluster_Administration
%doc hi-IN/Cluster_Suite_Overview

%package -n %{name}-it-IT
Summary: Cluster Administration Suite
Group: Documentation
Requires: %{name}-en-US = 5.1.0-7
Requires(post,postun): coreutils

%description -n %{name}-it-IT
Clustered systems provide reliability, scalability, and
availability to critical production services. Using the Red Hat Cluster Manager,
administrators can create high availability clusters for
filesharing, Web servers, and more. This book discusses the
installation and configuration of cluster systems.

%post -n %{name}-it-IT
%define _locale %(echo it-IT |sed 's/-/_/')
if [ -d /usr/share/gnome/help/%{name}/%{_locale} ]; then
	rm -rf /usr/share/gnome/help/%{name}/%{_locale}
fi
ln -sf %{_docdir}/%{name}-it-IT-%{version} /usr/share/gnome/help/%{name}/%{_locale};


%postun -n %{name}-it-IT
%define _locale %(echo it-IT |sed 's/-/_/')
if [ "$1" = 0 ]; then
	rm -f /usr/share/gnome/help/%{name}/%{_locale}
fi

%posttrans -n %{name}-it-IT
%define _locale %(echo it-IT |sed 's/-/_/')
if [ -d %{_docdir}/%{name}-it-IT-%{version} ]; then
	if [ -d /usr/share/gnome/help/%{name}/%{_locale} ]; then
		rm -rf /usr/share/gnome/help/%{name}/%{_locale}
	fi
	ln -sf %{_docdir}/%{name}-it-IT-%{version} /usr/share/gnome/help/%{name}/%{_locale};
fi

%files -n %{name}-it-IT
%defattr(-,root,root,-)
%doc it-IT/*.xml
%doc it-IT/images
%doc it-IT/Common_Content
%doc it-IT/Virtual_Server_Administration
%doc it-IT/Cluster_Administration
%doc it-IT/Cluster_Suite_Overview

%package -n %{name}-ja-JP
Summary: Cluster Administration Suite
Group: Documentation
Requires: %{name}-en-US = 5.1.0-7
Requires(post,postun): coreutils

%description -n %{name}-ja-JP
Clustered systems provide reliability, scalability, and
availability to critical production services. Using the Red Hat Cluster Manager,
administrators can create high availability clusters for
filesharing, Web servers, and more. This book discusses the
installation and configuration of cluster systems.

%post -n %{name}-ja-JP
%define _locale %(echo ja-JP |sed 's/-/_/')
if [ -d /usr/share/gnome/help/%{name}/%{_locale} ]; then
	rm -rf /usr/share/gnome/help/%{name}/%{_locale}
fi
ln -sf %{_docdir}/%{name}-ja-JP-%{version} /usr/share/gnome/help/%{name}/%{_locale};


%postun -n %{name}-ja-JP
%define _locale %(echo ja-JP |sed 's/-/_/')
if [ "$1" = 0 ]; then
	rm -f /usr/share/gnome/help/%{name}/%{_locale}
fi

%posttrans -n %{name}-ja-JP
%define _locale %(echo ja-JP |sed 's/-/_/')
if [ -d %{_docdir}/%{name}-ja-JP-%{version} ]; then
	if [ -d /usr/share/gnome/help/%{name}/%{_locale} ]; then
		rm -rf /usr/share/gnome/help/%{name}/%{_locale}
	fi
	ln -sf %{_docdir}/%{name}-ja-JP-%{version} /usr/share/gnome/help/%{name}/%{_locale};
fi

%files -n %{name}-ja-JP
%defattr(-,root,root,-)
%doc ja-JP/*.xml
%doc ja-JP/images
%doc ja-JP/Common_Content
%doc ja-JP/Virtual_Server_Administration
%doc ja-JP/Cluster_Administration
%doc ja-JP/Cluster_Suite_Overview

%package -n %{name}-kn-IN
Summary: Cluster Administration Suite
Group: Documentation
Requires: %{name}-en-US = 5.1.0-7
Requires(post,postun): coreutils

%description -n %{name}-kn-IN
Clustered systems provide reliability, scalability, and
availability to critical production services. Using the Red Hat Cluster Manager,
administrators can create high availability clusters for
filesharing, Web servers, and more. This book discusses the
installation and configuration of cluster systems.

%post -n %{name}-kn-IN
%define _locale %(echo kn-IN |sed 's/-/_/')
if [ -d /usr/share/gnome/help/%{name}/%{_locale} ]; then
	rm -rf /usr/share/gnome/help/%{name}/%{_locale}
fi
ln -sf %{_docdir}/%{name}-kn-IN-%{version} /usr/share/gnome/help/%{name}/%{_locale};


%postun -n %{name}-kn-IN
%define _locale %(echo kn-IN |sed 's/-/_/')
if [ "$1" = 0 ]; then
	rm -f /usr/share/gnome/help/%{name}/%{_locale}
fi

%posttrans -n %{name}-kn-IN
%define _locale %(echo kn-IN |sed 's/-/_/')
if [ -d %{_docdir}/%{name}-kn-IN-%{version} ]; then
	if [ -d /usr/share/gnome/help/%{name}/%{_locale} ]; then
		rm -rf /usr/share/gnome/help/%{name}/%{_locale}
	fi
	ln -sf %{_docdir}/%{name}-kn-IN-%{version} /usr/share/gnome/help/%{name}/%{_locale};
fi

%files -n %{name}-kn-IN
%defattr(-,root,root,-)
%doc kn-IN/*.xml
%doc kn-IN/images
%doc kn-IN/Common_Content
%doc kn-IN/Virtual_Server_Administration
%doc kn-IN/Cluster_Administration
%doc kn-IN/Cluster_Suite_Overview

%package -n %{name}-ko-KR
Summary: Cluster Administration Suite
Group: Documentation
Requires: %{name}-en-US = 5.1.0-7
Requires(post,postun): coreutils

%description -n %{name}-ko-KR
Clustered systems provide reliability, scalability, and
availability to critical production services. Using the Red Hat Cluster Manager,
administrators can create high availability clusters for
filesharing, Web servers, and more. This book discusses the
installation and configuration of cluster systems.

%post -n %{name}-ko-KR
%define _locale %(echo ko-KR |sed 's/-/_/')
if [ -d /usr/share/gnome/help/%{name}/%{_locale} ]; then
	rm -rf /usr/share/gnome/help/%{name}/%{_locale}
fi
ln -sf %{_docdir}/%{name}-ko-KR-%{version} /usr/share/gnome/help/%{name}/%{_locale};


%postun -n %{name}-ko-KR
%define _locale %(echo ko-KR |sed 's/-/_/')
if [ "$1" = 0 ]; then
	rm -f /usr/share/gnome/help/%{name}/%{_locale}
fi

%posttrans -n %{name}-ko-KR
%define _locale %(echo ko-KR |sed 's/-/_/')
if [ -d %{_docdir}/%{name}-ko-KR-%{version} ]; then
	if [ -d /usr/share/gnome/help/%{name}/%{_locale} ]; then
		rm -rf /usr/share/gnome/help/%{name}/%{_locale}
	fi
	ln -sf %{_docdir}/%{name}-ko-KR-%{version} /usr/share/gnome/help/%{name}/%{_locale};
fi

%files -n %{name}-ko-KR
%defattr(-,root,root,-)
%doc ko-KR/*.xml
%doc ko-KR/images
%doc ko-KR/Common_Content
%doc ko-KR/Virtual_Server_Administration
%doc ko-KR/Cluster_Administration
%doc ko-KR/Cluster_Suite_Overview

%package -n %{name}-ml-IN
Summary: Cluster Administration Suite
Group: Documentation
Requires: %{name}-en-US = 5.1.0-7
Requires(post,postun): coreutils

%description -n %{name}-ml-IN
Clustered systems provide reliability, scalability, and
availability to critical production services. Using the Red Hat Cluster Manager,
administrators can create high availability clusters for
filesharing, Web servers, and more. This book discusses the
installation and configuration of cluster systems.

%post -n %{name}-ml-IN
%define _locale %(echo ml-IN |sed 's/-/_/')
if [ -d /usr/share/gnome/help/%{name}/%{_locale} ]; then
	rm -rf /usr/share/gnome/help/%{name}/%{_locale}
fi
ln -sf %{_docdir}/%{name}-ml-IN-%{version} /usr/share/gnome/help/%{name}/%{_locale};


%postun -n %{name}-ml-IN
%define _locale %(echo ml-IN |sed 's/-/_/')
if [ "$1" = 0 ]; then
	rm -f /usr/share/gnome/help/%{name}/%{_locale}
fi

%posttrans -n %{name}-ml-IN
%define _locale %(echo ml-IN |sed 's/-/_/')
if [ -d %{_docdir}/%{name}-ml-IN-%{version} ]; then
	if [ -d /usr/share/gnome/help/%{name}/%{_locale} ]; then
		rm -rf /usr/share/gnome/help/%{name}/%{_locale}
	fi
	ln -sf %{_docdir}/%{name}-ml-IN-%{version} /usr/share/gnome/help/%{name}/%{_locale};
fi

%files -n %{name}-ml-IN
%defattr(-,root,root,-)
%doc ml-IN/*.xml
%doc ml-IN/images
%doc ml-IN/Common_Content
%doc ml-IN/Virtual_Server_Administration
%doc ml-IN/Cluster_Administration
%doc ml-IN/Cluster_Suite_Overview

%package -n %{name}-mr-IN
Summary: Cluster Administration Suite
Group: Documentation
Requires: %{name}-en-US = 5.1.0-7
Requires(post,postun): coreutils

%description -n %{name}-mr-IN
Clustered systems provide reliability, scalability, and
availability to critical production services. Using the Red Hat Cluster Manager,
administrators can create high availability clusters for
filesharing, Web servers, and more. This book discusses the
installation and configuration of cluster systems.

%post -n %{name}-mr-IN
%define _locale %(echo mr-IN |sed 's/-/_/')
if [ -d /usr/share/gnome/help/%{name}/%{_locale} ]; then
	rm -rf /usr/share/gnome/help/%{name}/%{_locale}
fi
ln -sf %{_docdir}/%{name}-mr-IN-%{version} /usr/share/gnome/help/%{name}/%{_locale};


%postun -n %{name}-mr-IN
%define _locale %(echo mr-IN |sed 's/-/_/')
if [ "$1" = 0 ]; then
	rm -f /usr/share/gnome/help/%{name}/%{_locale}
fi

%posttrans -n %{name}-mr-IN
%define _locale %(echo mr-IN |sed 's/-/_/')
if [ -d %{_docdir}/%{name}-mr-IN-%{version} ]; then
	if [ -d /usr/share/gnome/help/%{name}/%{_locale} ]; then
		rm -rf /usr/share/gnome/help/%{name}/%{_locale}
	fi
	ln -sf %{_docdir}/%{name}-mr-IN-%{version} /usr/share/gnome/help/%{name}/%{_locale};
fi

%files -n %{name}-mr-IN
%defattr(-,root,root,-)
%doc mr-IN/*.xml
%doc mr-IN/images
%doc mr-IN/Common_Content
%doc mr-IN/Virtual_Server_Administration
%doc mr-IN/Cluster_Administration
%doc mr-IN/Cluster_Suite_Overview

%package -n %{name}-or-IN
Summary: Cluster Administration Suite
Group: Documentation
Requires: %{name}-en-US = 5.1.0-7
Requires(post,postun): coreutils

%description -n %{name}-or-IN
Clustered systems provide reliability, scalability, and
availability to critical production services. Using the Red Hat Cluster Manager,
administrators can create high availability clusters for
filesharing, Web servers, and more. This book discusses the
installation and configuration of cluster systems.

%post -n %{name}-or-IN
%define _locale %(echo or-IN |sed 's/-/_/')
if [ -d /usr/share/gnome/help/%{name}/%{_locale} ]; then
	rm -rf /usr/share/gnome/help/%{name}/%{_locale}
fi
ln -sf %{_docdir}/%{name}-or-IN-%{version} /usr/share/gnome/help/%{name}/%{_locale};


%postun -n %{name}-or-IN
%define _locale %(echo or-IN |sed 's/-/_/')
if [ "$1" = 0 ]; then
	rm -f /usr/share/gnome/help/%{name}/%{_locale}
fi

%posttrans -n %{name}-or-IN
%define _locale %(echo or-IN |sed 's/-/_/')
if [ -d %{_docdir}/%{name}-or-IN-%{version} ]; then
	if [ -d /usr/share/gnome/help/%{name}/%{_locale} ]; then
		rm -rf /usr/share/gnome/help/%{name}/%{_locale}
	fi
	ln -sf %{_docdir}/%{name}-or-IN-%{version} /usr/share/gnome/help/%{name}/%{_locale};
fi

%files -n %{name}-or-IN
%defattr(-,root,root,-)
%doc or-IN/*.xml
%doc or-IN/images
%doc or-IN/Common_Content
%doc or-IN/Virtual_Server_Administration
%doc or-IN/Cluster_Administration
%doc or-IN/Cluster_Suite_Overview

%package -n %{name}-pa-IN
Summary: Cluster Administration Suite
Group: Documentation
Requires: %{name}-en-US = 5.1.0-7
Requires(post,postun): coreutils

%description -n %{name}-pa-IN
Clustered systems provide reliability, scalability, and
availability to critical production services. Using the Red Hat Cluster Manager,
administrators can create high availability clusters for
filesharing, Web servers, and more. This book discusses the
installation and configuration of cluster systems.

%post -n %{name}-pa-IN
%define _locale %(echo pa-IN |sed 's/-/_/')
if [ -d /usr/share/gnome/help/%{name}/%{_locale} ]; then
	rm -rf /usr/share/gnome/help/%{name}/%{_locale}
fi
ln -sf %{_docdir}/%{name}-pa-IN-%{version} /usr/share/gnome/help/%{name}/%{_locale};


%postun -n %{name}-pa-IN
%define _locale %(echo pa-IN |sed 's/-/_/')
if [ "$1" = 0 ]; then
	rm -f /usr/share/gnome/help/%{name}/%{_locale}
fi

%posttrans -n %{name}-pa-IN
%define _locale %(echo pa-IN |sed 's/-/_/')
if [ -d %{_docdir}/%{name}-pa-IN-%{version} ]; then
	if [ -d /usr/share/gnome/help/%{name}/%{_locale} ]; then
		rm -rf /usr/share/gnome/help/%{name}/%{_locale}
	fi
	ln -sf %{_docdir}/%{name}-pa-IN-%{version} /usr/share/gnome/help/%{name}/%{_locale};
fi

%files -n %{name}-pa-IN
%defattr(-,root,root,-)
%doc pa-IN/*.xml
%doc pa-IN/images
%doc pa-IN/Common_Content
%doc pa-IN/Virtual_Server_Administration
%doc pa-IN/Cluster_Administration
%doc pa-IN/Cluster_Suite_Overview

%package -n %{name}-pt-BR
Summary: Cluster Administration Suite
Group: Documentation
Requires: %{name}-en-US = 5.1.0-7
Requires(post,postun): coreutils

%description -n %{name}-pt-BR
Clustered systems provide reliability, scalability, and
availability to critical production services. Using the Red Hat Cluster Manager,
administrators can create high availability clusters for
filesharing, Web servers, and more. This book discusses the
installation and configuration of cluster systems.

%post -n %{name}-pt-BR
%define _locale %(echo pt-BR |sed 's/-/_/')
if [ -d /usr/share/gnome/help/%{name}/%{_locale} ]; then
	rm -rf /usr/share/gnome/help/%{name}/%{_locale}
fi
ln -sf %{_docdir}/%{name}-pt-BR-%{version} /usr/share/gnome/help/%{name}/%{_locale};


%postun -n %{name}-pt-BR
%define _locale %(echo pt-BR |sed 's/-/_/')
if [ "$1" = 0 ]; then
	rm -f /usr/share/gnome/help/%{name}/%{_locale}
fi

%posttrans -n %{name}-pt-BR
%define _locale %(echo pt-BR |sed 's/-/_/')
if [ -d %{_docdir}/%{name}-pt-BR-%{version} ]; then
	if [ -d /usr/share/gnome/help/%{name}/%{_locale} ]; then
		rm -rf /usr/share/gnome/help/%{name}/%{_locale}
	fi
	ln -sf %{_docdir}/%{name}-pt-BR-%{version} /usr/share/gnome/help/%{name}/%{_locale};
fi

%files -n %{name}-pt-BR
%defattr(-,root,root,-)
%doc pt-BR/*.xml
%doc pt-BR/images
%doc pt-BR/Common_Content
%doc pt-BR/Virtual_Server_Administration
%doc pt-BR/Cluster_Administration
%doc pt-BR/Cluster_Suite_Overview

%package -n %{name}-ru-RU
Summary: Cluster Administration Suite
Group: Documentation
Requires: %{name}-en-US = 5.1.0-7
Requires(post,postun): coreutils

%description -n %{name}-ru-RU
Clustered systems provide reliability, scalability, and
availability to critical production services. Using the Red Hat Cluster Manager,
administrators can create high availability clusters for
filesharing, Web servers, and more. This book discusses the
installation and configuration of cluster systems.

%post -n %{name}-ru-RU
%define _locale %(echo ru-RU |sed 's/-/_/')
if [ -d /usr/share/gnome/help/%{name}/%{_locale} ]; then
	rm -rf /usr/share/gnome/help/%{name}/%{_locale}
fi
ln -sf %{_docdir}/%{name}-ru-RU-%{version} /usr/share/gnome/help/%{name}/%{_locale};


%postun -n %{name}-ru-RU
%define _locale %(echo ru-RU |sed 's/-/_/')
if [ "$1" = 0 ]; then
	rm -f /usr/share/gnome/help/%{name}/%{_locale}
fi

%posttrans -n %{name}-ru-RU
%define _locale %(echo ru-RU |sed 's/-/_/')
if [ -d %{_docdir}/%{name}-ru-RU-%{version} ]; then
	if [ -d /usr/share/gnome/help/%{name}/%{_locale} ]; then
		rm -rf /usr/share/gnome/help/%{name}/%{_locale}
	fi
	ln -sf %{_docdir}/%{name}-ru-RU-%{version} /usr/share/gnome/help/%{name}/%{_locale};
fi

%files -n %{name}-ru-RU
%defattr(-,root,root,-)
%doc ru-RU/*.xml
%doc ru-RU/images
%doc ru-RU/Common_Content
%doc ru-RU/Virtual_Server_Administration
%doc ru-RU/Cluster_Administration
%doc ru-RU/Cluster_Suite_Overview

%package -n %{name}-si-LK
Summary: Cluster Administration Suite
Group: Documentation
Requires: %{name}-en-US = 5.1.0-7
Requires(post,postun): coreutils

%description -n %{name}-si-LK
Clustered systems provide reliability, scalability, and
availability to critical production services. Using the Red Hat Cluster Manager,
administrators can create high availability clusters for
filesharing, Web servers, and more. This book discusses the
installation and configuration of cluster systems.

%post -n %{name}-si-LK
%define _locale %(echo si-LK |sed 's/-/_/')
if [ -d /usr/share/gnome/help/%{name}/%{_locale} ]; then
	rm -rf /usr/share/gnome/help/%{name}/%{_locale}
fi
ln -sf %{_docdir}/%{name}-si-LK-%{version} /usr/share/gnome/help/%{name}/%{_locale};


%postun -n %{name}-si-LK
%define _locale %(echo si-LK |sed 's/-/_/')
if [ "$1" = 0 ]; then
	rm -f /usr/share/gnome/help/%{name}/%{_locale}
fi

%posttrans -n %{name}-si-LK
%define _locale %(echo si-LK |sed 's/-/_/')
if [ -d %{_docdir}/%{name}-si-LK-%{version} ]; then
	if [ -d /usr/share/gnome/help/%{name}/%{_locale} ]; then
		rm -rf /usr/share/gnome/help/%{name}/%{_locale}
	fi
	ln -sf %{_docdir}/%{name}-si-LK-%{version} /usr/share/gnome/help/%{name}/%{_locale};
fi

%files -n %{name}-si-LK
%defattr(-,root,root,-)
%doc si-LK/*.xml
%doc si-LK/images
%doc si-LK/Common_Content
%doc si-LK/Virtual_Server_Administration
%doc si-LK/Cluster_Administration
%doc si-LK/Cluster_Suite_Overview

%package -n %{name}-ta-IN
Summary: Cluster Administration Suite
Group: Documentation
Requires: %{name}-en-US = 5.1.0-7
Requires(post,postun): coreutils

%description -n %{name}-ta-IN
Clustered systems provide reliability, scalability, and
availability to critical production services. Using the Red Hat Cluster Manager,
administrators can create high availability clusters for
filesharing, Web servers, and more. This book discusses the
installation and configuration of cluster systems.

%post -n %{name}-ta-IN
%define _locale %(echo ta-IN |sed 's/-/_/')
if [ -d /usr/share/gnome/help/%{name}/%{_locale} ]; then
	rm -rf /usr/share/gnome/help/%{name}/%{_locale}
fi
ln -sf %{_docdir}/%{name}-ta-IN-%{version} /usr/share/gnome/help/%{name}/%{_locale};


%postun -n %{name}-ta-IN
%define _locale %(echo ta-IN |sed 's/-/_/')
if [ "$1" = 0 ]; then
	rm -f /usr/share/gnome/help/%{name}/%{_locale}
fi

%posttrans -n %{name}-ta-IN
%define _locale %(echo ta-IN |sed 's/-/_/')
if [ -d %{_docdir}/%{name}-ta-IN-%{version} ]; then
	if [ -d /usr/share/gnome/help/%{name}/%{_locale} ]; then
		rm -rf /usr/share/gnome/help/%{name}/%{_locale}
	fi
	ln -sf %{_docdir}/%{name}-ta-IN-%{version} /usr/share/gnome/help/%{name}/%{_locale};
fi

%files -n %{name}-ta-IN
%defattr(-,root,root,-)
%doc ta-IN/*.xml
%doc ta-IN/images
%doc ta-IN/Common_Content
%doc ta-IN/Virtual_Server_Administration
%doc ta-IN/Cluster_Administration
%doc ta-IN/Cluster_Suite_Overview

%package -n %{name}-te-IN
Summary: Cluster Administration Suite
Group: Documentation
Requires: %{name}-en-US = 5.1.0-7
Requires(post,postun): coreutils

%description -n %{name}-te-IN
Clustered systems provide reliability, scalability, and
availability to critical production services. Using the Red Hat Cluster Manager,
administrators can create high availability clusters for
filesharing, Web servers, and more. This book discusses the
installation and configuration of cluster systems.

%post -n %{name}-te-IN
%define _locale %(echo te-IN |sed 's/-/_/')
if [ -d /usr/share/gnome/help/%{name}/%{_locale} ]; then
	rm -rf /usr/share/gnome/help/%{name}/%{_locale}
fi
ln -sf %{_docdir}/%{name}-te-IN-%{version} /usr/share/gnome/help/%{name}/%{_locale};


%postun -n %{name}-te-IN
%define _locale %(echo te-IN |sed 's/-/_/')
if [ "$1" = 0 ]; then
	rm -f /usr/share/gnome/help/%{name}/%{_locale}
fi

%posttrans -n %{name}-te-IN
%define _locale %(echo te-IN |sed 's/-/_/')
if [ -d %{_docdir}/%{name}-te-IN-%{version} ]; then
	if [ -d /usr/share/gnome/help/%{name}/%{_locale} ]; then
		rm -rf /usr/share/gnome/help/%{name}/%{_locale}
	fi
	ln -sf %{_docdir}/%{name}-te-IN-%{version} /usr/share/gnome/help/%{name}/%{_locale};
fi

%files -n %{name}-te-IN
%defattr(-,root,root,-)
%doc te-IN/*.xml
%doc te-IN/images
%doc te-IN/Common_Content
%doc te-IN/Virtual_Server_Administration
%doc te-IN/Cluster_Administration
%doc te-IN/Cluster_Suite_Overview

%package -n %{name}-zh-CN
Summary: Cluster Administration Suite
Group: Documentation
Requires: %{name}-en-US = 5.1.0-7
Requires(post,postun): coreutils

%description -n %{name}-zh-CN
Clustered systems provide reliability, scalability, and
availability to critical production services. Using the Red Hat Cluster Manager,
administrators can create high availability clusters for
filesharing, Web servers, and more. This book discusses the
installation and configuration of cluster systems.

%post -n %{name}-zh-CN
%define _locale %(echo zh-CN |sed 's/-/_/')
if [ -d /usr/share/gnome/help/%{name}/%{_locale} ]; then
	rm -rf /usr/share/gnome/help/%{name}/%{_locale}
fi
ln -sf %{_docdir}/%{name}-zh-CN-%{version} /usr/share/gnome/help/%{name}/%{_locale};


%postun -n %{name}-zh-CN
%define _locale %(echo zh-CN |sed 's/-/_/')
if [ "$1" = 0 ]; then
	rm -f /usr/share/gnome/help/%{name}/%{_locale}
fi

%posttrans -n %{name}-zh-CN
%define _locale %(echo zh-CN |sed 's/-/_/')
if [ -d %{_docdir}/%{name}-zh-CN-%{version} ]; then
	if [ -d /usr/share/gnome/help/%{name}/%{_locale} ]; then
		rm -rf /usr/share/gnome/help/%{name}/%{_locale}
	fi
	ln -sf %{_docdir}/%{name}-zh-CN-%{version} /usr/share/gnome/help/%{name}/%{_locale};
fi

%files -n %{name}-zh-CN
%defattr(-,root,root,-)
%doc zh-CN/*.xml
%doc zh-CN/images
%doc zh-CN/Common_Content
%doc zh-CN/Virtual_Server_Administration
%doc zh-CN/Cluster_Administration
%doc zh-CN/Cluster_Suite_Overview

%package -n %{name}-zh-TW
Summary: Cluster Administration Suite
Group: Documentation
Requires: %{name}-en-US = 5.1.0-7
Requires(post,postun): coreutils

%description -n %{name}-zh-TW
Clustered systems provide reliability, scalability, and
availability to critical production services. Using the Red Hat Cluster Manager,
administrators can create high availability clusters for
filesharing, Web servers, and more. This book discusses the
installation and configuration of cluster systems.

%post -n %{name}-zh-TW
%define _locale %(echo zh-TW |sed 's/-/_/')
if [ -d /usr/share/gnome/help/%{name}/%{_locale} ]; then
	rm -rf /usr/share/gnome/help/%{name}/%{_locale}
fi
ln -sf %{_docdir}/%{name}-zh-TW-%{version} /usr/share/gnome/help/%{name}/%{_locale};


%postun -n %{name}-zh-TW
%define _locale %(echo zh-TW |sed 's/-/_/')
if [ "$1" = 0 ]; then
	rm -f /usr/share/gnome/help/%{name}/%{_locale}
fi

%posttrans -n %{name}-zh-TW
%define _locale %(echo zh-TW |sed 's/-/_/')
if [ -d %{_docdir}/%{name}-zh-TW-%{version} ]; then
	if [ -d /usr/share/gnome/help/%{name}/%{_locale} ]; then
		rm -rf /usr/share/gnome/help/%{name}/%{_locale}
	fi
	ln -sf %{_docdir}/%{name}-zh-TW-%{version} /usr/share/gnome/help/%{name}/%{_locale};
fi

%files -n %{name}-zh-TW
%defattr(-,root,root,-)
%doc zh-TW/*.xml
%doc zh-TW/images
%doc zh-TW/Common_Content
%doc zh-TW/Virtual_Server_Administration
%doc zh-TW/Cluster_Administration
%doc zh-TW/Cluster_Suite_Overview


%changelog

* Tue Jun 26 2007 Michael Hideo Smith mhideo@redhat.com 5.1.0-1
- Resolves: #245685
- Content Updates

