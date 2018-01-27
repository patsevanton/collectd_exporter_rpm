#!/bin/bash

list_dependencies=(rpm-build rpmdevtools)

for i in ${list_dependencies[*]}
do
    if ! rpm -qa | grep -qw $i; then
        echo "__________Dont installed '$i'__________"
        #yum -y install $i
    fi
done

rm -rf ~/rpmbuild/
mkdir -p ~/rpmbuild/{RPMS,SRPMS,BUILD,SOURCES,SPECS}
cp collectd_exporter.init collectd_exporter.conf ~/rpmbuild/SOURCES
spectool -g -R collectd_exporter.spec
rpmbuild -bb collectd_exporter.spec
