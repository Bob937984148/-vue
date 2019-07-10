<template>
    <div id="sj-main">
        <div class="sj-h ">
            <a href="http://127.0.0.1:3001/#/my"><i class="sh-i1"></i></a>
            <div>绑定手机</div>
            <i class="sh-i2"></i>
            <div style="clear：both;"></div>
        </div>
        <div class="sj-b">
            <img src="http://127.0.0.1:3000/img/式神录爬虫/小图/黑圈叹号.png">
            <span class="sj-b-sp">为保障您的账号安全，需要验证您在网易通行证设置的手机号。</span>
            <div class="sj-b-d">网易通行证设置的手机号</div>
            <span class="sj-b-sp1">{{phone}}</span>
            <div class="sj-b-d1">
                <input type="number" placeholder="短信验证码" oninput="if(value.length>6)value=value.slice(0,6)" v-model="ks">
                <button @click="hqdxyzm" :style='pstyle'>{{dxyzxx}}</button>
            </div>
            <button :class="yzys">验证</button>
        </div>

    </div>
</template>
<script>
import {Toast} from 'mint-ui';
export default {
    data(){
        return{
            ph_list:[],
            phone:'',
            ks:'',
            yzys:'sj-b-bt1',
            n:60,
            kk:null,
            dxyzxx:'获取短信验证码',
            pstyle:''
        }
    },
    created(){
        this.getuser();
    },
    mounted(){
    },
    watch:{
        ks(){
            this.ipvl();
        }
    },
    methods:{
        djs(){
            if(this.n<2){
                clearInterval(this.kk);
                this.n=60;
                this.pstyle='';
                this.dxyzxx='获取短信验证码'
            }else{
                this.n-=1;
                this.dxyzxx=this.n+'秒后重发'
            }
        },
        hqdxyzm(){
            this.kk=setInterval(this.djs,1000);
            this.pstyle='color:#888';
            Toast('发送成功！');
        },
        ipvl(){
            var ivalue=this.ks;
            if(ivalue.length==6){
                this.yzys='sj-b-bt1-red sj-b-bt1';
            }else{
                this.yzys='sj-b-bt1';
            }
        },
        getuser(){
            this.axios.get('http://127.0.0.1:3000/getuser').then((result)=>{
                this.ph_list=result.data[0];
                this.islogin();
            })
        },
        islogin(){
            if(this.ph_list[0]=='-1'){
                this.$router.push({path:'/login'});
            }else{
                var p=this.ph_list.phone;
                this.phone='(+86)'+p.slice(0,3)+'****'+p.slice(7,11);
            }
        }
    }
}
</script>
<style>
#sj-main{
    width: 750px;
    margin: 0 auto;
}
.sj-h{
    width: 100%;
    height: 63px;
    padding: 18px 20px;
    background-color: #fff;
    border-bottom: 1px solid #ddd;
}
.sh-i1{
    float: left;
    display: block;
    width:26px;height: 26px; 
    background-image: url('http://127.0.0.1:3000/img/式神录爬虫/小图/后退.png');
    background-size: cover;
}
.sh-i2{
    float: left;
    margin-top:10px;
    display: block;
    width:26px;height: 8px; 
    background-image: url('http://127.0.0.1:3000/img/式神录爬虫/小图/三点.png');
    background-size: cover;
}
.sj-h div{
    font-size: 23px;
    font-weight: 700;
    width: 654px;
    float: left;
    display:flex;
    justify-content:center;
    align-items:center;
}
.sj-b{
    padding: 25px;
}
.sj-b img{
    width: 21px;
    height: 21px;
    margin-bottom: -3px;
}
.sj-b-sp{
    padding-left: 5px;
    font-size: 21px;
}
.sj-b-d{
    display: inline-block;
    margin-top: 70px;
    width: 230px;
    font-size: 20px;
    font-weight: 200;
}
.sj-b-sp1{
    font-weight: bolder
}
.sj-b-d1{
    padding: 20px 20px 20px 20px;
    margin-top: 20px;
    height:70px;
    border: 1px solid #ddd;
    border-radius: 7px; 
    background-color: #fff;
}
#sj-main .sj-b-d1 input{
    padding: 0;
    padding-top:6px;
    height: 30px;
    margin: 0;
    width: 468px;
    border: none;
}
#sj-main .sj-b-d1 input::-webkit-input-placeholder{
    font-size: 23px;
    font-weight:500;
    color:#888;
}
.sj-b-d1 button{
    color:#e74e4b;
    font-size: 23px;
    font-weight:500;
    border:none;
    border-left: 1px solid #ddd;
    border-radius: 0px;
    width: 180px;
    padding: 0;
    padding-left: 20px;
}
#sj-main .sj-b-bt1{
    margin-top: 20px;
    width: 100%;
    height: 61px;
    background-color: #ccc;
    border: none;
    border-radius: 30px; 
    color: #fff;
    font-size: 23px;
}
#sj-main .sj-b .sj-b-bt1-red{
    background-color: #e74e4b;
}
</style>
