import rclpy
import os
import torch
import torchvision
import cv2
import time
from rclpy.node import Node
from std_msgs.msg import Float64MultiArray
from std_msgs.msg import String
from sensor_msgs.msg import Image
from .object_detector import detect_objects
from .dope_model import DopeNetwork

class CoordinatesPublisher(Node):

    def __init__(self):
        super().__init__('coordinates_publisher')
        self.publisher_ = self.create_publisher(Float64MultiArray, 'coordinates', 10)
        use_cuda = torch.cuda.is_available()
        device = torch.device("cuda" if use_cuda else "cpu")
       
        #self.publisher_ = self.create_publisher(String, 'coordinates', 10)
        self.model = DopeNetwork()
        weights_path = os.path.join("/home/student/master_thesis_projects/dope-script", "mustard_60.pth")
        state_dict = torch.load(weights_path, map_location=device)
        new_state_dict = {key.replace('module.', ''): value for key, value in state_dict.items()} 
        self.model.load_state_dict(new_state_dict)
        self.model.eval()
        
        self.subscriber_ = self.create_subscription(
            Image,
            '/camera/color/image_raw',  # Topic name
            self.subscriber_callback,
            10
        )
        
        self.coordinates = []

    def subscriber_callback(self, msg):
        # Process the message received from the 'processed_data' topic
        received_message = msg.data
        print("msg_header",msg.header)
        # Get the current timestamp
        current_timestamp = time.time()
        print("current_timestamp",current_timestamp)
        result = detect_objects(self.model, msg)
        if len(result) > 0:
            raw_points = result[0]['raw_points']
            # if you want to see the points drawn on the image uncomment the following lines	
            #self.coordinates = [item for item in raw_points if item is not None]
            #image_path = os.path.join(os.getcwd(), "output_640_480_rgb_image_test.png")
            #image = cv2.imread(image_path)
            #points = [(int(round(x)), int(round(y))) for x, y in self.coordinates]
            #color = (0, 255, 0)  # Green
            #thickness = 5 		
            #for point in points:
            #	cv2.circle(image, point, thickness, color, -1)
            #cv2.imwrite("output_640_480_rgb_image_test_with_points.png", image)
        # Now publish the coordinates based on the received message
        self.publish_coordinates()
        
    def publish_coordinates(self):
        # Create the message to publish
        pub_msg = Float64MultiArray()

        # Flatten the coordinates and add them to the message
        for coord in self.coordinates:
            pub_msg.data.extend(coord)

        # Publish the coordinates
        self.publisher_.publish(pub_msg)
        self.get_logger().info(f'Publishing coordinates: {pub_msg.data}')

def main(args=None):
    rclpy.init(args=args)
    coordinates_publisher = CoordinatesPublisher()
    rclpy.spin(coordinates_publisher)
    coordinates_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
