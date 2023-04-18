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

    gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_ros_gz_sim, 'launch', 'gz_sim.launch.py')),
        launch_arguments={
            'gz_args': '-r /home/leo/gazebo_leorover_model/lunar_landscape_prototype.sdf'
        }.items(),
    )

    spawn = Node(package='ros_gz_sim', executable='create',
                 arguments=[
                    '-name', 'leorover',
                    '-x', '0.0',
                    '-z', '0.0',
                    '-Y', '0.0',
                    '-file', '/home/leo/gazebo_leorover_model/leorover.sdf'],
                 output='screen')


    parameters=[]
    arguments=[
        '/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock',
        '/model/leorover/odometry@nav_msgs/msg/Odometry]gz.msgs.Odometry',
        '/cmd_vel@geometry_msgs/msg/Twist]gz.msgs.Twist',
        '/scan@sensor_msgs/msg/LaserScan[gz.msgs.LaserScan',
        '/imu@sensor_msgs/msg/Imu[gz.msgs.IMU',
        '/body_camera/camera_info@sensor_msgs/msg/CameraInfo[gz.msgs.CameraInfo',
        '/body_camera/image@sensor_msgs/msg/Image[gz.msgs.Image',
        '/realsense_d455/camera_info@sensor_msgs/msg/CameraInfo[gz.msgs.CameraInfo',
        '/realsense_d455/image@sensor_msgs/msg/Image[gz.msgs.Image',
        '/realsense_d455/depth_image@sensor_msgs/msg/Image[gz.msgs.Image',
        '/model/leorover/tf@tf2_msgs/msg/TFMessage[gz.msgs.Pose_V',
        '/world/lunar_landscape/model/leorover/joint_state@sensor_msgs/msg/JointState[gz.msgs.Model',
    ]

    remappings=[
        ('/clock', '/leo/clock'),
        ('/model/leorover/odometry', '/leo/odometry'),
        ('/cmd_vel', '/cmd_vel'),
        ('/scan', '/leo/scan'),
        ('/imu', '/leo/imu'),
        ('/body_camera/camera_info', '/leo/body_camera/camera_info'),
        ('/body_camera/image', '/leo/body_camera/image'),
        ('/realsese_d455/camera_info', '/leo/realsese_d455/camera_info'),
        ('/realsese_d455/image', '/leo/realsese_d455/image'),
        ('/realsese_d455/depth_image', '/leo/realsese_d455/depth_image'),
        ('/model/leorover/tf','/tf'),
        ('/world/lunar_landscape/model/leorover/joint_state','/joint_states')
    ]

    # Parse robot description from xacro
    robot_description_file =  '/home/leo/gazebo_leorover_model/leorover.sdf'
    # robot_description_config = xacro.process_file(robot_description_file)
    # robot_description = {"robot_description": robot_description_file.toxml()}
    doc = xacro.parse(open(xacro_file))
    xacro.process_doc(doc)
    robot_description = {'robot_description': doc.toxml()}

    bridge = Node(
        package='ros_gz_bridge', 
        executable='parameter_bridge', 
        output='screen',
        arguments=arguments,
        remappings=remappings)
    
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
      

    return LaunchDescription([
        gz_sim,
        spawn,
        bridge,
        robot_state_publisher,
        static_tf_base_footprint,
        static_tf_rp_lidar,
        static_tf_camera,
        static_tf_realsense_camera,
        ])
    
