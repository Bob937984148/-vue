# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import requests
from lxml import etree
import time

html = '''<html lang="zh-cmn-Hans"><head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="format-detection" content="telephone=no">
  <meta name="viewport" content="width=device-width,user-scalable=no,initial-scale=1.0,minimum-scale=1.0,maximum-scale=1.0,minimal-ui,shrink-to-fit=no,viewport-fit=cover">
  <meta name="keywords" content="阴阳师,藏宝阁,网易游戏交易平台,网易游戏,阴阳师藏宝阁,阴阳师交易平台">
  <meta name="description" content="阴阳师藏宝阁，网易游戏推出的阴阳师官方线下交易平台，每一笔交易都与游戏数据对应，支持多种支付方式。买号选装备，上网易游戏阴阳师藏宝阁。"><title>阴阳师藏宝阁</title>
  <link rel="shortcut icon" href="https://cbg-yys.res.netease.com/rc6e513044067c7312a0e9/favicon.ico">
  
    <link rel="stylesheet" href="https://cbg-yys.res.netease.com/rc6e513044067c7312a0e9/css/swiper.min.css">
  
    <link rel="stylesheet" href="https://cbg-yys.res.netease.com/rc6e513044067c7312a0e9/dist/main.css">
  
<script type="text/javascript">
!function(g,l,d,p){var v,h=null,f=1,s=-1,m=-2,w=-3,N=g.document,E=g.encodeURIComponent,b=g.performance;function _(t,r){return 0<=t.indexOf(r)}function t(t,r,e){t.attachEvent?t.attachEvent("on"+r,e):t.addEventListener(r,e,!1)}function S(t,r){t.product=N.domain.split(".")[0],t.client=t.client||p;var e,n,o,a,i,c,u,f,s,m,g=N.referrer;v||(e="fingerprint",n=N.cookie.match("(^|;)\\s*"+e+"\\s*=\\s*([^;]+)"),v=n?n.pop():""),t.useragent=navigator.userAgent,g&&(t.from=g),v&&(t.fingerprint=v),o=function(t,r){var e=[];if(r){for(var n in r)r.hasOwnProperty(n)&&e.push(n+"="+E(r[n]));t+=(_(t,"?")?"&":"?")+e.join("&")}return t}(d,t),a=r,u=new Image,f=!0,s=function(){clearTimeout(c),u.onload=u.onerror=h,a&&a(f);try{u=h,delete u}catch(t){}},m=function(){f=!1,s()},c=i&&setTimeout(m,i),u.onload=s,u.onerror=m,u.src=o}function r(){return b&&b.now?Math.round(b.now()):(new Date).getTime()}if(1>Math.random()){var e,T=r(),y=!0;function n(t,r){var e=T,n=r;if(y=!1,b){var o=b.timing||{};o.navigationStart&&(e=o.navigationStart),o.loadEventEnd&&(n=o.loadEventEnd),!t&&b.now&&(e=0,n=parseInt(b.now()))}var a,i,c=(a=t?f:s,(i=n-e)<0?(a=m,i=0):18e5<i&&(a=w,i=0),{status:a,duration:i}),u={log:"page_load",status:c.status,time:c.duration};c.status!=f&&(u.time_start=e,u.time_end=n),S(u),setTimeout(function(){},100)}t(g,"beforeunload",function(){y&&(clearTimeout(e),n(!1,r()))}),t(g,"load",function(){if(y){var t=r();e=setTimeout(function(){n(!0,t)},100)}})}!function(){var o,a=!1,i=!0,c={},u=function(t){var r=t.stack.replace(/\n/gi,"").split(/\bat\b/).slice(0,9).join("@").replace(/\?[^:]+/gi,""),e=t.toString();return _(r,e)||(r=e+"@"+r),r},f=function(t){s(function(t){try{if(t.stack){var r=t.stack.match("https?://[^)^\n]+"),e=(r=r?r[0]:"").match(":(\\d+):(\\d+)");e||(e=[0,0,0]);var n=u(t),o=r.replace(e[0],"");return t.fnName&&(o+=":"+t.fnName),{msg:t.message,info:n,rowNum:e[1],colNum:e[2],target:o}}return t.name&&t.message&&t.description?{target:t.fnName,msg:t.message,info:"name:"+t.name+",desc:"+t.description+",number:"+t.number}:t}catch(a){return{msg:"__parse_error__",info:(a.message||a.toString())+"-"+t.toString()}}}(t))},e=function(t){if(!t)return!0;if(!i){var r=t.msg;if(_(r,"ReferenceError")||_(r,"\u672A\u5B9A\u4E49"))return!0}return a||(n=(e=t).target+e.msg,!!c[n]||(c[n]=!0,!1));var e,n},s=function(t){if(!e(t)){var r={log:"js_error",filename:t.target,msg:t.msg,info:t.info};t.rowNum&&(r.linenumber=t.rowNum+":"+t.colNum),S(r)}},m=g.onerror;g.onerror=function(t,r,e,n,o){var a,i,c=t;o&&o.stack&&(c=u(o)),a=c,i="Event",Object.prototype.toString.call(a)==="[object "+(i||"Object")+"]"&&(c+=c.type?"--"+c.type+"--"+(c.target?c.target.tagName+"::"+c.target.src:""):""),s({msg:t,info:c,target:r,rowNum:e,colNum:n}),m&&m.apply(g,arguments)},g.addEventListener?g.addEventListener("error",function(t,r){var e=t.target,n=(e.tagName||"").toUpperCase();if(_(["IMG","SCRIPT","LINK"],n)&&null===e.getAttribute("no-tracer")&&"prefetch"!==e.getAttribute("rel")){if(_(r="LINK"==n?e.href:e.src,"/1.gif?"))return;_(r,l)&&"SCRIPT"==n&&(a=!0),S({log:"js_error",filename:r,msg:"LOAD_FAILED"})}},!0):i=!1;var t={watch:function(e,n){return function(){try{return e.apply(this,n||arguments)}catch(r){if(r.fnName=/^function\s+[^\(]*/.exec(e.toString())[0],f(r),!o){var t=g.onerror;g.onerror=function(){},o=setTimeout(function(){g.onerror=t,o=null},50)}throw r}}},reportError:f,send:s};g.CBG_JS_REPORT=t}()}(window,"https://cbg-yys.res.netease.com/rc6e513044067c7312a0e9","https://other-tracer.cbg.163.com/1.gif","h5");
</script>
<script type="text/javascript" charset="utf-8" async="" src="https://cbg-yys.res.netease.com/rc6e513044067c7312a0e9/dist/product-detail.js?4846af"></script><script type="text/javascript" charset="utf-8" async="" src="https://cbg-yys.res.netease.com/rc6e513044067c7312a0e9/dist/pdetail-role.js?4846af"></script></head>
<body>
  <div class="page-app"><div class="page-loading vpa-router-view"><div serverid="22" ordersn="201811071001616-22-YTKQUQANALXCJ" class="pageProductDetail with-site-navbar page-product-role"><div class="site-header site-navbar site-navbar-normal site-navbar-fixed"><div class="left"><a href="javascript:;"><i class="icon icon-back"></i></a></div><div class="title">商品详情</div><div class="right"><div class="navbar-menu"><a href="javascript:;"><i class="icon nav-message icon-more"><!----></i></a><!----></div></div></div><div class="request-status-ctrl outer-content"><!----><!----><div class="list-block border pdetailPreview"><div class="list-item hd"><div class="color-gray"><span class="area-server icon-text">中国区-iOS-竹之幽</span><span class="icon icon-ios"></span></div><div class="color-primary"><span class="icon-text">已取回</span><!----></div></div><div class="list-item"><div class="role-info"><!----><h2 class="fz-large"><span class="level">60级</span><i class="icon s-l icon-publicity"></i></h2><!----><ul class="intro"><li>SSR 49</li><li>六星式神 65</li><li>签到775天</li></ul><ul class="highlight"><li>六星SSR31个</li><li>京都之主</li></ul></div></div><div class="list-item"><div class="ft clearfix"><!----><p class="pull-right seller">
        卖家: 暗黑少女"
      </p><!----></div></div></div><div class="request-status-ctrl main-content"><!----><!----><div class="page-role-detail with-site-footbar product-detail" style="min-height: 670px;"><div class="c-sticky-fix-pholder" style="height: 0.265625px;"></div><div class="c-sticky sticky-tab" style=""><div class="hair-tab"><div class="tabs"><a href="javascript:;" class="item">式神</a><a href="javascript:;" class="item">资产</a><a href="javascript:;" class="item">斗技</a><a href="javascript:;" class="item">御魂</a><a href="javascript:;" class="item">阴阳术</a><a href="javascript:;" class="item">皮肤/收集品</a><a href="javascript:;" class="item on">徽章</a><span class="line animate" style="transform: translateX(671.5px);"></span></div></div></div><div class="content role-detail"><!----><!----><!----><!----><!----><!----><div class="content-honors" pophonor="[object Object]"><ul class="honors"><li><div class="ico-wrap"><img src="https://cbg-yys.res.netease.com/game_res/badge/950003.png" class="ico"><!----></div><p class="name tof">大蛇·完胜</p></li><li><div class="ico-wrap"><img src="https://cbg-yys.res.netease.com/game_res/badge/950007.png" class="ico"><!----></div><p class="name tof">地域·天下一</p></li><li><div class="ico-wrap"><img src="https://cbg-yys.res.netease.com/game_res/badge/950013.png" class="ico"><!----></div><p class="name tof">秘闻·天下一</p></li><li><div class="ico-wrap"><img src="https://cbg-yys.res.netease.com/game_res/badge/950017.png" class="ico"><!----></div><p class="name tof">呱世无双</p></li><li><div class="ico-wrap"><img src="https://cbg-yys.res.netease.com/game_res/badge/950021.png" class="ico"><!----></div><p class="name tof">轻呱熟路</p></li><li><div class="ico-wrap"><img src="https://cbg-yys.res.netease.com/game_res/badge/900404.png" class="ico"><!----></div><p class="name tof">大结界师</p></li><li><div class="ico-wrap"><img src="https://cbg-yys.res.netease.com/game_res/badge/900414.png" class="ico"><!----></div><p class="name tof">馆主·博</p></li><li><div class="ico-wrap"><img src="https://cbg-yys.res.netease.com/game_res/badge/950055.png" class="ico"><!----></div><p class="name tof">功高盖世</p></li><li><div class="ico-wrap"><img src="https://cbg-yys.res.netease.com/game_res/badge/950051.png" class="ico"><!----></div><p class="name tof">饕餮盛宴</p></li><li><div class="ico-wrap"><img src="https://cbg-yys.res.netease.com/game_res/badge/950047.png" class="ico"><!----></div><p class="name tof">换斗移星</p></li><li><div class="ico-wrap"><img src="https://cbg-yys.res.netease.com/game_res/badge/950059.png" class="ico"><!----></div><p class="name tof">神乎其技</p></li><li><div class="ico-wrap"><img src="https://cbg-yys.res.netease.com/game_res/badge/950035.png" class="ico"><!----></div><p class="name tof">决胜千里</p></li><li><div class="ico-wrap"><img src="https://cbg-yys.res.netease.com/game_res/badge/950031.png" class="ico"><!----></div><p class="name tof">勇冠三军</p></li><li><div class="ico-wrap"><img src="https://cbg-yys.res.netease.com/game_res/badge/950043.png" class="ico"><!----></div><p class="name tof">震古烁今</p></li><li><div class="ico-wrap"><img src="https://cbg-yys.res.netease.com/game_res/badge/950039.png" class="ico"><!----></div><p class="name tof">所向无敌</p></li><li><div class="ico-wrap"><img src="https://cbg-yys.res.netease.com/game_res/badge/950060.png" class="ico"><!----></div><p class="name tof">终极之巅</p></li></ul><p class="content-tips">
    仅展示高级徽章
  </p></div></div><span></span><div class="popup-normal popup-head-skin"><!----></div><div class="popup-normal popup-yuhun"><!----></div><div class="popup-normal popup-honor" parseres="function () { [native code] }"><!----></div></div></div><div class="site-footbar pdetailOperaion"><div class="actions actions-buyer"><a class="btn btn-collect"><i class="icon icon-collect"></i><span class="icon-text">收藏</span></a><button class="btn btn-large disabled">
        已取回
      </button></div></div></div></div></div></div>
  <script>
  var CBG_CONFIG = {
    pName: "yys",
    
    
    
    cgiRoot: "/cgi",
    apiRoot: "/cgi/api",
    webRoot: "/cgi/mweb",
    centerRoot: "https://dc-ios.cbg.163.com",
    resUrl: "https://cbg-yys.res.netease.com",
    staticUrl: "https://cbg-yys.res.netease.com/rc6e513044067c7312a0e9",
    trackerDomain: "https://other-tracer.cbg.163.com",
    ServerTime: "2018-11-30 20:30:01",
    ServerTimestamp: 1543581001000
  };
  var ResUrl = CBG_CONFIG.resUrl;
  </script>

  <script src="https://cbg-yys.res.netease.com/js/game_auto_config.js"></script><script src="https://cbg-yys.res.netease.com/rc6e513044067c7312a0e9/??lib/accessibility.js,dist/lib.js,lib/swiper.min.js,js/com_config.js,js/config.js,lib/tracker.js,js/log.js,dist/main.js" charset="utf-8"></script>

<div class="pc-entry"><img src="https://cbg-yys.res.netease.com/rc6e513044067c7312a0e9/images/pc/qr-code.png" alt="二维码"><br>扫一扫<br>手机访问体验更佳</div><iframe src="chrome-extension://lgcegncnkmnfbncafipagoiopcjjjici/bar.html" id="xh-bar" class="top" style="height: 0px; visibility: visible;"></iframe></body></html>'''

xp = '''/html/body/div[@class='page-app']/div[@class='page-loading vpa-router-view']/div[@class='pageProductDetail with-site-navbar page-product-role']/div[@class='request-status-ctrl outer-content']/div[@class='request-status-ctrl main-content']/div[@class='page-role-detail with-site-footbar product-detail']/div[@class='content role-detail']/div[@class='content-skin']/ul[@class='skin-hero'][1]/li[1]/div[@class='skin-wrap']/img/@src'''


class sslSpider:

    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
        self.pageurl = "https://yys.cbg.163.com/cgi/mweb/equip/10/201811062101616-10-3BCYCTTI5RDCJ"

    # def file_name(self):
        # fname_list = []
        # for root, dirs, fname in os.walk(file_dir):
        #     for i in fname:
        #         k = i.replace('.png', '')
        #         fname_list.append(k)
        #     self.getUrl(fname_list)

    def getUrl(self, html):
        parseHtml = etree.HTML(html)
        i = 1
        while i < 17:
            geturl = '''/html/body/div[@class='page-app']/div[@class='page-loading vpa-router-view']/div[@class='pageProductDetail with-site-navbar page-product-role']/div[@class='request-status-ctrl outer-content']/div[@class='request-status-ctrl main-content']/div[@class='page-role-detail with-site-footbar product-detail']/div[@class='content role-detail']/div[@class='content-honors']/ul[@class='honors']/li[''' + str(
                i) + ''']/div[@class='ico-wrap']/img[@class='ico']/@src'''
            getname = '''/html/body/div[@class='page-app']/div[@class='page-loading vpa-router-view']/div[@class='pageProductDetail with-site-navbar page-product-role']/div[@class='request-status-ctrl outer-content']/div[@class='request-status-ctrl main-content']/div[@class='page-role-detail with-site-footbar product-detail']/div[@class='content role-detail']/div[@class='content-honors']/ul[@class='honors']/li[''' + str(
                i) + ''']/p[@class='name tof']'''
            url = parseHtml.xpath(geturl)[0]
            print(url)
            name = parseHtml.xpath(getname)[0].text
            print(name)
            name = './徽章/' + name + '.png'
            self.writeimg(url, name)
            time.sleep(1)
            i += 1

    def writeimg(self, url, filename):
        res = requests.get(url, headers=self.headers)
        res.encoding = "utf-8"
        img = res.content
        if img:
            with open(filename, 'ab') as f:
                print("%s正在下载" % filename)
                f.write(img)
                print("%s下载成功" % filename)
        else:
            print('%s不存在' % filename)
if __name__ == "__main__":
    spider = sslSpider()
    # spider.file_name("./式神")
    spider.getUrl(html)


''' + str(i) + '''
