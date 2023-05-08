import rclpy
from rclpy.node import Node
from gpiozero import PhaseEnableRobot


from geometry_msgs.msg import Twist

robot = PhaseEnableRobot(left=(5, 12), right=(6, 13))

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber')
        self.subscription = self.create_subscription(
            Twist,
            'cmd_vel',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        
        print(msg.linear.x)
        print(msg.angular.z)
        x = msg.linear.x
        z = msg.angular.z
        #self.get_logger().info('I heard: "%s"' % msg.data)
        if x > 0:
            robot.forward(speed = 0.6)
            if z > 0:
                robot.left_motor.forward(speed = 0.4)
                robot.right_motor.forward(speed = 0.8)
            elif z < 0:
                robot.left_motor.forward(speed = 0.8)
                robot.right_motor.forward(speed = 0.4)
                
        elif x == 0:
            if z > 0:
                robot.left(speed = 0.4)
            elif z < 0:
                robot.right(speed = 0.4)
            else:
                robot.stop()
                
        elif x < 0:
            robot.backward(speed = 0.6)
            if z < 0:
                robot.left_motor.backward(speed = 0.4)
                robot.right_motor.backward(speed = 0.8)
            elif z > 0:
                robot.left_motor.backward(speed = 0.8)
                robot.right_motor.backward(speed = 0.4)
        else:
            robot.stop()
        


def main(args=None):
    rclpy.init(args=args)

    minimal_subscriber = MinimalSubscriber()

    rclpy.spin(minimal_subscriber)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
