import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.launch_description_sources import AnyLaunchDescriptionSource
from launch.actions import GroupAction
from launch_ros.actions import PushRosNamespace

robot_namespace=None
try:
    path_prefix = os.path.expanduser('~') # Find the {$HOME} directory
    with open(os.path.join(path_prefix,'namespace')) as namespace_file:
        for line in namespace_file:
            robot_namespace=line.strip()
except Exception as e:
    print(e)
    print("##############################################")
    print("File 'namespace' not found in $HOME directory!")
    print("Falling back on default namespace: leo0X!")
    print("##############################################")


if robot_namespace is None:
    robot_namespace="leo0X"
tf_prefix=robot_namespace

def generate_launch_description():
    leorover_realsense_node = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('leorover_realsense'), 'launch'),
            '/d455_launch.py'])
    )
    rviz_node = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('leorover_description'), 'launch'),
            '/start_rviz2.launch.py'])
    )
    leorover_state_publisher_node = IncludeLaunchDescription(
        AnyLaunchDescriptionSource([os.path.join(
            get_package_share_directory('leorover_description'), 'launch'),
            '/state_publisher.launch.xml',]),
        launch_arguments={'robot_namespace':tf_prefix}.items(),
    )
    leorover_realsense_camera_static_tf_publisher_node = IncludeLaunchDescription(
        AnyLaunchDescriptionSource([os.path.join(
            get_package_share_directory('leorover_description'), 'launch'),
            '/realsense_camera_static_tf_publisher.launch.xml',]),
        launch_arguments={'robot_namespace':tf_prefix}.items(),
    )

    bringup_with_namespace = GroupAction(
        actions=[
            PushRosNamespace(robot_namespace),
            leorover_realsense_camera_static_tf_publisher_node,
            leorover_state_publisher_node,
            rviz_node
        ]
    )

    return LaunchDescription([
    bringup_with_namespace
    ])

