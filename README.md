# ros-docker

A Docker environment for ROS development.

Intially used for class projects of the course _Intelligent UAV Design and Implementation_

Current ROS version: `Noetic`

Supported Platforms: `Linux`, `Windows`, `WSL`

### 使用方式

##### 前提条件

- 设备平台符合要求（暂不支持`macOS`）
- 已安装`Docker`和`Docker Compose`（官方文档：[Docker](https://docs.docker.com/get-docker/)、[Docker Compose](https://docs.docker.com/compose/install/)）
   - 如果在`WSL`中操作，还需启用`Docker Desktop`的`WSL Integration`功能（方法详见[官方文档](https://docs.docker.com/desktop/features/wsl/#enabling-docker-support-in-wsl-2-distributions)）
- 已安装至少一种主流 IDE（推荐使用`VSCode`）

##### 使用 DevContainer（开箱即用）

1. 根据设备平台，选择对应的`docker-compose.{Platform}.yml`文件填入`devcontainer.json`中的`dockerComposeFile`。

   > 注意：这里的设备平台指的是代码/终端所在的位置，如果你的代码文件夹已经在某个`WSL`分发版本（如`Ubuntu`）的虚拟磁盘中，且已经使用`VSCode`的`Connect to WSL`功能打开，那么应该选择`docker-compose.wsl.yml`

2. 使用`VSCode`打开项目文件夹，点击左下角绿色图标，在正上方弹出的菜单中选择`Reopen in Container`即可。

   > 如果没有找到`Reopen in Container`选项，说明`VSCode`还没有安装`Dev Containers`插件，可以点击正上方弹出菜单中的`Dev Container`选项自动安装，或在插件市场中自行安装

3. 等待`VSCode`下载镜像并构建容器，完成后会自动进入容器中，可以在`VSCode`的终端中执行`ros`命令，不需要使用`roscore`命令启动`ROS`。默认配置下，你的代码文件夹会被映射到容器中的`/workspace`目录下，开启新终端时会自动进入该目录。

   > 如果下载镜像的过程中出现网络问题，可以尝试更换 Docker 镜像源（方法请自行上网查询）或使用本仓库的构建的镜像（方法见下）

   > 你可以使用`rosrun turtlesim turtlesim_node`测试`ROS`环境是否正常运行，如果看到乌龟窗口弹出，说明环境配置成功。在`Linux`平台下，你可能需要使用`xhost +`命令允许 GUI 应用。

##### 手动启动 Docker 容器并连接

1. 根据设备平台，选择对应的`docker-compose.{Platform}.yml`文件，修改其中的`volumes`字段，添加一个条目将项目文件夹映射到容器中，示例如下：

   > 注意：这里的设备平台指的是代码/终端所在的位置，如果你的代码文件夹已经在某个`WSL`分发版本（如`Ubuntu`）的虚拟磁盘中，且计划使用`WSL`终端执行以下命令，那么应该选择`docker-compose.wsl.yml`

   ```yaml
   volumes:
     - ../:/workspace
   ```

   > 注意：这里的`/workspace`是容器中的目录，可以根据需要修改。

2. 执行以下命令启动容器。

   ```bash
   cd ./.devcontainer/
   docker compose -f docker-compose.{Platform}.yml up -d
   ```

3. 等待镜像下载和容器构建。完成后，可以使用以下命令进入容器并执行`ros`命令（不需要使用`roscore`命令启动`ROS`）。

   > 如果下载镜像的过程中出现网络问题，可以尝试更换 Docker 镜像源（方法请自行上网查询）或使用本仓库的构建的镜像（方法见下）

   ```bash
   docker exec -it ros bash
   ```

   > 你可以使用`rosrun turtlesim turtlesim_node`测试`ROS`环境是否正常运行，如果看到乌龟窗口弹出，说明环境配置成功。在`Linux`平台下，你可能需要使用`xhost +`命令允许 GUI 应用。

4. 你也可以使用`VSCode`的`Attach to Running Container`功能连接到容器（与使用 DevContainer 体验相同）。

##### 使用本仓库构建的镜像

根据设备平台，选择对应的`docker-compose.{Platform}.yml`文件，修改其中的`build`字段，改为`image`字段，示例如下：

```diff
- build:
-   context: .
-   dockerfile: Dockerfile
+ image: ghcr.io/franguam/ros-docker
```

之后，重新按照“使用 DevContainer”或“手动启动 Docker 容器并连接”部分所述的步骤操作即可。

> 本仓库构建的镜像并不会定期更新，建议用户搭建环境完成后升级全部依赖（`apt upgrade`）

### 实用命令

##### 批量修改文件权限

```bash
find -name *.py -print -exec chmod +x {} \;
```

##### [Linux] 允许 GUI 应用

```bash
xhost +
```

##### 后台运行命令

```bash
<command> &
```
