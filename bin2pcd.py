import numpy as np
import struct, sys, os
import open3d as o3d


def bin_to_pcd(bin_fn, sensor_type):
    pts, extra = [], []

    with open(bin_fn, 'rb') as f:
        if sensor_type == "Continental":
            rec = 29
            while (chunk := f.read(rec)):
                if len(chunk) < rec: break
                x, y, z, v, r = struct.unpack('<fffff',  chunk[:20])
                RCS           = struct.unpack('<B',      chunk[20:21])[0]
                az, el        = struct.unpack('<ff',     chunk[21:29])
                pts.append([x,y,z])
                extra.append([v, r, RCS, az, el])

        elif sensor_type == "ContinentalObject":
            rec = 20
            while (chunk := f.read(rec)):
                if len(chunk) < rec: break
                x, y, z, vx, vy = struct.unpack('<fffff', chunk)
                pts.append([x,y,z])
                extra.append([vx, vy])

        elif sensor_type == "Aeva":
            rec = 29
            while (chunk := f.read(rec)):
                if len(chunk) < rec: break
                x, y, z, refl, vel = struct.unpack('<fffff', chunk[:20])
                t_off   = struct.unpack('<I', chunk[20:24])[0]
                line_id = struct.unpack('<B', chunk[24:25])[0]
                inten   = struct.unpack('<f', chunk[25:29])[0]
                pts.append([x,y,z])
                extra.append([refl, vel, t_off, line_id, inten])

        else:
            raise ValueError("sensor_type must be Continental / ContinentalObject / Aeva")

    return np.asarray(pts, dtype=np.float32), np.asarray(extra), sensor_type


def save_to_pcd(points: np.ndarray, extra: np.ndarray, sensor_type: str, pcd_fn: str):
    if sensor_type == "Continental":
        fields = ["x","y","z","velocity","range","RCS","azimuth","elevation"]
        types  = ["F","F","F","F","F","U","F","F"]     # PCD TYPE
        sizes  = ["4","4","4","4","4","1","4","4"]     # byte size
    elif sensor_type == "ContinentalObject":
        fields = ["x","y","z","vx","vy"]
        types  = ["F","F","F","F","F"]
        sizes  = ["4"]*5
    else:   # Aeva
        fields = ["x","y","z","reflectivity","velocity",
                  "time_offset_ns","line_index","intensity"]
        types  = ["F","F","F","F","F","U","U","F"]   # uint32, uint8
        sizes  = ["4","4","4","4","4","4","1","4"]


    if extra.size:   data = np.hstack([points, extra.astype(np.float64)])
    else:            data = points
    ascii_lines = [" ".join(map(str, row)) for row in data]


    with open(pcd_fn, 'w') as fp:
        fp.write("# .PCD v0.7 - Point Cloud Data file format\n")
        fp.write(f"FIELDS {' '.join(fields)}\n")
        fp.write(f"SIZE   {' '.join(sizes)}\n")
        fp.write(f"TYPE   {' '.join(types)}\n")
        fp.write(f"COUNT  {' '.join(['1']*len(fields))}\n")
        fp.write(f"WIDTH  {len(points)}\n")
        fp.write("HEIGHT 1\n")
        fp.write("VIEWPOINT 0 0 0 1 0 0 0\n")
        fp.write(f"POINTS {len(points)}\n")
        fp.write("DATA ascii\n")
        fp.write("\n".join(ascii_lines))

    print(f"Saved {pcd_fn}  ({len(points)} pts, {sensor_type})")


def main(bin_fn, pcd_fn, sensor_type):
    pts, extra, _ = bin_to_pcd(bin_fn, sensor_type)
    save_to_pcd(pts, extra, sensor_type, pcd_fn)


    try:
        pcd = o3d.io.read_point_cloud(pcd_fn)
        print("open3d read OK:", pcd)
    except Exception as e:
        print("open3d read FAILED:", e)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <input.bin> <output.pcd> <sensor_type>")
        sys.exit(1)
    main(sys.argv[1], sys.argv[2], sys.argv[3])
