<template>
    <div id="yj-main">
        <div class="yj-h yj-bj-b">
            <a href="http://127.0.0.1:3001/#/my"><i class="yh-i1"></i></a>
            <div>意见反馈</div>
            <i class="yh-i2"></i>
            <div style="clear：both;"></div>
        </div>
        <div class="yj-b yj-mt yj-bj-b">
            <textarea v-model='kwords' name="反馈"  cols="30" rows="9" placeholder="请留下您在使用过程中遇到的问题，或提出宝贵建议" maxlength="500" ></textarea>
            <div>{{val}}</div>
        </div>
        <div class="yj-f yj-mt yj-bj-b">
            <div>
                <i>联系电话</i>
                <input type="number" placeholder="选填，便于我们联系您"/>
            </div>
        </div>
        <div class="yj-bt">
            <button @click="tj">提交</button>
        </div>
        <div id="yj-tishi" v-show='ts'>
            <div>{{tishi}}</div>
        </div>
    </div>
</template>
<script>
import {Toast} from 'mint-ui';
export default {
    data(){
        return{
            val:'0/500',
            kwords:'',
            tishi:'',
            ts:false,
        }
    },
    watch:{
        kwords(){
            this.va();
        }
    },
    methods:{
        va(){
            var x=this.kwords;
            this.val=x.length+'/500';
        },
        isfalse(){
            this.ts=false;
        },
        tj(){
            var reg=/[\u4e00-\u9fa5_a-zA-Z0-9]+/;
            if(reg.test(this.kwords)){
                this.tishi='感谢您的反馈！';
            }else{
                this.tishi='请做有效的输入！';
            }
            this.kwords='';
            this.ts=true;
            setTimeout(this.isfalse,1000);
        }
    }
}
</script>
<style>
#yj-tishi{
    position: relative;
    width: 281px;
    top:-265px;
    left:241px;
    background-color: rgba(0,0,0,0.4);
    border-radius: 7px;
}
#yj-tishi>div{
    padding: 20px;
    font-size: 30px;
    color: #fff;
}
#yj-main{
    width: 750px;
    margin: 0 auto;
}
.yj-h{
    width: 100%;
    height: 63px;
    padding: 18px 20px;
}
.yh-i1{
    float: left;
    display: block;
    width:26px;height: 26px; 
    background-image: url('http://127.0.0.1:3000/img/式神录爬虫/小图/后退.png');
    background-size: cover;
}
.yh-i2{
    float: left;
    margin-top:10px;
    display: block;
    width:26px;height: 8px; 
    background-image: url('http://127.0.0.1:3000/img/式神录爬虫/小图/三点.png');
    background-size: cover;
}
.yj-h div{
    font-size: 25px;
    font-weight: 700;
    width: 654px;
    float: left;
    display:flex;
    justify-content:center;
    align-items:center;
}
.yj-b{
    width: 100%;
}
.yj-b textarea{
    margin: 0;padding:14px 21px;
    border: none;
}
.yj-b div{
    color: #888;
    padding: 0;
    text-align: right;
    margin-top:-4px;
    font-weight: bold;
}
.yj-f{
    width: 100%;

}
.yj-f input{
    width: 639px !important;
    border: none !important;
    margin: 0 !important;
}
.yj-f div{
    padding: 14px 21px;
}
.yj-bt{
    margin-top:20px; 
}
.yj-bt button{
    width: 100%;
    height: 61px;
    border-radius: 30px;
    background:#e74e4b;
    color: #fff;
    font-size:23px;
    font-weight:300;
}
.yj-mt{
    margin-top:7px;
}
.yj-bj-b{
    background: #fff;
}
.app-container{
    padding: 0;
}
</style>

