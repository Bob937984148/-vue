<template>
   <div class="shop">
     <div class="shop-header">
       <div class="shop-title">
         订单
       </div>
       <div class="email">
         <a href="javascript:;"></a>
       </div>
       <div class="tabs" >
         <a class="item" @click="toggle(1)" :class="{'on':hasshow1}" href="javasprit:;">全部</a>
         <a class="item" @click="toggle(2)" :class="{'on':hasshow2}" href="javasprit:;">代付款</a>
         <a class="item" @click="toggle(3)" :class="{'on':hasshow3}" href="javasprit:;">已取消</a>
         <span class="line" :class="{'lineO1':line1,'lineO2':line2}"></span>
       </div>
     </div>
    <div v-if="listshow==1">
    <div class="wrapper1"  v-for="item in list" :key="item[0].user_id" >
          <div class="hd" >
            <!-- <span class="level">{{item.lv}}级</span> -->
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
          <div class="lyj-btn">
            <a href="javascript:;" class="lyj-btn1" @click="delet(item[0].user_id)">取消订单</a>
            <a href="javascript:;" class="lyj-btn2">立即支付</a>
          </div>
    </div>
    </div>
    <div class="spinner" v-if="!hasshow1">
      <i class="icon-empty"></i>
      <div class="empty-text">目前没有任何订单哦</div>
    </div>


   </div>
</template>
<script>
   //练习1:创建元素
   //练习2:发送请求获取购物车列表中数据
   //练习3:小计
  export default {
    created() {
      this.shopList();
      
    },
    computed:{
      getSubTotal:function(){
        //累加求和购物车所有商品
        var sum=0;
        for(var item of this.list){
          sum+=item.price*item.count;
        }
        return sum;
      }
    },
    data(){
      return {
        list:[],
        hasshow1:true,
        hasshow2:false,
        hasshow3:false,
        line1:false,
        line2:false,
        isShow:true,
        listshow:1,
        lyjshoplist:0,
      }
    },
    methods:{
      toggle(res){
        this.hasshow1=false;
        this.hasshow2=false;
        this.hasshow3=false;
        this.line1=false;
        this.line2=false;   
        this.listshow=0;
       if(res==1){
         this.hasshow1=true;
         this.listshow=1;
       }else if(res==2){
        this.line1=true;
        this.hasshow2=true;
        this.listshow=0;
        
       }else if(res==3){
         this.line2=true
         this.hasshow3=true
         this.listshow=0;
       }
      },
			updateItemCount(id,count){
				//同步购物车数量
				//id  购物车id
				//count 购物车中数量
				var url="http://127.0.0.1:3000/updateCart?id="+id+"&count="+count;
				this.axios.get(url).then(result=>{
					
				})
			},
      cartSub(e){
				var id=e.target.dataset.id;
				for(var item of this.list){
					if(item.id== id && item.count>1){
						item.count--;
						//同步数据
						this.updateItemCount(item.id,item.count);
						break;
					}
				}
      },
      cartAdd(e){
        //1:获取当前按钮绑定购物车id
        var id = e.target.dataset.id
        //2:创建循环购物车数组内容
        for(var item of this.list){
        //3:判断当前元素id是否与元素id
          if(item.id == id){
            //4:修改数据
						item.count++;
						this.updateItemCount(item.id,item.count);
            break;
          }
        }
      },
      shopList(){
        var shoplist1=this.$store.state.shoplist1
        for(var i in shoplist1){
        var url = `http://127.0.0.1:3000/home?id=${shoplist1[i]}`;
        this.axios.get(url).then(result=>{
        this.list.push(result.data);
        
         })
       }
      },
      delet(x){
        
        var ind = this.$store.state.shoplist1.indexOf(`${x}`);
        this.$store.state.shoplist1.splice(ind,1); 
        this.$router.push(`/home`);
      }
    }
  }  
</script>
<style> 
  /* .search-f{display: none} */
  .shop-header{
    background:#fff;
    position:relative
    }
  .shop-title{
    font-size: 22px;
    text-align: center;
    font-weight: 700;
    padding-top:20px;
  }
  .email{
    background-image: url("../img/email.svg")
  }
  .line{
    background: #e74e4b;
    border-radius: 25%;
    position: absolute;
    left:95px;bottom:5px;
    width:25px;height:4px;
    transition:left .5s;
  }
  .lineO1{
    position: absolute;
    left:326px;bottom:5px !important;
    transition:left .5s;
  }
  .lineO2{
    position: absolute;
    left:566px;bottom:5px !important;
    transition:left .5s;
  }
  .tabs{padding-top:60px;padding-bottom:15px;}
  .tabs .item{
    margin-left:90px;
    margin-right:90px;
    color: #888;
    font-size:20px;
    }
  .on{
    font-weight: 700;
    color: #1e1e1e !important;
  }
  .wrapper1{
    background-color: #fff;
    width:750px;
    margin-top:8px;
    padding-bottom: 70px;
    /* position:absolute;  
    left:426px;top:132px; */
  }
  .hd{
    padding-top:10px;
  }
.icon-empty{
  width:208px;height: 152px;
  position:absolute;
  left:680px;top:296px;
  background-image: url("../img/icon-empty.png");
  background-size: 100% 100%;
}
.empty-text{
  font-size: 20px;
  color: #888;
  margin-top:310px;
  text-align: center;
}
.lyj-btn{
  float:right;
  font-size:20px;
  margin-top:20px;
}
.lyj-btn1{
  margin:20px;
  padding:6px;
  color: #1e1e1e;
  border:1px solid  #e5e5e5;
  border-radius: 35%;
}
.lyj-btn2{
  margin:20px;
  padding:6px;
  color: #e74e4b;
  border:1px solid  #e74e4b;
  border-radius: 35%;
}
</style>