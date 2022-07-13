#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
import geometry_msgs.msg

def talker():

    pub = rospy.Publisher('chatter', geometry_msgs.msg.PoseStamped, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(2) # 10hz
    auto = geometry_msgs.msg.PoseStamped()
    while not rospy.is_shutdown():
        # hello_str = "hello world %s" % rospy.get_time()
        auto.pose.position.x += 1  
        auto.pose.position.x %= 60 
        if(auto.pose.position.y):
            auto.pose.position.y -= 1
        else:
            auto.pose.position.y = 60
        auto.pose.position.z = auto.pose.position.x * auto.pose.position.y
        rospy.loginfo(auto)
        pub.publish(auto)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass