from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import TextSubstitution, LaunchConfiguration


def generate_launch_description():

    namespace_args = DeclareLaunchArgument("robot_namespace", default_value=TextSubstitution(text="leo0X"))
    ns = namespace_args["robot_namespace"]
    return LaunchDescription([

    Node(package="tf2_ros",
                executable="static_transform_publisher",
                arguments=["0", "0", "0", "0", "0", "0", f"{ns}/realsense_camera_link", f"realsense_camera_{ns}_link"])
    ])