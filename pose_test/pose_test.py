from pose_format import Pose
from pose_format.pose_visualizer import PoseVisualizer


with open("example.pose", "rb") as f:
    pose = Pose.read(f.read())

v = PoseVisualizer(pose)

v.save_video("example.mp4", v.draw())