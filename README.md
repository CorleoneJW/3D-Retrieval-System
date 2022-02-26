# 3D-Retrieval-System
3D Retrieval System on ModelNet40.
This is the last project of my bachelor career.

## Preview
<p>
  <span>Take a look and manipulate models.</span><br>
  <img src="https://github.com/CorleoneJW/3D-Retrieval-System/blob/main/readmesrc/library.gif" alt="Model_Library"/>
  <img src="https://github.com/CorleoneJW/3D-Retrieval-System/blob/main/readmesrc/retrieval.gif" alt="Model_Retrieve"/>
</p>

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
<img src="https://img.shields.io/badge/Three.js-0.77.1-blue" />
<img src="https://img.shields.io/badge/Django-3.1.7-blue" />
<img src="https://img.shields.io/badge/Python-3.6.13-blue" />
<img src="https://img.shields.io/badge/Pytorch-1.8.1-blue" />
<img src="https://img.shields.io/badge/Cuda-10.2.89-blue" />
<img src="https://img.shields.io/badge/Python_pcl-0.3-blue" />
</p>

## Usage
Pull down the project and install dependencies.<br>
cd data directory and run python start.py.<br>
default port:8000.<br>
```
$ python start.py
```
cd frontend and run npm run dev.<br>
default port:8081.<br>
```
$ npm run dev
```
#cd backend and run python manage.py runserver 8081(If you wanna try another port,please reset the port in frontend by yourself).<br>
```
$ python manage.py runserver 8082
```
Should prepare the data treated before.<br>
Contact me to get.<br>

## Contributor
DHU-WangJie<br>

## License
<a href="https://github.com/CorleoneJW/3D-Retrieval-System/blob/main/LICENSE">MIT License</a>
