<template>
    <div>
<div class="back">
    <div class="g-hd">
        <div class="g-in">
            <a href="#" target="_blank" >
                <div class="m-logo ">

                </div>
            </a>
            <div class="m-tr-block txt-muted">
                <span>已有账号？去</span>
                <a id="btn_login" href="#">登录</a>
            </div>
        </div>

    </div>
    <div class="g-bd">
        <div class="clearfix m-tab">
            <div class="left select"><span>普通账号</span></div>
            <a class="right" id="rightBtn" href="#" target="_blank"><span style="color: #666">靓号注册</span><p class="new">new</p></a>
        </div>

        <div class="m-opr clearfix">
            <form autocomplete="off" id="bind-phone-form">
                <div class="u-input firstelem">
                    <label class="u-label" for="inpt-account">账号 :&nbsp;</label>
                    <input type="text" id="inpt-account" name="email" class="i-inpt-small" placeholder="6-18位字母数字组合"  v-model="email">
                    <div class="u-tip f-dn">
                        <div class="spritebg u-clear" id="auto-id-1544786117257"></div>
                    </div>
                    
                    <span id="showUname"></span>
                </div>
                <div class="u-input">
                    <label class="u-label">密码  :&nbsp;</label>
                    <input type="password" class="i-inpt" placeholder="6-16位密码，区分大小写" id="inpt-pw" name="pwd" v-model="pwd">
                    <span id="showUpwd"></span>
                </div>
                <div class="u-input">
                    <label class="u-label">确认密码  :&nbsp;</label>
                    <input type="password" class="i-inpt" placeholder="再次输入密码" v-model="pwd2">
                </div>
                <div class="u-input" style="height: 44px overflow:inherit">
                    <label class="u-label" style="margin-top: -5px">验证码 :&nbsp;</label>
                    <div style="float: left">
                        <div class="yidun_tips" style="line-height: 40px">       <span class="yidun_tips__icon">
                            </span>       
                         <span class="yidun_tips__text">点此进行验证</span>     
                         </div>
                    </div>
                </div>
                <div class="u-inpt j-phone-box">
                    <label class="u-label">手机号</label>
                    <input type="text" class="i-inpt " maxlength="20" placeholder="11位手机号" id="inpt-phone" name="phone" v-model="phone">
                    <span id="showPhone"></span>
                </div>
                <div class="u-input u-note">
                    <label class="u-label"></label><span class="changephone j-cgp" style="font-size: 12px">切换到国际手机</span>
                </div>
                <div class="u-input u-note">
                    <label class="u-label"></label><span style="font-size: 12px">忘记密码时，可通过手机快速找回密码</span>
                </div>
                <div class="u-input">
                    <label class="u-label" for="inpt-sms">短信验证码：</label>
                    <input type="text" class="i-inpt smsize" maxlength="6" placeholder="输入短信验证码" id="inpt-sms" name="sms">
                    <div class="u-tip f-dn"><div class="spritebg u-clear" id="auto-id-1544838106126"></div></div>
                    <span class="b-btn btn-getsms">获取验证码</span>
                </div>
                <div class="u-inpu" style="height: 58px;">
                    <label class="u-label">&nbsp;</label>
                    <div class="b-btn btn-reg btn-red" style="width: 320px" @click="handleReg()">&nbsp;&nbsp;注  册  </div>
                </div>
                <div class="u-tips">
                    <label class="u-label">&nbsp;</label>
                    <span class="tip">
                    <span class="m-agree m-agree-ok">
                        <input type="checkbox" class="u-agree"></span>
                    <span style="margin-left: 10px;">用户勾选即代表同意</span>
                    <a href="http://reg.163.com/agreement.shtml" target="_blank">《网易邮箱服务条款》</a>和<a href="http://reg.163.com/agreement_game.shtml" target="_blank">《网易隐私政策》</a></span>
                </div>
            </form>
        </div>
        <div>
            <a href="https://id.163.com/gj/?from=webzj_zc" target="_blank" style="display:block;position:initial;margin:0 auto;width:900px;height:180px;overflow:hidden;border-radius:2px;"><img src="//ursdoccdn.nosdn.127.net/reg/app_xc_small_170402.png"></a></div>
        </div>
    </div>
        <div class="g-ft">
            <div class="g-in">
                <div class="m-cp">
                    <p><a href="http://corp.163.com/eng/about/overview.html" target="_blank">About NetEase</a>-<a href="http://gb.corp.163.com/gb/about/overview.html" target="_blank">公司简介</a>-<a href="http://gb.corp.163.com/gb/contactus.html" target="_blank">联系方式</a>-<a href="http://reg.163.com/help/help_oauth2.html?v=20141215" target="_blank">OAuth2.0认证֤</a>-<a href="http://corp.163.com/gb/job/job.html" target="_blank">招聘信息</a>-<a href="http://help.163.com/" target="_blank">客户服务</a>-<a href="http://gb.corp.163.com/gb/legal.html" target="_blank">相关法律</a>-<a href="http://emarketing.biz.163.com/" target="_blank">网络营销</a></p>
                    <p>网易公司版权所有 ?1997-2018</p>
                </div>
            </div>
        </div>
</div>
</template>
<script>
export default {
    data(){
        return{
            email:"",
            pwd:"",
            pwd2:"",
            phone:"",
            isSumit:true,
        }
    },
    methods:{
        handleReg(){
            if(!this.isSumit){
                return;
            }else{
            var regname = /^[a-z0-9_]{6,18}$/i;
            var regpwd = /^[a-z0-9_]{6,16}$/i;
            var regpho = /^1[3-8]\d{9}$/
            if(!regname.test(this.email)){
                alert("用户名不能为空")
                return;
            }
            if(!regpwd.test(this.pwd)){
                alert("密码格式不正确")
                return;
            }           
            if(this.pwd != this.pwd2){
                alert("两次密码不一致，请修改")
                return;
            }
            if(!regpho.test(this.phone)){
                alert("手机号码不正确")
                return;
            }
            var data = new URLSearchParams();
            data.append('email',this.email);
            data.append('upwd',this.pwd);
            data.append('phone',this.phone);
            console.log(data);
            var url = "http://127.0.0.1:3000/register";
            this.axios.post(url,data).then(result=>{
                console.log(result.data);
            })
            }
        }
    }
}
</script>
<style>
    *{
    margin: 0;
    padding: 0;
    font-family: ΢���ź�;
}
.back{
    width: 100%;
    /*height: 1000px;*/
    background: #efefef;
}
.g-in a{
    position: relative;
}

.m-logo{
    float: left;
    width: 300px;
    height: 60px;
    background-position: -50px -18px;
    margin-top: 22px;
    /* background:url("../../img/sprite.png") no-repeat; */
    position: absolute;
    left: -50px;

}
.m-tr-block{
    float: right;
    font-size: 18px;
    margin-top: 50px;
}
.m-tr-block a{
    text-decoration: none;
    color: #ca5252;
    /*cursor: pointer;*/
}
.m-tr-block a:hover{
    color:#c82333 ;
}
.m-tr-block span{
    cursor:default;
    color: rgb(102, 102, 102);

}
.g-bd{
    width: 1000px;
    height: 908px;
    background: #fff;
    margin: 0 auto;
    border-radius: 6px;
    position: relative;
    box-shadow: 0 3px 3px #cbc9c9;
}

.g-hd{
    /*width: 640px;*/
    height:130px;
    width: 1000px;
    margin: 0 auto;
}
.m-tab{
    width: 320px;
    margin: 0 auto;
    padding-top: 44px;
    padding-bottom: 24px;
}
.m-tab .select{
    background: #ca5252;
    border-color: #ca5252;
    color: #fff3cd;
}
.m-tab .left{
    width: 158px;
    border:1px solid #ccc;
    border-right: 0;
    height: 40px;
    line-height: 38px;
    text-align: center;
    font-size: 16px;
    float: left;
}

.m-tab .right{
    display: block;
    width: 158px;
    border:1px solid #ccc;
    border-left:0;
    line-height: 38px;
    text-align: center;
    font-size: 16px;
    float: right;
    position: relative;
    text-decoration: none;
    color: #666;
    cursor: pointer;
}
.m-tab .right>span{
    text-decoration: none;
    color: #666;
    cursor: pointer;
}
.m-tab .new{
    position: absolute;
    font-size: 9px;
    color: #fff;
    background: #ca5252;
    height: 12px;
    line-height: 9px;
    width: 26px;
    top:4px;
    border-radius: 2px;
    right: 12px;
}
.p{
    display: block;
}
.m-opr{
    height: 620px;
    margin-top: 0;
}

.m-opr .i-inpt {
    float: left;
    height: 44px;
    margin-top: 12px;
    border:1px solid #ddd;
    font-size: 16px;
    text-indent: 0.5em;
    width: 320px;
}
.m-opr .i-inpt-small{
    width: 320px;
    float: left;
    height: 44px;
    margin-top: 12px;
    border:1px solid #ddd;
    font-size: 16px;
    text-indent: 0.5em;
}
.input{
    padding-left: 0;
    color: #333;
    /*font-weight: bold;*/
    line-height: 30px;
    outline: 0px;
}
.m-opr .u-input{
    position: relative;
    float: left;
    height: 72px;
    width: 100%;
}
.m-opr .u-input.firstelem{
    overflow:visible;
    float: left;
    height: 72px;
    width: 100%;
}
.m-opr .u-label {
    float: left;
    width: 340px;
    text-align: right;
    margin-top: 12px;
    font-size: 16px;
    line-height: 45px;
    color: #333;
}
.label,.summary{
    cursor: default;
}
.m-opr .u-tip {
    position: relative;
    float: left;
    width: 40px;
    height: 40px;
    margin-left: -42px;
    margin-top: 15px;
    z-index: 11;
    background: #fff;
}
.f-dn{
    display: none !important;
}
.m-opr .u-clear {
    position: absolute;
    width: 20px;
    height: 20px;
    left: 10px;
    top: 10px;
    cursor: pointer;
    background-position: -325px -101px;
    opacity: 0.5;
}

.m-opr .m-select{
    line-height: 40px;
    float: left;
    width: 108px;
    height: 46px;
    margin-top: 12px;
    border-color: #ddd;
    margin-left: 10px;
    font-size: 14px;
}
.m-opr .u-input {
    position: relative;
    float: left;
    height: 72px;
    width: 100%;
    overflow: hidden;
}
.m-opr .u-label {
    float: left;
    width: 340px;
    text-align: right;
    margin-top: 12px;
    font-size: 16px;
    line-height: 45px;
    color: #333;
}
label{
    cursor: default;
}
.m-opr .i-inpt{
    float: left;
    height: 44px;
    width: 320px;
    margin-top: 12px;
    border:1px solid #ddd;
    font-size: 16px;
    text-indent: 0.5em;
    line-height: 44px \9;
}
input{
    padding-left: 0;
    color: lightgrey;
    line-height: 30px;
}
.m-opr .u-note {
    height: 22px;
    line-height: 22px;
    color: #999;
}
.u-note .changephone {
    cursor: pointer;
    color: #4cb5ff;
}
.m-opr .i-inpt.smsize {
    width: 190px;
    padding-top: 1px;
    padding-bottom: 1px;
}
.m-opr .u-tip {
    position: relative;
    float: left;
    width: 40px;
    height: 40px;
    margin-left: -42px;
    margin-top: 15px;
    z-index: 11;
    background: #fff;
}
.m-opr .btn-getsms {
    float: left;
    height: 46px;
    width: 120px;
    font-size: 16px;
    line-height: 46px;
    margin: 12px 0 0 10px;
    color: #fff;
    background: #2c82ff;
    text-align: center;
}
.m-opr .u-inpu {
    position: relative;
    float: left;
    width: 100%;
    overflow: hidden;
}
.m-opr .btn-red {
    background: #ca5252;
}
.m-opr .b-btn {
    float: left;
    border: 0;
    width: 120px;
    height: 46px;
    margin-top: 12px;
    text-align: center;
    font-size: 18px;
    color: #fff;
    line-height: 46px;
    cursor: pointer;
}
.m-opr .tip {
    margin-top: 10px;
    color: #b1b1b1;
    float: left;
    width: 322px;
    font-size: 12px;
}
.m-agree-ok {
    background-position: 0 -278px;
}
.m-agree {
    display: block;
    float: left;
    width: 14px;
    height: 14px;
    cursor: pointer;
    border: solid 1px #aaa;
    color: #999;
    font-size: 12px;
    /* background: url(../img/sprite.png) -9999px -9999px no-repeat; */
}
.u-agree {
    cursor: pointer;
    float: left;
    width: 14px;
    height: 14px;
    line-height: 20px;
    border: 1px solid #ccc;
    background: #fff;
    opacity: 0;
}
.g-ft{
    background:  #efefef;
}
.g-in {
    width: 1000px;
    margin: 0 auto;
}
.m-cp {
    padding: 30px 0;
}
.m-cp p {
    padding-bottom: 10px;
    margin-bottom: 0px;
    text-align: center;
    color: #b1b1b1;
    font-size: 12px;
}
.m-cp p a {
    padding: 0 6px;
}
.m-cp p, .m-cp p a {
    color: #b1b1b1;
}
a, a:active, a:hover, a:visited {
    text-decoration: none;
}
 .yidun_tips{
    text-align: center;
    width: 318px;
    height:40px;
    background: linear-gradient(180deg,#fff 0,#ebedf0 87%);
    color: #45494c;
    line-height: 40px;
}

</style>
