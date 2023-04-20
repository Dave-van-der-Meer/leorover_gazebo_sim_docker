import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, SetEnvironmentVariable, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
from launch.launch_description_sources import PythonLaunchDescriptionSource
import xacro

def generate_launch_description():

    pkg_ros_gz_sim = get_package_share_directory('ros_gz_sim')
    leorover_urdf_path = os.path.join(get_package_share_directory('leorover_description'))

    xacro_file = os.path.join(leorover_urdf_path,
                              'urdf',
                              'leo_sim.urdf.xacro')

    pkg_leorover_gazebo = get_package_share_directory('leorover_gazebo')
    gazebo_world_file = os.path.join(pkg_leorover_gazebo, 'worlds', 'lunar_landscape_prototype.sdf')
    gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_ros_gz_sim, 'launch', 'gz_sim.launch.py')),
        launch_arguments={
            'gz_args': f'-r {gazebo_world_file}'}.items(),
    )

    robot_description_file = os.path.join(pkg_leorover_gazebo, 'robots', 'leorover.sdf')
    spawn = Node(package='ros_gz_sim', executable='create',
                 arguments=[
                    '-name', 'leorover',
                    '-x', '0.0',
                    '-z', '0.0',
                    '-Y', '0.0',
                    '-file', robot_description_file],
                 output='screen')


    # Parse robot description from xacro
    doc = xacro.parse(open(xacro_file))
    xacro.process_doc(doc)
    robot_description = {'robot_description': doc.toxml()}


    pkg_leorover_gazebo_bridge = get_package_share_directory('leorover_gazebo_bridge')
    bridge = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_leorover_gazebo_bridge, 'launch', 'leorover_gazebo_bridge.launch.py')),
    )

  
    robot_state_publisher = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='both',
        parameters=[robot_description],
    )

    static_tf_base_footprint = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='base_footprint_publisher',
        arguments=['0', '0', '0', '0', '0', '0', '1', '/leorover/base_footprint', 'base_footprint']
    )

    static_tf_rp_lidar = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='rp_lidar_publisher',
        arguments=['0', '0', '0', '0', '0', '1', '0', 'rp_lidar_optical_frame', 'leorover/rp_lidar_frame/gpu_lidar']
    )
    
    static_tf_camera = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='camera_publisher',
        arguments=['0', '0', '0', '0', '0', '0', '1', 'camera_optical_frame', 'leorover/internal_camera_optical_frame/internal_camera']
    )

    static_tf_realsense_camera = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='realsense_camera_publisher',
        arguments=['0', '0', '0', '-0.5', '0.5', '-0.5', '0.5', 'realsense_camera_link', 'leorover/realsense_camera_optical_frame/realsense_d455']
    )

    pkg_leorover_gazebo = get_package_share_directory('leorover_gazebo')
    rviz = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_leorover_gazebo, 'launch', 'rviz2.launch.py')),
    )
    

    return LaunchDescription([
        gz_sim,
        spawn,
        bridge,
        robot_state_publisher,
        static_tf_base_footprint,
        static_tf_rp_lidar,
        static_tf_camera,
        static_tf_realsense_camera,
        rviz,
        ])
    
