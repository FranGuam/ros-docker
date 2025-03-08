import cv2
import rospy

from tello import Tello, TelloROS

def test_base_class():
    drone = Tello()
    drone.send_command_and_receive_response("sdk?")
    drone.send_command_and_receive_response("sn?")
    drone.send_command_and_receive_response("battery?")
    drone.send_command_and_receive_response("wifi?")
    drone.send_command_and_receive_response("takeoff", 20)
    print("State: ", drone.get_state())
    img = cv2.cvtColor(drone.get_image(), cv2.COLOR_RGB2BGR)
    cv2.imshow("tello_image", img)
    drone.send_command_and_receive_response("land", 20)
    cv2.waitKey(0)

def test_ros_class():
    rospy.init_node('tello', anonymous=True)
    drone = TelloROS()
    drone.send_command_and_receive_response("sdk?")
    drone.send_command_and_receive_response("sn?")
    drone.send_command_and_receive_response("battery?")
    drone.send_command_and_receive_response("wifi?")
    drone.send_command_and_receive_response("takeoff", 20)
    print("State: ", drone.get_state())
    img = cv2.cvtColor(drone.get_image(), cv2.COLOR_RGB2BGR)
    cv2.imshow("tello_image", img)
    drone.send_command_and_receive_response("land", 20)
    cv2.waitKey(0)

def test_state():
    rospy.init_node('tello', anonymous=True)
    drone = TelloROS()
    drone.send_command_and_receive_response("mon")
    while True:
        print("State: ", drone.get_state())


if __name__ == '__main__':
    # test_base_class()
    # test_ros_class()
    # test_state()
