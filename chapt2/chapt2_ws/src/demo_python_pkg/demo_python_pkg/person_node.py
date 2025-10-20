import rclpy
from rclpy.node import Node

class PersonNode(Node):
    def __init__(self, node_name: str , name: str = "张三", age: int = 18) -> None:
        super().__init__(node_name)
        self.name = name
        self.age = age

    def eat(self, food_name: str = "小炒肉"):
        # print(f"{self.age}岁的{self.name}正在吃{food_name}")
        self.get_logger().info(f"{self.age}岁的{self.name}正在吃{food_name}")

def main():
    rclpy.init()
    node = PersonNode('zhangsan','张三', 18)
    node.eat('小炒肉')
    rclpy.spin(node)
    rclpy.shutdown()