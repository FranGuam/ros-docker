# Tello 无人机相关资源

这个文件夹中包含了

- `./docs/`：Tello 无人机说明书、SDK 文档、定位毯说明书
- `./h264decoder/`: 一个开源的 Python H264 视频流解码器，可用于解码无人机传回的视频流
- `./demo/`: 一个可用于控制 Tello 无人机的最小 Demo

### Demo 使用说明

1. 安装 h264decoder

   ```bash
   cd ./h264decoder/
   pip install .
   ```

2. 修改 Demo 中执行的任务

   `control.py`中提供了 3 个示例函数，其中`test_base_class()`和`test_ros_class()`均会查看无人机基本参数、控制无人机起飞、截取无人机摄像头拍摄的一帧图像并显示、控制无人机降落，差异是`test_ros_class()`会向 ROS 发布无人机的状态流和视频流，可用`rviz`查看；`test_state()`则会实时打印无人机的状态，以供调试的方便。请按需选择函数并解注。

3. 运行 Demo

   ```bash
   cd ./demo/
   python control.py
   ```
