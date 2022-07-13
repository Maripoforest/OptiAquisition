import rospy
from nav_msgs.msg import Odometry
import geometry_msgs.msg
import pandas as pd
import time

ot = time.time()

def callBack(msg):
    global ot
    print(time.time())
    rospy.loginfo(msg.pose.position.x)
    rospy.loginfo(msg.pose.position.y)
    rospy.loginfo(msg.pose.position.z)
    if (time.time() - ot) >= 10:
        dataframe = pd.DataFrame({'time': t, 'x': x})
        dataframe.to_csv("test.csv", index=False, sep=',')
        ot = time.time()

def record():
    print("runnning")
    rospy.init_node('opti_data_aquisition')
    rospy.Subscriber('chatter',geometry_msgs.msg.PoseStamped, callBack)
    rospy.spin()
    print("ended")

if __name__ == '__main__' :
    record()