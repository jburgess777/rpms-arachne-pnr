%global commit0 7e135edb31feacde85ec5b7e5c03fc9157080977

# The upstream makefile gets version information by invoking git. We can't
# do that. We can still use what the Makefile calls GIT_REV, because that's
# our shortcommit0 variable extracted from commit0 below.  We have to
# hard-code VER and VER_HASH here, as ver0 and verhash0.  When updating this
# package spec for a new git snapshot, clone the git repo, run make in it,
# and inspect the generated version_(has).cc to determine the correct values.
%global ver0 0.1+203+0
%global verhash0 59750

%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:           arachne-pnr
Version:        0.1
Release:        0.4.20170628git%{shortcommit0}%{?dist}
Summary:        Place and route for FPGA compilation
License:        GPLv2
URL:            https://github.com/cseed/arachne-pnr
Source0:        https://github.com/cseed/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
BuildRequires:  icestorm

%description
Arachne-pnr implements the place and route step of the hardware
compilation process for FPGAs. It accepts as input a technology-mapped
netlist in BLIF format, as output by the Yosys synthesis suite for
example. It currently targets the Lattice Semiconductor iCE40 family
of FPGAs. Its output is a textual bitstream representation for
assembly by the IceStorm icepack command. The output of icepack is a
binary bitstream which can be uploaded to a hardware device.

Together, Yosys, arachne-pnr and IceStorm provide an fully open-source
Verilog-to-bistream tool chain for iCE40 1K and 8K FPGA development.

%prep
%setup -q -n %{name}-%{commit0}

# can't use git from Makefile to extract version information
sed -i 's/^VER =.*/VER = %{ver0}/' Makefile
sed -i 's/^GIT_REV =.*/GIT_REV = %{shortcommit0}/' Makefile
sed -i 's/^VER_HASH =.*/VER_HASH = %{verhash0}/' Makefile

%build
make %{?_smp_mflags} \
     CXXFLAGS="%{optflags}" \
     PREFIX="%{_prefix}" \
     ICEBOX="%{_datadir}/icestorm"

%install
make install PREFIX="%{_prefix}" \
             DESTDIR="%{buildroot}" \
             ICEBOX="%{_datadir}/icestorm"

%files
%license COPYING
%doc README.md
%{_bindir}/*
%{_datadir}/%{name}

%changelog
* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1-0.4.20170628git7e135ed
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Sep 17 2017 Eric Smith <brouhaha@fedoraproject.org> 0.1-0.3.20170628git7e135ed
- updated to latest upstream.

* Mon Sep 12 2016 Eric Smith <brouhaha@fedoraproject.org> 0.1-0.2.20160813git52e69ed
- Updated directory used for icebox for consistency with icestorm package.

* Mon Sep 12 2016 Eric Smith <brouhaha@fedoraproject.org> 0.1-0.1.20160813git52e69ed
- Initial version.
