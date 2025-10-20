# workspace 创建

```bash
colcon build  # chapt2_ws 内执行        src 同级目录

colcon build --packages-select demo_cpp_pkg
```

```cmake
# demo_python_pkg/CMakeLists.txt
  <depend>demo_cpp_pkg</depend>  # python_node 依赖 cpp_node
```