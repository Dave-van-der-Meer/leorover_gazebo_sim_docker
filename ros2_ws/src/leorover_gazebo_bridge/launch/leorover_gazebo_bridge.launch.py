from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, SetEnvironmentVariable
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node  

def generate_launch_description():
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
        ('/model/leorover/tf','/tf')
    ]

    return LaunchDescription([

    # Nodes to launch
    Node(
        package='ros_gz_bridge', 
        executable='parameter_bridge', 
        output='screen',
        arguments=arguments,
        remappings=remappings),
    ])
