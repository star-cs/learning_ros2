#include <rclcpp/rclcpp.hpp>

class PersonNode : public rclcpp::Node
{
public:
    PersonNode(const std::string& node_name, const std::string& name, int age) : Node(node_name), name_(name), age_(age)
    {
        RCLCPP_INFO(this->get_logger(), "Person node has been started.");
    }

    void eat(const std::string &food)
    {
        RCLCPP_INFO(this->get_logger(), "I'm eating %s. My name is %s and I am %d years old.", food.c_str(), name_.c_str(), age_);
    }

private:
    std::string name_;
    int age_;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<PersonNode>("person_node", "Jane", 18);
    node->eat("Apple");
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}