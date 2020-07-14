## Wall Robot Navigation

A Wall following Robot is desined to move along a wall without hitting.There will be obstacles in its path and the robot has to make decisions which direction to move and roam around the environment in which it is placed.There will be sensors mounted on the robot which are used to calculate the distances of the obstacles and the walls which are fed into the Robot algorithms to make decisions.

[![Click here to watch a Demonstration video of Wall Following]](https://github.com/Rupakanth/Projects/blob/master/Wall%20Robot%20Navigation/Data%20and%20Images/videoplayback.mp4?raw=true)

The following study on wall following is made Using SCITOS G5 Robot while navigating a room in a clock wise direction for 4 rounds, using 24 ultrasound sensors arranged circularly around its waist.24 ultrasound readings and the simplified distances were collected at the same time step, so each file has the same number of rows (one for each sampling time step)

### SCITOS G5
![SCITOS G5](https://github.com/Rupakanth/Projects/blob/master/Wall%20Robot%20Navigation/Data%20and%20Images/SCITOS%20G5.png?raw=true)

The Robot desined to be a Left following Robot based on the which takes decisions which takes decisions based on following algotithm.

![](https://github.com/Rupakanth/Projects/blob/master/Wall%20Robot%20Navigation/Data%20and%20Images/Algo.png?raw=true)

The data is collected and tested from the environment shown below

![](https://github.com/Rupakanth/Projects/blob/master/Wall%20Robot%20Navigation/Data%20and%20Images/Environment.jpg?raw=true)

The following is the Perception(darker margin) and the Trajectory(blue line) of Robot while it surrounds thtough the above environment

![](https://github.com/Rupakanth/Projects/blob/master/Wall%20Robot%20Navigation/Data%20and%20Images/Normal%20trajectory.jpg?raw=true)

Expriments have been made in the Robot using Single layer and Multi layer Neural Networks with and without inclusion of Short Term Memory in the Robot.

### Perception, Trajectory and confusion matrix without using STM.

![](https://github.com/Rupakanth/Projects/blob/master/Wall%20Robot%20Navigation/Data%20and%20Images/Trajectory%20Without%20STM.jpg?raw=true)

![](https://github.com/Rupakanth/Projects/blob/master/Wall%20Robot%20Navigation/Data%20and%20Images/Confusion%20matrix%20without%20STM.png?raw=true)

### Perception, Trajectory and confusion matrix by using STM.

![](https://github.com/Rupakanth/Projects/blob/master/Wall%20Robot%20Navigation/Data%20and%20Images/Trajectory%20with%20STM.jpg?raw=true)

![](https://github.com/Rupakanth/Projects/blob/master/Wall%20Robot%20Navigation/Data%20and%20Images/Confusion%20matrix%20without%20STM.png?raw=true)

It is seen that for single layer Neural Network to work well STM is needed while Multi layer Neural Network does not need STM to perform well.

Lets check how effficient are Machine Learning algorithms perform this task.

