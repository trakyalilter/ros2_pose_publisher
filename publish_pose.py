#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import PoseStamped, Point, Quaternion
from std_msgs.msg import Header

def publish_pose():
    # Initialize the ROS Node
    rospy.init_node('pose_publisher', anonymous=True)

    # Create a publisher to send PoseStamped messages on the '/turtle1/pose' topic
    pub = rospy.Publisher('/turtle1/pose', PoseStamped, queue_size=10)

    # Set the rate at which the message will be published (10 Hz)
    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        # Create a PoseStamped message
        pose_stamped = PoseStamped()

        # Set the header (frame_id and timestamp)
        pose_stamped.header.stamp = rospy.Time.now()
        pose_stamped.header.frame_id = "world"  # Set the frame_id for visualization

        # Set the position (x, y, z)
        pose_stamped.pose.position = Point(2.0, 3.0, 0.0)

        # Set the orientation (quaternion: x, y, z, w)
        pose_stamped.pose.orientation = Quaternion(0.0, 0.0, 0.0, 1.0)

        # Publish the PoseStamped message
        pub.publish(pose_stamped)

        # Sleep to maintain the desired rate
        rate.sleep()

if __name__ == '__main__':
    try:
        publish_pose()
    except rospy.ROSInterruptException:
        pass
