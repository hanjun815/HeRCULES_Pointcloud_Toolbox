import open3d as o3d
import numpy as np
import struct
import os

def read_bin_file(filename, type):
    points = []
    with open(filename, "rb") as file:
        while True:
            if type == "Continental":
                data = file.read(29)
                if len(data) < 29:
                    break
                x, y, z, v, r = struct.unpack('fffff', data[:20])
                RCS = struct.unpack('B', data[20:21])
                azimuth, elevation = struct.unpack('ff', data[21:29])
            elif type == "ContinentalObject":
                data = file.read(20)
                if len(data) < 20:
                    break
                x, y, z, vx, vy = struct.unpack('fffff', data[:20])
            elif type == "Aeva": 
                data = file.read(29)
                if len(data) < 29:
                    break
                x, y, z, reflectivity, velocity = struct.unpack('fffff', data[:20])
                time_offset_ns = struct.unpack('I', data[20:24])
                line_index = struct.unpack('B', data[24:25])
                intensity = struct.unpack('f', data[25:29])
            else:
                raise ValueError("Unsupported sensor type")
            points.append([x, y, z])
    return points

def visualize_point_cloud(points):
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(np.array(points))
    o3d.visualization.draw_geometries([pcd])

# Example Usage
filename = input("Enter the path of bin file: ")
type = input("Enter the sensor type (Continental, ContinentalObject, Aeva): ") 
pointcloud = read_bin_file(filename, type)
visualize_point_cloud(pointcloud)
