# Differential-drive-obstacle-avoidance
Create a catkin package and build it 

	$ mkdir -p catkin_ws/src
    $ cd catkin_ws/src
    $ git clone
    $ cd ..
    $ catkin_make
  
Source your workspace where you cloned the repository

	$ gedit ~/.bashrc
	
Add source ~/(YOUR_WORKSPACE_NAME)/devel/setup.bash at the end of the text file and restart the terminal

NOTE: Copy paste the /obstacle folder from /catkin_ws/src/robot_gazebo/worlds/gazebo to .ros/models

Load the model and world into the Simulator

    $ roslaunch robot_gazebo main_urdf.launch
    
Test if the simulation is working with teleoperation

    $ roslaunch robot_gazebo teleop_key.launch   
 
NOTE: The simulator starts in a paused mode, click the pause/play icon at the bottom of the screen

Try the obstacle avoidance script

    $ cd catkin_ws/src/robot_gazebo/scripts
    $ chmod +x avoidance.py
    $ ./avoidance.py
    
