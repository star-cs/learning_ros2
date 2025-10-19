# 创建功能包

`‵‵bash
ros2 pkg create demo_cpp_pkg --build-type ament_cmake --license Apache-2.0
```

```txt
# packet.xml
  <depend>rclcpp</depend>


# CMakeLists.txt
find_package(rclcpp REQUIRED)

add_executable(cpp_node src/cpp_node.cpp)

ament_target_dependencies(cpp_node rclcpp) # 替换 include link

install(TARGETS cpp_node
  DESTINATION lib/${PROJECT_NAME}
)
```

demo_cpp_pkg 同级目录 执行 colcon build 

cpp/01_pkg/install/demo_cpp_pkg/lib/demo_cpp_pkg/cpp_node 实际运行程序

```bash
cd build/demo_cpp_pkg

ldd cpp_node # 显示依赖
```

```bash 
soruce install/setup.bash   # 添加环境变量

ros2 run demo_cpp_pkg       # 运行
```