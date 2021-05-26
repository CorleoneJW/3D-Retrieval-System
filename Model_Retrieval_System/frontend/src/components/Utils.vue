<template>
  <div>
      <div class="drawForm">
          <el-row :gutter="20">
              <el-col :span="10" style="height: 750px">
                  <p>请上传待转换文件</p>
                  <el-upload
                  action="string"
                  accept=".ply,.obj,.pcd"
                  ref="upload"
                  :before-upload="onBeforeUploadPly"
                  :on-change="fileChange"
                  :http-request="nullfunction"
                  :auto-upload="true"
                  :file-list="fileList"
                  :limit="1"
                  style="display: flex;justify-content: left;align-items: center"
                  >
                  <el-button size="small" type="primary">点击上传</el-button>
                  </el-upload>
                  <p>请选择要转换的格式类型</p>
                  <el-select v-model="changeFormat" placeholder="请选择">
                    <el-option
                      v-for="item in options"
                      :key="item.value"
                      :label="item.label"
                      :value="item.value">
                    </el-option>
                  </el-select>
                  <el-button size="small" type="primary" @click="downLoadFormatFile" style="margin-top: 1%">下载</el-button>
                  <div style="margin-top:450px">
                    <div>
                      <p><el-icon class="el-icon-loading"></el-icon>后续将更新更多模型转换格式。</p>
                      <p><el-icon class="el-icon-loading"></el-icon>欢迎联系github给予模型工具方面的意见。</p>
                    </div>
                  </div>
              </el-col>
              <el-col :span="7">
                  <el-card shadow="hover" >
                        <div slot="header">
                            <p><i class="el-icon-reading"></i>&ensp;格式转换使用说明</p>
                        </div>
                        <div>
                            <p>1.格式转换可上传.obj、.ply与.pcd格式文件。</p>
                            <p>2.使用流程</p>
                            <el-timeline :reverse="reverse">
                                <el-timeline-item
                                  v-for="(activity, index) in activities"
                                  :key="index"
                                  :timestamp="activity.timestamp">
                                  {{activity.content}}
                                </el-timeline-item>
                            </el-timeline>
                            <p>为了正常使用，请确保文件拓展名前没有英文句号'.'。</p>
                        </div>
                  </el-card>
              </el-col>
              <el-col :span="7">
                    <el-card shadow="hover" >
                          <div slot="header">
                              <p><i class="el-icon-news"></i>&ensp;数据介绍</p>
                          </div>
                          <div>
                              <p>1.ply文件:</p>
                              <p>PLY文件格式是Stanford大学开发的一套三维mesh模型数据格式，图形学领域内很多著名的模型数据，比如Stanford的三维扫描数据库（其中包括很多文章中会见到的Happy Buddha, Dragon, Bunny兔子），Geogia Tech的大型几何模型库，北卡(UNC)的电厂模型等，最初的模型都是基于这个格式的。</p>
                              <p>2.pcd文件</p>
                              <p>PCD（Point Cloud Date，点云数据） 对应的文件格式为 （*.pcd），是PCL官方指定格式，具有ASCII和binary两种数据存储类型，pcd格式具有文件头，用于描绘点云的整体信息。</p>
                              <p>3.obj文件</p>
                              <p>obj文件是3D模型文件格式。由Alias|Wavefront公司为3D建模和动画软件"Advanced Visualizer"开发的一种标准，适合用于3D软件模型之间的互导，也可以通过Maya读写。</p>
                          </div>
                    </el-card>
                </el-col>
          </el-row>
        </div>
  </div>
</template>

<script>
export default {
  name: "Utils",
  data(){
      return{
          value: '',
          reverse: false,   //走马灯显示顺序逆序
          activities: [{      //走马灯内容
            content: '上传符合数据格式的文件',
            timestamp: '第一步'
          }, {
            content: '等待转换，根据文件大小决定时间',
            timestamp: '第二步'
          }, {
            content: '点击下载按钮，下载转换完毕文件',
            timestamp: '第三步'
          }],
          options: [{     //bottom组内容
            value: 'ply',
            label: '.ply格式'
          }, {
            value: 'pcd',
            label: '.pcd格式'
          }],
          fileList:[],          //作为上传文件的存储List
          changeFormat:null,    //转换为什么格式的标志
      }
  },
  methods:{
      nullfunction(){

      },
      onBeforeUploadPly(file){
        return new Promise((resolve, reject) => {
          const isPly = this.judegePly(file.name);
          const isPcd = this.judegePcd(file.name);
          const isObj = this.judegeObj(file.name);
          if(!isPly&&!isPcd&&!isObj){
            this.$message.error('上传文件只能是obj、pcd或ply格式!');
            return reject(false);
          }
          else{
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
            console.log("responsedata:",response.data);
            this.currentCategory = this.totalCategories[response.data.category];
            this.train = true;
            this.libPage = 1;
            this.libpageChange();
          })
      },
      fileChange(file){
            this.$refs.upload.clearFiles();
            this.fileList = [{name: file.name,url:URL.createObjectURL(file.raw),raw:file.raw}];
      },
      judegePly(name){
            //判断是否是ply文件
            let fileName = name.substring(name.lastIndexOf('.')+1);
            let isPly = fileName === 'ply';
            return isPly;
      },
      judegePcd(name){
            //判断是否是pcd文件
            let fileName = name.substring(name.lastIndexOf('.')+1);
            let isPcd = fileName === 'pcd';
            return isPcd;
      },
      judegeObj(name){
            //判断是否是obj文件
            let fileName = name.substring(name.lastIndexOf('.')+1);
            let isObj = fileName === 'obj';
            return isObj;
      },
      downLoadFormatFile(){
          const formData = new FormData();
          formData.append('file',this.fileList[0].raw);
          formData.append('target',this.changeFormat);
          // console.log('formData',formData);
          let config = { // 配置请求头
            headers: {'Content-Type': 'multipart/form-data'},
            responseType:'blob'
          }
          this.$axios.post("http://127.0.0.1:8082/changeFormat/",formData,config).then(response=>{
            // console.log("responsedata:",response);
            let formatData = response.data
            let filename = response.headers["content-disposition"];
            filename = filename.substring(filename.lastIndexOf('=')+1);
            const reader = new FileReader();
            reader.readAsDataURL(formatData);
            reader.onload = (e) =>{
                var link = document.createElement("a");
                link.href = e.target.result;
                link.download = filename;
                link.click();
                window.URL.revokeObjectURL(link.href);
            }
          })
      }
  }
}
</script>

<style scoped>

</style>
