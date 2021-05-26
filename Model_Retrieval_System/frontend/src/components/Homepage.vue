<template>
  <div>
    <el-row :gutter="20">
      <el-col :span="17">
        <div style="text-align: left">
          <el-card shadow="hover" >
            <div slot="header">
                <p><i class="el-icon-tickets"></i>&ensp;Docs</p>
            </div>
            <div>
              <p>This the document of Retrieval System.</p>
              <p>欢迎使用模型检索系统，该系统基于改进三维物体级联分类网络进行检索。</p>
              <p>使用数据集为Priceton Project推出的ModelNet40数据集</p>
              <p>本系统包含以下页面及功能:</p>
              <p>1.模型库页面：ModelNet40数据集上所有数据查看与下载，提供搜索种类功能。</p>
              <p>2.模型检索页面：ModelNet40模型检索功能，上传模型对应npy文件（可于模型库中下载），检索后将展示全部同类物体。</p>
              <p>3.模型概览页面：本系统模型与其他ModelNet40上经典模型对比结果概览，还可查阅部分网络于ModelNet40上的分类准确度。</p>
              <p>4.模型工具页面：转换.obj、.ply、.pcd文件为其他页面可选格式，将在未来提供更多类型转换、添加特征信息等模型工具。</p>
              <br><p>注：本系统可与通常浏览器一样使用分页标签打开关闭网页。</p>
              <p>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp三维物体级联网络论文地址:<a href="https://arxiv.org/abs/2011.04522">https://arxiv.org/abs/2011.04522</a></p>
            </div>
          </el-card>
        </div>
        <div style="margin-top: 1%">
          <el-card shadow="hover">
              <p><el-icon class="el-icon-loading"></el-icon>作者github:<a href="https://github.com/CorleoneJW">https://github.com/CorleoneJW</a></p>
              <p><el-icon class="el-icon-loading"></el-icon>个人主页:<a href="https://corleonejw.github.io/">https://corleonejw.github.io/</a></p>
              <p><el-icon class="el-icon-loading"></el-icon>欢迎于github提问</p>
          </el-card>
        </div>
      </el-col>
      <el-col :span="6">
        <el-card shadow="hover" ><el-calendar v-model="date"></el-calendar></el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script>
    export default {
        data(){
            return{
                value: null,
                date:new Date(),
                iconClasses: ['icon-rate-face-1', 'icon-rate-face-2', 'icon-rate-face-3'],
                imagesbox:[
                ]
            }
        },
        mounted(){
            history.pushState(null, null, document.URL);
            window.addEventListener('popstate', function () {
                history.pushState(null, null, document.URL);
                //这里是设置点击浏览器后退按钮不会返回到登录页，为了防止用户点击在首页时点击浏览器后退按钮返回到登录页
            });
        },
        methods:{
            jumpModelLibrary(){
                this.$router.push();
            },
        }
    }
</script>

<style>
    .el-card__body{
        padding:10px !important;
    }
    .mtitle{
        margin-bottom: 20px;
        margin-top: 10px;
    }
    .mcard{
        background-color:#F7F7F7;
    }
    .mform{
        padding:20px;
    }
    .mchart{
        display:flex;
        justify-content: center;
    }
    .drawForm{
        padding:20px;
        text-align:left;
    }
     .el-carousel__item h3 {
         color: #475669;
         font-size: 14px;
         opacity: 0.75;
         line-height: 200px;
         margin: 0;
     }
    .el-carousel__item:nth-child(2n) {
        background-color: #99a9bf;
    }

    .el-carousel__item:nth-child(2n+1) {
        background-color: #d3dce6;
    }

    .el-calendar-table .el-calendar-day {
        height: 50px;
      }
    a:link {
    color: #000000;
    text-decoration: none;
    }
    a:visited {
    color: #000000;
    text-decoration: none;
    }
    a:hover {
    color: #999999;
    text-decoration: underline;
    }
</style>
