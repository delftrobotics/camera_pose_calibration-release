cmake_minimum_required(VERSION 2.8.3)
project(dr_base)

find_package(catkin REQUIRED COMPONENTS
	dr_cmake
)

catkin_package(
	CATKIN_DEPENDS dr_cmake
)
