<template>
    <div id="dj-main">
        <div class="dj-h ">
            <a href="http://127.0.0.1:3001/#/my"><i class="dh-i1"></i></a>
            <div>我的出售</div>
            <i class="dh-i2"></i>
            <div style="clear：both;"></div>
        </div>
        <div class="dj-hh" @click="dj">
            <a >登记中</a>
            <a >登记成功</a>
            <a >登记取消</a>
            <a >全部</a>
        </div>
        <div>
            <div id="dj-xhb">
                <div></div>
            </div>
        </div>
        <div class="dj-lb">
            <div class="dj-lb-wd">
                <div>
                    <img>
                    <p>暂无相关物品</p>
                </div>
                <div>
                    <a href="http://127.0.0.1:3001/#/myshop"><span>若大人的角色商品登记成功且上架过藏宝阁，对该商品后续的操作需在【我的出售】进行</span></a>
                    <img>
                    <p>暂无相关物品</p>
                </div>
                <div>
                    <img>
                    <p>暂无相关物品</p>
                </div>
                <div>
                    <a href="http://127.0.0.1:3001/#/myshop"><span>若大人的角色商品登记成功且上架过藏宝阁，对该商品后续的操作需在【我的出售】进行</span></a>
                    <img>
                    <p>暂无相关物品</p>
                </div>
            </div>
        </div>
        <button>我要登记</button>
    </div>
</template>
<script>
export default {
    data(){
        return{
            mydj:[]
        }
    },
    created(){
        this.getuser();
    },
    methods:{
        getuser(){
            this.axios.get('http://127.0.0.1:3000/getuser').then((result)=>{
                this.mydj=result.data[0];
                this.islogin();
            })
        },
        islogin(){
            if(this.mydj[0]=='-1'){
                this.$router.push({path:'/login'});
            }
        },
        dj:function(e){
            var wd=document.getElementsByClassName('dj-lb-wd')[0];
            var xhb=document.getElementById('dj-xhb');
            var hh=document.getElementsByClassName('dj-hh')[0].children;
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
                xhb.style.transform='translateX(187px)';
                xhb.style.transition='all 0.4s linear';
            }
            if(c==hh[2]){
                wd.style.transform='translateX(-1500px)';
                wd.style.transition='all 0.3s linear';
                xhb.style.transform='translateX(374px)';
                xhb.style.transition='all 0.4s linear';
            }
            if(c==hh[3]){
                wd.style.transform='translateX(-2250px)';
                wd.style.transition='all 0.3s linear';
                xhb.style.transform='translateX(561px)';
                xhb.style.transition='all 0.4s linear';
            }
        }
    }
}
</script>
<style>
#dj-main{
    width: 750px;
    margin: 0 auto;
}
#dj-xhb{
    width: 187px;
    height: 5px;
    display: flex;
    justify-content: center;
}
.dj-h{
    width: 100%;
    height: 63px;
    padding: 18px 20px;
    background-color: #fff;
}
.dh-i1{
    float: left;
    display: block;
    width:26px;height: 26px; 
    background-image: url('http://127.0.0.1:3000/img/式神录爬虫/小图/后退.png');
    background-size: cover;
}
.dh-i2{
    float: left;
    margin-top:10px;
    display: block;
    width:26px;height: 8px; 
    background-image: url('http://127.0.0.1:3000/img/式神录爬虫/小图/三点.png');
    background-size: cover;
}
.dj-h div{
    font-size: 23px;
    font-weight: 700;
    width: 654px;
    float: left;
    display:flex;
    justify-content:center;
    align-items:center;
}
#dj-xhb>div{
    width: 26px;
    height: 4px;
    background-color: #e74e4b;
    border-radius: 2px;
}
.dj-hh+div{
    width: 100%;
    background-color: #fff;
    border-bottom: 1px solid #ddd;
    padding-bottom: 10px;
    margin-bottom:10px; 
}
#dj-main button{
    width: 100%;
    height: 61px;
    background-color: #e74e4b;
    border-radius: 30px;
    font-size: 22px;
    color:#fff;
}
.dj-lb{
    width: 750px;
    overflow: hidden;
}
.dj-lb-wd{
    width: 3000px;
    height: 600px;
}
.dj-lb-wd div img{
    display: inline-block;
    background-image: url('http://127.0.0.1:3000/img/式神录爬虫/小图/无登记图.png');
    width: 195px;
    height: 142px;
    background-size: cover;
    padding: 70px;
    margin: 212px 0 10px 299px;
}
.dj-lb-wd div a{
    display: block;
    float: left;
    width: 750px;
    height: 53px;
    background-color: rgb(255,250,239);
    padding: 15px;
}
.dj-lb-wd div a span{
    color: #e74e4b;
    font-size: 18px;
}
.dj-lb-wd div{
    width: 750px;
    float: left;
}
.dj-lb-wd div p{
    text-align: center;
    font-size: 20px;
}
.dj-hh{
    margin-top:-2px;
    height: 27px;
}
.dj-hh a{
    display: inline-block;
    width: 187px;
    height: 27px;
    color:#888;
    text-align: center;
    background-color: #fff;
}
</style>
