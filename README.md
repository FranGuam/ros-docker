# ros-docker

A Docker environment for ROS development.

Intially used for class projects of the course _Intelligent UAV Design and Implementation_ at EE Dept., Tsinghua Univ.

Current ROS version: `Noetic`

Supported Platforms: `Linux`, `Windows`, `WSL`, `macOS`(Partial)

## 使用方式

### 前提条件

- 已安装`Docker`和`Docker Compose`（官方文档：[Docker](https://docs.docker.com/get-docker/)、[Docker Compose](https://docs.docker.com/compose/install/)）
   - 如果在`WSL`中操作，还需启用`Docker Desktop`的`WSL Integration`功能（方法详见[官方文档](https://docs.docker.com/desktop/features/wsl/#enabling-docker-support-in-wsl-2-distributions)，默认是启用的）
- 已安装至少一种主流 IDE（推荐使用`VSCode`）
- 如果需要图形化界面（如`rqt_graph`,`rviz`），则要求设备平台已配备X窗口服务器
   - 对于`Linux`平台，不需要额外安装软件，但需要执行`xhost +`命令解除访问限制（每次重启后都需要执行该命令）
   - 对于`Windows`和`WSL`平台，在已安装`WSL`（`Docker Desktop`会自动安装）的前提下，需要在`WSL Settings`中开启`可选功能->启用GUI应用程序`选项
   - 对于`macOS`平台，可以使用`XQuartz`（配置方法见下），但由于其`GLX`版本限制无法运行部分使用`OpenGL`的应用（包括`rviz`、`gazebo`）。如果有使用这些应用的需求，可以安装同类X窗口服务器（需要用户自行寻找，可能比较艰难，但如果你找到了合适的，请务必告诉我）或使用`noVNC`解决方案（下一条）
   - 对于任何平台，均可以使用`noVNC`解决方案，选择`docker-compose.novnc.yml`即可。按下面的流程构建容器后，如果运行了有图形化界面的应用，则打开浏览器访问`http://localhost:8080`并点击连接就可以看到，不需要额外安装软件。此方案的缺点在于浏览器内显示的其实是一个远程桌面，宽高无法实时调整，本机应用与`docker`内应用也不能无缝切换
 
#### 安装 XQuartz

1. 从[官网](https://www.xquartz.org/index.html)下载`.pkg`包并安装，或使用`Homebrew`安装：

   ```bash
   brew install --cask xquartz
   ```

2. 安装好后，在`Launchpad`中找到并启动应用，或使用如下命令启动：

   ```bash
   open -a XQuartz
   ```

3. 在`macOS`的顶栏找到`设置/首选项`，点开后找到`安全选项卡`，勾选`允许来自网络客户端的连接`
4. 重启电脑（登出账号再登入或许已经足够，但重启也不会花你太多时间）
5. 在终端里执行：

   ```bash
   xhost +
   ```

   > 注：之后每次重启电脑后都需要执行该命令

### 方法一：使用 DevContainer（开箱即用）

1. 根据设备平台，选择对应的`docker-compose.{Platform}.yml`文件填入`devcontainer.json`中的`dockerComposeFile`。

   > 注意：这里的设备平台指的是代码/终端所在的位置，如果你的代码文件夹已经在某个`WSL`分发版本（如`Ubuntu`）的虚拟磁盘中，且已经使用`VSCode`的`Connect to WSL`功能打开，那么应该选择`docker-compose.wsl.yml`

2. 使用`VSCode`打开项目文件夹，点击左下角绿色图标，在正上方弹出的菜单中选择`Reopen in Container`即可。

   > 如果没有找到`Reopen in Container`选项，说明`VSCode`还没有安装`Dev Containers`插件，可以点击正上方弹出菜单中的`Dev Container`选项自动安装，或在插件市场中自行安装

3. 等待`VSCode`下载镜像并构建容器，完成后会自动进入容器中，可以在`VSCode`的终端中执行`ros`命令，不需要使用`roscore`命令启动`ROS`。默认配置下，你的代码文件夹会被映射到容器中的`/workspace`目录下，开启新终端时会自动进入该目录。

   > 如果下载镜像的过程中出现网络问题，可以尝试更换 Docker 镜像源（方法请自行上网查询）或使用本仓库的构建的镜像（方法见下）

   > 你可以使用`rostopic list`测试`ROS`环境是否正常运行（需要在`VSCode`内新建终端并执行命令，不要在本机的终端内执行），如果输出没有报错，那么说明环境配置成功
   
   > 你可以使用`rqt_graph`测试`GUI`应用是否能正常显示，如果看到有窗口弹出，说明环境配置成功

### 方法二：手动启动 Docker 容器并连接

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

   > 你可以使用`rostopic list`测试`ROS`环境是否正常运行（需要在`VSCode`内新建终端并执行命令，不要在本机的终端内执行），如果输出没有报错，那么说明环境配置成功
   
   > 你可以使用`rqt_graph`测试`GUI`应用是否能正常显示，如果看到有窗口弹出，说明环境配置成功

4. 你也可以使用`VSCode`的`Attach to Running Container`功能连接到容器（与使用 DevContainer 体验相同）。

### 使用本仓库构建的镜像

根据设备平台，选择对应的`docker-compose.{Platform}.yml`文件，修改其中的`build`字段，改为`image`字段，示例如下：

```diff
- build:
-   context: .
-   dockerfile: Dockerfile
+ image: ghcr.io/franguam/ros-docker
```

之后，重新按照“使用 DevContainer”或“手动启动 Docker 容器并连接”部分所述的步骤操作即可。

> 本仓库构建的镜像并不会定期更新，建议用户搭建环境完成后升级全部依赖（`apt upgrade`）

## 实用命令

### 批量修改文件权限

```bash
find -name *.py -print -exec chmod +x {} \;
```

### 允许 GUI 应用（解除访问限制）

```bash
xhost +
```

### 后台运行命令

```bash
<command> &
```
