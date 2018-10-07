# ROS Average Points

This is a simple project with the aim to learn ROS. The code is written in python.

Package name is `avg_points`.

There are currently 4 nodes:

1. `generate_points.py` - Generates 10 points every second (Publisher - `random_point`)
1. `calculate_average.py` - Read the points and calculate average (Subscriber - `random_point`)
1. `generate_box.py` - Generates 1 box every 10 seconds (Publisher - `random_box`)
1. `points_in_box.py` - Calculate the number of points in a box (Subscriber - `random_point`,`random_box`)

To calculate average of points, run `roslaunch avg_points avg_points.launch`
To find the points in a box, run `roslaunch avg_points points_in_box.launch`

## Custom messages
Files under `msg` are all the custom messages definition.

To "install" the message type,
```
roscd avg_points
cd ../..
catkin_make install
source devel/setup.bash
```