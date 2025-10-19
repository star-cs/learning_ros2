
# 创建功能包

```bash
ros2 pkg create --build-type ament_python --license Apache-2.0 demo_python_pkg
```

```python
# demo_python_pkg.python_node 添加的节点代码
...

# setup.py
entry_points={
        'console_scripts': [
            'python_node = demo_python_pkg.python_node:main',
        ],
    },

# packet.xml
  <depend>rclpy</depend>
```

```bash
colcon build
```
- build 构建中间文件
- install 结果文件
- py/01_pkg/install/demo_python_pkg/lib/python3.10/site-packages/demo_python_pkg/python_node.py 实际运行代码
- install/setup.bash 添加环境变量 

```bash
source install/setup.bash 
ros2 run demo_python_pkg python_node  执行
```