<!--App.vue-->
<!--App.vue-->
<template>
 <div class="app-container">
    <!-- 搜索框 -->
    
     <router-view>
    </router-view>
    <!-- 底部导航 -->
    <div class="d-tabs" >
        <ul>
            <li>
                <a href="javascript:;" @click="jump(1)">
                    <img src="./img/biaoqian1-active.svg" v-if="down1">
                    <img src="./img/biaoqian1.svg" v-if="!down1">
                    <br>
                    首页
                </a>
            </li>
            <li>
                <a href="javascript:;" @click="jump(2)">
                    <img src="./img/biaoqian2-active.svg" v-if="down2">
                    <img src="./img/biaoqian2.svg" v-if="!down2">
                    <br>
                    订单
                </a>
            </li>
            <li>
                <a href="javascript:;" @click="jump(3)">
                    <img src="./img/biaoqian3-active.svg" v-if="down3">
                    <img src="./img/biaoqian3.svg" v-if="!down3"><br>
                    我的
                </a>
            </li>
        </ul>
    </div>
 </div>
</template>
<script>
export default {
    data(){
        return{
        down1:true,
        down2:false,
        down3:false,}
    },
    created() {
   },
    methods:{
    jump(e){
    this.$router.push(`/ShopList`);
    this.down1=true;
    this.down2=false;
    this.down3=false;
    if(e==1){
        this.$router.push(`/home`);
    }else if(e==2){
        this.down1=false;
        this.down2=true;
    }else if(e==3){
        this.down1=false;
        this.down3=true;
        this.$router.push(`/my`);
      }
    },
}
}
</script>


<style>
/*App.vue 顶部和底部导航栏*/
.app-container{
    margin:0;padding:0;
    width:100%;max-width: 750px;min-width: 750px;
    height:100%;
    margin:0 auto;
    font-family: 'Helvetica Neue', Helvetica, sans-serif;
    font-size: 17px;
    line-height: 21px;
    color: #000;
    background-color: #efeff4;
 }
 .search-f{
     width:100%;
     position: relative;
     }
 .search{
     width:42rem;height:1rem;
     margin-top:5px;
     position:fixed;
     left:570px;top:-6px;
 }
 .email{
    width:3rem;height:42px;
    display: inline-block;
    background-image:url("./img/email.svg");
    background-size:100%;
    background-position: -7px -11px;
    background-repeat: no-repeat;
    position: fixed;
    left:1274px;top:8px;
 }
 .psearch{
    display: inline-block;
    width:21px;height:21px;
    background-image: url("./img/search.svg");
    background-size:100%;
    position:fixed;
    top:6px;left:590px 
 }
 .search>input{
    margin-left:15px;
    border-radius:14px;
 }
 .d-tabs{
     width:750px;height:67px;
     position:fixed;
     bottom:0px;left:auto;
     background-color: #fff;
 }
 .d-tabs>ul{
     list-style:none;
     justify-content: space-around;
     display: flex;
     height:100%;
     padding-top:4px;
 }
 .d-tabs>ul>li{
      width: 250px;
      display: inline-block;
      margin:0px 105px; 
      
 }
 .d-tabs>ul>li>a{
     color: #555;
     font-size: 15px;
     }
 .d-tabs>ul>li>a>img{
     width:33px;height:33px;
     display: inline-block
 }
</style>
