#!/usr/bin/tclsh

set arch "x86_64"
set base "3dcanvas-1.2.4"

if {[file exists build]} {
    file delete -force build
}

file mkdir build/BUILD build/RPMS build/SOURCES build/SPECS build/SRPMS
file copy -force $base.tar.gz build/SOURCES

set buildit [list rpmbuild --target $arch --define "_topdir [pwd]/build" -bb 3dcanvas.spec]
exec >@stdout 2>@stderr {*}$buildit

