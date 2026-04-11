import os

from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterFile
from launch_ros.substitutions import FindPackageShare

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.conditions import IfCondition
from launch.substitutions import (
    Command,
    FindExecutable,
    LaunchConfiguration,
    PathJoinSubstitution,
    TextSubstitution,
    PythonExpression,
)


def generate_launch_description():

    pkg_robot_cell_desc = get_package_share_directory('ur_atc_robot_cell_description')

    gz_resource_path = SetEnvironmentVariable(
        name='GZ_SIM_RESOURCE_PATH',
        value=[os.path.join(pkg_robot_cell_desc, '..')]
    )


    ur_type = LaunchConfiguration("ur_type")
    tf_prefix = LaunchConfiguration("tf_prefix")
    robot_ip = LaunchConfiguration("robot_ip")
    hardware_protocol = LaunchConfiguration("hardware_protocol")

    declared_arguments = []

    declared_arguments.append(
        DeclareLaunchArgument(
            "hardware_protocol",
            default_value="real",
            choices=["real", "gazebo"],
            description="Choose between 'real' robot driver or 'gazebo' simulation.",
        )
    )

    declared_arguments.append(
        DeclareLaunchArgument(
            "ur_type",
            description="Type/series of used UR robot.",
            choices=[
                "ur3",
                "ur3e",
                "ur5",
                "ur5e",
                "ur10",
                "ur10e",
                "ur16e",
                "ur20",
                "ur30",
            ],
            default_value="ur5e",
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "tf_prefix",
            default_value="",
            description="TF Prefix"
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument(
            "robot_ip",
            default_value="192.168.56.101",  # put your robot's IP address here
            description="IP address by which the robot can be reached.",
        )
    )
    declared_arguments.append(
        DeclareLaunchArgument("launch_rviz", default_value="true", description="Launch RViz?")
    )

    description_launchfile = PathJoinSubstitution(
        [FindPackageShare("ur_atc_robot_cell_control"), "launch", "rsp.launch.py"]
    )
    description_file = PathJoinSubstitution(
                [
                    FindPackageShare("ur_atc_robot_cell_control"),
                    "urdf",
                    "my_robot_cell_controlled.urdf.xacro",
                ]
            )
    controllers_file = PathJoinSubstitution(
        [FindPackageShare("ur_atc_robot_cell_control"), "config", "ros2_controllers.yaml"]
    )

    launch_real = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [PathJoinSubstitution([FindPackageShare("ur_robot_driver"), "launch", "ur_control.launch.py"])]
        ),
        condition=IfCondition(PythonExpression(["'", hardware_protocol, "' == 'real'"])),
        launch_arguments={
            "ur_type": ur_type,
            "robot_ip": robot_ip,
            "tf_prefix": [ur_type, "_"],
            "rviz_config_file": PathJoinSubstitution(
                        [
                            FindPackageShare("ur_atc_robot_cell_description"),
                            "rviz",
                            "urdf.rviz",
                        ]
                    ),
            "description_launchfile": description_launchfile,
            "controllers_file": controllers_file,
        }.items(),
    )

    launch_gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [PathJoinSubstitution([FindPackageShare("ur_simulation_gz"), "launch", "ur_sim_control.launch.py"])]
        ),
        condition=IfCondition(PythonExpression(["'", hardware_protocol, "' == 'gazebo'"])),
        launch_arguments={
            "ur_type": ur_type,
            "tf_prefix": tf_prefix,
            # "simulation_gz": "true",
            "description_file": description_file,
            "controllers_file": controllers_file,
        }.items(),
    )

    # my_controllers = ["joint_trajectory_controller"]

    cartesian_controllers = [
        "cartesian_compliance_controller",
        "cartesian_force_controller",
        "cartesian_motion_controller",
        "motion_control_handle",
        "joint_trajectory_controller"
    ]
    cartesian_spawners = [
        Node(
            package="controller_manager",
            executable="spawner",
            output="screen",
            arguments=[controller, "--inactive"],
        )
        for controller in cartesian_controllers
    ]

    return LaunchDescription(
        declared_arguments + 
        [
            launch_real,
            launch_gazebo,
            # gz_resource_path
        ] +
        cartesian_spawners
    )
