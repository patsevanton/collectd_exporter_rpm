%global _prefix /usr/local

Name:    collectd_exporter
Version: 0.4.0
Release: 1%{?dist}
Summary: A server that accepts collectd stats via HTTP POST and exports them via HTTP for Prometheus consumption

Group:   Development Tools
URL:     https://github.com/prometheus/collectd_exporter
License: ASL 2.0
Source0: https://github.com/prometheus/collectd_exporter/releases/download/v%{version}/%{name}-%{version}.linux-amd64.tar.gz
Source1: collectd_exporter.init
Source2: collectd_exporter.conf

%description
An exporter for collectd.
It accepts collectd's binary network protocol as sent by 
collectd's network plugin and metrics in JSON format via HTTP POST
as sent by collectd's write_http plugin, and
transforms and exposes them for consumption by Prometheus.

%prep
%setup -n %{name}-%{version}.linux-amd64

%install
rm -rf $RPM_BUILD_ROOT
%{__install} -m 0755 -d %{buildroot}%{_bindir}
%{__install} -m 0755 collectd_exporter %{buildroot}/%{_bindir}/%{name}
%{__install} -m 0755 -d %{buildroot}/etc/init.d/
%{__install} -m 0755 %{SOURCE1} %{buildroot}/etc/init.d/collectd_exporter
%{__install} -m 0644 %{SOURCE2} %{buildroot}/etc/collectd_exporter.conf

%files
%{_bindir}/%{name}
/etc/init.d/collectd_exporter
/etc/collectd_exporter.conf
