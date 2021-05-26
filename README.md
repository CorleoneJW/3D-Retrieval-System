# 3D-Retrieval-System
3D Retrieval System on ModelNet40.
This is the last project of my bachelor career.

## Preview
![image](https://github.com/CorleoneJW/3D-Retrieval-System/blob/main/readmesrc/%E6%A8%A1%E5%9E%8B%E5%BA%93.gif)
![image](https://github.com/CorleoneJW/3D-Retrieval-System/blob/main/readmesrc/%E6%A8%A1%E5%9E%8B%E6%A3%80%E7%B4%A2.gif)

## Background
This Model Retrieval System based on the imporved Fast Hybrid Cascade NetWork.<br>
Paper:https://arxiv.org/abs/2011.04522.<br>
Faster,Stronger.<br>
该项目为基于改进后的三维物体级联分类网络的检索系统。<br>
项目基于论文:https://arxiv.org/abs/2011.04522.<br>
对一阶段与二阶段分别进行改进，提升网络整体推理速度与准确度。<br>

## Environment
<p>
<img src="https://img.shields.io/badge/Build-Success-green" />
<img src="https://img.shields.io/badge/Vue-3.0-blue" />
<img src="https://img.shields.io/badge/Django-3.1.7-blue" />
<img src="https://img.shields.io/badge/Python-3.6.13-blue" />
<img src="https://img.shields.io/badge/Pytorch-1.8.1-blue" />
<img src="https://img.shields.io/badge/Cuda-10.2.89-blue" />
</p>

## Usage
Pull down the project and install dependencies.<br>
cd data directory and run python start.py.<br>
```
$ python start.py
```
cd frontend and run npm run build.<br>
```
$ npm run build
```
#cd backend and run python manage.py runserver 8081(If you wanna try another port,please reset the port in frontend by yourself).<br>
```
$ python manage.py runserver 8081
```
Should prepare the data treated before.<br>
Contact me to get.<br>

## Contributor
DHU-WongJie<br>

## License
<a href="https://github.com/CorleoneJW/3D-Retrieval-System/blob/main/LICENSE">MIT License</a>
