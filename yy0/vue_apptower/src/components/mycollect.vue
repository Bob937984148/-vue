<template>
    <div id="co-main">
        <div class="co-h ">
            <a href="http://127.0.0.1:3001/#/my"><i class="ch-i1"></i></a>
            <div>我的收藏</div>
            <i @click="qiehuan" class="ch-i2">编辑</i>
            <div style="clear：both;"></div>
        </div>
        <div id="wsct">
            <img src="http://127.0.0.1:3000/img/式神录爬虫/小图/无收藏图.png">
            <p>有时候，喜欢的商品，不收藏就错过了</p>
        </div>
    </div>
</template>
<script>
export default {
    data(){
        return{
            collect:[]
        }
    },created(){
        this.getuser();
    },
    methods:{
        getuser(){
            this.axios.get('http://127.0.0.1:3000/getuser').then((result)=>{
                this.collect=result.data[0];
                this.islogin();
            })
        },
        islogin(){
            if(this.collect[0]=='-1'){
                this.open('http://127.0.0.1:3001/#/login');
            }
        },
        qiehuan(){
            var i2=document.getElementsByClassName('ch-i2')[0];
            if(i2.innerHTML=='编辑'){
                i2.innerHTML='取消';
            }else{
                i2.innerHTML='编辑';
            }
        }
    }
}
</script>
<style>
#co-main{
    width: 750px;
    margin: 0 auto;
}
.co-h{
    width: 100%;
    height: 63px;
    padding: 18px 20px;
    background-color: #fff;
}
.ch-i1{
    float: left;
    display: block;
    width:26px;height: 26px; 
    background-image: url('http://127.0.0.1:3000/img/式神录爬虫/小图/后退.png');
    background-size: cover;
}
.ch-i2{
    float: left;
    display: block;
    width:44px;height: 21px; 
    font-weight: 600;
    font-size: 20px;
}
#co-main .co-h div{
    font-size: 23px;
    font-weight: 700;
    width: 634px;
    float: left;
    display:flex;
    justify-content:center;
    align-items:center;
}
#wsct img{
    display: block;
    margin: 130px auto 20px auto;
}
#wsct p{
    text-align: center;
    font-size: 20px;
}
</style>
