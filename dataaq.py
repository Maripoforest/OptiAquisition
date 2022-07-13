import rospy
from nav_msgs.msg import Odometry
import geometry_msgs.msg
import pandas as pd
import time
import csv
import os

# x = []
# y = []
# z = []
# t = []
# ot = time.time()


def callBack(msg):
    global ot, x, y, z, t, filename
    print(time.time())

    rospy.loginfo(msg.pose.position.x)
    rospy.loginfo(msg.pose.position.y)
    rospy.loginfo(msg.pose.position.z)
    content = [time.time(), msg.pose.position.x, msg.pose.position.y, msg.pose.position.z, msg.pose.orientation.x, msg.pose.orientation.y, msg.pose.orientation.z, msg.pose.orientation.w]
    csv_writeline(filename, content)

    # x.append(msg.pose.position.x)
    # y.append(msg.pose.position.y)
    # z.append(msg.pose.position.z)
    # t.append(time.time())

    # if (time.time() - ot) >= 10:
    #     dataframe = pd.DataFrame({'time': t, 'x': x, 'y': y, 'z': z})
    #     dataframe.to_csv("test2.csv", index=False, sep=',')
    #     ot = time.time()

def record():
    print("runnning")
    rospy.init_node('opti_data_aquisition')
    rospy.Subscriber('chatter',geometry_msgs.msg.PoseStamped, callBack)
    rospy.spin()
    print("ended")

def csv_writeline(filename, filecontent):
    with open(filename, 'a+', newline='') as write_obj:
        csv_writer = csv.writer(write_obj)
        csv_writer.writerow(filecontent)

if __name__ == '__main__' :
    filename = ""
    filename = input("Name the file: ")
    filename = filename + ".csv"
    header = ["time", "x", "y", "z", "qx", "qy", "qz", "qw"]
    try: 
        open(filename, 'x')
        csv_writeline(filename, header)
        record()
    except:
        if os.stat(filename).st_size == 0:
            l = 0
        else:
            file = pd.read_csv(filename)
            l = len(file)
        print("file already exists with",l,"lines")
        rp = input("Continue? yes/no\n")
        if (rp == 'yes'):
            if(l == 0):
                csv_writeline(filename, header)
            record()
    
