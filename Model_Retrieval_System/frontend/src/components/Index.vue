<template>
    <el-container class="home-container">
        <el-header>
            <!-- 导航栏 -->
            <el-col :span="20">
                <div >
                    <img src="../assets/logo1.png" height="60" width="60" align="left">
                </div>
                <div display="flex">
                    <h1 align="left" display="inline" style="color:#FFFAF0;font-size:26px">模型检索系统</h1>
                </div>
            </el-col>
        </el-header>
        <el-container>
            <el-aside width="160px">
                <div class="toggle-button">|||</div>
                <!-- 侧边栏 -->
                <el-col>
                    <el-menu display="flex" :default-active="$route.path" router background-color="#333744" text-color="#fff" active-text-color="#ffd04b">
                        <template v-for="(item) in menuitem">
                            <el-menu-item align="left" :key="item.name" :index="item.path" @click="addTab(item.name,item.path)">
                                <i :class="item.class"></i>
                                {{item.name}}
                            </el-menu-item>
                        </template>
                    </el-menu>
                </el-col>
            </el-aside>
            <el-main>
                <!-- Body -->
                <el-tabs v-model="editableTabsValue" type="card" @tab-remove="removeTab" @tab-click="dolist($event.name)" >
                    <el-tab-pane
                            :key="'首页'"
                            :label="'首页'"
                            :name="'首页'"
                    >
                    </el-tab-pane>
                    <template v-for="(item) in editableTabs">
                        <el-tab-pane
                                v-if="item.name!=''"
                                :key="item.name"
                                :label="item.title"
                                :name="item.name"
                                closable
                        >
                            {{item.content}}
                        </el-tab-pane>
                    </template>
                </el-tabs>
                <router-view></router-view>
            </el-main>
        </el-container>
    </el-container>
</template>

<script>
    export default {
        data() {
            return {
                menuitem: [          //动态生成左侧导航栏
                    {path: '/Homepage', name: '首页', class: 'el-icon-house'},
                    {path: '/All', name: '模型库', class: 'el-icon-suitcase'},
                    {path: '/Single', name: '模型检索', class: 'el-icon-search'},
                    {path: '/Statistic', name: '网络对比', class: 'el-icon-data-line'},
                    {path: '/Utils', name: '模型工具', class: 'el-icon-brush'}
                ],
                //tabs动态生成初始化
                editableTabsValue: '首页',     //默认点亮tab
                editableTabs: [{
                    title: '',
                    name: ''
                }],
                tabIndex: 1
            }
        },
        //默认运行
        mounted() {

            history.pushState(null, null, document.URL);
            window.addEventListener('popstate', function () {
                history.pushState(null, null, document.URL);
                //这里是设置点击浏览器后退按钮不会返回到登录页，为了防止用户点击在首页时点击浏览器后退按钮返回到登录页
            });
        },
        methods: {
            dolist(n) {
                let curpath = '';
                this.menuitem.forEach((item) => {
                    if (item.name == n) {
                        curpath = item.path;
                    }
                });
                this.$router.push({path: curpath});    //点击菜单跳转到对应页面，浏览器地址也跳转到指定URL
            },
            //点击左侧导航栏添加未出现的tab
            addTab(targetName, e) {
                this.$router.push({path: e})    //点击菜单跳转到对应页面，浏览器地址也跳转到指定URL
                if (targetName == '首页') {
                    this.editableTabsValue = targetName;
                    return;
                }
                let tabs = this.editableTabs;       //从data中得到对应tabs数组
                let flag = false;       //默认没有存在，flag为true则表示存在对应tab
                tabs.forEach((tab) => {      //循环，判断是否存在当前点击的对应tab，没有就才加上
                    if (tab.name === targetName) {
                        flag = true;
                        this.editableTabsValue = targetName;
                    }
                });
                if (flag === false) {
                    this.editableTabs.push({
                        title: targetName,
                        name: targetName,
                    });
                    // this.tabIndex++;
                    this.editableTabsValue = targetName;
                }
            },
            //删除tab
            removeTab(targetName) {
                let tabs = this.editableTabs;
                let activeName = this.editableTabsValue;
                if (activeName == targetName) {        //寻找当前点亮的tab,如果是要删除的，则寻找另外一个tab点亮,先后再前
                    tabs.forEach((tab, index) => {
                        if (tab.name == targetName) {
                            let nextTab = tabs[index + 1] || tabs[index - 1];
                            if (nextTab) {
                                if (nextTab.name == '')
                                    activeName = '首页';
                                else
                                    activeName = nextTab.name;
                            }
                        }
                    });
                }
                this.editableTabsValue = activeName;
                this.editableTabs = tabs.filter(tab => tab.name != targetName);
                this.dolist(this.editableTabsValue);
            }
        }
    }
</script>

<style scoped>
    .home-container{
        height: 100%;
    }
    .toggle-button{
        background-color: #4A5064;
        font-size: 10px;
        line-height: 24px;
        color:#ffffff;
        text-align: center;
        letter-spacing: 0.2em;
    }
    .el-header{
        background-color: #373d41;
        text-align: center;
        line-height: 20px;
        display: flex;
        flex-direction: row;
        justify-items: center;
    }
    .el-aside{
        width: 16%;
        background-color: #333744;
    }
    .el-menu-item{
        width:160px;
    }
    .btn{
        float: right;
        margin: auto 10px auto auto;
    }
</style>
