from setuptools import find_packages, setup

package_name = 'coordinates_publisher'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools','torch','torchvision'],
    zip_safe=True,
    maintainer='student',
    maintainer_email='ge46joy@tum.de',
    description='ROS2 package to publish coordinates',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publisher_node = coordinates_publisher.publisher_node:main',
        ],
    },
)
