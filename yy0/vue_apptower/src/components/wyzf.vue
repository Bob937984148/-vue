<template>
    <div id="wyzf">
        <div id="wyzf-h">
            <div>
                <img src="http://127.0.0.1:3000/img/式神录爬虫/小图/网易支付.png">
                <span>补全账户信息</span>
                <i>欢迎你，xxxx<a href="">退出</a></i>
                <div style="clear:both;"></div>
            </div>
        </div>
        <div id="wyzf-b">
            <div class="b-top">
                <img src="http://127.0.0.1:3000/img/式神录爬虫/小图/手机.png">
                <div>
                    <h4>绑定手机</h4>
                    <h5>轻松了解资金变动，实时掌握支付信息</h5>
                </div>
            </div>
            <div class="b-bottom">
                <table>
                    <tr>
                        <td><div>关联手机</div></td>
                        <td class='t-z'><span> 152***2009</span><a href="">使用其他号码</a><i>|</i><a href="">帮助</a></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td class="t-2"><div>验证码</div></td>
                        <td ><input type="text"></td>
                        <td><button class="yzm">获取验证码</button></td>
                    </tr>
                    <tr>
                        <td class="t-2"><div>将军令</div></td>
                        <td ><input type="text"></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td></td>
                        <td ><button class="xyb">下一步</button></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td></td>
                        <td class="wyxy"><input type="checkbox" name='xy' value="xy"><div>我同意<a href="https://epay.163.com/urs/agreement.jsp">《网易支付服务协议》</a></div></td>
                        <td></td>
                    </tr>
                </table>
            </div>
        </div>
        <div id="wyzf-f">
            <div>
经营许可证编号：浙B2-20100458  网易支付客服电话：400-0881188  网易（杭州）网络有限公司版权所有 ©1997-2019</div>
        </div>
        
    </div>
</template>
<script>
export default {
    data(){
        return{

        }
    }
}
</script>
<style>
#wyzf{
    width: 100%;
}
#wyzf-h{
    width: 100%;
    background-color: #fff;
    margin-bottom: 40px;
}
#wyzf-h>div{
    width: 1000px;
    margin: 0 auto;
    background-color: #fff;
}
#wyzf-h>div>img{
    width: 170px;
    height: 48px;
    margin: 10px;
    float: left;
}
#wyzf-h>div>span{
    border-left: 1px solid #333;
    padding: 5px;
    font-size: 25px;
    color:#777;
    margin-top: 17px;
    float: left;
}
#wyzf-h>div>i{
    display:block;
    float: right;
    padding-top:28px;
}
#wyzf-b{
    width: 1000px;
    margin: 0 auto;
    background-color: #fff;
    padding: 60px;
}
#wyzf-b>.b-top{
    padding-bottom: 40px;
    display: flex;
    border-bottom: 1px dashed #888;
}
#wyzf-b>.b-top>img{
    margin-left: 142px;
    width: 110px;
    height: 100px;
}
#wyzf-b>.b-top>div{
    margin: 23px 0 0 23px;
}
#wyzf-b>.b-top>div>h4{
    font-size: 20px;
    margin-bottom: 10px;
}
#wyzf-b>.b-bottom{
    width: 500px;
    margin: 40px auto;
}
.b-bottom>table>tr>td:first-child>div{
    font-size: 15px;
    margin: 17px 0px; 
    padding-right: 10px;
}
.b-bottom>table>tr td .yzm{
    height: 40px;
    margin: -15px 0px 0px 15px;
    border: 1px solid #e53;
    color:#e53;
}
.b-bottom>table>tr td .xyb{
    width: 140px;height: 40px;
    background-color: #e53;
    color: #fff;
    margin: 0px 0px 0px 0px;
}
.b-bottom>table>tr .wyxy>div{
    margin-top: 10px;
    display: inline-block;
    font-size: 14px;
}
#wyzf-b>.b-bottom>table tr .t-2>div{
    margin: -18px 15px 0px 13px;
}
#wyzf-b .b-bottom .t-z span{
    margin: 0 100px 15px 0px;
}
#wyzf-b .b-bottom .t-z a{
    font-size: 10px;
}
#wyzf-b .b-bottom .t-z i{
    margin: 0 3px;
    display: inline-block;
    font-style: unset;
    color:#bbb;
}
#wyzf-f{
    margin-top: 30px;
    width: 100%;
    background: #ddd;
    text-align: center;
}
#wyzf-f div{
    padding: 50px ;
    font-size: 10px;
    color: #777;
}
</style>


