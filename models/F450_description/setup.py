from setuptools import setup
import os
from glob import glob

package_name = 'F450_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*')),
        (os.path.join('share', package_name, 'meshes'), glob('meshes/*')),
        (os.path.join('share', package_name, 'config'), glob('config/*')),
         (os.path.join('share', package_name, 'include'), glob('include/*')),
          (os.path.join('share', package_name, 'hooks'), glob('hooks/*')),
          (os.path.join('share', package_name, 'src'), glob('src/*')),
    ],
    install_requires=['setuptools'],
    extras_require={
        'test': ['pytest'],
    },
    zip_safe=True,
    maintainer='Munagala Sai Raghava',
    maintainer_email='sairaghava2001@gmail.com',
    description='Description of the ' + package_name + ' package',
    license='Apache-2.0',  # Replace with your actual license
    entry_points={
        'console_scripts': [
            # Add your console scripts here if any
        ],
    },
)
