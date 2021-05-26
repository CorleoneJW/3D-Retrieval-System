<template>
  <div>
    <el-row style="margin-bottom: 0px">
      <el-col :span="6">
        <el-row>
          <el-input v-model="search" placeholder="搜索" clearable style="width: 50%;float: left;margin-left: 5%;" @change="searchCat"></el-input>
        </el-row>
        <el-row>
          <el-button-group id="group1">
            <el-button type="primary" id="button0" @click="catChange(0)">{{currentCategories[0]}}</el-button>
            <el-button type="primary" id="button1" @click="catChange(1)">{{currentCategories[1]}}</el-button>
            <el-button type="primary" id="button2" @click="catChange(2)">{{currentCategories[2]}}</el-button>
            <el-button type="primary" id="button3" @click="catChange(3)">{{currentCategories[3]}}</el-button>
          </el-button-group >
          <el-button-group id="group2">
            <el-button type="primary" id="button4" @click="catChange(4)">{{currentCategories[4]}}</el-button>
            <el-button type="primary" id="button5" @click="catChange(5)">{{currentCategories[5]}}</el-button>
            <el-button type="primary" id="button6" @click="catChange(6)">{{currentCategories[6]}}</el-button>
            <el-button type="primary" id="button7" @click="catChange(7)">{{currentCategories[7]}}</el-button>
          </el-button-group>
          <el-button-group id="group3">
            <el-button type="primary" id="button8" @click="catChange(8)">{{currentCategories[8]}}</el-button>
            <el-button type="primary" id="button9" @click="catChange(9)">{{currentCategories[9]}}</el-button>
            <el-button type="primary" id="button10" @click="catChange(10)">{{currentCategories[10]}}</el-button>
            <el-button type="primary" id="button11" @click="catChange(11)">{{currentCategories[11]}}</el-button>
          </el-button-group>
          <el-button-group id="group4">
            <el-button type="primary" id="button12" @click="catChange(12)">{{currentCategories[12]}}</el-button>
            <el-button type="primary" id="button13" @click="catChange(13)">{{currentCategories[13]}}</el-button>
            <el-button type="primary" id="button14" @click="catChange(14)">{{currentCategories[14]}}</el-button>
            <el-button type="primary" id="button15" @click="catChange(15)">{{currentCategories[15]}}</el-button>
          </el-button-group>
          <el-button-group id="group5">
            <el-button type="primary" id="button16" @click="catChange(16)">{{currentCategories[16]}}</el-button>
            <el-button type="primary" id="button17" @click="catChange(17)">{{currentCategories[17]}}</el-button>
            <el-button type="primary" id="button18" @click="catChange(18)">{{currentCategories[18]}}</el-button>
            <el-button type="primary" id="button19" @click="catChange(19)">{{currentCategories[19]}}</el-button>
          </el-button-group>
        </el-row>
        <el-row>
          <el-pagination background layout="prev, pager, next" :total="40" :page-size="20" @current-change="showButton" :current-page.sync="catPage"></el-pagination>
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
export default {
  name: "All",
  data() {
    return {
      totalCategories: ["airplane", "bathtub", "bed", "bench", "bookshelf", "bottle", "bowl", "car", "chair", "cone", "cup", "curtain", "desk", "door", "dresser", "flower_pot", "glass_box", "guitar", "keyboard",
        "lamp", "laptop", "mantel", "monitor", "night_stand", "person", "piano", "plant", "radio", "range_hood", "sink", "sofa", "stairs", "stool", "table", "tent", "toilet", "tv_stand", "vase", "wardrobe", "xbox"],
      categoryNum_train: [626, 106, 515, 173, 572, 335, 64, 197, 889, 167, 79, 138, 200, 109, 200, 149, 171, 155, 145, 124, 149, 284, 465, 200, 88, 231, 240, 104, 115, 128, 680, 124, 90, 392, 163, 344, 267, 475, 87, 103],
      categoryNum_test: [100, 50, 100, 20, 100, 100, 20, 100, 100, 20, 20, 20, 86, 20, 86, 20, 100, 100, 20, 20, 20, 100, 100, 86, 20, 100, 100, 20, 100, 20, 100, 20, 20, 100, 20, 100, 100, 100, 20, 20],
      currentCategories: ["null", "null", "null", "null", "null", "null", "null", "null", "null", "null", "null", "null", "null", "null", "null", "null", "null", "null", "null", "null"],
      currentCategory: "airplane",    //当前种类，默认为飞机
      catPage: 1,      //左侧种类页数，默认第一页
      libPage: 1,      //检索库当前页数，默认第一页
      libNum: 626,      //检索库当前类总数，默认为飞机
      singleNum: 8,    //检索库每页显示数量
      currentModelnum:8,  //当前页面显示数量
      search: "",     //搜索框文本
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
      detailMesh:null,      //详情页msh
      detailLight:null,     //详情页灯光
      detailRenderer:null,    //详情页渲染器
      detailControls:null,    //详情页控制器
      dialogVisible:false,    //dialog是否展示控制,
      radio:"训练集",          //选择训练集还是测试集的radio
      downloadPlyHttp:null,      //下载ply地址url
      downloadNpyHttp:null,      //下载npy地址url
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
      searchCat(){
          //搜索框
          let searchText = this.search;
          for(let i=0;i<40;i++){
            if(searchText==this.totalCategories[i]){
              if(i<20){
                this.catPage=1;
                this.showButton();
                let docId = 'button'+i;
                let tempButton;
                tempButton = document.getElementById(docId);
                let originClass = tempButton.getAttribute("class");
                let newClass = originClass.concat(" flashbutton");
                tempButton.setAttribute("class",newClass);
                let timer = setInterval(()=>{
                  tempButton.setAttribute("class",originClass);
                  clearInterval(timer);
                },2000);
              }
              else{
                this.catPage=2;
                this.showButton();
                let docId = 'button'+(i-20);
                let tempButton;
                tempButton = document.getElementById(docId);
                let originClass = tempButton.getAttribute("class");
                let newClass = originClass.concat(" flashbutton");
                tempButton.setAttribute("class",newClass);
                let timer = setInterval(()=>{
                  tempButton.setAttribute("class",originClass);
                  clearInterval(timer);
                },2000);
              }
            }
          }
      },
      showButton(){
          //通过修改data中对应数据显示左边按钮
          // console.log("catPage",this.catPage);
          if(this.catPage==1){
            for(let i=0;i<20;i++){
              Vue.set(this.currentCategories,i,this.totalCategories[i]);
            }
          }
          else if(this.catPage==2){
            for(let i=20;i<40;i++){
              Vue.set(this.currentCategories,i-20,this.totalCategories[i]);
            }
          }else{
            for(let i=0;i<20;i++){
              Vue.set(this.currentCategories,i,this.totalCategories[i]);
            }
          }
      },
      catChange(buttonIndex){
          //更改按钮的相应事件，获取当前种类
          let catIndex = buttonIndex;
          if(this.catPage==2){
            catIndex+=20;
          }
          this.currentCategory = this.totalCategories[catIndex];    //获得当前种类
          // console.log("cat",this.currentCategory)
          this.libPage = 1;     //右侧模型库当前页面重置为1
          this.loadModel()
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
          let npystr = 'http://127.0.0.1:8000/'+'afterTreat/'+showState+'/'+this.pad(this.totalCategories.indexOf(this.currentCategory)+1,3)+'.'
          +this.currentCategory+'_'+this.pad(detailIndex,9)+'.npy';
          // console.log("plyaddress"+modelIndex,plystr)
          console.log("npystr",npystr);
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

          //render
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
      }
  },
  mounted() {
      this.showButton()
      this.loadModel()
  }
}
</script>

<style scoped>
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
   from { background-color: #409EFF; -webkit-box-shadow: 0 0 9px #333; }
   50% { background-color: #2daebf; -webkit-box-shadow: 0 0 18px #2daebf; }
   to { background-color: #409EFF; -webkit-box-shadow: 0 0 9px #333; }
}
</style>
