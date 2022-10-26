# Copyright 2020 TIER IV, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import launch
from launch.actions import SetLaunchConfiguration
from launch.conditions import IfCondition
from launch.conditions import UnlessCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.descriptions import ComposableNode
from autoware_utils.respawnable_node_container import RespawnableNodeContainer


def generate_launch_description():
    relay_components = []

    relay_components.append(
        ComposableNode(
            package="topic_tools",
            plugin="topic_tools::RelayNode",
            name="route_relay",
            namespace="awapi",
            parameters=[
                {
                    "input_topic": LaunchConfiguration("input_route"),
                    "output_topic": LaunchConfiguration("get_route"),
                }
            ],
            extra_arguments=[{"use_intra_process_comms": LaunchConfiguration("use_intra_process")}],
        )
    )

    relay_components.append(
        ComposableNode(
            package="topic_tools",
            plugin="topic_tools::RelayNode",
            name="predict_object_relay",
            namespace="awapi",
            parameters=[
                {
                    "input_topic": LaunchConfiguration("input_object"),
                    "output_topic": LaunchConfiguration("get_predicted_object"),
                }
            ],
            extra_arguments=[{"use_intra_process_comms": LaunchConfiguration("use_intra_process")}],
        )
    )

    relay_components.append(
        ComposableNode(
            package="topic_tools",
            plugin="topic_tools::RelayNode",
            name="nearest_traffic_signal_relay",
            namespace="awapi",
            parameters=[
                {
                    "input_topic": LaunchConfiguration("input_nearest_traffic_signal"),
                    "output_topic": LaunchConfiguration("get_nearest_traffic_signal"),
                }
            ],
            extra_arguments=[{"use_intra_process_comms": LaunchConfiguration("use_intra_process")}],
        )
    )

    relay_components.append(
        ComposableNode(
            package="topic_tools",
            plugin="topic_tools::RelayNode",
            name="ready_module_relay",
            namespace="awapi",
            parameters=[
                {
                    "input_topic": LaunchConfiguration("input_path_change_ready"),
                    "output_topic": LaunchConfiguration("get_path_change_ready"),
                }
            ],
            extra_arguments=[{"use_intra_process_comms": LaunchConfiguration("use_intra_process")}],
        )
    )

    relay_components.append(
        ComposableNode(
            package="topic_tools",
            plugin="topic_tools::RelayNode",
            name="force_available_relay",
            namespace="awapi",
            parameters=[
                {
                    "input_topic": LaunchConfiguration("input_path_change_force_available"),
                    "output_topic": LaunchConfiguration("get_path_change_force_available"),
                }
            ],
            extra_arguments=[{"use_intra_process_comms": LaunchConfiguration("use_intra_process")}],
        )
    )

    relay_components.append(
        ComposableNode(
            package="topic_tools",
            plugin="topic_tools::RelayNode",
            name="running_modules_relay",
            namespace="awapi",
            parameters=[
                {
                    "input_topic": LaunchConfiguration("input_path_change_running"),
                    "output_topic": LaunchConfiguration("get_path_change_running"),
                }
            ],
            extra_arguments=[{"use_intra_process_comms": LaunchConfiguration("use_intra_process")}],
        )
    )

    relay_components.append(
        ComposableNode(
            package="topic_tools",
            plugin="topic_tools::RelayNode",
            name="autoware_engage_relay",
            namespace="awapi",
            parameters=[
                {
                    "input_topic": LaunchConfiguration("set_engage"),
                    "output_topic": LaunchConfiguration("output_autoware_engage"),
                }
            ],
            extra_arguments=[{"use_intra_process_comms": LaunchConfiguration("use_intra_process")}],
        )
    )

    relay_components.append(
        ComposableNode(
            package="topic_tools",
            plugin="topic_tools::RelayNode",
            name="vehicle_engage_relay",
            namespace="awapi",
            parameters=[
                {
                    "input_topic": LaunchConfiguration("set_engage"),
                    "output_topic": LaunchConfiguration("output_vehicle_engage"),
                }
            ],
            extra_arguments=[{"use_intra_process_comms": LaunchConfiguration("use_intra_process")}],
        )
    )

    relay_components.append(
        ComposableNode(
            package="topic_tools",
            plugin="topic_tools::RelayNode",
            name="put_route_relay",
            namespace="awapi",
            parameters=[
                {
                    "input_topic": LaunchConfiguration("set_route"),
                    "output_topic": LaunchConfiguration("output_route"),
                }
            ],
            extra_arguments=[{"use_intra_process_comms": LaunchConfiguration("use_intra_process")}],
        )
    )

    relay_components.append(
        ComposableNode(
            package="topic_tools",
            plugin="topic_tools::RelayNode",
            name="put_goal_relay",
            namespace="awapi",
            parameters=[
                {
                    "input_topic": LaunchConfiguration("set_goal"),
                    "output_topic": LaunchConfiguration("output_goal"),
                }
            ],
            extra_arguments=[{"use_intra_process_comms": LaunchConfiguration("use_intra_process")}],
        )
    )

    relay_components.append(
        ComposableNode(
            package="topic_tools",
            plugin="topic_tools::RelayNode",
            name="lane_change_approval_relay",
            namespace="awapi",
            parameters=[
                {
                    "input_topic": LaunchConfiguration("set_lane_change_approval"),
                    "output_topic": LaunchConfiguration("output_lane_change_approval"),
                }
            ],
            extra_arguments=[{"use_intra_process_comms": LaunchConfiguration("use_intra_process")}],
        )
    )

    relay_components.append(
        ComposableNode(
            package="topic_tools",
            plugin="topic_tools::RelayNode",
            name="force_lane_change_relay",
            namespace="awapi",
            parameters=[
                {
                    "input_topic": LaunchConfiguration("set_force_lane_change"),
                    "output_topic": LaunchConfiguration("output_force_lane_change"),
                }
            ],
            extra_arguments=[{"use_intra_process_comms": LaunchConfiguration("use_intra_process")}],
        )
    )

    relay_components.append(
        ComposableNode(
            package="topic_tools",
            plugin="topic_tools::RelayNode",
            name="external_approval_relay",
            namespace="awapi",
            parameters=[
                {
                    "input_topic": LaunchConfiguration("set_path_change_approval"),
                    "output_topic": LaunchConfiguration("output_path_change_approval"),
                }
            ],
            extra_arguments=[{"use_intra_process_comms": LaunchConfiguration("use_intra_process")}],
        )
    )

    relay_components.append(
        ComposableNode(
            package="topic_tools",
            plugin="topic_tools::RelayNode",
            name="force_approval_relay",
            namespace="awapi",
            parameters=[
                {
                    "input_topic": LaunchConfiguration("set_path_change_force"),
                    "output_topic": LaunchConfiguration("output_path_change_force"),
                }
            ],
            extra_arguments=[{"use_intra_process_comms": LaunchConfiguration("use_intra_process")}],
        )
    )

    relay_components.append(
        ComposableNode(
            package="topic_tools",
            plugin="topic_tools::RelayNode",
            name="obstacle_avoid_approval_relay",
            namespace="awapi",
            parameters=[
                {
                    "input_topic": LaunchConfiguration("set_obstacle_avoid_approval"),
                    "output_topic": LaunchConfiguration("output_obstacle_avoid_approval"),
                }
            ],
            extra_arguments=[{"use_intra_process_comms": LaunchConfiguration("use_intra_process")}],
        )
    )

    relay_components.append(
        ComposableNode(
            package="topic_tools",
            plugin="topic_tools::RelayNode",
            name="traffic_signal_relay",
            namespace="awapi",
            parameters=[
                {
                    "input_topic": LaunchConfiguration("input_traffic_signals"),
                    "output_topic": LaunchConfiguration("get_traffic_signals"),
                }
            ],
            extra_arguments=[{"use_intra_process_comms": LaunchConfiguration("use_intra_process")}],
        )
    )

    relay_components.append(
        ComposableNode(
            package="topic_tools",
            plugin="topic_tools::RelayNode",
            name="overwrite_traffic_signals_relay",
            namespace="awapi",
            parameters=[
                {
                    "input_topic": LaunchConfiguration("set_overwrite_traffic_signals"),
                    "output_topic": LaunchConfiguration("output_overwrite_traffic_signals"),
                }
            ],
            extra_arguments=[{"use_intra_process_comms": LaunchConfiguration("use_intra_process")}],
        )
    )

    relay_components.append(
        ComposableNode(
            package="topic_tools",
            plugin="topic_tools::RelayNode",
            name="speed_exceeded_relay",
            namespace="awapi",
            parameters=[
                {
                    "input_topic": LaunchConfiguration("input_stop_speed_exceeded"),
                    "output_topic": LaunchConfiguration("get_stop_speed_exceeded"),
                }
            ],
            extra_arguments=[{"use_intra_process_comms": LaunchConfiguration("use_intra_process")}],
        )
    )

    relay_components.append(
        ComposableNode(
            package="topic_tools",
            plugin="topic_tools::RelayNode",
            name="crosswalk_status_relay",
            namespace="awapi",
            parameters=[
                {
                    "input_topic": LaunchConfiguration("set_crosswalk_status"),
                    "output_topic": LaunchConfiguration("input_external_crosswalk_status"),
                }
            ],
            extra_arguments=[{"use_intra_process_comms": LaunchConfiguration("use_intra_process")}],
        )
    )

    relay_components.append(
        ComposableNode(
            package="topic_tools",
            plugin="topic_tools::RelayNode",
            name="intersection_status_relay",
            namespace="awapi",
            parameters=[
                {
                    "input_topic": LaunchConfiguration("set_intersection_status"),
                    "output_topic": LaunchConfiguration("input_external_intersection_status"),
                }
            ],
            extra_arguments=[{"use_intra_process_comms": LaunchConfiguration("use_intra_process")}],
        )
    )

    relay_components.append(
        ComposableNode(
            package="topic_tools",
            plugin="topic_tools::RelayNode",
            name="expand_stop_range_relay",
            namespace="awapi",
            parameters=[
                {
                    "input_topic": LaunchConfiguration("set_expand_stop_range"),
                    "output_topic": LaunchConfiguration("input_expand_stop_range"),
                }
            ],
            extra_arguments=[{"use_intra_process_comms": LaunchConfiguration("use_intra_process")}],
        )
    )

    relay_components.append(
        ComposableNode(
            package="topic_tools",
            plugin="topic_tools::RelayNode",
            name="pose_initialization_request_relay",
            namespace="awapi",
            parameters=[
                {
                    "input_topic": LaunchConfiguration("set_pose_initialization_request"),
                    "output_topic": LaunchConfiguration("input_pose_initialization_request"),
                }
            ],
            extra_arguments=[{"use_intra_process_comms": LaunchConfiguration("use_intra_process")}],
        )
    )

    container = RespawnableNodeContainer(
        name="awapi_relay_container",
        namespace="awapi",
        package="rclcpp_components",
        executable=LaunchConfiguration("container_executable"),
        composable_node_descriptions=relay_components,
        output="screen",
    )

    set_container_executable = SetLaunchConfiguration(
        "container_executable",
        "component_container",
        condition=UnlessCondition(LaunchConfiguration("use_multithread")),
    )

    set_container_mt_executable = SetLaunchConfiguration(
        "container_executable",
        "component_container_mt",
        condition=IfCondition(LaunchConfiguration("use_multithread")),
    )

    return launch.LaunchDescription(
        [set_container_executable, set_container_mt_executable] + [container]
    )
