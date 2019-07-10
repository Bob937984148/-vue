<template>
    <div id="ms-main">
        <div class="ms-h ">
            <a href="http://127.0.0.1:3001/#/my"><i class="mh-i1"></i></a>
            <div>我的出售</div>
            <i class="mh-i2"></i>
            <div style="clear：both;"></div>
        </div>
        <div class="sp-hh" @click="dj">
            <a >全部</a>
            <a >上架中</a>
            <a >未上架</a>
            <a >已售出</a>
            <a >已取回</a>
        </div>
        <div>
            <div id="sp-xhb">
                <div></div>
            </div>
        </div>
        <div class="sp-lb">
            <div class="sp-lb-wd">
                <div>
                    <img>
                    <p>您还没有出售的商品</p>
                    <p>想要出售的商品，需先登记成功后才能出售哦～</p>
                    <button>我要登记</button>
                </div>
                <div>
                    <img>
                    <p>暂无相关商品</p>
                </div>
                <div>
                    <img>
                    <p>暂无相关商品</p>
                </div>
                <div>
                    <img>
                    <p>暂无相关商品</p>
                </div>
                <div>
                    <img>
                    <p>暂无相关商品</p>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    data(){
        return{
            mshop:[]
        }
    },
    created(){
        this.getuser();
    },
    methods:{
        getuser(){
            this.axios.get('http://127.0.0.1:3000/getuser').then((result)=>{
                this.mshop=result.data[0];
                this.islogin();
            })
        },
        islogin(){
            if(this.mshop[0]=='-1'){
                this.$router.push({path:'/login'});
            }
        },
        dj:function(e){
            var wd=document.getElementsByClassName('sp-lb-wd')[0];
            var xhb=document.getElementById('sp-xhb');
            var hh=document.getElementsByClassName('sp-hh')[0].children;
            var c=e.target;
            for(var x of hh){
                x.style.color='#888';
                x.style.fontSize='18px';
            }
            c.style.color='#333';
            c.style.fontSize='23px';
            if(c==hh[0]){
                wd.style.transform='translateX(0px)';
                wd.style.transition='all 0.3s linear';
                xhb.style.transform='translateX(0px)';
                xhb.style.transition='all 0.4s linear';
            }
            if(c==hh[1]){
                wd.style.transform='translateX(-750px)';
                wd.style.transition='all 0.3s linear';
                xhb.style.transform='translateX(150px)';
                xhb.style.transition='all 0.4s linear';
            }
            if(c==hh[2]){
                wd.style.transform='translateX(-1500px)';
                wd.style.transition='all 0.3s linear';
                xhb.style.transform='translateX(300px)';
                xhb.style.transition='all 0.4s linear';
            }
            if(c==hh[3]){
                wd.style.transform='translateX(-2250px)';
                wd.style.transition='all 0.3s linear';
                xhb.style.transform='translateX(450px)';
                xhb.style.transition='all 0.4s linear';
            }
            if(c==hh[4]){
                wd.style.transform='translateX(-3000px)';
                wd.style.transition='all 0.3s linear';
                xhb.style.transform='translateX(600px)';
                xhb.style.transition='all 0.4s linear';
            }
        },
    }
}
</script>
<style>
#ms-main{
    width: 750px;
    margin: 0 auto;
}
#sp-xhb{
    width: 150px;
    height: 5px;
    display: flex;
    justify-content: center;
}
.ms-h{
    width: 100%;
    height: 63px;
    padding: 18px 20px;
    background-color: #fff;
}
.mh-i1{
    float: left;
    display: block;
    width:26px;height: 26px; 
    background-image: url('http://127.0.0.1:3000/img/式神录爬虫/小图/后退.png');
    background-size: cover;
}
.mh-i2{
    float: left;
    margin-top:10px;
    display: block;
    width:26px;height: 8px; 
    background-image: url('http://127.0.0.1:3000/img/式神录爬虫/小图/三点.png');
    background-size: cover;
}
.ms-h div{
    font-size: 23px;
    font-weight: 700;
    width: 654px;
    float: left;
    display:flex;
    justify-content:center;
    align-items:center;
}
#sp-xhb>div{
    width: 26px;
    height: 4px;
    background-color: #e74e4b;
    border-radius: 2px;
}
.sp-hh+div{
    width: 100%;
    background-color: #fff;
    border-bottom: 1px solid #ddd;
    padding-bottom: 10px;
    margin-bottom:10px; 
}
.sp-hh{
    margin-top:-2px;
    height: 27px;
}
.sp-hh a{
    display: inline-block;
    width: 150px;
    height: 27px;
    color:#888;
    text-align: center;
    background-color: #fff;
}
.sp-lb{
    width: 750px;
    overflow: hidden;
}
.sp-lb-wd{
    width: 3750px;
}
.sp-lb-wd div{
    width: 710px;
    float: left;
    background-color: #F1F1F1;
    margin: 20px;
    text-align: center;
}
.sp-lb-wd div img{
    background-image: url('http://127.0.0.1:3000/img/式神录爬虫/小图/无出售图.png');
    background-size: cover;
    width: 196px;
    height: 143px;
    margin-top: 150px;
    border: none;
}
.sp-lb-wd div p{
    font-size: 20px;
    color:#999;
}
.sp-lb-wd div button{
    width: 95%;
    height: 61px;
    background-color: #e74e4b;
    border-radius: 30px;
    font-size: 22px;
    color:#fff;
}
</style>
