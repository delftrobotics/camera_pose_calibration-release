Name:           ros-indigo-camera-pose-calibration
Version:        0.1.1
Release:        0%{?dist}
Summary:        ROS camera_pose_calibration package

Group:          Development/Libraries
License:        Apache 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-cv-bridge
Requires:       ros-indigo-dr-base
Requires:       ros-indigo-eigen-conversions
Requires:       ros-indigo-image-transport
Requires:       ros-indigo-nodelet
Requires:       ros-indigo-pcl-ros
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-tf
Requires:       ros-indigo-tf-conversions
Requires:       ros-indigo-visualization-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-cv-bridge
BuildRequires:  ros-indigo-dr-base
BuildRequires:  ros-indigo-eigen-conversions
BuildRequires:  ros-indigo-image-transport
BuildRequires:  ros-indigo-nodelet
BuildRequires:  ros-indigo-pcl-ros
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-tf
BuildRequires:  ros-indigo-tf-conversions
BuildRequires:  ros-indigo-visualization-msgs

%description
Camera pose calibration using the OpenCV asymmetric circles pattern.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Apr 27 2016 Ronald Ensing <r.m.ensing@delftrobotics.com> - 0.1.1-0
- Autogenerated by Bloom

