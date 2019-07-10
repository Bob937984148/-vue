<template>
    <div id="hp-main">
        <div class="hp-h ">
            <a href="http://127.0.0.1:3001/#/my"><i class="hh-i1"></i></a>
            <div>帮助中心</div>
            <i class="hh-i2"></i>
            <div style="clear：both;"></div>
        </div>
        <div class="hp-hh" @click="dj">
            <a >购买问题</a>
            <a >出售问题</a>
            <a >其他问题</a>
        </div>
        <div>
            <div id="hp-xhb">
                <div></div> 
            </div>
        </div>
        <div class="hp-lb">
            <div class="hp-lb-wd">
                <div  class="hp-lb-d hp-gm-dj">
                    <ul @click="gmdj">
                        <li>1. 怎么挑选想买的角色？
                            <div>
                                <p> 1. 进入首页点击“全部商品”。</p>
                                <p> 2. 在商品列表，点击右上角的【筛选】，根据您的需要选择相对应的操作系统 、 区服、价格区间、等级、式神、阴阳术、资产、斗技、皮肤和素材，点击【完成】即可查看到对应的角色。 </p>
                            </div>
                        </li>
                        <li>2. 如何购买？
                            <div>
                                <p>在角色详情页点击【立即购买】，确认您的使用的购买账号、平台等信息，支付成功后即完成购买。</p>
                                <p>• 下单后，订单支付时间为3小时，若超出支付时间仍未完成付款，系统则会自动取消订单。若仍想继续购买该角色，则需要重新下单。</p>
                                <p>• 若多个玩家同时对同一商品下单，第一个完成支付的玩家将成功购买。</p>
                            </div>
                        </li>
                        <li>3. 支持哪些支付方式？
                            <div>
                                <p>藏宝阁内交易均使用“网易支付”（网易公司为方便用户进行网上交易，推出的安全、稳定、快捷的在线支付平台）进行付款，支持使用的支付方式有：</p>
                                <p>• 网易支付余额</p>
                                <p>• 快捷支付（储蓄卡及信用卡）</p>
                                <p>• 手机网银（储蓄卡及信用卡）</p>
                            </div>
                        </li>
                        <li>4. 购买的角色怎么使用？
                            <div>
                                <p>1. 购买成功后，使用收货账号登录对应的游戏区服，即可查看到您购买的角色。</p>
                                <p>2. 若登录后未显示，可能是网络延迟问题，请10分钟后重试。</p>
                                <p>3. 购买角色不涉及游戏账号的交易。</p>
                                <p>4. 为保护卖家信息安全，购买的角色将被清除好友等个人信息。</p>
                            </div>
                        </li>
                    </ul>
                </div>
                <div  class="hp-lb-d hp-sp-dj">
                    <ul @click="spdj">
                        <li>1. 什么样的角色才能出售？
                            <div>
                                <p>1.满足以下两个条件的角色才能在藏宝阁出售：</p>
                                <p>• 等级满足60级，且至少拥有3个不同的SSR式神（两面佛除外）；</p>
                                <p>• 角色在游戏内无违规行为；</p>
                                <p>2.交易只涉及用户在游戏内的角色，您原有的网易通行证账号归属保持不变。</p>
                            </div>
                        </li>
                        <li>2. 角色出售流程是怎样的？
                            <div>
                                <p> 角色的出售流程包括：<br>
                                   1. 登记角色  2. 游戏内确认  3.上架  4. 出售   5. 考察  6. 收款。 
                                </p>
                                <h3>1. 登记角色</h3>
                                <p>登录藏宝阁后，点击【登记出售】，在登记列表中找到【我要登记】；</p>
                                <img src="http://127.0.0.1:3000/img/式神录爬虫/小图/shop1.png">
                                <p>选择想要出售的角色：</p>
                                <img src="http://127.0.0.1:3000/img/式神录爬虫/小图/shop2.png">
                                <p>点击【确定登记】：</p>
                                <img src="http://127.0.0.1:3000/img/式神录爬虫/小图/shop3.png">
                                <p>查看到已登记说明（登记期为7天）。</p>
                                <img src="http://127.0.0.1:3000/img/式神录爬虫/小图/shop4.png">
                                <h3>2. 游戏内确认</h3>
                                <p>请在藏宝阁登记后3天内，到游戏庭院左边【网易精灵】灯笼 -【精灵推荐】-【藏宝阁登记确认】内确认。</p>
                                <img src="http://127.0.0.1:3000/img/式神录爬虫/小图/shop5.png">
                                <img src="http://127.0.0.1:3000/img/式神录爬虫/小图/shop6.png">
                                <h3>3. 上架</h3>
                                <p>在【我的登记】中找到登记成功的商品，点击【上架】，查看相关的上架说明；</p>
                                <img src="http://127.0.0.1:3000/img/式神录爬虫/小图/shop7.png">
                                <p>设置角色在藏宝阁的上架天数和售价，点击【上架】后完成；</p>
                                <img src="http://127.0.0.1:3000/img/式神录爬虫/小图/shop8.png">
                                <h3>4. 公示期</h3>
                                <p> 角色首次上架成功后将进入24个小时的公示期，公示期内该角色不能被购买。 </p>
                                <h3>5. 出售</h3>
                                <p> 您的角色将在藏宝阁上展示，其他玩家可以直接购买。 </p>
                                <h3>6. 考察</h3>
                                <p>角色成功售出后，将有3天的考察期，保证买卖双方的交易安全。</p>
                                <p>考察期是指藏宝阁对成功订单进行审核的时间（3天）。</p>
                                <h3>7. 收款</h3>
                                <p>通过考察期后，您可以在网易支付余额中查看到您的资金收入。</p>
                            </div>
                        </li>
                        <li>3. 登记后可以取消吗？
                            <div>
                                <p>登记：指有出售意向的玩家预先把角色登记在藏宝阁（此时并未正式上架）。通过登记期后，方可作为商品上架销售。</p>
                                <p style="margin-top:20px;">1. 登记期为7天。在登记期间，玩家可自行取消登记。</p>
                                <p>2. 登记期结束后，玩家可在30天内登录藏宝阁前往【我的出售】手动确认上架，逾期则登记过期。如需出售，玩家需重新登记。</p>
                            </div>
                        </li>
                        <li>4. 角色上架后会展示哪些信息？
                            <div>
                                <p>目前藏宝阁上架会展示的信息：</p>
                                <p>1. 展示您所拥有的式神及式神的详细信息；<br>（式神包括：全部SSR式神、5星及以上的SR\R\N式神、黑达摩）</p>
                                <p>2. 展示您所拥有的资产、荣誉及结界卡信息；<br>（资产包括：金币、勾玉、符咒等）</p>
                                <p>3. 展示您的斗技/协同斗技积分及段位；</p>
                                <p>4. 展示您此角色里全部+15的御魂和在上述第1条中式神已装备的御魂；</p>
                                <p>5. 展示4位主角的情报、技能等级、御灵等级信息；</p>
                                <p>6. 展示您所拥有的式神皮肤、阴阳师皮肤、御灵皮肤、庭院皮肤及头像框。</p>
                            </div>
                        </li>
                        <li>5. 上架后怎么取回游戏？
                            <div>
                                <p>请您按以下步骤将角色取回游戏：</p>
                                <p>1.在“我的-我的出售”中找到需要取回的角色；</p>
                                <p>2.点击“下架”；</p>
                                <p>3.下架成功后，点击“取回”，如提示取回成功，即可登录游戏查看您的角色。</p>
                            </div>
                        </li>
                        <li>6. 售出后怎么收款？
                            <div>
                                <p> 1. 角色售出后，卖方所得金额须通过3天考察期。 </p>
                                <p>
                                     2. 考察期通过后，售出资金将自动转入卖方的
                                     <span style="color:rgb(0,153,255);">网易支付账户</span>，可
                                     <span style="color:rgb(0,153,255);">提现至本人银行卡</span>。
                                </p>
                            </div>
                        </li>
                    </ul>
                </div>
                <div  class="hp-lb-d hp-ot-dj">
                    <ul @click="otdj">
                        <li>1. 交易收费规则？
                            <div>
                                <table class="hp-table">
                                    <tr>
                                        <td></td>
                                        <td>收费</td>
                                        <td>其他</td>
                                    </tr>
                                    <tr>
                                        <td>买方</td>
                                        <td>不收取任何费用</td>
                                        <td></td>
                                    </tr>
                                    <tr>
                                        <td>卖方</td>
                                        <td> 收取交易金额的8%作为信息费 </td>
                                        <td>1.最低收取：25元<br>2.信息费不足0.01元的部分，按0.01元收取。</td>
                                    </tr>
                                </table>
                                <p>收费举例：</p>
                                <p>卖方以1200.3元出售一个角色，交易成功后，收取1200.3*8%≈96.02元信息费。卖方实际收入为1200.3-96.02=1104.28元。</p>
                            </div>
                        </li>
                        <li>2. 支持交易的平台及服务器？
                            <div>
                                <p>1.不支持跨平台交易。</p>
                                <p>即iOS上的角色购买后只能在iPhone上游戏，安卓的角色购买后也仅能继续在安卓设备上游戏。</p>
                                <p>2.支持iOS及网易官方安卓的角色进行交易。其他合作渠道的安卓角色暂不支持。</p>
                                <p>3.当前支持的服务器：</p>
                                <p>【8月29日新增】</p>
                                <p>中国区-IOS：春之樱、夏之蝉、竹之幽</p>
                                <p>全平台：举手相庆、暖风春穗、欢庆鼓舞</p>
                                <p>国际区：海外加速区</p>
                                <p>【已开放】</p>
                                <p>网易-双平台：网易-携手同心、网易-结伴同游、网易-两情相悦、网易-春樱共赏、网易-风雨同行、网易-谜之暗影、网易-遥远之忆、网易-孤高之心、网易-心意相通、网易-永生之谜、网易-情比金坚、网易-同心一意、 网易-相知相依、网易-相伴相随、网易-形影不离、网易-缥缈之旅</p>
                                <p>中国区-IOS ：夜之月、松之苍、莲之净、桂之馥、兰之雅、雀之羽、云之遏</p>
                                <p>全平台：樱之忆、追月逐兔、依偎相守、相伴长情、朝夕相伴、深情厚谊、携手共度、相伴同行、旧友新朋、B站-两心无间、B站-亲密无间、B站-情深谊长、B站-情意相投</p>
                            </div>
                        </li>
                        <li>3. 如何修改绑定手机？
                            <div>
                                <p>修改藏宝阁绑定手机流程如下：</p>
                                <p>1.点击“我的”-“手机号”，进入修改手机页面；</p>
                                <p>2.根据页面提示，完成已有手机号的短信安全校验；</p>
                                <p>3.输入需要修改的新手机号，进行短信验证；</p>
                                <p>4.验证通过后，完成手机修改。</p>
                            </div>
                        </li>
                        <li>4. 设置网易通行证手机号？
                            <div>
                                <p>
                                     如您的使用的是网易邮箱帐号，且未在通行证绑定安全手机，需要
                                     <span style="color:rgb(0,153,255);">登录网易邮箱帐号</span>
                                    (https://reg.163.com/mibao/controller/mob/index.jsp)完成绑定。 
                                </p>
                                <p style="margin-top:20px;">网易通行证安全手机绑定流程如下：</p>
                                <p>1.登录成功后，点击页面“帐号管理”--“安全手机”，进入手机服务页面；</p>
                                <img src="http://127.0.0.1:3000/img/式神录爬虫/小图/bind-ph1.png">
                                <p>2.在打开页面中，在安全手机后点击 “立即设置”；</p>
                                <img src="http://127.0.0.1:3000/img/式神录爬虫/小图/bind-ph2.png">
                                <p>3.根据页面提示操作，验证通过后即可关联成功</p>
                                <img src="http://127.0.0.1:3000/img/式神录爬虫/小图/bind-ph3.png">
                            </div>
                        </li>
                        <li>5. 网易支付实名认证可以更改吗？
                            <div>
                                <p>抱歉，暂时无法修改（网易支付会以您账号首次支付的银行卡身份进行实名认证）。</p>
                            </div>
                        </li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    data(){
        return{wd:{},hh:{},xhb:{},gm:{},sp:{},ot:{}}
    },
    mounted(){
        this.nwd();
    },
    methods:{
        nwd(){
            this.wd=document.getElementsByClassName('hp-lb-wd')[0];
            this.hh=document.getElementsByClassName('hp-hh')[0].children;
            this.xhb=document.getElementById('hp-xhb');
            var gm=document.getElementsByClassName('hp-gm-dj')[0].children[0];
            for(var x of gm.children){
                x.children[0].style.display='none';
            }
            this.gm=gm;
            var sp=document.getElementsByClassName('hp-sp-dj')[0].children[0];
            for(var x of sp.children){
                x.children[0].style.display='none';
            }
            this.sp=sp;
            var ot=document.getElementsByClassName('hp-ot-dj')[0].children[0];
            for(var x of ot.children){
                x.children[0].style.display='none';
            }
            this.ot=ot;
        },
        dj:function(e){
            var c=e.target;
            if(c==this.hh[0]){
                this.wd.style.transform='translateX(0px)';
                this.wd.style.transition='all 0.3s linear';
                this.xhb.style.transform='translateX(0px)';
                this.xhb.style.transition='all 0.4s linear';
            }
            if(c==this.hh[1]){
                this.wd.style.transform='translateX(-750px)';
                this.wd.style.transition='all 0.3s linear';
                this.xhb.style.transform='translateX(250px)';
                this.xhb.style.transition='all 0.4s linear';
            }
            if(c==this.hh[2]){
                this.wd.style.transform='translateX(-1500px)';
                this.wd.style.transition='all 0.3s linear';
                this.xhb.style.transform='translateX(500px)';
                this.xhb.style.transition='all 0.4s linear';
            }
        },
        dianji:function(div1){// 传参一个父元素div1为形参
            console.log('000');
            function isIn(el,arr){//判断el元素是否在数组arr中，如果在则返回true，否则返回false
                for(var i of arr){
                    if(i==el){return true;}
                }
                return false;
            }
            console.log('000');
            console.log(div1);
            div1.onclick=function(e){//这里是手风琴效果js，事件绑在父元素上，利用冒泡
                console.log(111)
                var d=e.target;//将点击的元素赋值给变量d
                var c=d.children[0];//将点击元素的子元素赋值给c
                if(isIn(d,div1.children)){//如果点击的元素在父元素的子元素中
                    console.log(222)
                    for(var i of div1.children){//遍历父元素的子元素
                        console.log(333)
                        if(i!=d){//将不为点击元素的所有子元素高度更改为61px；；
                            console.log(444)
                            i.style.height='61px'; //子元素的子元素display设为none
                            i.children[0].style.display='none';
                        }
                    }
                    if(c.style.display=='none'){//如果点击元素的子元素display值为none
                        console.log(555)
                        c.style.display='block'; //那么将点击元素的子元素display值改为block
                        var h=c.clientHeight+61; //获取点击元素子元素的高度并加上61px赋值给h
                        d.style.height=h+'px';//将点击元素的高度设置为获取的高度h
                        d.style.transition='height 0.3s linear';//为点击元素的高度设置过渡
                    }else{//否则
                        console.log(666)
                        d.style.height='61px'; //设置点击元素的高度为61px
                        d.style.transition='all 0.3s linear';//为点击元素的高度设置过渡
                        c.style.display='none';//将点击元素的子元素display值改为none
                    }
                }    
            }
        },
        spdj(){
            this.dianji(this.sp);
        },
        gmdj(){
            this.dianji(this.gm);
        },
        otdj(){
            this.dianji(this.ot);
        }
    }
}
</script>
<style>
#hp-main{
    width: 750px;
    margin: 0 auto;
}
#hp-xhb{
    width: 250px;
    height: 5px;
    display: flex;
    justify-content: center;
}
#hp-xhb>div{
    width: 26px;
    height: 4px;
    background-color: #e74e4b;
    border-radius: 2px;
}
.hp-h{
    width: 100%;
    height: 63px;
    padding: 18px 20px;
    background-color: #fff;
}
.hh-i1{
    float: left;
    display: block;
    width:26px;height: 26px; 
    background-image: url('http://127.0.0.1:3000/img/式神录爬虫/小图/后退.png');
    background-size: cover;
}
.hh-i2{
    float: left;
    margin-top:10px;
    display: block;
    width:26px;height: 8px; 
    background-image: url('http://127.0.0.1:3000/img/式神录爬虫/小图/三点.png');
    background-size: cover;
}
.hp-h div{
    font-size: 23px;
    font-weight: 700;
    width: 654px;
    float: left;
    display:flex;
    justify-content:center;
    align-items:center;
}
.hp-hh{
    margin: 0;padding: 0;
    width: 100%;
    display: flex;
    background-color: #fff;
}
.hp-hh+div{
    width: 100%;
    background-color: #fff;
    border-bottom: 1px solid #ddd;
    padding-bottom: 10px;
    margin-bottom:10px; 
}
.hp-hh a{
    display: block;
    text-align: center;
    padding: 20px 0 5px 0;
    width: 250px;
    font-size: 19px;
    font-weight:lighter;
    color: #888;
}
.hp-lb{
    width: 750px;
    overflow: hidden;
}
.hp-lb-wd{
    width: 2250px;
}
.hp-lb-wd div{
    width: 750px;
    float: left;
    background-color: #FFF;
}
.hp-lb-d ul{
    list-style-type: none;
}
.hp-lb-d ul li{

    width: 720px;
    height: 61px;
    border-bottom:1px solid #ddd;
    padding: 20px 0px; 
    margin: 0 20px;
    font-size: 22px;
    color: #000;
}
.hp-lb-d ul li div{
    width: 720px;
    /* display: none; */
    padding: 20px 15px;
}
.hp-lb-d ul li div p{
    font-size: 18px;
    font-weight: lighter;
    color: #000;
}
.hp-table{
    border-collapse:collapse;
}
.hp-table tr td{
    border: 1px solid #ddd;
    font-size: 18px;
    color:#333;
    padding: 20px 15px;
}
.hp-sp-dj ul li div img{
    width: 683px;
}
</style>

