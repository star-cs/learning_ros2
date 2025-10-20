import rclpy
from rclpy.node import Node

def main():
    rclpy.init()
    node = Node("python_node")
    node.get_logger().info("你好 python 节点")
    node.get_logger().warn("你好 python 节点")
    rclpy.spin(node)  # 循环
    rclpy.shutdown()

if __name__ == "__main__":
    main()

#  export RCUTILS_CONSOLE_OUTPUT_FORMAT='[{severity}][{time}]-[{name}-{line_number}]: {message}'

# [INFO] [1760862563.978143826] [python_node]: 你好 python 节点

# ros2 node list 查看 node 