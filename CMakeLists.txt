cmake_minimum_required(VERSION 3.5)
project(pose_publisher)

find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)

ament_python_install_package(${PROJECT_NAME})

install(PROGRAMS
  publish_pose.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
