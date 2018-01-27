%global _prefix /usr/local

Name:    collectd_exporter
Version: 0.4.0
Release: 1%{?dist}
Summary: A server that accepts collectd stats via HTTP POST and exports them via HTTP for Prometheus consumption

Group:   Development Tools
URL:     https://github.com/prometheus/collectd_exporter
License: ASL 2.0
Source0: https://github.com/prometheus/collectd_exporter/releases/download/v%{version}/%{name}-%{version}.linux-amd64.tar.gz

%description
An exporter for collectd.
It accepts collectd's binary network protocol as sent by 
collectd's network plugin and metrics in JSON format via HTTP POST
as sent by collectd's write_http plugin, and
transforms and exposes them for consumption by Prometheus.

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/%{_bindir}
%{__install} -m 755 %{SOURCE0} %{buildroot}/%{_bindir}/%{name}

%files
%{_bindir}/%{name}
