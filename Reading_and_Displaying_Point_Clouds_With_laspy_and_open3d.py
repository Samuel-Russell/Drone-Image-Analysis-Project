import numpy as np
import laspy
import open3d as o3d

las = laspy.read('/Users/samuelrussell/Documents/Potsdam_Uni/WS2/Tanzania_Extended_Internship_03_03_22/dense_points/dense_cloud_low_22_12_21_local.las')

point_cloud = las

points = np.vstack((point_cloud.x, point_cloud.y, point_cloud.z)).transpose()
colors = np.vstack((point_cloud.red, point_cloud.green, point_cloud.blue)).transpose()

pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(points)
pcd.colors = o3d.utility.Vector3dVector(colors/65535)
o3d.visualization.draw_geometries([pcd])