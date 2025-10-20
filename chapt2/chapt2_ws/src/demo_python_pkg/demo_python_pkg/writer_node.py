import rclpy
from rclpy.node import Node
from demo_python_pkg.person_node import PersonNode

class WriterNode(PersonNode):
    def __init__(self, node_name, name: str = "张三", age: int = 18, book: str = "") -> None:
        super().__init__(node_name, name, age)
        print("WriterNode init")
        self.book = book

def main():
    rclpy.init()
    node = WriterNode('lisi_node','李四', 30, '三国演义')
    node.eat('烤牛排')
    node.get_logger().info(f"{node.age}岁的{node.name}正在写{node.book}")
    rclpy.spin(node)
    rclpy.shutdown()