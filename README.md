# 一些小工具

基于 ubuntu 20.04，Python 3.9.6 环境编写

### ffmpeg2png.py
使用ffmpeg将当前目录下所有jpg图片转换为png图片

#### 安装依赖
```shell
apt update && apt install ffmpeg python3
ffmpeg -version #查看版本
```
```shell
python3 ffmpeg2png.py
```
or
```shell
python ffmpeg2png.py
```