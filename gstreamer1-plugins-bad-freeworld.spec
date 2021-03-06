Summary:        GStreamer 1.0 streaming media framework "bad" plug-ins
Name:           gstreamer1-plugins-bad-freeworld
Epoch:          1
Version:        1.19.1
Release:        1%{?dist}
License:        LGPLv2+
URL:            https://gstreamer.freedesktop.org/
Source0:        %{url}/src/gst-plugins-bad/gst-plugins-bad-%{version}.tar.xz
Patch0:         build_what_we_need_only.patch

BuildRequires:  gcc-objc++
BuildRequires:  meson
BuildRequires:  gstreamer1-devel >= %{version}
BuildRequires:  gstreamer1-plugins-base-devel >= %{version}
BuildRequires:  gstreamer1-plugins-bad-free-devel >= %{version}
BuildRequires:  check
BuildRequires:  libXt-devel
BuildRequires:  orc-devel
BuildRequires:  libdca-devel
BuildRequires:  faad2-devel
BuildRequires:  libmms-devel
BuildRequires:  mjpegtools-devel >= 2.0.0
BuildRequires:  librtmp-devel
%ifarch x86_64
BuildRequires:  svt-hevc-devel
Provides:  gstreamer1-svt-hevc = %{version}-%{release}
Provides:  gstreamer1-svt-hevc%{?_isa} = %{version}-%{release}
Obsoletes: gstreamer1-svt-hevc < %{version}-%{release}
%endif
BuildRequires:  vo-amrwbenc-devel
#BuildRequires:  vo-aacenc-devel
BuildRequires:  libusbx-devel
BuildRequires:  x265-devel
BuildRequires:  libde265-devel


%description
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains plug-ins that have licensing issues, aren't tested
well enough, or the code is not of good enough quality.


%prep
%autosetup -p1 -n gst-plugins-bad-%{version}


%build
# Note we don't bother with disabling everything which is in Fedora, that
# is unmaintainable, instead we selectively run make in subdirs
%meson \
    -D package-name='gst-plugins-bad 1.0 rpmfusion rpm' \
    -D package-origin='http://rpmfusion.org/' \
    -D doc=disabled \
    -D introspection=disabled \
    -D examples=disabled \
%ifnarch x86_64
    -D svthevcenc=disabled \
%endif
    -D nls=disabled


%meson_build


%install
%meson_install

rm -rf %{buildroot}%{_datadir}/gstreamer-1.0/encoding-profiles/

%files
%doc AUTHORS NEWS README RELEASE
%license COPYING
# Take the whole dir for proper dir ownership (shared with other plugin pkgs)
%{_datadir}/gstreamer-1.0

# Plugins without external dependencies
%{_libdir}/gstreamer-1.0/libgstdvbsuboverlay.so
%{_libdir}/gstreamer-1.0/libgstdvdspu.so
%{_libdir}/gstreamer-1.0/libgstsiren.so

# Plugins with external dependencies
%{_libdir}/gstreamer-1.0/libgstde265.so
%{_libdir}/gstreamer-1.0/libgstdtsdec.so
%{_libdir}/gstreamer-1.0/libgstfaad.so
%{_libdir}/gstreamer-1.0/libgstmms.so
%{_libdir}/gstreamer-1.0/libgstmpeg2enc.so
%{_libdir}/gstreamer-1.0/libgstmplex.so
%{_libdir}/gstreamer-1.0/libgstrtmp.so
%ifarch x86_64
%{_libdir}/gstreamer-1.0/libgstsvthevcenc.so
%endif
#%%{_libdir}/gstreamer-1.0/libgstvoaacenc.so
%{_libdir}/gstreamer-1.0/libgstvoamrwbenc.so
%{_libdir}/gstreamer-1.0/libgstx265.so


%changelog
* Tue Jun 08 2021 Leigh Scott <leigh123linux@gmail.com> - 1.19.1-1
- Update

* Sat Apr 17 2021 Leigh Scott <leigh123linux@gmail.com> - 1.18.4-3
- Rebuild for new mjpegtools

* Wed Apr 14 2021 Leigh Scott <leigh123linux@gmail.com> - 1.18.4-2
- Rebuild for new x265

* Wed Mar 17 2021 Leigh Scott <leigh123linux@gmail.com> - 1.18.4-1
- 1.18.4

* Sat Feb 06 2021 Leigh Scott <leigh123linux@gmail.com> - 1.18.2-3
- Add Obsoletes gstreamer1-svt-hevc

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.18.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Sun Dec 13 2020 Leigh Scott <leigh123linux@gmail.com> - 1.18.2-1
- 1.18.3

* Sun Nov  1 2020 Leigh Scott <leigh123linux@gmail.com> - 1.18.1-1
- 1.18.1

* Tue Oct 27 2020 Leigh Scott <leigh123linux@gmail.com> - 1.18.0-2
- Rebuild for libde256

* Wed Sep  9 2020 Leigh Scott <leigh123linux@gmail.com> - 1.18.0-1
- 1.18.0

* Tue Sep  8 2020 Leigh Scott <leigh123linux@gmail.com> - 1.17.90-2
- Enable svt-hevc for x86_64

* Sun Aug 23 2020 Leigh Scott <leigh123linux@gmail.com> - 1.17.90-1
- 1.17.90

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.17.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 08 2020 Leigh Scott <leigh123linux@gmail.com> - 1.17.2-1
- 1.17.2

* Mon Jun 22 2020 Leigh Scott <leigh123linux@gmail.com> - 1.17.1-2
- Add BuildRequires gcc-objc++

* Mon Jun 22 2020 Leigh Scott <leigh123linux@gmail.com> - 1.17.1-1
- 1.17.1

* Sun May 31 2020 Leigh Scott <leigh123linux@gmail.com> - 1.16.2-6
- Rebuild for new x265 version

* Fri Mar 13 2020 Leigh Scott <leigh123linux@gmail.com> - 1.16.2-5
- Fixup for i686

* Thu Mar 12 2020 Leigh Scott <leigh123linux@gmail.com> - 1.16.2-4
- Rebuilt for i686

* Sun Feb 23 2020 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.16.2-3
- Rebuild for x265

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.16.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Feb 01 2020 Leigh Scott <leigh123linux@googlemail.com> - 1.16.2-1
- 1.16.2

* Thu Nov 28 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.16.1-2
- Rebuild for new x265

* Wed Sep 25 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.16.1-1
- 1.16.1

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.16.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 02 2019 Nicolas Chauvet <kwizart@gmail.com> - 1.16.0-2
- Rebuilt for x265

* Wed Apr 24 2019 Leigh Scott <leigh123linux@gmail.com> - 1.16.0-1
- 1.16.0

* Mon Mar 18 2019 Sérgio Basto <sergio@serjux.com> - 1.15.2-1
- Update to 1.15.2

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.15.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Feb 28 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.15.1-2
- Rebuild for new x265

* Sat Feb 09 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.15.1-1
- 1.15.1

* Fri Dec 07 2018 Antonio Trande <sagitter@fedoraproject.org> - 1.14.4-3
- Undo latest commit

* Sun Nov 18 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.14.4-2
- Rebuild for new x265

* Tue Oct 09 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.14.4-1
- 1.14.4

* Thu Oct 04 2018 Sérgio Basto <sergio@serjux.com> - 1.14.3-2
- Mass rebuild for x264 and/or x265

* Tue Sep 18 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.14.3-1
- 1.14.3

* Sat Aug 18 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.14.2-1
- 1.14.2

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.14.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 31 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.14.1-1
- 1.14.1

* Fri Mar 23 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.14.0-1
- 1.14.0

* Wed Feb 28 2018 Rex Dieter <rdieter@fedoraproject.org> - 1.13.1-1
- 1.13.1

* Wed Feb 28 2018 Nicolas Chauvet <kwizart@gmail.com> - 1.12.4-3
- Rebuilt for x265

* Sun Dec 31 2017 Sérgio Basto <sergio@serjux.com> - 1.12.4-2
- Mass rebuild for x264 and x265

* Mon Dec 11 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.12.4-1
- Update to 1.12.4

* Mon Oct 16 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.12.3-2
- Rebuild for ffmpeg update

* Thu Sep 21 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.12.3-1
- Update to 1.12.3

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.12.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 18 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.12.2-1
- Update to 1.12.2

* Fri Jun 23 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.12.1-1
- Update to 1.12.1

* Wed May 17 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.12.0-2
- Bump version for ffmpeg and x265 rebuild

* Fri May 12 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.12.0-1
- Update to 1.12.0

* Sun Apr 30 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.11.90-2
- Rebuild for x265 update

* Tue Apr 18 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.11.90-1
- Update to 1.11.90

* Sun Mar 19 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.11.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Feb 27 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.11.2-1
- Update to 1.11.2

* Mon Jan 16 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.11.1-2
- enable libde265

* Mon Jan 16 2017 Leigh Scott <leigh123linux@googlemail.com> - 1.11.1-1
- Update to 1.11.1
- Remove libmimic bits as mimic is no longer included in the source

* Tue Jan 03 2017 Dominik Mierzejewski <rpm@greysector.net> - 1.10.2-2
- rebuild for x265

* Wed Nov 30 2016 leigh scott <leigh123linux@googlemail.com> - 1.10.2-1
- Update to 1.10.2

* Fri Nov 11 2016 Hans de Goede <j.w.r.degoede@gmail.com> - 1.10.0-1
- Rebase to new upstream release 1.10.0

* Tue Nov 08 2016 Sérgio Basto <sergio@serjux.com> - 1.8.2-2
- Rebuild for x265-2.1

* Sun Jun 12 2016 Hans de Goede <j.w.r.degoede@gmail.com> - 1.8.2-1
- Rebase to new upstream release 1.8.2

* Wed May 18 2016 Hans de Goede <j.w.r.degoede@gmail.com> - 1.8.1-1
- Rebase to new upstream release 1.8.1

* Sat Jan 23 2016 Hans de Goede <j.w.r.degoede@gmail.com> - 1.6.3-1
- Rebase to new upstream release 1.6.3

* Thu Dec 24 2015 Hans de Goede <j.w.r.degoede@gmail.com> - 1.6.2-1
- Rebase to new upstream release 1.6.2

* Sat Oct 31 2015 Hans de Goede <j.w.r.degoede@gmail.com> - 1.6.1-1
- Rebase to new upstream release 1.6.1
- Enable x265 plugin

* Sat May 16 2015 Hans de Goede <j.w.r.degoede@gmail.com> - 1.4.5-2
- Add a patch from upstream fixing a faad2 crash which crashes firefox (rf3636)

* Sat May 16 2015 Hans de Goede <j.w.r.degoede@gmail.com> - 1.4.5-1
- Rebase to new upstream release 1.4.5

* Wed Oct  1 2014 Hans de Goede <j.w.r.degoede@gmail.com> - 1.4.3-1
- Rebase to new upstream release 1.4.3

* Sat Aug 30 2014 Hans de Goede <j.w.r.degoede@gmail.com> - 1.4.1-1
- Rebase to new upstream release 1.4.1

* Sun Jun 15 2014 Hans de Goede <j.w.r.degoede@gmail.com> - 1.2.4-1
- Rebase to new upstream release 1.2.4

* Sat Feb 15 2014 Michael Kuhn <suraia@ikkoku.de> - 1.2.3-1
- Update to 1.2.3.

* Thu Jan 09 2014 Michael Kuhn <suraia@ikkoku.de> - 1.2.2-1
- Update to 1.2.2.

* Tue Jan 07 2014 Nicolas Chauvet <kwizart@gmail.com> - 1.2.1-2
- Rebuilt for librtmp

* Sat Nov 16 2013 Hans de Goede <j.w.r.degoede@gmail.com> - 1.2.1-1
- Rebase to new upstream release 1.2.1

* Sun Nov 10 2013 Nicolas Chauvet <kwizart@gmail.com> - 1.2.0-2
- Rebuilt for mjpegtools update to 2.1.0

* Sun Oct 13 2013 Hans de Goede <j.w.r.degoede@gmail.com> - 1.2.0-1
- Rebase to new upstream release 1.2.0

* Thu Aug  8 2013 Hans de Goede <j.w.r.degoede@gmail.com> - 1.1.3-1
- Rebase to new upstream release 1.1.3

* Tue Aug  6 2013 Hans de Goede <j.w.r.degoede@gmail.com> - 1.0.9-1
- New upstream release 1.0.9

* Mon Mar 25 2013 Hans de Goede <j.w.r.degoede@gmail.com> - 1.0.6-1
- New upstream release 1.0.6

* Sat Mar  2 2013 Hans de Goede <j.w.r.degoede@gmail.com> - 1.0.5-1
- New upstream release 1.0.5
- Drop no longer needed PyXML BuildRequires (rf#2572)

* Sat Nov  3 2012 Hans de Goede <j.w.r.degoede@gmail.com> - 1.0.2-2
- Include some more files in %%doc (rf#2473)

* Sun Oct 28 2012 Hans de Goede <j.w.r.degoede@gmail.com> - 1.0.2-1
- New upstream release 1.0.2

* Sun Sep 23 2012 Hans de Goede <j.w.r.degoede@gmail.com> - 0.11.99-1
- New upstream release 0.11.99
- Use global rather then define (rf#2473)
- Disable vo-aacenc plugin for now (rf#1742)
- Enable siren plugin now that it has been ported to the 1.0 API

* Sun Sep  9 2012 Hans de Goede <j.w.r.degoede@gmail.com> - 0.11.93-1
- First version of gstreamer1-plugins-ugly for rpmfusion

