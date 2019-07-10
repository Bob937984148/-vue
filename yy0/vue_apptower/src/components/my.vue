<template>
    <div id="my-main">
        <div class="mb-1  my-gd">
            <div class="my-title">我的藏宝阁</div>
            <a href="" class="my-yjtb"><i class='my-main-i'></i></a>
        </div>
        <div style="width:100%;height:507px;"></div>
        <div class="my-bj mb-1">
            <p class="my-hj" v-html="vhtml">
                <!-- <i class="my-tou"></i>
                <img :src="'http://127.0.0.1:3000/'+user.uimg" > -->
            </p>
            <p class="my-hj" v-html="vhtml1">
                <!-- <button id="my-login">登录</button>
                <span >{{user.nickname}}</span> -->
            </p>
        </div>
        <div class="mb-1 kheight">
            <ul class="mui-table-view">
                <li class="mui-table-view-cell">
                    <a class='my-zd-a' href="http://127.0.0.1:3001/#/mycollect">
                        <img class='my-img' src="http://127.0.0.1:3000/img/式神录爬虫/小图/收藏图标.png">
                        <div>我的收藏</div>
                        <i class="my-i"></i>
                    </a>
                </li>
            </ul>
        </div>
        <div class="mb-1">
            <ul class="mui-table-view">
                <li class="mui-table-view-cell">
                    <a class='my-zd-a' href="http://127.0.0.1:3001/#/mydj">
                        <img class='my-img' src="http://127.0.0.1:3000/img/式神录爬虫/小图/登记.png">
                        <div>我的登记</div>
                        <i class="my-i"></i>
                    </a>
                </li>
                <li class="mui-table-view-cell">
                    <a class='my-zd-a' href="http://127.0.0.1:3001/#/myshop"> 
                        <img class='my-img' src="http://127.0.0.1:3000/img/式神录爬虫/小图/出售.png">
                        <div>我的出售</div>
                        <i class="my-i"></i>
                    </a>
                </li>
                <li class="mui-table-view-cell">
                    <a class='my-zd-a' href="http://127.0.0.1:3001/#/wyzf">
                        <img class='my-img' src="http://127.0.0.1:3000/img/式神录爬虫/小图/支付.png">
                        <div>&nbsp;网易支付</div>
                        <i class="my-i"></i>
                    </a>
                </li>
            </ul>
        </div>
        <div class="mb-1">
            <ul class="mui-table-view">
                <li class="mui-table-view-cell">
                    <a class='my-zd-a' href="http://127.0.0.1:3001/#/shouji">
                        <img class='my-img' src="http://127.0.0.1:3000/img/式神录爬虫/小图/手机号.png">
                        <div>&nbsp;手机号</div>
                        <i class="my-i"></i>
                    </a>
                </li>
                <li class="mui-table-view-cell">
                    <a class='my-zd-a' href="http://127.0.0.1:3001/#/help">
                        <img class='my-img' src="http://127.0.0.1:3000/img/式神录爬虫/小图/帮助.png">
                        <div>帮助中心</div>
                        <i class="my-i"></i>
                    </a>
                </li>
                <li class="mui-table-view-cell">
                    <a class='my-zd-a' href="http://127.0.0.1:3001/#/yjfk">
                        <img class='my-img' src="http://127.0.0.1:3000/img/式神录爬虫/小图/意见.png">
                        <div>意见反馈</div>
                        <i class="my-i"></i>
                    </a>
                </li>
            </ul>
        </div>
        <div class="mb-1 my-outlgin" v-if='show'>
            <ul class="mui-table-view">
                <li class="mui-table-view-cell my-jz">
                    <a class='my-zd-a my-tc' href="http://127.0.0.1:3001/#/shoucang">退出登录
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
            user:[],
            vhtml:'',
            vhtml1:'',
            show:false,//控制元素隐藏与显示，false为隐藏，true为显示
            
        }
    },
    created(){
        this.getuser();
        },
    mounted(){
    },
    methods:{
        getel(){
            // var outlogin=document.getElementsByClassName('my-outlgin')[0];
            console.log(this.user.id);
            if(this.user.id=='-1'){
                    this.vhtml='<i class="my-tou"></i>'
                    this.vhtml1='<button id="my-login">登录</button>';
                    this.show=false;
                    // outlogin.style.display='none';
            }else{
                this.$nextTick(()=>{
                    this.vhtml="<img src='http://127.0.0.1:3000/"+this.user.uimg+"'>";
                    this.vhtml1=`<span >${this.user.nickname}</span>`;
                    this.show=true;
                    // outlogin.style.display='block';
                })
            }
        },
        getuser(){
            this.axios.get('http://127.0.0.1:3000/getuser').then((result)=>{
                this.user=result.data[0];
                this.getel();
            })
        }
    }
}
</script>
<style>
#my-main{
    width: 750px;
    margin: 0 auto;
    /* display: flex; */
    flex-direction: column;
    overflow: auto;
}
#my-main .my-zd-a{
    display: flex;
    justify-content:space-between;
    font-size: 20px;
    width: 735px;
    margin: -3px -15px !important;
}
#my-main .my-zd-a div{
    /* display: inline-block; */
    width: 655px;
    margin-top:7px; 
}
.khright{
    height: 75px;
}
#my-login+span{
    font-size: 20px;
    color: #ddd;
}
#my-main .my-i{
    display: inline-block;
    margin-top: 10px;
    width: 9px;
    height: 15px;
    background-image: url('http://127.0.0.1:3000/img/式神录爬虫/小图/右括号.png');
}
.my-tou{
    /* position: relative; */
    display: block;
    width: 126px;
    height: 126px;
    border-radius: 50%;
    background-image: url('http://127.0.0.1:3000/img/式神录爬虫/主页/tou.png');
    background-size: cover;
    justify-content:space-between;
    /* top:10%;
    left:40%; */

}
.my-bj>p>img{
    width: 126px;
    height: 126px;
    border-radius: 50%;
    justify-content:space-between;
}
.my-hj{
    display: flex;
    justify-content:center;
}
.my-title{
    width: 105px;
    font-size: 20px;
    font-weight: bolder;
    margin: 18px auto;
}
.my-bj{
    position:absolute;
    top:63px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    width: 750px;
    height: 475px;
    background-image: url('http://127.0.0.1:3000/img/式神录爬虫/主页/header-bg.jpg');
    background-repeat:repeat-y;
}
.my-gd{
    width: 750px;
    height: 63px;
    background: #fff;
    position:fixed;
    top:0;
    z-index: 5;
}
.my-main-i{
    background-image: url("http://127.0.0.1:3000/img/式神录爬虫/小图/邮件图标.png");
    width: 25px;height: 22px;
    display: block;
    position: relative;
    left: 705px;
    top:-37px;
}
.my-jz{
    text-align: center;
}
#my-main .my-bj p button{
    width: 80px;
    height: 40px;
    border:1px solid #e74e4b;
    background: #e74e4b;
    border-radius: 20px 20px 20px 20px;
    font-size:1.3rem;
    color:#fff;
}
.mb-1{
    margin-bottom: 0.4rem;
}

.my-img{
    margin: 5px 26px 0 5px;  
}
#my-main .my-tc{
    display: block;
    font-size: 22px;
    color:#e74e4b;
    margin: 7px;
    text-align: center;
}
#my-main .my-bj p span{
    color:#fff;
    font-size: 23px;
}
</style>

