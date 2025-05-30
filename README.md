# HeRCULES_Pointcloud_Toolbox

 <div align="center">

<img src="https://github.com/user-attachments/assets/23b06242-baea-45d0-b941-140038ea2557" width="400" height="200"/>
<img src="https://github.com/user-attachments/assets/7557ce09-8abc-4769-9cf8-b62d103e3bf0" width="400" height="200"/>
 </div>

## What is Pointcloud Toolbox?
The HeRCULES Pointcloud Toolbox is a sophisticated software suite tailored for processing and analyzing the HeRCULES (Heterogeneous Radar Place Recognition) dataset. This toolbox offers robust functionalities for manipulating point cloud data from various range sensors, making it an essential tool for researchers in place recognition, SLAM (Simultaneous Localization and Mapping), and other related fields.

For the HeRCULES dataset, visit: [https://sites.google.com/view/herculesdataset](https://sites.google.com/view/herculesdataset).

For ROS message usage from the HeRCULES dataset, refer to: [https://github.com/hanjun815/HeRCULES_file_player](https://github.com/hanjun815/HeRCULES_file_player).

The HeRCULES_Pointcloud_Toolbox excels with two core functionalities:
- Visualization for a comprehensive graphical representation of range sensor data.
- File Handling(bin to pcd) 

## Files and Functions
1. binVisualizer.py: Visualize the bin file using open3d.
- Input: bin file from HeRCULES dataset.
- Output: visualize the 3D pointcloud via open3d.
2. bin2pcd.py: Reads .bin files from different sensors and outputs processed data in .pcd format.

## License and Citation
- When using the dataset or code, please cite our paper:
```
@INPROCEEDINGS { hjkim-2025-icra,
    AUTHOR = { Hanjun Kim and Minwoo Jung and Chiyun Noh and Sangwoo Jung and Hyunho Song and Wooseong Yang and Hyesu Jang and Ayoung Kim },
    TITLE = { HeRCULES: Heterogeneous Radar Dataset in Complex Urban Environment for Multi-session Radar SLAM },
    BOOKTITLE = { Proceedings of the IEEE International Conference on Robotics and Automation (ICRA) },
    YEAR = { 2025 },
    MONTH = { May. },
    ADDRESS = { Atlanta },
}
```

## Copyright Notice
All datasets are copyrighted by SNU RPM Labs and are distributed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 License. This license requires proper attribution to the author for any use, prohibits commercial usage, and mandates that derivative works be licensed similarly.

## Contributors
- Maintainer: Hanjun Kim (hanjun815@snu.ac.kr)
- Minwoo Jung: The original author

