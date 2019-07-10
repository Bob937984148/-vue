<template>
<div class="app-first">
  <div class="search-f">
    <div class="search">
        <input type="text" placeholder="    搜索">
         <i class="psearch"></i>
        <i class="email"></i>
    </div>
    </div>
<!--第一个：背景大图-->
  <div class="app-home"></div>  
     <!--台阶1-->
  <div class="app-text">
    <a href="javascript:;">
      <span>2018年8月29日起，藏宝阁支持更多服务器啦，点击即可查看</span>
    </a>
  </div>
    <!--台阶2-->
  <div class="short">
    <a href="javascript:;" class="short-a">
      <i class="short1"></i>
      <span>登记出售</span>
    </a>
    <a href="javascript:;" class="short-b">
      <i class="short2"></i>
      <span>全部商品</span>
    </a>
  </div>
    <!--台阶3-->
    <div class="auto-top">
      <a href="javascript:;" class="title-item1">
        <div class="title">炼狱茨木童子</div>
        <div class="sub-title">鬼手在试图吞噬我的意志</div>
      </a>
      <a href="javascript:;" class="title-item2">
        <div class="title">妖刀姬</div>
        <div class="sub-title">看我大长腿么</div>
      </a>
      <a href="javascript:;" class="title-item3">
        <div class="title">日月同辉</div>
        <div class="sub-title">成功移民欧洲</div>
      </a>
      <a href="javascript:;" class="title-item4">
        <div class="title">鬼切</div>
        <div class="sub-title">一起斗技去</div>
      </a>
    </div>
     <!--商品-->
     <div class="com">
        <h2>
          <i class="con1"></i>
          <div>最新上架</div>
          <i class="con2"></i>
        </h2>
        <div class="wrapper" v-for="item in list" :key="item.user_id" @click="getMore(item[0].user_id)">
          <div class="hd" >
            <span class="level">{{item[0].lv}}级</span>
            <span class="platform">{{item[0].site}}
              <i class="icon-ios"></i>
              <i class="icon-pub"></i>
            </span>
            <span class="price">￥{{item[0].price}}</span>
          </div>
          <div class="intro">
            <ul class="base">
              <li>SSR 43</li>
              <li>六星式神 19</li>
              <li>签到{{item[0].days}}天</li>
            </ul>
            <div class="collect">0人收藏</div>
          </div>
          <div class="start">
            <span>六星SSR21个</span>
            <span>斗技2553</span>
          </div>
          <ul class="hero-item">
            <li>
              <div class="frame">
                <div class=wrap>
                  <img :src="'http://127.0.0.1:3000/img'+item[0].src" alt="">
                  <span class="font_small1"></span>
                  <p>满</p>
                  <span class="font_small2">觉</span>
                  <span class="leave_icons">
                    <i></i>
                    <i></i>
                    <i></i>
                    <i></i>
                    <i></i>
                    <i></i>
                  </span>
                </div>
                <div class="name">{{item[0].name}}</div>
              </div>
            </li>
            <li>
              <div class="frame">
                <div class=wrap>
                  <img :src="'http://127.0.0.1:3000/img'+item[1].src" alt="">
                  <span class="font_small1"></span>
                  <p>满</p>
                  <span class="font_small2">觉</span>
                  <span class="leave_icons">
                    <i></i>
                    <i></i>
                    <i></i>
                    <i></i>
                    <i></i>
                    <i></i>
                  </span>
                </div>
                <div class="name">{{item[1].name}}</div>
              </div>
            </li>
            <li>
              <div class="frame">
                <div class=wrap>
                 <img :src="'http://127.0.0.1:3000/img'+item[2].src" alt="">
                  <span class="font_small1"></span>
                  <p>满</p>
                  <span class="font_small2">觉</span>
                  <span class="leave_icons">
                    <i></i>
                    <i></i>
                    <i></i>
                    <i></i>
                    <i></i>
                    <i></i>
                  </span>
                </div>
                <div class="name">{{item[2].name}}</div>
              </div>
            </li>
            <li>
              <div class="frame">
                <div class=wrap>
                  <img :src="'http://127.0.0.1:3000/img'+item[3].src" alt="">
                  <span class="font_small1"></span>
                  <p>满</p>
                  <span class="font_small2">觉</span>
                  <span class="leave_icons">
                    <i></i>
                    <i></i>
                    <i></i>
                    <i></i>
                    <i></i>
                    <i></i>
                  </span>
                </div>
                <div class="name">{{item[3].name}}</div>
              </div>
            </li>
            <li>
              <div class="frame">
                <div class=wrap>
                  <img :src="'http://127.0.0.1:3000/img'+item[4].src" alt="">
                  <span class="font_small1"></span>
                  <p>满</p>
                  <span class="font_small2">觉</span>
                  <span class="leave_icons">
                    <i></i>
                    <i></i>
                    <i></i>
                    <i></i>
                    <i></i>
                    <i></i>
                  </span>
                </div>
                <div class="name">{{item[4].name}}</div>
              </div>
            </li>
          </ul>
        </div>
        <div class="more">
          <a href="" class="btn1" @click.prevent="getuser">查看全部</a>
        </div>
        <div class="top">
          <a href="#"></a>
        </div>
        <div class="entry">
          <img src="../img/entry.png" alt="">
          <br>关注微信公众号
          <br>手游交易更方便
        </div>
     </div>
  
</div>
</template>
<script>
 export default {
   created() {
      //当组件对象创建成功后即可发送ajax请求
      this.getuser();
      // this.getuser_ss()
   },
   methods:{
      getMore(e){
        this.$router.push(`/equip/${e}`)
      },
     getuser(){
       //1:发送ajax请求
       this.jjdata+=5;
      for(var i=1;i<this.jjdata;i++){
        var url = `http://127.0.0.1:3000/home?id=${i}`;
        this.axios.get(url).then(result=>{
        // console.log(result.data);
        this.list.push(result.data);
         })
       }
     }
   },
   data(){
     return {
       list:[],
       jjdata:0
     }
   }
 }  
</script>
<style>
.app-home{
  background-image: url("../img/bjt.jpg");
  width:100%;height:412px;
  background-size: 100% auto;
  background-repeat:no-repeat; 
}
.app-text{
  height:53px;
  background: #fffaef;
}
.app-text>a{
  color:#e74e4b;
  line-height: 53px;
}
.short{
  height:73px;
}
.short>a{
  font-size: 20px;
  color:#000;
  background: #fff;
  line-height: 73px;
  display:inline-block;
  width:375px;height:73px;
  text-align: center;
  }
.short>a>span{
  line-height: 73px;
  margin-left:10px;
  vertical-align: middle;
}
.short1{
  vertical-align: middle;
  display: inline-block;
  width:34px;height:34px;
  background-image: url("../img/short1.svg");
  background-size: 100%;
}
.short-b{
  float:left; 
}
.short2{
  vertical-align: middle;
  display: inline-block;
  width:34px;height:34px;
  background-image: url("../img/short2.svg");
  background-size: 100%;
}
.auto-top{
  display: block;
}
.auto-top>a{
  display: inline-block;
  width:50%;
  height:105px;
  background-repeat: no-repeat;
  background-position:100%;
  background-size: 75px auto ;
}
.title-item1{
  background-image: url("../img/title1.png");
  color: rgb(112, 151, 146);
  background-color: rgb(245, 252, 251);
}
.title-item2{
  background-image: url("../img/title2.png");
  color: rgb(206, 124, 40);
  background-color: rgb(253, 247, 240);
}
.title-item3{
  background-image: url("../img/title2.png");
  color: rgb(244, 147, 147);
  background-color: rgb(255, 245, 245);
}
.title-item4{
  background-image: url("../img/title4.png");
  color: rgb(125, 181, 202);
  background-color: rgb(242, 249, 252);
}
.title{
  width:277px;height:33px;
  font-size: 23px;
  font-weight: 700;
  margin-left:10px;
}
.sub-title{
  width:277px;height:53px;
  font-size:16px;
  margin-left:10px;
}
.com{
  position:relative;
  background: #f5f5f5;
  height:1000px;
  }
.com>h2{margin-bottom:0}
.com>h2>div{
  text-align: center;
  background: #fff;
}
.con1{
  width:112px;height:17px;
  background-image: url("../img/con1.png");
  background-size:100% 100%;
  display: block;
  position:absolute;
  left:160px;top:0px;
}
.con2{
  width:112px;height:17px;
  background-image: url("../img/con2.png");
  background-size:100% 100%;
  display: block;
  position:absolute;
  left:450px;top:0px;
}
.wrapper{
  background: #ffffff;
  height:330px;
  padding-bottom: 20px;
  z-index:1000;
}
.level{
  font-size:22px;
  font-weight: 700;
  vertical-align: middle;
}
.platform{
  color: #888;
  margin-left:5px;
}
.icon-ios{
  margin-top:5px;
  width:22px;height:22px;
  display: inline-block;
  background-size: 100% 100%;
  background-image:url("../img/phone.png") 
}
.icon-pub{
  margin-left:5px;
  width:22px;height:22px;
  display: inline-block;
  background-size: 100% 100%;
  background-image:url("../img/g.svg") 
}
.price{
    float: right;
    color: #e74e4b;
    font-size: 28px;
    font-weight: 700;
}
.base{
  display:inline-block;
  list-style: none;
}
.base>li{
  color: #888;
  display: inline;
}
.collect{
  display:inline-block;
  float: right;
}
.start{
  
  display: inline-block;
}
.start>span{
  height:30px;
  background: #f1f1f1;
  display: inline-block;
  margin:5px;
  border-radius:3px;
}
.hero-item{
  height:158px;
  list-style: none;
  padding:0;
  background-color: #fff;
}
.hero-item>li{float: left;margin:0 8px}
.frame{
  width:133px;height:133px;
  border-top-right-radius: .15rem;
  border-color: #f8d26b;
  border: .1rem solid #fabf20
}
.wrap{position:relative;margin-bottom: 0}
.wrap>img{width:100%;height:100%}
.font_small1{
  width:20px;height:20px;
  background: #4b322c;
  position: absolute;
  left:5px;top:4px;
  transform: rotate(45deg);
}
.wrap>p{
  position:absolute;
  left:8px;top:3px;
  color:#fff;
  text-align: center;
  font-size:.8rem;
}
.font_small2{
  width:18px;height:18px;
  background: #aa39c6;
  position: absolute;
  left:110px;top:95px;
  color:#fff;
  text-align: center;
  font-size:.9rem;
}
.leave_icons{
  padding-left:28px;
  position:absolute;
  left:0px;bottom:5px;
  width:130px;height:15px;
  display: block;
  background: rgba(250,191,32,.6);
  background-color: hsla(44,91%,70%,.6);
}
.leave_icons>i{
  width:11px;height:14px;
  display: inline-block;
  background-image:url("../img/puple.png");
  background-size: 100% 100%;
}
.name{
  width:130px;
  border-bottom-right-radius: .15rem;
  background: #f2f2f2;
  font-size: 14px;
  text-align: center;
  margin-top: 0;
  margin-bottom: 10px;

}
.btn1{
  font-size: 20px;
  display: block;
  line-height: 42px;
  width:146px;height:42px;
  border-radius: 20px;
  color:#1e1e1e;
  border: 1px solid #e5e5e5;
  background-color: #fff;
  margin:25px auto;
  margin-bottom: 100px;
  text-align: center;
}
.top{
  display: block
}
.top>a{
  width:64px;height:60px;
  background-image: url("../img/top.svg");
  background-size:100% 100%; 
  position:fixed;
  right:400px;bottom:100px
}
.entry{
  position: fixed;
  right:160px;top:40%;
  text-align: center;
  color:#888;
  background: #fff;
  padding:12px
}
</style>