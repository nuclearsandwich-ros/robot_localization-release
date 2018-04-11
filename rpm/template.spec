Name:           ros-kinetic-robot-localization
Version:        2.4.3
Release:        0%{?dist}
Summary:        ROS robot_localization package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/robot_localization
Source0:        %{name}-%{version}.tar.gz

Requires:       eigen3-devel
Requires:       ros-kinetic-cmake-modules
Requires:       ros-kinetic-diagnostic-msgs
Requires:       ros-kinetic-diagnostic-updater
Requires:       ros-kinetic-eigen-conversions
Requires:       ros-kinetic-geographic-msgs
Requires:       ros-kinetic-geometry-msgs
Requires:       ros-kinetic-message-filters
Requires:       ros-kinetic-message-runtime
Requires:       ros-kinetic-nav-msgs
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-sensor-msgs
Requires:       ros-kinetic-std-msgs
Requires:       ros-kinetic-std-srvs
Requires:       ros-kinetic-tf2
Requires:       ros-kinetic-tf2-geometry-msgs
Requires:       ros-kinetic-tf2-ros
Requires:       ros-kinetic-xmlrpcpp
Requires:       yaml-cpp-devel
BuildRequires:  eigen3-devel
BuildRequires:  python-catkin_pkg
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-cmake-modules
BuildRequires:  ros-kinetic-diagnostic-msgs
BuildRequires:  ros-kinetic-diagnostic-updater
BuildRequires:  ros-kinetic-eigen-conversions
BuildRequires:  ros-kinetic-geographic-msgs
BuildRequires:  ros-kinetic-geometry-msgs
BuildRequires:  ros-kinetic-message-filters
BuildRequires:  ros-kinetic-message-generation
BuildRequires:  ros-kinetic-nav-msgs
BuildRequires:  ros-kinetic-rosbag
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-roslint
BuildRequires:  ros-kinetic-rostest
BuildRequires:  ros-kinetic-rosunit
BuildRequires:  ros-kinetic-sensor-msgs
BuildRequires:  ros-kinetic-std-msgs
BuildRequires:  ros-kinetic-std-srvs
BuildRequires:  ros-kinetic-tf2
BuildRequires:  ros-kinetic-tf2-geometry-msgs
BuildRequires:  ros-kinetic-tf2-ros
BuildRequires:  ros-kinetic-xmlrpcpp
BuildRequires:  yaml-cpp-devel

%description
Provides nonlinear state estimation through sensor fusion of an abritrary number
of sensors.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Wed Apr 11 2018 Tom Moore <ayrton04@gmail.com> - 2.4.3-0
- Autogenerated by Bloom

* Wed Jan 03 2018 Tom Moore <ayrton04@gmail.com> - 2.4.2-0
- Autogenerated by Bloom

* Thu Dec 21 2017 Tom Moore <ayrton04@gmail.com> - 2.4.1-3
- Autogenerated by Bloom

* Thu Dec 21 2017 Tom Moore <ayrton04@gmail.com> - 2.4.1-2
- Autogenerated by Bloom

* Thu Dec 21 2017 Tom Moore <ayrton04@gmail.com> - 2.4.1-1
- Autogenerated by Bloom

* Fri Dec 15 2017 Tom Moore <ayrton04@gmail.com> - 2.4.1-0
- Autogenerated by Bloom

* Mon Jun 12 2017 Tom Moore <ayrton04@gmail.com> - 2.4.0-0
- Autogenerated by Bloom

* Thu Oct 27 2016 Tom Moore <ayrton04@gmail.com> - 2.3.1-0
- Autogenerated by Bloom

* Thu Aug 11 2016 Tom Moore <ayrton04@gmail.com> - 2.3.0-1
- Autogenerated by Bloom

* Thu Jul 28 2016 Tom Moore <ayrton04@gmail.com> - 2.3.0-0
- Autogenerated by Bloom

* Sun Apr 24 2016 Tom Moore <ayrton04@gmail.com> - 2.2.3-0
- Autogenerated by Bloom

