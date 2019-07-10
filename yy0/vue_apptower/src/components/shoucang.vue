<template>
    <div style="width:760px;dispaly:flex;" id="sc-main">
        <div class="wk">
        <p>式神皮肤（总数：101）</p>
            <div v-for='item in bzclist' :key='item.id' class='fl' >
                    <img :src="'http://127.0.0.1:3000/'+item.src" class="bj">
                    <div class="k">
                        <div class="ht">{{item.pname}}</div>
                    </div>
            </div>
            <div style="clear:both;"></div>
        </div>
        <div class="wk">
            <p>阴阳师皮肤（总数：15）</p>
            <div v-for='item in bzcyys' :key='item.id' class='fl' >
                    <img :src="'http://127.0.0.1:3000/'+item.src" class="bj">
                    <div class="k">
                        <div class="ht">{{item.pname}}</div>
                    </div>
            </div>
            <div style="clear:both;"></div>
        </div>
        <div class="wk">
            <p>庭院皮肤（总数：5）</p>
            <div v-for='item in ty' :key='item.id' class="tyk fl">
                <img :src="'http://127.0.0.1:3000/'+item.src" class="bj ty">
                <img src="http://127.0.0.1:3000/img/式神录爬虫/小图/框.png" class="kk">
                <p>{{item.name}}</p>
            </div>
            <div style="clear:both;"></div>
        </div>
        <div class="wk">
            <p>头像框（总数：127）</p>
            <div v-for='item in touxk' :key='item.id' class='fl' >
                    <img :src="'http://127.0.0.1:3000/'+item.src" class="bj">
            </div>
        </div>
    </div>
</template>
<script>
export default {
    data(){
        return{
            bzclist:[],
            bzcyys:[],
            touxk:[],
            ty:[{id:1,src:'img/式神录爬虫/庭院皮肤/枫色秋庭.png',name:'枫色秋庭'},
                {id:2,src:'img/式神录爬虫/庭院皮肤/暖池青苑.png',name:'暖池青苑'},
                {id:3,src:'img/式神录爬虫/庭院皮肤/暖春翠庭.png',name:'暖春翠庭'},
                {id:4,src:'img/式神录爬虫/庭院皮肤/盛夏幽庭.png',name:'盛夏幽庭'},
                {id:5,src:'img/式神录爬虫/庭院皮肤/雪月华庭.png',name:'雪月华庭'},
            ]
        }
    },
    created(){
        this.getpf();
        this.getyyspf();
        this.txk();
    },
    methods:{
        getpf(){
            this.axios.get('http://127.0.0.1:3000/getpf').then((result)=>{
                // console.log(result.data[0].id);
                this.bzclist=result.data;
            })
        },
        getyyspf(){
            this.axios.get('http://127.0.0.1:3000/getyyspf').then((result)=>{
                this.bzcyys=result.data;
            })
        },
        txk(){
            this.axios.get('http://127.0.0.1:3000/txk').then((result)=>{
                this.touxk=result.data;
            })
        },

    }
}
</script>
<style >
 #sc-main{
    overflow: auto;
}
#sc-main .fl{
    position: relative;
    float: left;
    width: 23%;
    margin-bottom: 2rem;
    margin-left: 10px;
}
#sc-main .k{ 
    position: absolute;
    width: 100%;
    background-image: url('http://127.0.0.1:3000/img/pfk.png');
    background-size:cover;
    height: 277px;
    z-index: 1;
    top:-10px;
    left: -1px;
}
#sc-main .kk{
    position: absolute;
    width: 93%;
    top:-7px;
    left: -5px;
    margin-left: 20px;
}
#sc-main .ht{
    width:21%;
    font-size:1.2rem;
    color:#fff;
    padding-left:10px;
    padding-top: 1rem;
}
#sc-main .bj{
    width: 96%;
    padding-left: 10px;
    background-size:cover;
}
#sc-main .ty{
    width: 92%;
    margin-left: 12px; 
}
#main p{
    text-align: center;
    width: 100%;
}
#sc-main .wk{
    position: relative;
    width: 100%;
    height: auto;
}
#sc-main .wk>p{
    font-size: 20px;
    font-weight: bolder;
}
#sc-main .tyk{
    width: 48%;
}

</style>

