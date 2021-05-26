{% csrf_token %}
<template>
  <div>
    <el-row style="margin-bottom: 0px">
      <el-col :span="6">
        <el-row>
          <div class="uploadModelDiv" id="uploadDiv" style="border: 1px dashed"></div>
        </el-row>
        <el-row>
          <div style="margin-bottom: 5px">
          <span>注:只能上传npy与ply文件，上传npy文件使用检索</span>
          </div>
          <el-upload
          action="string"
          accept=".ply,.npy"
          ref="upload"
          :before-upload="onBeforeUploadPly"
          :on-change="fileChange"
          :http-request="nullfunction"
          :auto-upload="true"
          :file-list="fileList"
          :limit="1"
          style="display: flex;justify-content: center;align-items: center"
          >
          <el-button size="small" type="primary">点击上传</el-button>
          </el-upload>
          <el-button size="small" type="primary" @click="startRetrieval" style="margin-top: 1%">检索</el-button>
        </el-row>
      </el-col>
      <el-col :span="18">
        <el-row style="margin-bottom: 0px">
          <el-col :span="8">
          <h1 style="margin-top: 1px;float:left;">⭐{{currentCategory}}</h1>
          </el-col>
          <el-col :span="16" >
          <el-radio-group @change="changeSet" v-model="radio" style="float: right">
            <el-radio-button label="训练集"></el-radio-button>
            <el-radio-button label="测试集"></el-radio-button>
          </el-radio-group>
          </el-col>
        </el-row>
        <el-row style="margin-bottom: 0px">
          <el-row :gutter="20" id="libRow0">
<!--            第一行-->
            <el-dialog
              title="详情"
              :visible.sync="dialogVisible"
              width="700px" @close="detailClose">
              <div id="detailContainer" class="detailModelDiv" style="margin-left: 5%"></div>
              <span slot="footer" class="dialog-footer">
                <el-button type="primary"><a :href="downloadNpyHttp" download="" title="下载" style="color: white">下载npy</a></el-button>
                <el-button type="primary"><a :href="downloadPlyHttp" download="" title="下载" style="color: white">下载ply</a></el-button>
                <el-button type="primary" @click="dialogVisible = false">返 回</el-button>
              </span>
            </el-dialog>
            <el-col :span="6" id="col0">
            <el-card :body-style="{ padding: '0px' }" class="modelCard" shadow="hover">
              <div id="container0" class="modelDiv"></div>
              <div>
                <span id="span0" style="float:left;margin-top:10px"></span>
                <el-button type="primary" style="float: right;margin-top: 0px" @click="showDetails(0)">查看详情</el-button>
              </div>
            </el-card>
            </el-col>
            <el-col :span="6" id="col1">
            <el-card :body-style="{ padding: '0px' }" class="modelCard" shadow="hover">
              <div id="container1" class="modelDiv"></div>
              <div>
                <span id="span1" style="float:left;margin-top:10px"></span>
                <el-button type="primary" style="float:right;margin-top: 0px" @click="showDetails(1)">查看详情</el-button>
              </div>
            </el-card>
            </el-col>
            <el-col :span="6" id="col2">
            <el-card :body-style="{ padding: '0px' }" class="modelCard" shadow="hover">
              <div id="container2" class="modelDiv"></div>
              <div>
                <span id="span2" style="float:left;margin-top:10px"></span>
                <el-button type="primary" style="float:right;margin-top: 0px" @click="showDetails(2)">查看详情</el-button>
              </div>
            </el-card>
            </el-col>
            <el-col :span="6" id="col3">
            <el-card :body-style="{ padding: '0px' }" class="modelCard" shadow="hover">
              <div id="container3" class="modelDiv"></div>
              <div>
                <span id="span3" style="float:left;margin-top:10px"></span>
                <el-button type="primary" style="float:right;margin-top: 0px" @click="showDetails(3)">查看详情</el-button>
              </div>
            </el-card>
            </el-col>
          </el-row>
          <el-row :gutter="20" id="libRow1">
<!--            第二行-->
            <el-col :span="6" id="col4">
            <el-card :body-style="{ padding: '0px' }" class="modelCard" shadow="hover">
              <div id="container4" class="modelDiv"></div>
              <div>
                <span id="span4" style="float:left;margin-top:10px"></span>
                <el-button type="primary" style="float: right;margin-top: 0px" @click="showDetails(4)">查看详情</el-button>
              </div>
            </el-card>
            </el-col>
            <el-col :span="6" id="col5">
            <el-card :body-style="{ padding: '0px' }" class="modelCard" shadow="hover">
              <div id="container5" class="modelDiv"></div>
              <div>
                <span id="span5" style="float:left;margin-top:10px"></span>
                <el-button type="primary" style="float:right;margin-top: 0px" @click="showDetails(5)">查看详情</el-button>
              </div>
            </el-card>
            </el-col>
            <el-col :span="6" id="col6">
            <el-card :body-style="{ padding: '0px' }" class="modelCard" shadow="hover">
              <div id="container6" class="modelDiv"></div>
              <div>
                <span id="span6" style="float:left;margin-top:10px"></span>
                <el-button type="primary" style="float:right;margin-top: 0px" @click="showDetails(6)">查看详情</el-button>
              </div>
            </el-card>
            </el-col>
            <el-col :span="6" id="col7">
            <el-card :body-style="{ padding: '0px' }" class="modelCard" shadow="hover">
              <div id="container7" class="modelDiv"></div>
              <div>
                <span id="span7" style="float:left;margin-top:10px"></span>
                <el-button type="primary" style="float:right;margin-top: 0px" @click="showDetails(7)">查看详情</el-button>
              </div>
            </el-card>
            </el-col>
          </el-row>
        </el-row>
        <el-row style="margin-top: 5px;margin-bottom: 0px">
          <el-pagination background background layout="total,prev, pager, next,jumper" :total="libNum" :page-size="singleNum" @current-change="libpageChange" :current-page.sync="libPage"></el-pagination>
        </el-row>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import Vue from 'vue';
import * as THREE from 'three';
import {PLYLoader} from "three/examples/jsm/loaders/PLYLoader";
import Stats from "three/examples/jsm/libs/stats.module";
import { TrackballControls } from 'three/examples/jsm/controls/TrackballControls.js';
import axios from "axios";
export default {
  name: "All",
  data() {
    return {
      totalCategories: ["airplane", "bathtub", "bed", "bench", "bookshelf", "bottle", "bowl", "car", "chair", "cone", "cup", "curtain", "desk", "door", "dresser", "flower_pot", "glass_box", "guitar", "keyboard",
        "lamp", "laptop", "mantel", "monitor", "night_stand", "person", "piano", "plant", "radio", "range_hood", "sink", "sofa", "stairs", "stool", "table", "tent", "toilet", "tv_stand", "vase", "wardrobe", "xbox"],
      categoryNum_train: [626, 106, 515, 173, 572, 335, 64, 197, 889, 167, 79, 138, 200, 109, 200, 149, 171, 155, 145, 124, 149, 284, 465, 200, 88, 231, 240, 104, 115, 128, 680, 124, 90, 392, 163, 344, 267, 475, 87, 103],
      categoryNum_test: [100, 50, 100, 20, 100, 100, 20, 100, 100, 20, 20, 20, 86, 20, 86, 20, 100, 100, 20, 20, 20, 100, 100, 86, 20, 100, 100, 20, 100, 20, 100, 20, 20, 100, 20, 100, 100, 100, 20, 20],
      currentCategory: "airplane",    //当前种类，默认为飞机
      libPage: 1,      //检索库当前页数，默认第一页
      libNum: 626,      //检索库当前类总数，默认为飞机
      singleNum: 8,    //检索库每页显示数量
      currentModelnum:8,  //当前页面显示数量
      train: true,     //判断训练集还是测试集
      container:[],     //容器
      camera: [],      //相机变量
      cameraTarget: [],  //相机目标坐标变量
      scene: [],         //场景
      loader: [],        //加载器
      material: [],      //材质
      mesh: [],          //mesh
      light: [],         //灯光
      renderer:[],       //渲染器
      controls:[],      //控制器
      detailContainer:null,   //详情页容器
      detailCamera:null,      //详情页摄像机
      detailCameraTarget:null,    //详情页目标坐标
      detailScene:null,       //详情页场景
      detailLoader:null,    //详情页加载器
      detailMaterial:null,   //详情页材质
      detailMesh:null,      //详情页mesh
      detailLight:null,     //详情页灯光
      detailRenderer:null,    //详情页渲染器
      detailControls:null,    //详情页控制器
      dialogVisible:false,    //dialog是否展示控制,
      radio:"训练集",          //选择训练集还是测试集的radio
      fileList:[],          //作为上传文件的存储List
      uploadContainer:null,     //上传容器
      uploadCamera:null,      //上传摄像机
      uploadCameraTarget:null,     //上传目标坐标
      uploadScene:null,       //上传场景
      uploadLoader:null,    //上传加载器
      uploadMaterial:null,    //上传材质
      uploadMesh:null,      //上传mesh
      uploadLight:null,     //上传灯光
      uploadRenderer:null,    //上传渲染器
      downloadPlyHttp:null,      //下载ply模型地址
      downloadNpyHttp:null,      //下载npy模型地址
    };
  },
  methods: {
      pad(num,n){
          //num为传入正整数，n为补零后位数
          let len = num.toString().length;
          while(len<n){
            num = "0"+num;
            len++;
          }
          return num;
      },
      init: function (divId="null",category="null",state="null",serial=1,modelIndex=1) {
          //初始化对应的相机、场景、辅助和渲染器、模型等
          this.container[modelIndex] = document.getElementById(divId);

          //camera
          this.camera[modelIndex] = new THREE.PerspectiveCamera( 75, this.container[modelIndex].clientWidth / this.container[modelIndex].clientHeight, 0.1, 1000 );

          this.cameraTarget[modelIndex] = new THREE.Vector3( 0, 0, 0 );

          //scene
          this.scene[modelIndex] = new THREE.Scene();
          this.scene[modelIndex].background = new THREE.Color( 0x000000 );
          this.scene[modelIndex].fog = new THREE.Fog( 0x72645b, 2, 15 );

          // PLY file
          let plystr = 'http://127.0.0.1:8000/'+category+'/'+state+'/'+category+'_'+this.pad(serial,4)+'.ply';
          // console.log("plyaddress"+modelIndex,plystr)
          this.loader[modelIndex] = new PLYLoader();
          this.loader[modelIndex].load( plystr, (geometry)=>{
                // console.log("geometry"+modelIndex,geometry);
                geometry.computeVertexNormals();
                this.material[modelIndex] = new THREE.MeshStandardMaterial({ color: 0x0055ff, flatShading: true });
                this.mesh[modelIndex] = new THREE.Mesh( geometry, this.material[modelIndex] );
                this.mesh[modelIndex].position.set(0,0,0);
                this.mesh[modelIndex].scale.multiplyScalar( 5 );
                this.mesh[modelIndex].castShadow = true;
                this.mesh[modelIndex].receiveShadow = true;
                this.scene[modelIndex].add( this.mesh[modelIndex] );
          } );

          //red:x,green:y,blue:z
          this.camera[modelIndex].position.set(5,5,5);
          this.camera[modelIndex].up.set(0,0,1);

          //light
          this.light[modelIndex] = new THREE.HemisphereLight( 0x443333, 0x111122 );
          this.scene[modelIndex].add(this.light[modelIndex]);
          this.addShadowedLight(5,5,5,0xffffff,1.35,modelIndex);
          this.addShadowedLight(2.5,5,-5,0xffaa00,1,modelIndex);

          //helper
          // let plane = new THREE.Plane(new THREE.Vector3(0, 0, 1))
          // let planeHelper = new THREE.PlaneHelper(plane,10, 0xffffff);
          // let axesHelper = new THREE.AxesHelper(10);
          // axesHelper.position.set(0,0,0);
          // this.scene[modelIndex].add(axesHelper);
          // this.scene[modelIndex].add(planeHelper);

          // renderer
          this.renderer[modelIndex] = new THREE.WebGLRenderer( { antialias: true } );
          // this.renderer.setPixelRatio( window.devicePixelRatio );
          this.renderer[modelIndex].setSize( this.container[modelIndex].clientWidth, this.container[modelIndex].clientHeight);
          this.renderer[modelIndex].outputEncoding = THREE.sRGBEncoding;
          this.container[modelIndex].appendChild( this.renderer[modelIndex].domElement );

          // stats

          // let stats = new Stats();
          // container.appendChild( stats.dom );

          //control
          // this.controls[modelIndex] = new TrackballControls( this.camera[modelIndex], this.renderer[modelIndex].domElement );
          // this.controls[modelIndex].minDistance = 0.1;
          // this.controls[modelIndex].maxDistance = 1000;

      },
      animate() {
          //调用渲染、控制状态等
          this.render();
          //更新控制器
          // for(let i = 0;i<this.currentModelnum;i++){
          //     // this.stats.update();    //更新状态
          //     this.controls[i].update();
          // }

          //旋转
        	const timer = Date.now() * 0.0005;
        	for(let i = 0;i<this.currentModelnum;i++){
             this.camera[i].position.x = Math.sin( timer ) * 5;
             this.camera[i].position.z = Math.cos( timer ) * 5;
          }
          requestAnimationFrame( this.animate );
      },
      render() {
          //渲染相机
          for(let i=0;i<this.currentModelnum;i++){
              this.camera[i].lookAt( this.cameraTarget[i] );      //设置相机对准坐标
              this.renderer[i].render( this.scene[i], this.camera[i] );      //渲染
          }
      },
      addShadowedLight( x, y, z, color, intensity, modelIndex) {

				const directionalLight = new THREE.DirectionalLight( color, intensity );
				directionalLight.position.set( x, y, z );
				this.scene[modelIndex].add( directionalLight );

				directionalLight.castShadow = true;

				const d = 1;
				directionalLight.shadow.camera.left = - d;
				directionalLight.shadow.camera.right = d;
				directionalLight.shadow.camera.top = d;
				directionalLight.shadow.camera.bottom = - d;

				directionalLight.shadow.camera.near = 1;
				directionalLight.shadow.camera.far = 4;

				directionalLight.shadow.mapSize.width = 1024;
				directionalLight.shadow.mapSize.height = 1024;

				directionalLight.shadow.bias = - 0.001;

			},
      addDetailShadowedLight( x, y, z, color, intensity) {

				const directionalLight = new THREE.DirectionalLight( color, intensity );
				directionalLight.position.set( x, y, z );
				this.detailScene.add( directionalLight );

				directionalLight.castShadow = true;

				const d = 1;
				directionalLight.shadow.camera.left = - d;
				directionalLight.shadow.camera.right = d;
				directionalLight.shadow.camera.top = d;
				directionalLight.shadow.camera.bottom = - d;

				directionalLight.shadow.camera.near = 1;
				directionalLight.shadow.camera.far = 4;

				directionalLight.shadow.mapSize.width = 1024;
				directionalLight.shadow.mapSize.height = 1024;

				directionalLight.shadow.bias = - 0.001;

			},
      loadModel(){
          //初始所有模型div
          for(let i = 0;i<this.singleNum;i++){
            document.getElementById('container'+i).innerHTML='';
            document.getElementById('col'+i).style.display = "block";
          }
          //初始化两行模型div
          // document.getElementById('libRow0').innerHTML = '';
          // document.getElementById('libRow1').innerHTML = '';
          //判断是训练集还是测试集
          let showState = 'train';
          if(this.train==true){   //判断为训练集
              this.libNum = this.categoryNum_train[this.totalCategories.indexOf(this.currentCategory)];
              showState = 'train';
          }
          else if(this.train==false){    //判断为测试集
              this.libNum = this.categoryNum_test[this.totalCategories.indexOf(this.currentCategory)];
              showState = 'test';
          }
          //获得当前页面该显示多少模型，currentModelnum来控制
          if(this.libPage==Math.ceil(this.libNum/this.singleNum)){   //如果是最后一页，会改变当前页面显示数量
            this.currentModelnum = this.libNum%this.singleNum;
            //当刚好满足最后一页个数为singleNum,要变为singleNum,否则会少显示一页的数据
            if(this.currentModelnum == 0){
              this.currentModelnum = this.singleNum;
            }
            //如果不等于8，那就会隐藏一部分div
            if(this.currentModelnum!=this.singleNum){
              for(let j = this.currentModelnum;j<this.singleNum;j++){
                document.getElementById('col'+j).style.display = "none";    //将内部html清空
              }
            }
          }else{
            this.currentModelnum = this.singleNum;
          }
          //动态添加模型div
          // console.log("currentModelnum",this.currentModelnum);
          // for(let i = 0;i<this.currentModelnum;i++){
          //     let addStr = '<el-col :span="6">' +
          //           '<el-card :body-style="{ padding: \'0px\' }" class="modelCard" shadow="hover">' +
          //           '<div id="container'+i+'" class="modelDiv"></div>' +
          //           '<div>' +
          //           '<span id="span'+i+'" style="float:left;margin-top:15px"></span>' +
          //           '<el-button type="primary" style="float: right;margin-top: 5px">查看详情</el-button>' +
          //           '</div>' +
          //           '</el-card>' +
          //           '</el-col>';
          //     if(i<4) {
          //           document.getElementById('libRow0').innerHTML = document.getElementById('libRow0').innerHTML + addStr;
          //     }else if(i>=4&&i<8){
          //           document.getElementById('libRow1').innerHTML = document.getElementById('libRow1').innerHTML + addStr;
          //     }
          // }
          // console.log('Row0',document.getElementById('libRow0').innerHTML);
          // console.log('Row1',document.getElementById('libRow1').innerHTML);

          //渲染新的模型
          let startIndex = ((this.libPage-1)*this.singleNum)+1;   //当前页面开始的第一个样本序号
          if(this.train==false){
            startIndex += this.categoryNum_train[this.totalCategories.indexOf(this.currentCategory)];
          }
          for(let i=0;i<this.currentModelnum;i++){
              this.init('container'+i,this.currentCategory,showState,startIndex+i,i);
              document.getElementById('span'+i).innerHTML=this.currentCategory+'_'+this.pad(startIndex+i,4)+'.ply';
          }
          //添加渲染，动画效果
          this.animate();
      },
      libpageChange(){
        for(let i = 0 ;i<this.singleNum;i++){
          this.renderer[i].forceContextLoss();
          // this.renderer[i] = null;
        }
        this.loadModel()
      },
      showDetails(modelIndex){
        this.dialogVisible=true;
        setTimeout(()=>{
          this.detailContainer = document.getElementById('detailContainer');
        let detailIndex = ((this.libPage-1)*this.singleNum)+modelIndex+1;   //获取对应序号
        if(this.train == false){
          detailIndex += this.categoryNum_train[this.totalCategories.indexOf(this.currentCategory)];
        }
        let showState=null;
        if(this.train==true){
          showState = 'train';
        }else if(this.train==false){
          showState = 'test'
        }
        //camera
        this.detailCamera = new THREE.PerspectiveCamera( 75, 600 / 600, 0.1, 1000 );
        this.detailCameraTarget = new THREE.Vector3( 0, 0, 0 );
        //scene
        this.detailScene = new THREE.Scene();
        this.detailScene.background = new THREE.Color( 0x000000 );
        this.detailScene.fog = new THREE.Fog( 0x72645b, 2, 15 );
        // PLY file
          let plystr = 'http://127.0.0.1:8000/'+this.currentCategory+'/'+showState+'/'+this.currentCategory+'_'+this.pad(detailIndex,4)+'.ply';
          // console.log("plyaddress"+modelIndex,plystr)
          let npystr = 'http://127.0.0.1:8000/'+'afterTreat/'+showState+'/'+this.pad(this.totalCategories.indexOf(this.currentCategory)+1,3)+'.'
          +this.currentCategory+'_'+this.pad(detailIndex,9)+'.npy';
          this.downloadPlyHttp = plystr;
          this.downloadNpyHttp = npystr;
          this.detailLoader = new PLYLoader();
          this.detailLoader.load( plystr, (geometry)=>{
                // console.log("geometry"+modelIndex,geometry);
                geometry.computeVertexNormals();
                this.detailMaterial = new THREE.MeshStandardMaterial({ color: 0x0055ff, flatShading: true });
                this.detailMesh = new THREE.Mesh( geometry, this.detailMaterial );
                this.detailMesh.position.set(0,0,0);
                this.detailMesh.scale.multiplyScalar( 5 );
                this.detailMesh.castShadow = true;
                this.detailMesh.receiveShadow = true;
                this.detailScene.add( this.detailMesh );
          } );

          //camera position and up to
          this.detailCamera.position.set(5,5,5);
          this.detailCamera.up.set(0,0,1);

          //light
          this.detailLight = new THREE.HemisphereLight( 0x443333, 0x111122 );
          this.detailScene.add(this.detailLight);
          this.addDetailShadowedLight(5,5,5,0xffffff,1.35);
          this.addDetailShadowedLight(2.5,5,-5,0xffaa00,1);

          //helper
          let plane = new THREE.Plane(new THREE.Vector3(0, 0, 1))
          let planeHelper = new THREE.PlaneHelper(plane,10, 0xffffff);
          let axesHelper = new THREE.AxesHelper(10);
          axesHelper.position.set(0,0,0);
          this.detailScene.add(axesHelper);
          this.detailScene.add(planeHelper);

          //renderer
          this.detailRenderer = new THREE.WebGLRenderer( { antialias: true } );
          this.detailRenderer.setSize( 600, 600);
          this.detailRenderer.outputEncoding = THREE.sRGBEncoding;
          this.detailContainer.appendChild( this.detailRenderer.domElement );


          //control
          this.detailControls = new TrackballControls( this.detailCamera, this.detailRenderer.domElement );
          this.detailControls.minDistance = 0.1;
          this.detailControls.maxDistance = 1000;

          //渲染，动画效果
          this.detailAnimate();
          },0)
      },
      detailAnimate(){
        this.detailRender();
        this.detailControls.update();
        requestAnimationFrame(this.detailAnimate);
      },
      detailRender(){
        this.detailCamera.lookAt(this.detailCameraTarget);
        this.detailRenderer.render(this.detailScene,this.detailCamera);
      },
      detailClose(){
          //退出dialog清空内容
          this.detailContainer.innerHTML = '';
          this.detailRenderer.forceContextLoss(); //去除webgl上下文
      },
      changeSet(label){
        if(label=="训练集"){
          this.train = true;
          this.libPage = 1;
          this.libpageChange();
        }else if(label=="测试集"){
          this.train = false;
          this.libPage = 1;
          this.libpageChange();
        }
      },
      onBeforeUploadPly(file){
          return new Promise((resolve, reject) => {
            const isPly = this.judegePly(file.name);
            const isNpy = this.judegeNpy(file.name);
            if(!isPly&&!isNpy){
              this.$message.error('上传文件只能是npy或ply格式!');
              return reject(false)
            }
            else
            {
              return resolve(true)
            }
            });
      },
      uploadPly(fileName,fileRaw){
          // console.log("upload:")
          // console.log("fileRaw:",fileRaw)
          const formData = new FormData();
          formData.append('file',fileRaw);
          // console.log('formData',formData);
          let config = { // 配置请求头
            headers: {'Content-Type': 'multipart/form-data'}
          }
          this.$axios.post("http://127.0.0.1:8082/test/Result/",formData,config).then(response=>{
            // console.log("responsedata:",response.data);
            this.currentCategory = this.totalCategories[response.data.category];
            this.train = true;
            this.libPage = 1;
            this.libpageChange();
          })
      },
      startRetrieval(){
          // console.log("file url",this.fileList[0].url)
          this.uploadPly(this.fileList[0].name,this.fileList[0].raw)
      },
      nullfunction(){

      },
      fileChange(file){
          this.$refs.upload.clearFiles();
          document.getElementById('uploadDiv').innerHTML = '';
          this.fileList = [{name: file.name,url:URL.createObjectURL(file.raw),raw:file.raw}];
          this.uploadModelShow(file);
      },
      judegePly(name){
          //判断是否是ply文件
          let fileName = name.substring(name.lastIndexOf('.')+1);
          let isPly = fileName === 'ply';
          return isPly;
      },
      judegeNpy(name){
          //判断是否是npy文件
          let fileName = name.substring(name.lastIndexOf('.')+1);
          let isNpy = fileName === 'npy';
          return isNpy;
      },
      npy2plyModel(name){
          const fileRegex = /^[0-9]{3}./;   //正则判断是否符合需要转换的模式，不是所有npy都可以
          if(fileRegex.test(name)){
              //获得文件种类与编号等属性
              let fileName = name.substring(4,name.lastIndexOf('.'));   //获得中间种类与标号信息
              let category = fileName.substring(0,fileName.lastIndexOf('_'));
              let serial = fileName.substring(fileName.lastIndexOf('0')+1);
              //获得文件为训练集还是测试集
              let showState = '';
              if(parseInt(serial)<=this.categoryNum_train[this.totalCategories.indexOf(category)]) {  //若数字大于该样本训练集样本数，则为测试集
                  showState = 'train';
              }else {
                showState = 'test'
              }
              //合成点云文件地址
              let plystr = 'http://127.0.0.1:8000/'+category+'/'+showState+'/'+category+'_'+this.pad(parseInt(serial),4)+'.ply';
              // console.log('plystr',plystr)
              return plystr
          }
          else{
            return ''
          }
      },
      uploadModelShow(file){
          this.uploadContainer = document.getElementById('uploadDiv');
          //camera
          this.uploadCamera = new THREE.PerspectiveCamera( 75, 350 / 350, 0.1, 1000 );
          this.uploadCameraTarget = new THREE.Vector3( 0, 0, 0 );
          //scene
          this.uploadScene = new THREE.Scene();
          this.uploadScene.background = new THREE.Color( 0x000000 );
          this.uploadScene.fog = new THREE.Fog( 0x72645b, 2, 15 );
          //PLY file
          this.uploadLoader = new PLYLoader();
          let objectUrl = '';
          if(this.judegeNpy(file.name)){   //判断文件格式是否为npy
            objectUrl = this.npy2plyModel(file.name);
          }
          else if(this.judegePly(file.name)){   //判断文件格式是否为ply
            objectUrl = URL.createObjectURL(file.raw);
          }
          this.uploadLoader.load( objectUrl, (geometry)=>{
                // console.log("geometry",geometry);
                geometry.computeVertexNormals();
                this.uploadMaterial = new THREE.MeshStandardMaterial({ color: 0x0055ff, flatShading: true });
                this.uploadMesh = new THREE.Mesh( geometry, this.uploadMaterial );
                this.uploadMesh.position.set(0,0,0);
                this.uploadMesh.scale.multiplyScalar( 5 );
                this.uploadMesh.castShadow = true;
                this.uploadMesh.receiveShadow = true;
                this.uploadScene.add( this.uploadMesh );
          } );

          //camera position and up to
          this.uploadCamera.position.set(5,5,5);
          this.uploadCamera.up.set(0,0,1);

          //light
          this.uploadLight = new THREE.HemisphereLight( 0x443333, 0x111122 );
          this.uploadScene.add(this.uploadLight);
          this.addUploadShadowedLight(5,5,5,0xffffff,1.35);
          this.addUploadShadowedLight(2.5,5,-5,0xffaa00,1);

          //renderer
          this.uploadRenderer = new THREE.WebGLRenderer( { antialias: true } );
          this.uploadRenderer.setSize( 350, 350);
          this.uploadRenderer.outputEncoding = THREE.sRGBEncoding;
          this.uploadContainer.appendChild( this.uploadRenderer.domElement );

          //animate
          this.uploadAnimate();

      },
      addUploadShadowedLight( x, y, z, color, intensity) {

          const directionalLight = new THREE.DirectionalLight( color, intensity );
          directionalLight.position.set( x, y, z );
          this.uploadScene.add( directionalLight );

          directionalLight.castShadow = true;

          const d = 1;
          directionalLight.shadow.camera.left = - d;
          directionalLight.shadow.camera.right = d;
          directionalLight.shadow.camera.top = d;
          directionalLight.shadow.camera.bottom = - d;

          directionalLight.shadow.camera.near = 1;
          directionalLight.shadow.camera.far = 4;

          directionalLight.shadow.mapSize.width = 1024;
          directionalLight.shadow.mapSize.height = 1024;

          directionalLight.shadow.bias = - 0.001;

        },
      uploadAnimate(){
          this.uploadRender();
          const timer = Date.now() * 0.0005;
          this.uploadCamera.position.x = Math.sin( timer ) * 5;
          this.uploadCamera.position.z = Math.cos( timer ) * 5;
          requestAnimationFrame(this.uploadAnimate);
      },
      uploadRender(){
        this.uploadCamera.lookAt(this.uploadCameraTarget);
        this.uploadRenderer.render(this.uploadScene,this.uploadCamera);
      }
  },
  mounted() {
      this.loadModel()
  }
}
</script>

<style scoped>
.uploadModelDiv{
  height: 350px;
  width: 350px;
  margin: 25px;
}
.detailModelDiv{
  height:600px;
  width: 600px;
}
.modelDiv{
  height: 300px;
  width: 100%;
}
.modelCard {
    height: 350px;
    width: 300px;
  }
.el-row {
    margin-bottom: 20px;
    &:last-child {
      margin-bottom: 0;
    }
  }
.el-button-group{
  margin-bottom: 20px;
}
.el-button{
  width: 97px;
  text-align: center ;
}
.flashbutton{
  -webkit-animation: bluePulse 2s;
}
@-webkit-keyframes bluePulse {
   from { background-color: #2daebf; -webkit-box-shadow: 0 0 9px #333; }
   50% { background-color: #409EFF; -webkit-box-shadow: 0 0 18px #409EFF; }
   to { background-color: #2daebf; -webkit-box-shadow: 0 0 9px #333; }
}
</style>
