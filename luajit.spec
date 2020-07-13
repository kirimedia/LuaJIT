Name:           luajit 
Version:        %{version} 
Release:        %{release} 
License:        Proprietary
Vendor:         Mail.Ru
Group:          System Environment/Libraries
Source0:        luajit-%{current_datetime}.tar.gz
BuildRoot:      %{_tmppath}/luajit-%{current_datetime}
Summary:        LuaJIT 
Provides:       libluajit
Obsoletes:      libluajit

%package -n luajit-devel
Summary:        LuaJIT devel package
Group:          System Environment/Libraries
Requires:       luajit
Provides:       libluajit-devel
Obsoletes:      libluajit-devel

%description
LuaJIT library

%description -n luajit-devel
LuaJIT devel package

%define prefix /usr

%prep
[ "%{buildroot}" != "/" ] && rm -fr %{buildroot}
%setup -b 0 -n luajit-%{current_datetime}

%build
cd ..
cd luajit-%{current_datetime}
make

%install
make DESTDIR=%{buildroot} PREFIX=%{prefix} MULTILIB=%{multilib} install
rm %{buildroot}%{prefix}/%{multilib}/libluajit-*.a

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%{prefix}/bin/*
%{prefix}/%{multilib}/libluajit-*.so.*
%{prefix}/share/luajit-*
%{prefix}/share/man/*/*

%files -n luajit-devel
%{prefix}/include/*
%{prefix}/%{multilib}/libluajit-*.so
%{prefix}/%{multilib}/pkgconfig/*
