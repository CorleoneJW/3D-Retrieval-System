<template>
  <div>
      <div class="drawForm">
            <el-row :gutter="20">
                <el-col :span="17">
                    <el-card shadow="hover" >
                        <div slot="header">
                            <p><i class="el-icon-data-analysis"></i>&ensp;网络对比</p>
                        </div>
                        <el-row>
                          <el-col :span="12">
                            <div class="mchart"><div id="myChart1" ref="myChart1" style="width:95%;height:350px;"></div></div>
                          </el-col>
                          <el-col :span="12">
                            <div class="mchart"><div id="myChart2" ref="myChart2" style="width:95%;height:350px;"></div></div>
                          </el-col>
                        </el-row>
                    </el-card>
                </el-col>
              <el-col :span="7">
                  <el-card shadow="hover" >
                        <div slot="header">
                            <p><i class="el-icon-notebook-2"></i>&ensp;经典网络概况</p>
                        </div>
                        <div>
                            <el-table
                                :data="tableData"
                                style="width: 100%"
                                border
                                height="500px"
                                :row-class-name="tableRowClassName">
                                <el-table-column
                                  fixed
                                  prop="modelName"
                                  label="模型"
                                  width="226px">
                                </el-table-column>
                                <el-table-column
                                  prop="acc"
                                  label="准确度"
                                  width="226px">
                                </el-table-column>
                            </el-table>
                        </div>
                  </el-card>
              </el-col>
            </el-row>
        </div>
  </div>
</template>

<script>
    export default {
        data(){
            return{
                value: null,
                tableData:[
                  {
                    modelName:'Cascade',
                    acc:'92.4%'
                  },
                  {
                    modelName:'VoxNet',
                    acc:'83.0%'
                  },
                  {
                    modelName:'PointNet',
                    acc:'89.2%'
                  },
                  {
                    modelName:'PointNet++',
                    acc:'90.7%'
                  },
                  {
                    modelName:'MVCNN-New',
                    acc:'92.7%'
                  },
                  {
                    modelName:'3DCapsule',
                    acc:'92.7%'
                  },
                  {
                    modelName:'LDGCNN',
                    acc:'92.9%'
                  },
                  {
                    modelName:'MLVCNN',
                    acc:'94.16%'
                  },
                  {
                    modelName:'VIPGAN',
                    acc:'91.98%'
                  },
                  {
                    modelName:'KCNet',
                    acc:'91.00%'
                  },
                  {
                    modelName:'PVNet',
                    acc:'93.2%'
                  },
                  {
                    modelName:'LightNet',
                    acc:'88.93%'
                  },
                  {
                    modelName:'VRN Ensemble',
                    acc:'95.54%'
                  },
                  {
                    modelName:'3DGAN',
                    acc:'83.3%'
                  },
                  {
                    modelName:'FusionNet',
                    acc:'90.8%'
                  },
                  {
                    modelName:'3DShapeNets',
                    acc:'77%'
                  },
                  {
                    modelName:'FPNN',
                    acc:'88.4%'
                  },
                  {
                    modelName:'RotationNet',
                    acc:'97.37%'
                  },
                  {
                    modelName:'3D-CapsNets',
                    acc:'82.73%'
                  }
                ]
            }
        },
        mounted(){
            this.drawBar();
            history.pushState(null, null, document.URL);
            window.addEventListener('popstate', function () {
                history.pushState(null, null, document.URL);
                //这里是设置点击浏览器后退按钮不会返回到登录页，为了防止用户点击在首页时点击浏览器后退按钮返回到登录页
            });
        },
        methods:{
            drawBar(){
                // 基于准备好的dom，初始化echarts实例
                var myChart1 = this.$echarts.init(document.getElementById('myChart1'))
                var myChart2 = this.$echarts.init(document.getElementById('myChart2'))
                // 绘制图表
                myChart1.setOption({
                    title:{
                      show:true,
                      text:'准确率(%)',
                    },
                    tooltip: {
                        trigger: 'axis',
                        axisPointer: {            // 坐标轴指示器，坐标轴触发有效
                                          type: 'shadow'
                                      }
                    },
                    legend: {
                        data:[]
                    },
                    grid: {
                        left: '3%',
                        right: '4%',
                        bottom: '3%',
                        containLabel: true
                    },
                    toolbox: {
                        feature: {
                            saveAsImage: {}
                        }
                    },
                    xAxis: {
                        data: ['Cascade','MVCNN','PointNet','PointNet++','VoxNet']
                    },
                    yAxis: {
                        min:60,
                        max:100,
                        type: 'value'
                    },
                    series: [
                        {
                            label: {
                                show: true,
                                position: 'top'
                            },
                            name:'准确率',
                            type:'bar',
                            data:[{value:92.4,itemStyle:{color:'#a90000'}},
                                {value:95.0,itemStyle:{color:'#f47920'}},
                                {value:89.2,itemStyle:{color:'#ffc20e'}},
                                {value:90.7,itemStyle:{color:'#65c294'}},
                                {value:83.0,itemStyle:{color:'#65c294'}}],
                            emphasis:{
                              focus: 'series'
                            }
                        }
                    ]
                });
                myChart2.setOption({
                    title:{
                        show:true,
                        text:'单个样本推理速度(ms)',
                    },
                    visualMap: [{
                      show: false,
                      type: 'continuous',
                      seriesIndex: 0,
                      min:0,
                      max:15,
                    }],
                    tooltip: {
                        trigger: 'axis',
                        axisPointer: {            // 坐标轴指示器，坐标轴触发有效
                                          type: 'shadow'
                                      }
                    },
                    legend: {
                        data:[]
                    },
                    grid: {
                        left: '3%',
                        right: '4%',
                        bottom: '3%',
                        containLabel: true
                    },
                    toolbox: {
                        feature: {
                            saveAsImage: {}
                        }
                    },
                    xAxis: {
                        data: ['Cascade','MVCNN','PointNet','PointNet++','VoxNet']
                    },
                    yAxis: {
                        type: 'value'
                    },
                    series: [
                        {
                            label: {
                                show: true,
                                position: 'top'
                            },
                            name:'准确率',
                            type:'line',
                            data:[0.29, 13.5, 1.8, 2.9, 0.25],
                            emphasis:{
                              focus: 'series'
                            }
                        }
                    ]
                });
                window.addEventListener('resize', () => {
                    // 自动渲染echarts
                    myChart1.resize();
                    myChart2.resize();
                });
            },
          tableRowClassName({row, rowIndex}) {
                if (rowIndex === 0) {
                  return 'warning-row';
                }
                return '';
            }
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
    .el-table .warning-row {
    background: oldlace;
    }
</style>
