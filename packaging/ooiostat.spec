Name:           ooiostat
Version:        0.1.0
Release:        1%{?dist}
Summary:        Monitors storage device read/write throughput, service times, and queue latency.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ooiostat
Source0:        ooiostat-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ooiostat is a sovereign, capability-bounded DISK IO METER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ooiostat
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ooiostat-uninstall

%files
/usr/bin/ooiostat
/usr/bin/ooiostat-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
