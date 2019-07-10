<template>
    <div id="pf-main">
        <div v-for='item in list' :key='item.id' class="pffl">
            <img :src="'http://127.0.0.1:3000/'+item.src" class="dw">
            <p>{{item.pname}}</p>
        </div>
        <div style='clear:both;'></div>
            <span>仅显示高级徽章</span>
    </div>
</template>
<script>
export default {
    data(){
        return{
            list:[],
        }
    },
    created(){
        this.gethz();
    },
    methods:{
        gethz(){
            var url=`http://127.0.0.1:3000/gethz`;
            this.axios(url).then((result)=>{
                console.log(result.data);
                this.list=result.data;
            })
        },
    }
}
</script>
<style>  /*解决页面跳转样式失效问题*/
#pf-main{width: 760px;}
.pffl{
    width: 20%;
    float: left;
    height: 170px;
}
#pf-main .pffl p{
    width: 80px;
    margin: 0 auto;
}
.pffl .dw{
    width: 125px;
    height: 125px;
}
#pf-main span{
    width: 126px;
    display: block;
    color:#888;
    font-size: 18px;
    margin-top: 15px;
    margin: 0 auto;
}
</style>
