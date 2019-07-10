<template>
<div class="bod1" id="Equip">
<!--商品内容    -->
<div>
    <div class="list-block ">
        <!--大区-->
        <div class="list-item hd">
            <div class="gray">
                <span>{{userDate.site}}</span> 
            </div>
            <div class="color-primary">
                <span class="icon-text">公示期</span>
            </div>
        </div>
        <hr/>
        <!--60级-->
        <div class="list-item ">
            <div class="role-info ">
                <h2>
                    <span>{{userDate.lv}}级</span>
                        <img class="gongshi" src="data:image/svg+xml;charset=utf-8,<svg width='30' height='30' viewBox='0 0 30 30' xmlns='http://www.w3.org/2000/svg'><g fill='none' fill-rule='evenodd'><rect fill='%235CC2FF' width='30' height='30' rx='4'/><path d='M10.464 4.536l2.112.84c-1.704 5.016-3.96 8.856-6.768 11.496l-1.8-1.56C6.888 12.6 9.048 9 10.464 4.536zm9.024 12.72a50.666 50.666 0 0 1 4.488 8.256l-2.136.96c-.336-.768-.648-1.536-.984-2.256-4.176.624-8.808 1.104-13.944 1.44l-.408-2.208c1.704-.552 4.08-4.224 7.152-11.016l2.232.768c-1.92 4.056-3.888 7.44-5.856 10.152 3.408-.24 6.72-.6 9.888-1.08-.792-1.584-1.608-3.024-2.472-4.32l2.04-.696zM19.08 4.344c1.344 4.368 3.648 7.944 6.96 10.704l-1.632 1.872c-3.48-2.976-5.904-6.792-7.272-11.472l1.944-1.104z' fill='%23FFF'/></g></svg>" alt="#"/>
                </h2>
                <p class="price1">￥{{userDate.price}}</p>
                <ul class="intro">
                    <li>SSR 48</li>
                    <li>六星式神 26</li>
                    <li>签到{{userDate.days}}天</li>
                </ul>
                
                <div class="clearf"></div>
            </div>
        </div>
        <hr/>
        <!--公示期-->
        <div class="list-item">
            <p>公示期至2019-1-26 12:51</p>
            <p>卖家：11</p>
        </div>
        <hr/>
    </div>
</div>
<!--式神资产斗技-->
<div class="hair-tab">

    <a href="javascript:;" @click  = "show(1)" :class="{bgred:naSs}">式神</a>
    <a href="javascript:;" @click = "show(2)" :class="{bgred:naZc}" >资产</a>
    <a href="javascript:;" @click = "show(3)" :class="{bgred:naDj}" >斗技</a>
    <a href="javascript:;" @click = "show(4)" :class="{bgred:naYh}" >御魂</a>
    <a href="javascript:;" @click = "show(5)" :class="{bgred:naYys}" >阴阳术</a>
    <a href="javascript:;" @click = "show(6)" :class="{bgred:naPf}" >皮肤/收集品</a>
    <a href="javascript:;" @click = "show(7)" :class="{bgred:naHz}" >徽章</a>
</div>
<hr/>
<div class="content role-detail">
    <!--式神-->
<div class="content-heroes" :class="{display: shishenClass}">
    <ul class="hero-tabs">
        <li class="tab-item current">
           
            <span @click="shDj()">
            <p>式神 - 等级</p>
             <p v-bind:class="{sanjiaotrans:ssDj}">▼</p>
             </span>  
                
            <ul class="filter-select " v-if="shSele == true">
                <li class="selected" :class="{colred:djClass}" @click="shDjclor(1)">等级</li>
                <li :class="{colred:xjClass}" @click="shDjclor(2)">星级</li>
                <li :class="{colred:xydClass}" @click="shDjclor(3)">稀有度</li>
            </ul>
        </li>

        <li class="tab-item"><span>碎片</span></li>
        <li class="tab-item"><span>图鉴</span></li>
        <div class="clearf"></div>
    </ul>

    <div class="content-wrap white">
        <div class="sub-tab-heroes">
            <transition-group name="flip-list" tag="ul" class="hero-list">
                <!-- <span> -->
                    <li class="hero-item hero-item-ssr "  v-for="list in shishen" :key="list.id">
                        <div class="frame">
                            <div class="wrap">
                                <img :src="'http://127.0.0.1:3000/img'+list.src" alt=""/>
                                <span class="awake">
                                    觉
                                </span>
                                <span class="level-status" v-if="list.ss_rank == 40">
                                    <span class="con" >满</span>
                                </span>
                                <span class="level-icons">
                                    <img v-if="list.ss_slevel >= 1" src="../img/式神录爬虫/小图/紫勾玉.png" alt="" class="icon  icon-star-awake"/>
                                    <img v-if="list.ss_slevel >= 2" src="../img/式神录爬虫/小图/紫勾玉.png" alt="" class="icon  icon-star-awake"/>
                                    <img v-if="list.ss_slevel >= 3" src="../img/式神录爬虫/小图/紫勾玉.png" alt="" class="icon  icon-star-awake"/>
                                    <img v-if="list.ss_slevel >= 4" src="../img/式神录爬虫/小图/紫勾玉.png" alt="" class="icon  icon-star-awake"/>
                                    <img v-if="list.ss_slevel >= 5" src="../img/式神录爬虫/小图/紫勾玉.png" alt="" class="icon  icon-star-awake"/>
                                    <img v-if="list.ss_slevel >= 6" src="../img/式神录爬虫/小图/紫勾玉.png" alt="" class="icon  icon-star-awake"/>
                                </span>
                            </div>
                        </div>
                        <div class="name">{{list.name}}</div>
                        <div class="clearf"></div>
                    </li>
                    
                <!-- </span> -->
            </transition-group>
            <ul class="hero-list"></ul>
        </div>
    </div>
</div>
<!--资产-->
<div class="content-asset white" :class="{display: zichanClass}">

    <!-- <span class="pull-right" >有永久勾玉卡</span>
    <h3>资产</h3> -->
    <section>
        <ul>
            <li>
                <img src="../img/式神录爬虫/小图/金币.png">
                <span class="name">金币</span>
                <span class="val">{{userDate.gold}}万</span>
            </li>
            <li>
                <img src="../img/式神录爬虫/小图/勾玉.png">
                <span class="name">勾玉</span>
                <span class="val">{{userDate.gouyu}}</span>                
            </li>
            <li>
                <img src="../img/式神录爬虫/小图/体力.png">
                <span class="name">体力</span>
                <span class="val">{{userDate.Vit}}</span>
            </li>
            <li>
                <img src="../img/式神录爬虫/小图/魂玉.png">
                <span class="name">魂玉</span>
                <span class="val">{{userDate.hunyu}}</span>
            </li>
            <div class="clearf"></div>
        </ul>
    </section>
     <section>
        <ul>
            <li>
                <img src="../img/式神录爬虫/小图/神秘符咒.png">
                <span class="name">神秘符咒</span>
                <span class="val">{{userDate.sm_amulet}}</span>
            </li>
            <li>
                <img src="../img/式神录爬虫/小图/现世符咒.png">
                <span class="name">现世符咒</span>
                <span class="val">{{userDate.xs_amulet}}</span>                
            </li>
            <li>
                <img src="../img/式神录爬虫/小图/御札.png">
                <span class="name">御札</span>
                <span class="val">{{userDate.yuzha}}</span>
            </li>
            <li>
                <img src="../img/式神录爬虫/小图/金御札.png">
                <span class="name">金御札</span>
                <span class="val">{{userDate.gold_yuzha}}</span>
            </li>
            <div class="clearf"></div>
        </ul>
    </section>
     <section>
        <ul>
            <li>
                <img src="../img/式神录爬虫/小图/八岐大蛇鳞片.png">
                <span class="name">八岐大蛇鳞片</span>
                <span class="val">{{userDate.bqds_lp}}</span>
            </li>
            <li>
                <img src="../img/式神录爬虫/小图/大蛇的逆鳞.png">
                <span class="name">大蛇的逆鳞</span>
                <span class="val">{{userDate.bqds_lp}}</span>                
            </li>
            <li>
                <img src="../img/式神录爬虫/小图/逢魔之魂.png">
                <span class="name">封魔之魂</span>
                <span class="val">{{userDate.ds_lp}}</span>
            </li>
            <div class="clearf"></div>
        </ul>
    </section>
     <section>
        <ul>
            <li>
                <img src="../img/式神录爬虫/小图/荣誉.png">
                <span class="name">荣誉</span>
                <span class="val">{{userDate.honor}}</span>
            </li>
            <li>
                <img src="../img/式神录爬虫/小图/勋章.png">
                <span class="name">勋章</span>
                <span class="val">{{userDate.xunzhang}}</span>                
            </li>
            <li>
                <img src="../img/式神录爬虫/小图/皮肤券.png">
                <span class="name">皮肤券</span>
                <span class="val">{{userDate.pfjuan}}</span>
            </li>
            <li>
                <img src="../img/式神录爬虫/小图/友情点.png">
                <span class="name">友情点</span>
                <span class="val">{{userDate.yqdian}}</span>
            </li>
            <li>
                <img src="../img/式神录爬虫/小图/魅力.png">
                <span class="name">魅力</span>
                <span class="val">{{userDate.charm}}</span>
            </li>
            <div class="clearf"></div>
        </ul>
    </section>
     <section>
        <ul>
            <li>
                <img src="../img/式神录爬虫/小图/樱饼.png">
                <span class="name">樱饼</span>
                <span class="val">{{userDate.yingbing}}</span>
            </li>
            <li>
                <img src="../img/式神录爬虫/小图/百鬼夜行门票.png">
                <span class="name">百鬼夜行门票</span>
                <span class="val">{{userDate.yingbing}}</span>                
            </li>
            <li>
                <img src="../img/式神录爬虫/小图/式神挑战卷.png">
                <span class="name">式神挑战券</span>
                <span class="val">{{userDate.sstzj}}</span>
            </li>
            <li>
                <img src="../img/式神录爬虫/小图/痴念之卷.png">
                <span class="name">痴念之券</span>
                <span class="val">{{userDate.cnzjuan}}</span>
            </li>
            <div class="clearf"></div>
        </ul>
    </section>
    
    <h3>六星结界卡</h3>
    <ul>

    </ul>
    <p class="content-tips">暂无</p>
    <div class="clearf"></div>
</div>
<!--斗技-->
<div class="content-pvp white" :class="{display: doujiClass}" >
    <p class="content-tips">以下为截止至2018-12-22 09:41:10</p>
    <h3>个人斗技</h3>
    <section>
        <img src="../img/式神录爬虫/pvp/个人斗技.png" alt="#">
        <div class="tof">
            <div class="data-item">
                <span class="data-name">段位</span>
                <span class="data-value">一段</span>
            </div>
            <div class="data-item">
                <span class="data-name">积分</span>
                <span class="data-value">1000</span>
                <span class="data-name">排名</span>
                <span class="data-value">30841</span>
            </div>     
        </div>
        <div class="clearf"></div>
    </section>
    
    <h3>协同斗技</h3>
    <section>
        <img src="../img/式神录爬虫/pvp/个人斗技.png" alt="#">
        <div class="tof">
            <div class="data-item">
                <span class="data-name">段位</span>
                <span class="data-value">一段</span>
            </div>
            <div class="data-item">
                <span class="data-name">积分</span>
                <span class="data-value">1000</span>
                <span class="data-name">排名</span>
                <span class="data-value">4515</span>
            </div>     
        </div>
        <div class="clearf"></div>
    </section>

</div>
<!--御魂-->
    <div class="content-yuhun" pop="[object Object]" :class="{display: yvhunClass}">
        <ul class="yuhun-tabs">
            <li class="sort" @click="showXinJi()">
                <span class="txt">
                    <span>星级</span>
                    <span class="sanjiao" v-bind:class="{sanjiaotrans: sj}">▼</span>
                    
                </span>
            </li>
            <li class="pos" @click="showYuhun(0)">   
                <span class="txt pos-1" v-bind:style="showYuhun0" >壹</span>
                <div v-bind:style="showYuhunDiv0"></div>
            </li>
            <li class="pos" @click="showYuhun(1)">   
                <span class="txt pos-2"
                v-bind:style="showYuhun1" >貳</span>
                <div v-bind:style="showYuhunDiv1"></div>
            </li>
            <li class="pos" @click="showYuhun(2)">   
                <span class="txt pos-3" v-bind:style="showYuhun2" >叁</span>
                <div v-bind:style="showYuhunDiv2"></div>
            </li>
            <li class="pos" @click="showYuhun(3)">   
                <span class="txt pos-4" v-bind:style="showYuhun3" >肆</span>
                <div v-bind:style="showYuhunDiv3"></div>
            </li>
            <li class="pos" @click="showYuhun(4)">   
                <span class="txt pos-5" v-bind:style="showYuhun4" >伍</span>
                <div v-bind:style="showYuhunDiv4"></div>
            </li>
            <li class="pos" @click="showYuhun(5)">   
                <span class="txt pos-6" v-bind:style="showYuhun5">陆</span>
                <div v-bind:style="showYuhunDiv0"></div>
            </li>
            <div class="clearf"></div>
        </ul>
        <div class="content-wrap">
            <h3>御魂总数 2109/6000</h3>
            <h3>+15御魂总数 211</h3>
            <!-- <ul class="yuhun-list">
                <span> -->
            <transition-group name="cell" tag="div" class="container yuhun-list" >
                    <div class="yuhun-item-wrap cell" v-for="item in yuhun" :key="item.id" @click="yhdetail(item.id)">
                        <div class="yvhun">
                            <div class="yvhun-item yvhun-pos-1 yun-level-6">
                                    <img :src="'http://127.0.0.1:3000/'+item.src">
                                    <img class="yvhun-img-border" src="../img/式神录爬虫/小图/yuhun-border-4.png" alt="#" v-bind:style="transform">
                                <div class="star">
                                    <i class="icon icon-star-unawake"></i>
                                    <i class="icon icon-star-unawake"></i>
                                    <i class="icon icon-star-unawake"></i>
                                    <i class="icon icon-star-unawake"></i>
                                    <i class="icon icon-star-unawake"></i>
                                    <i class="icon icon-star-unawake"></i>
                                </div>
                                <div class="label">+15</div>
                                <span class="equipped" v-if="item.yh_is == 1">装备
                                </span>
                            </div>
                        </div>
                    </div>
                    
            </transition-group>    
          
            <ul class="menu-sort" v-if="xinJicalss == 1">
                <li @click="yuhunattr('yh_rank')">等级</li>
                <li @click="yuhunattr('yh_slevel')">星级</li>
                <li @click="yuhunattr('yh_atk')">攻击</li>
                <li @click="yuhunattr('yh_defense')">防御</li>
                <li @click="yuhunattr('yh_life')">生命</li>
                <li @click="yuhunattr('yh_crit')">暴击</li>
                <li @click="yuhunattr('yh_crit_hurt')">暴击伤害</li>
                <li @click="yuhunattr('yh_speed')">速度</li>
                <li @click="yuhunattr('yh_hit')">效果命中</li>
                <li @click="yuhunattr('yh_resist')">效果抵抗</li>
                <li @click="yuhunattr('yh_atk_add')">攻击加成</li>
                <li @click="yuhunattr('yh_defense_add')">防御加成</li>
                <li @click="yuhunattr('yh_life_add')">生命加成</li>
            </ul>
        </div>
        <!-- 御魂详情 -->
<div class="swiper-slide" style="width: 750px; margin-right: 6px;" v-if="yhDetShow == 1">
    <div data-index="1" class="containter">
      <div class="popup-content">
        <div class="yuhun-detail">
          <header>
          <!-- <div class="yuhun-item equip yuhun-pos-1 yuhun-level-6"> -->
          <div class="yuhun-detail-img">
            <img :src="'http://127.0.0.1:3000/'+yhdet.src">
            <img class="yvhun-detail-img-border" src="../img/式神录爬虫/小图/yuhun-border-4.png" alt="#" v-bind:style="transform">           
            <div class="star">
              <i class="icon icon-star-unawake"></i>
              <i class="icon icon-star-unawake"></i>
              <i class="icon icon-star-unawake"></i>
              <i class="icon icon-star-unawake"></i>
              <i class="icon icon-star-unawake"></i>
              <i class="icon icon-star-unawake"></i>
            </div>
            
        </div>
            <h2>{{yhdet.name}}+{{yhdet.yh_rank}}</h2>
            <div class="star">
              <span class="level-icons">
                <img src="../img/式神录爬虫/小图/橙勾玉.png" alt="" class="icon  icon-star-awake"/>
                <img src="../img/式神录爬虫/小图/橙勾玉.png" alt="" class="icon  icon-star-awake"/>
                <img src="../img/式神录爬虫/小图/橙勾玉.png" alt="" class="icon  icon-star-awake"/>
                <img src="../img/式神录爬虫/小图/橙勾玉.png" alt="" class="icon  icon-star-awake"/>
                <img src="../img/式神录爬虫/小图/橙勾玉.png" alt="" class="icon  icon-star-awake"/>
                <img src="../img/式神录爬虫/小图/橙勾玉.png" alt="" class="icon  icon-star-awake"/>
              </span>
            </div>
           </header>
          <ul class="yuhun-attrs">
            <li v-if="yhdet.yh_main == '攻击'"><span class="pull-right">+{{yhdet.yh_atk}}</span>
            攻击</li>
            <li v-if="yhdet.yh_main == '攻击加成'"><span class="pull-right">+{{yhdet.yh_atk_add}}%</span>
            攻击加成</li>
            <li v-if="yhdet.yh_main == '生命'"><span class="pull-right">+{{yhdet.yh_life }}</span>
            生命</li>
            <li v-if="yhdet.yh_main == '生命加成'"><span class="pull-right">+{{yhdet.yh_life_add}}%</span>
            生命加成</li>
            <li v-if="yhdet.yh_main == '防御'"><span class="pull-right">+{{yhdet.yh_life }}</span>
            防御</li>
            <li v-if="yhdet.yh_main == '速度'"><span class="pull-right">+{{yhdet.yh_speed }}</span>
            速度</li>

          <li v-if="yhdet.yh_main != '攻击' && yhdet.yh_atk != 0 "><span  class="pull-right">+{{yhdet.yh_atk}}</span>
          攻击
          </li>
          <li v-if="yhdet.yh_main != '生命' && yhdet.yh_life != 0 "><span  class="pull-right">+{{yhdet.yh_life}}0</span>
          生命
          </li>
          <li v-if="yhdet.yh_main != '防御' && yhdet.yh_defense != 0 "><span  class="pull-right">+{{yhdet.yh_defense}}</span>
          防御
          </li>
          <li v-if="yhdet.yh_main != '攻击加成' && yhdet.yh_atk_add != 0 "><span  class="pull-right">+{{yhdet.yh_atk_add}}%</span>
          攻击加成
          </li>
          <li v-if="yhdet.yh_main != '生命加成' && yhdet.yh_life_add != 0 "><span  class="pull-right">+{{yhdet.yh_life_add}}%</span>
          生命加成
          </li>
          <li v-if="yhdet.yh_defense_add != 0 "><span   class="pull-right">+{{yhdet.yh_defense_add}}%</span>
          防御加成
          </li>
          <li v-if="yhdet.yh_main != '速度' && yhdet.yh_speed != 0 "><span  class="pull-right">+{{yhdet.yh_speed}}</span>
          速度
          </li>
          <li v-if="yhdet.yh_crit != 0 "><span  class="pull-right">+{{yhdet.yh_crit}}%</span>
          暴击
          </li>
          <li v-if="yhdet.yh_crit_hurt != 0 "><span  class="pull-right">+{{yhdet.yh_crit_hurt}}%</span>
          暴击伤害
          </li>
          <li v-if="yhdet.yh_hit != 0 "><span  class="pull-right">+{{yhdet.yh_hit}}%</span>
          效果命中
          </li>

        </ul>
    <div class="desc"><!---->
      <p>{{yhdet2}}</p>
      <p>{{yhdet4}}</p>
    </div>
  </div>
</div>
</div>
</div>
</div>

<!-- 阴阳术 -->
    <div class="content-yys" :class="{display: yinyangshuClass}">
        
    </div>
    <!-- 皮肤 -->
   <div style="width:760px;dispaly:flex;" id="sc-main" :class="{display: pifuClass}">
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

    <!-- 徽章 -->
    <div  :class="{display: huizhangClass}">
        <div id="pf-main">
        <div v-for='item in list' :key='item.id' class="pffl">
            <img :src="'http://127.0.0.1:3000/'+item.src" class="dw">
            <p>{{item.pname}}</p>
        </div>
        <div style='clear:both;'></div>
            <span>仅显示高级徽章</span>
    </div>
    </div>
</div>
    <div class="bb-d-tabs">
            <div class="bb-tab_sc">
                <i class="bb-icon bb-icon-collect"></i>
                <span>收藏</span>
            </div>
            <div class="bb-tab_gm" @click="jump1() ">
                <span >
                    加入购物车
                </span>
            </div>
    </div>
</div>

</template>

<script>
export default {
    data(){
        return {
           userId:this.$route.params.Id,
           sj:false,
           shishenClass: false,
           zichanClass: true,
           doujiClass: true,
           yvhunClass: true,
           yinyangshuClass: true,
           pifuClass:true,
           huizhangClass:true,
           xinJicalss:1,
           yhDetShow:0,
           shSele:false,
           ssDj:false,
           yuhun:[],
           yuhunsite:0,
           shishen:{},
           yhdet:{},
           yhdet2:{},
           yhdet4:{},
           userDate:{},
           djClass:true,
           xjClass:false,
           xydClass:false,
            naSs:true,
            naZc:false,
            naDj:false,
            naYh:false,
            naYys:false,
            naPf:false,
            naHz:false,
           transform:{
               transform:"rotate(0deg)",
           },
           showYuhun0:{
               color:"#E74E4B",
           },
           showYuhunDiv0:{
               backgroundColor:"#FEF3F3",
           },
           showYuhun1:{
               color:"#1E1E1E",
           },
           showYuhunDiv1:{
               backgroundColor:"#F3F3F3",
           },
           showYuhun2:{
               color:"#1E1E1E",
           },
           showYuhunDiv2:{
               backgroundColor:"#F3F3F3",
           },
           showYuhun3:{
               color:"#1E1E1E",
           },
           showYuhunDiv3:{
               backgroundColor:"#F3F3F3",
           },
           showYuhun4:{
               color:"#1E1E1E",
           },
           showYuhunDiv4:{
               backgroundColor:"#F3F3F3",
           },
           showYuhun5:{
               color:"#1E1E1E",
           },
           showYuhunDiv5:{
               backgroundColor:"#F3F3F3",
           }, 
           list:[],
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
            this.getYuhun();
            this.showXinJi();
            this.getshishen();
            this.getuser();
            this.getpf();
            this.gethz();
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
                console.log(result.data);
            })
        },
        gethz(){
            var url=`http://127.0.0.1:3000/gethz`;
            this.axios(url).then((result)=>{
                console.log(result.data);
                this.list=result.data;
            })
        },
        shDjclor(res){
                this.djClass = false;
                this.xjClass = false;
                this.xydClass = false;
                this.shSele = false;
                this.ssDj = false;
                if(res == 1){
                    this.djClass = true;
                    var url=`http://127.0.0.1:3000/sh?userId=${this.userId}&ss=ss_rank`;
                    this.axios.get(url).then(result=>{
                        this.shishen = result.data;
                        
                    })
                }else if(res == 2){
                    this.xjClass = true;
                    var url=`http://127.0.0.1:3000/sh?userId=${this.userId}&ss=ss_slevel`;
                    this.axios.get(url).then(result=>{
                        this.shishen = result.data;
                  
                    })
                }else{
                    this.xydClass = true;

                    var url=`http://127.0.0.1:3000/sh?userId=${this.userId}&ss=slv`;
                    this.axios.get(url).then(result=>{
                        this.shishen = result.data;
                 
                    })
                }
         },
        show(res){
            this.naSs = false;
            this.naZc = false;
            this.naDj = false;
            this.naYh = false;
            this.naYys = false;
            this.naPf = false;
            this.naHz = false;
            this.shishenClass = true;
            this.zichanClass = true;
            this.doujiClass = true;
            this.yvhunClass = true;
            this.yinyangshuClass = true;
            this.pifuClass = true;
            this.huizhangClass = true;
            if(res=="1"){
            this.naSs = true;
            this.shishenClass = false;
             
           }else
            if(res=="2"){
               this.naZc = true;
               this.zichanClass = false;
           }else if(res=="3"){
               this.naDj = true;
               this.doujiClass = false;
           }else if(res=="4"){
                this.naYh = true;
               this.yvhunClass = false;
           }else if(res=="5"){
               this.naYys = true;
               this.yinyangshuClass = false;
           }else if(res=="6"){
               this.naPf = true;
               this.pifuClass =false;
           }else if(res =="7"){
               this.naHz = true;
               this.huizhangClass = false;
           }
        },
        showXinJi(){
            if( this.xinJicalss == 0){
                 this.xinJicalss = true;
                 this.sj = false;
            }else{
                 this.sj = true;
                 this.xinJicalss = false;
              
            } 
        },
        showYuhun(site){
                this.showYuhun0 = {color:"#1E1E1E"}
                this.showYuhunDiv0 = {backgroundColor:"#F3F3F3"}
                this.showYuhun1 = {color:"#1E1E1E"}
                this.showYuhunDiv1 = {backgroundColor:"#F3F3F3"}
                this.showYuhun2 = {color:"#1E1E1E"}
                this.showYuhunDiv2 = {backgroundColor:"#F3F3F3"}
                this.showYuhun3 = {color:"#1E1E1E"}
                this.showYuhunDiv3 = {backgroundColor:"#F3F3F3"}
                this.showYuhun4 = {color:"#1E1E1E"}
                this.showYuhunDiv4 = {backgroundColor:"#F3F3F3"}
                this.showYuhun5 = {color:"#1E1E1E"}
                this.showYuhunDiv5 = {backgroundColor:"#F3F3F3"}
                this.getYuhun(site)
            if (site == 0){
                // 旋转
                this.transform = {transform:"rotate(0deg)"};
                this.showYuhun0 = {color:"#E74E4B"}
                this.showYuhunDiv0 = {backgroundColor:"#FEF3F3"}
            }else if(site == 1){
                 // 旋转
                this.transform = {transform:"rotate(-45deg)"};
                this.showYuhun1={color:"#E74E4B"}
                this.showYuhunDiv1={backgroundColor:"#FEF3F3"}
            }else if(site == 2){
                 // 旋转
                this.transform = {transform:"rotate(-90deg)"};
                this.showYuhun2={color:"#E74E4B"}
                this.showYuhunDiv2={backgroundColor:"#FEF3F3"}
            }else if(site == 3){
                 // 旋转
                this.transform = {transform:"rotate(-180deg)"};
                this.showYuhun3={color:"#E74E4B"}
                this.showYuhunDiv3={backgroundColor:"#FEF3F3"}
            }else if(site == 4){
                 // 旋转
                this.transform = {transform:"rotate(135deg)"};
                this.showYuhun4={color:"#E74E4B"}
                this.showYuhunDiv4={backgroundColor:"#FEF3F3"}; 
            }else if(site == 5){
                 // 旋转
                this.transform = {transform:"rotate(90deg)"};
                this.showYuhun5={color:"#E74E4B"}
                this.showYuhunDiv5={backgroundColor:"#FEF3F3"}
            }
        },
        shDj(){
            this.shSele = !this.shSele;
            this.ssDj = !this.ssDj;
           
        },
        yuhunattr(attr){
            var site = this.yuhunsite;
            if(site == undefined){
                site = 0;
            }
            var attr = attr;
            
            var url=`http://127.0.0.1:3000/yvattr?userId=${this.userId}&yh_site=${site}&attr=${attr}`;
            this.axios.get(url).then(result=>{
                this.yuhun = result.data;
                this.xinJicalss = 0;
            
            })
        },
        yhdetail(id){
            if(this.yhDetShow == 0){
                this.yhDetShow = 1;
                var yuhun = this.yuhun;
            for(var i in yuhun){
                if(this.yuhun[i].id == id){
                    this.yhdet = this.yuhun[i];
                }
            }
            var str = this.yhdet.effect;
            this.yhdet2 = str.split("||")[0];
            this.yhdet4 = str.split("||")[1];
            }else{
                this.yhDetShow =  0;
            }
        },
        getshishen(){
            
            var url=`http://127.0.0.1:3000/sh?userId=${this.userId}&ss=ss_rank`;
           
            this.axios.get(url).then(result=>{
                this.shishen = result.data;
                
            })
        },
        getYuhun(site){
            this.yuhunsite = site;

            var url = `http://127.0.0.1:3000/yv?userId=${this.userId}&yh_site=${site}`;
            this.axios.get(url).then(result=>{
                // 获取了玩家id为1的所有御魂id和相应的御魂属性
            this.yuhun = result.data;

            })
        },
        getuser(){
            var url = `http://127.0.0.1:3000/User?userId=${this.userId}`;
            this.axios.get(url).then(result=>{
                this.userDate = result.data[0];
                
            })
        },
        jump1(){
            this.$router.push(`/shopList`);
            this.$store.state.shoplist1.push(this.userId);
            
        }
    },
    computed:{
        // jump1(){
        //     var Msgs = this.$store.state.shoplist1;
        //   
        //     return Msgs
        // }
    },

}
</script>

<style>
.colred{
    color: #E74E4B;
}
.container{
    width: 750px !important;
}
.cell{
    border:0 solid white !important;
}
*{margin:0;padding:0}
.cell-move {
  transition: transform 1s;
}
.display{
    display:none;
}
hr{
    border-left:0;
    border-right: 0;
}
.clearf{
    clear:both !important;
    content:" ";
}
.relative{
    position:relative;
}
.bod1{
    background:#F5F5F5;
}
.white{
    background:white;
}
.list-block{
    background:white;
}

.content-heroes .content-wrap{
    padding:10px;
    box-sizing: border-box;
}
/*<!--ʽ���ʲ�����yvhun-->*/
.hair-tab{
    display:inline-flex;
    width: 100%;
    justify-content: space-between;
    margin-top:-1px;
}
.hair-tab a{
    width: auto;
    height:100%;
    min-width: 13.39%;
    padding: 14px;
    font-size: 22px;
    color:#8D8D8D;
    text-decoration: none;
    box-sizing: border-box;
    text-align: center;
    background: white;
    line-height:37px;
}
.bgred{
    background: #E74E4B !important;
    color:white !important;
}
/*div{*/
    /*border:1px solid red;*/
/*}*/

.bod1{
    width:750px;
    margin: auto;
    /*border: 1px solid blue;*/
}


.list-block .list-item {
    display:flex;
    padding:14px;
    justify-content: space-between;
}
.list-block .list-item p{
    font-size:17px;
    line-height: 34px;
    margin:0
}
/*������ʽ*/
.list-block .hd{
    display: flex;
    justify-content: space-between;
}
.list-block .hd .gray{
    margin-right:0.25rem;
    color:#8D8D8D;
    font-size:1rem;
}


.list-block .color-primary{
    color:black;
    font-size:1.1rem;
}
/*60��*/

.list-block .list-item .role-info h2 span{
    font-size: 1.4rem;

}
.list-block .list-item .role-info .price1{
    color: #e74e4b;
    font-weight: 700;
    font-size: 1.5rem;
    margin-left:-4px !important;
    font-size:26px;
    line-height: 42px;
}
.list-block .list-item .role-info ul{
    list-style: none;
    display:block;
}
.list-block .list-item .role-info .intro {
    height:20px;
    margin: 0.2rem 0px 0.2rem 0px;

}
.list-block .list-item .role-info .intro li{
    float:left;
    display:block;
    font-size:1rem;
    color:#8D8D8D;
    padding-right: 7px;
    font-size:20px;
}
.highlight li{
    float: left;
    padding: .1rem .3rem;
    font-size:0.8rem;
    background:#F1F1F1;
    display: block;
    width:auto;
    border-radius: .15rem;
}
.content-heroes .hero-tabs{
    list-style: none;
    background: white;
}
.content-heroes .hero-tabs li{
    float: left;
    width:231px;
}
.content-heroes .hero-tabs li:first-child {

    margin: 14px 14px 0 14px;
}
.content-heroes .hero-tabs li:nth-child(2) {

    margin: 14px 0 0 0;
}
.content-heroes .hero-tabs li:nth-child(3) {

    margin: 14px 14px 0 14px;
}
.content-heroes .hero-tabs li span{
    display: block;
    width: 230px;
    /* border: 1px solid #E74E4B;
    color: #E74E4B; */
    text-align: center;
    line-height:40px;
    border-radius: 5px;
    background: #f3f3f3;
}
.content-heroes .hero-tabs li.current span{
    border: 1px solid #E74E4B;
    
    background:white!important;
}
.content-heroes .hero-tabs li.current span p{
    color: #E74E4B;
    display: inline-block;
    font-size:17px;
    margin:0;
    transition:all 0.3s;
}
/* 式神-等级下详情 */
.content-heroes .hero-tabs li:first-child .filter-select{
    position:absolute;
    list-style: none;
    z-index:100;
    width:231px;
}
.content-heroes .hero-tabs li:first-child .filter-select li{
    border-bottom:1px solid #E5E5E5 ;
    text-align: center;
    line-height:56px;
    background: white;
    margin: 0;
    width:231px;
}
.content-heroes .hero-tabs li:first-child .filter-select li:first-child{
    box-shadow: black 2px;
    border-radius: 10px 10px 0 0 ;
}
.content-heroes .hero-tabs li:first-child .filter-select li:last-child{
    box-shadow: black 2px;
    border-radius: 0 0 10px 10px;
}
.content-heroes .content-wrap .sub-tab-heroes .hero-list  .hero-item-ssr .name{
   width:100%;
   background:#F2F2F2;
   line-height: 29px;
   text-align: center;
   border-bottom-right-radius: 0.3rem;
   border-bottom-left-radius: 0.3rem;
}
/*定位以及动画 ul*/
.content-heroes .content-wrap .sub-tab-heroes .hero-list{
    margin-right:10px;
    margin-top:5px;
    /*box-sizing: border-box; */
    width: 730px;
    display: flex;
    justify-content: space-around;
    flex-wrap:wrap;
}

.content-heroes .content-wrap .sub-tab-heroes .hero-list .hero-item{
   width: 145px;
    transition: all .6s;
    border-left: 10px;
    border-bottom:10px;
    display: inline-block;
    padding-right:10px;
    padding-bottom: 10px;
    height:171px;
}

/*资产*/

.content-wrap .sub-tab-heroes .hero-list{
    list-style: none;
}



.content-wrap .sub-tab-heroes .hero-list .frame{
    border:2px solid #F8D26B;
    height: 134px;

}
/*liͼƬ�µĵ�һ��div*/
.content-wrap .sub-tab-heroes .hero-list .frame .wrap{
    position: relative;
}
/*liͼƬ�µĵ�һ��div �µ�ͼƬ*/
.content-wrap .sub-tab-heroes .hero-list .frame .wrap>img{
    width: 131px;
    height:131px;
}

/*liͼƬ�µĵ�һ��div �µľ��ѱ�־*/
.content-wrap .sub-tab-heroes .hero-list .frame .wrap .awake{
    position:absolute;
    bottom:19px;
    right:0;
    font-size: 12px;
    background:#AA39C6 ;
    height: 16px;
    width:16px;
    color: white;
    text-align: center;
    border-radius: 3px;
    line-height: 16px;
}
/*liͼƬ�µĵ�һ��div �µľ�������*/
.hero-item-ssr .wrap:before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    border: 9px solid rgba(253,223,137,1);
    border-right-color: white;
    border-bottom-color: transparent;

    /*overflow: hidden;*/
}
/*liͼƬ�µĵ�һ��div �µĵȼ�����־����*/
.content-wrap .sub-tab-heroes .hero-list .frame .wrap .level-status{
    position:absolute;
    top:4px;
    left:4px;
    background: #4B322C;
    width:17px;
    height:17px;
    transform:rotate(45deg);
    /*transform-origin:*/

}
/*liͼƬ�µĵ�һ��div �µĵȼ�������*/
.content-wrap .sub-tab-heroes .hero-list .frame .wrap .level-status .con{
    transform:rotate(-45deg);
    display: block;
    margin-left:2px;
    color: #F5F5F5;
    font-size: 13px;
    vertical-align: top;
    margin-top:-2px;
}
/*liͼƬ�µĵ�һ��div �µĹ���*/
.content-wrap .sub-tab-heroes .hero-list .frame .wrap .level-icons{
    display: block;
    position: absolute;
    bottom: 4px;
    width:130px;
    box-sizing: border-box;
    background:rgba(227,203,145,0.5) ;
    padding: 1px 0 0 1px;
    height:15px;
    /* z-index: 20; */
    text-align: center;
}
.content-wrap .sub-tab-heroes .hero-list .frame .wrap .level-icons img{
    width:11px;
    height:14px;
    margin-left:-1px;
    vertical-align: top;
}
    /*li�µ�����*/


/*资产样式*/
.content .content-asset{
    padding:10px;
}
.content .content-asset .pull-right{
    float: right;
    font-weight: 400;
    font-size:100%;
}
.content .content-asset h3{
    font-weight: 400;
    font-size:85%;
} 
.content .content-asset section{
    padding: 5px;
    box-sizing: border-box;
    margin-bottom: 10px;
}
.content .content-asset ul {
    list-style: none;
    width:720px;
    background: #F7F7F7;
   
} 
.content .content-asset ul li{
    float: left;
    width: 50%;  
} 
.content .content-asset  ul li img{
    width:20px;
    vertical-align: middle;
} 
.content .content-asset ul li .name{
   padding:0 5px;
   display: inline-block;
   min-width: 63px;
   font-size:17px;
} 

/*六星结界卡*/
.content .content-asset .content-tips{
    text-align: center;
    display: block;
    background:#F7F7F7;
}
/*斗技*/
.content .content-pvp{
    padding: 10px;
}
.content .content-pvp .content-tips{
    font-size: 12px;
    color: #888888;
    text-align: center;
    margin-bottom:5px;
    line-height:20px;
}
.content .content-pvp h3{
    font-size: 85%;
    font-weight:lighter;
}
.content .content-pvp section{
    background:#F7F7F7;
    padding: 5px;
    margin-bottom: 10px;
    
}
.content .content-pvp section .tof .data-item {
    margin-top:6px;
   
}
.content .content-pvp section .tof .data-item span{
    
    color: #1e1e1e;
        font: 15px/1.7 PingFangSC-Light,Microsoft Yahei,Heiti SC,miui,helvetica;
    
}
.content .content-pvp section .tof .data-item .data-name{
    width: 35px;
    display: inline-block;
}
.content .content-pvp section .tof .data-item .data-value{
    width: 56px;
    display: inline-block;
}
.content .content-pvp section img{
    width: 60px;
    float: left;

    margin:3px 10px 10px 0;
}
/*御魂*/

.content .content-yuhun .yuhun-tabs {
    list-style: none;
    height:63px;
    background:white;
}
.content .content-yuhun .yuhun-tabs li{
    float: left;
    
}

.content .content-yuhun .yuhun-tabs li:nth-child(1){
    width:22%;
    height: 63px;
    background: white;
    text-align: center;
    border-bottom: 1px solid #EBEBEB;
    border-right:2px solid #EBEBEB;
    
}

.content .content-yuhun .yuhun-tabs li{
    padding:  14px 0;
    font: 22px/1.7 PingFangSC-Light,Microsoft Yahei,Heiti SC,miui,helvetica;
    border-bottom: 1px solid #EBEBEB;
} 
.content .content-yuhun .yuhun-tabs .pos{
    background: white;
    text-align: center;
    width: 13%;
    height:63px;
    position:relative;
    
}
.content .content-yuhun .yuhun-tabs .pos .txt{
    position:absolute;
    top:11px;
    left:38px;
    z-index:10;
}
.content .content-yuhun .yuhun-tabs .pos div{
    background: #F3F3F3;
    width: 45px;
    height:45px;
    content:"";
    margin: auto;
    margin-top:-5px;
    border-top-right-radius:50%;
    border-bottom-left-radius: 50%; 
    border-bottom-right-radius: 50%; 
    transform-origin: center;
}
.content .content-yuhun .yuhun-tabs .pos:nth-child(3) div{
    transform: rotate(-45deg);
} 
.content .content-yuhun .yuhun-tabs .pos:nth-child(4) div{
    transform: rotate(-90deg);
} 
.content .content-yuhun .yuhun-tabs .pos:nth-child(5) div{
    transform: rotate(-180deg);
} 
.content .content-yuhun .yuhun-tabs .pos:nth-child(6) div{
    transform: rotate(-225deg);
} 
.content .content-yuhun .yuhun-tabs .pos:nth-child(7) div{
    transform: rotate(-270deg);
} 
.content-yuhun .content-wrap{
    padding: 14px;
    background: white;
    position:relative;
    /*计算高*/
   
    
}
.content-yuhun .content-wrap h3:nth-child(1){
    font-size: 100%;
    font-weight: 400;
    display: block;
    margin: 3px ;
    font: 21px/1.7 PingFangSC-Light,Microsoft Yahei,Heiti SC,miui,helvetica;
}
.content-yuhun .content-wrap h3:nth-child(2){
    font-size: 100%;
    font-weight: 400;
    margin-top:7px;
    margin-bottom:3px;
    font: 21px/1.7 PingFangSC-Light,Microsoft Yahei,Heiti SC,miui,helvetica;
}
.content-yuhun .content-wrap ul{
    list-style:none;
}
/*li样式*/
.content-yuhun .content-wrap  .yuhun-item-wrap{
  
   width:147px;
   height:147px;
   /* height:138px; */
   padding-right: 14px;
   padding-bottom: 14px;
   display: inline-block;

}
/* li下div御魂块yvhun */
.content-yuhun .content-wrap  .yuhun-item-wrap .yvhun {
    width: 100%;
    height:100%;
   
    position:relative;
}
.content-yuhun .content-wrap  .yuhun-item-wrap .yvhun .yvhun-item{
    height:100%;
    border: 1px solid #503415;
    background: #ECE3D8;
}
/* 御魂图片 */
.content-yuhun .content-wrap  .yuhun-item-wrap .yvhun .yvhun-item>img{
    margin:auto;
    display: block;
    padding-top:27px; 
    width:60%;
}
/* 御魂图片的边框 */
.content-yuhun .content-wrap  .yuhun-item-wrap .yvhun .yvhun-item .yvhun-img-border{
    position:absolute;
    top:-14px;
    right:11px;
    transform-origin: 51% 59%;
    width:83%!important;
    transform: rotate(0deg);
}
/* 六个勾玉 */
.content-yuhun .content-wrap  .yuhun-item-wrap .yvhun .yvhun-item .star{
    width: 108px;
    display: flex;
    margin-left:27px;
    /* position: absolute; */
    
}
/* 六个勾玉下的每个图片 */
.content-yuhun .content-wrap  .yuhun-item-wrap .yvhun .yvhun-item .star i{
    background-image: url(../img/式神录爬虫/小图/橙勾玉.png);
    width:17px;
    height:20px;
    
    margin:0 -2px;
}
/* +15 */
.content-yuhun .content-wrap  .yuhun-item-wrap .yvhun .yvhun-item .label{
    position:absolute;
    left:0;
    top:0;
    color:white;
    background: linear-gradient(-90deg,transparent,
    rgba(0,0,0,.7) 54%,rgba(0,0,0,.7));
    font-size:12px;
    padding:0 5px 0 3px;

}
/* 装备 */
.content-yuhun .content-wrap  .yuhun-item-wrap .yvhun .yvhun-item span{
    position:absolute;
    right:0px;
    top:1px;
    color:white;
    background:#AA39C6;
    font-size:12px;
    padding:0 2px;
}
/* 阴阳术 */
.content-yys header {
    display:flex;
}
.content-yys header .avatar{
    width:196px;
    height:196px;
    margin-right:14px;
    
}

.content-yys .attrs {   
    width:494px;
    height:199px;
}
.content-yys .attrs .hero-attr{
    font: 21px/1.3 PingFangSC-Light,Microsoft Yahei,Heiti SC,miui,helvetica;
    font-family: 'Helvetica Neue', Helvetica, sans-serif;
    background: linear-gradient(90deg,#f4f0ec 80%,hsla(0,0%,100%,0));
    margin-bottom: 11PX;
    height: 31PX;
    line-height: 31PX;
}
.content-yys .attrs .hero-attr .pull-right{
    float:right;
}
.content-yys .attrs .hero-attr .pull-right .add{
    color:#D96932;
}
.content-yys .attrs .hero-attr .icon-hero-attr-attack{
    background-image: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAsCAMAAAAQPRtoAAAAYFBMVEVMaXGyl36yl3+yln+zlHuyl36xln6yl3+3nYfi29bj3diyl3zSwrjg2NLd1Myxl36/qZa6oo3ZzcWyln7VyL+okm3Fr6Cxl37MuKy2g4HEnpubTU2XRkafVlaqa2q9kY4MA0ojAAAAGHRSTlMAxf9cDvDbhf///yj///+o////RP8E/27AkpJSAAACKklEQVR4AXSV8XLCIAyHNXMTIiBlDGlL6/u/5cKIDBG/v3rXy1G+/JIeWo7whuPhDR/wlo9xxekT3vJ1GpacAYTEAVIAnEcVFwBQqM0rqOjVZVByBbCIVkw94NACXF8rvgHonZ8k9qgJHb387it+vgACysnjK1ZhIAM/XckNQGiMAQc4ITUZuL0KjqiFwREhYgT4PPV3n2R+NcQIIycy0Av26ITGBhVmYlEG8wf7TvSxCFZY8fO6psK2x6zFNlEr4TJZ5gO5r6lljpM0bdROJDiSYIfMnHqcVRibqJ2fBSs6YZ631LDne+r/qF1IsMpW/it2lOHpkD/RikRfqmCsgmMiZsSlvQriX89YNIfLce59yqzBtx+mkYiWo8bhwokFP5taM2nBDInmqN2KYFsq7okp/fDO6G3Dgi+ib4dyCCdYtxcozpekkJlKomuE+0PYhkxbE+hyytOg1DuvunZVv4xNO44uMfVjXJpHw3mtmVyaRhT2hAzliftSu5+TX0skFmIKyMRQu18zFmIt2Zf7cr8vS1g3RP2YspqxmmRKxH3N3dtKE0sxNafOck1ynZdovTEondNSakfPmnSwY8fz0k1lt5E4PY67yFPZzX6/9+K6LyzYdrNfNwyJbtH1Qbhuw9Q9ZkjciBgGe4yjFgIOYMG34U7Wwg2XJYdruPmVxZ5shcPVcy2ibWDsA+GH/5f6FzOK8M+8/Yv9jkBdSXKNzMpCUb1PbOuCMgAACFZTgqp6WvEAAAAASUVORK5CYII=)
    }


.icon-hero-attr-life{
    background-image: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAsCAMAAAAQPRtoAAAAYFBMVEVMaXGxl36yl3+yln6slXmxln6yl3+5oInh2tTj3diyl3yyl37SxLjd1c2xl3+9ppHBq5S2nITZz8Wxl36yln7HtKHWysDNvKzCrpu2kXqZaCi4mXGidj2pgU6dbjGwjF1WrnYiAAAAGnRSTlMA0v9lB+SF////KPX//7z/////pUT/////E6VkHkcAAAI4SURBVHgBdJXxersqDEC7bBukg4l0gIuK7/+WV9NwwR/2/NuP9uPkhN5a3uAFb7cXvMNL3q9PfHzCSz4/Lo98ASiNF2gF8HV14v4NYFDbHjQA3/dbzw/AgOhUx+hxAHj0J34BwKMZsMMM6AHgt7v7LjigVhF7BoNhF/3RCx41pgmfeGzwStuxE/33DZDQjhYPFM0WG0LCtBv4u7U8ABR/tJNoR/vqm79K/WPgDgAR/TEWvRDRikteUz2TJowAcD8LnviauNGOnWlnwQJrmQB+znFZFqwzUQr0RJ1EW06txsWCD01ptvQ/jQPHojm1GpcIXqkyn0TX1CQuEbzRk0wHsREdmtQeHNeUENkXs8R5CZnWxsBoObUaFwvmIyIrJRwyhZPokhrHxYIPEjFhcyFiptwMVEVJ7YjL1oL5+tl65bawZKKxHokKn6mxYKwF+2P43sxhdjhV0U3R8iuHYWEmyhHnebZ4XGzrgu4WhQNYyNu0OTZturXp19Hx/VMi8d0vJ8+FiygsMkvBSZnNE8DT58EIhk4sWsZSpy+NhTq2jVpW2TJurCk5cRFVdINB5J5SLVn2pRU9NjVbI4LrvtStPIsWXSttngXXrWx2PyosTMRERTv6EMy7378wLmFhzUSO1SkWXF6Y/h3TKNgUMJdeUrh4xyS1ELCiV8q2CO5fy5La6LFiglwsSVzXL7/Djqi0xHX9/zJMBVdQBgcW3CEPjdn5b2KoAJK4KK8rCdfIkhTV+8S2LigDAHFMTiXQEvMhAAAAAElFTkSuQmCC);

}
.icon-hero-attr-defense{
    background-image: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAsCAMAAAAQPRtoAAAAYFBMVEVMaXGyl36yl3+yln6sl3mxl36xln6yl3+2nYbe2NHj3dizl3vRxbna08qxl36+qZW5oYzWy8Gyln7EsaDLu6yOoX3Dx7aDmXG1vaeaqYpMcjZRdTtmhVJbfEZ1j2KmspcTV5dGAAAAE3RSTlMAxf9lCfLbhf///x7//6j///8+WH2WhgAAAkZJREFUeAGUlYlW4zAMRcFl88PBCd6Vpf//l4Pj6FQdp7NcdrCKdfukPkme1QOenx5wUQ+5nFe8vKqHvL2clrwr9aFxgv5Q6v2s4vNVKQM99MAo9fr51POllAXs2PExwSr11Vd8K6UGmBEdxmJQSn13vb8p5YBxQo81cCcGLnvv3gHQsmwCMHzoauDS9+6hPwYAIeJGygCch5cGuPdx/xNQCIIwA/tDjcIA9z7VCwCaFggyJaBeePrNwHMTbAAkShBEoohdi72L2qUJtvuRrmQFqvyBo8aCfRPMR4CYUUlE4RDtheh3FlyJK20ANFGtCURX4Cb6/S5cHElstWZeCmW90WLQcJ6jxuFqgpFzrJqXddZTopUKMOQ8NdEctUPwNB7N0lLqF52oFAqY0kxNu7dg0TVch2AUqmyJIjYq2OZEOwOa6Bo1DpexqCx0MKewhY2YAqBepEVNJjjSwbZSZUnUWFAZW6JlhBFuJ0zcu16pcR9o8W/4XgHMJm52jA0ba+NIBxlM4ZsC5jAmht4A3LsWQW6snMwv8ezX5N8ekpnoAN7JRdMy5jy4+wHMMFNDc8ZEkmsilpWLwjXnfA1bq5iX5LxMMs+Lt0CsnnPe1np2XpfrRrReB0xyXsRUtoGZaQD2ral3ZUk3wXdTeR9Ns0y4UTZACO42jPXo6TeM3GNV9Bne9XuMA+0cOmS4+p2836DH+X4ni81v0XEI/n70+jJa94OVfBgOl0BGzfww3cPh+o/XSvwaKHGRXCOzslBU7xPbuqAMAADoH1Agy0NRVgAAAABJRU5ErkJggg==);

}
.icon-hero-attr-speed{
    background-image: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAsCAMAAAAQPRtoAAAAXVBMVEVMaXGxl36yl3+yln6sl3myl36yl3+2nYbg2dTj3dizl3uxl37SxLnc1c2xl36/qpe6oo3XzMKyln7EsaCqtbvLu6y9wsSGm6h1kKAwX3zPz85UeI5khJc+aYOYqLJGSTe+AAAAE3RSTlMAzv9lCeeF////Hvj//6j///8+Elhc8wAAAgxJREFUeAF0y0EWwBAMQEE+RFDa+1+2275KZj/hK+KIwZFwJXvkgqtks1SQpoYmUK3RB0xt10knjG6UBVt1y/0nj25Y53jJKqPcykEYiqpSR8EVCFIAAoHsf5lDgEvrcn6fEsfH137f7YtPkoY2pKGz/fi99d4EWyJz0kI4GmhJton+3AUfgrymFxVcvMKVMnXOQ6hjE/3VBHtShyIid6eXElKhgfXkm+ivv72b/hNRSYPqrhSo877KMAPo/exjCWlScqo08HYz8DEES3q5UOaJJU8Tpov+4OFSS7DAM7ci8SNaIWoIl+9v+vNMDDX+iPYragiXtwTEPT8t3L9EI2oI1xAMwnzmYqIRNSZ4EVDmiagM0Uzwb1ydouMD0XqJnuGSxHnqFJ0QNXP2qI1wNcF626tniM4V8zwNjaj924qA2OvEJ0WUGYkeVWCYIRxECx7o0QvmuNdZorE22zru/VRXUuDLiaWXtOOyCo9TIY9kjrlg+mwwwKVarusqJTnyFtNfGRvjZ+S0eFqeRsZYkhEyIOpatrXLn3xfvCbGjVXL7xgF9oVtJUTzGm5OkW8lomn2GmPyEpHcLoyGARyAG8Ffgvc7JpisvA4M7th+La39FX1HkykYvfObvESL4GihPb/J3MC+N10w6x0gakZbazXjkPv/Czs0snFy/g+WuCivKwnXyJTX+4RbF5QBAMRYSNOICZCWAAAAAElFTkSuQmCC);

}
.icon-hero-attr-crit{
    background-image: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADIAAAAsCAMAAAAQPRtoAAAAYFBMVEVMaXGyl3+yl3+yln6sl3mxln6yl362nYbg2dTj3dizl3uyl37SxLnc1M69ppLAq5i5oYvXzMKyln7EsaHLu6x1UICagJ60obLSx8rIusJuR3qPcZVoP3WBX4m/r7uokahqzurhAAAAE3RSTlMAuf9lCdyM////HvX///////8+SFOxZAAAAjVJREFUeAF0wUESABEMRcHvgQRz/+vOVpWkW7dCoihRSVWFWifVmyIDpnnAJgwF1obj9r38wF56/WyVy5KEIAxFF7OQVEmjzfv9/385ETDaBXepdcfh5JDGs38AxDFlO+GzJPDF//iE/QNT8NmJL7+rs0uA44Q5nx3kgsBfO7sSsMi5Mb4h6PnsCvjGAbSxjlh5HwBAKlATAQR8tFcARseUjS3F1qiTxUr7UweCns9+trGU5BMlVw0YJSYCCFi0Y2JccpoqpmbAMMQibtAkF78B82ANVWqMN2g+VCPACtgAzHKsVCnaQIvYQRHoWy4lB6UYLFW8rgSaVBtyNSo9pp9fh+sruUCPlF01kqsD7qlXJXIGMQWvPenMh2oE+GBPpaTMWa0sB5dorC/QXa4OmCoebE0uYoXT8+NsqnW5CPCoYAmM8y5ol9ij2gFdtWHw/lsx4HPJiSpvo8dXlHhX7HWWa57BJz4J3c/S50iQbUoI1xuN7Nz0kcV1NKm0ucQYUgl+vpx06e/TsKjLI0yw9+NjrACa/jB/dqzeY6Hpk2M0fq5fFZvNeLrxxzEyeUjGU7ST/CAVmUz3hUC7VM1TqXmMkb3vC93KDtomn6kSi74B/95KUnO4H551wcMb8LxhxEVAR/cspcJyE/+cNgztMQarKDntMdqWUsIUAvy32skd9BShVjuZVBMwBQGvNj+pdggppfjJtq9/X2jR7JjzN/+DJC7S6kpQAJNRI1Nc7xNuXbAyUAYArLVOm7W44PwAAAAASUVORK5CYII=);
}
.content-yys .attrs .hero-attr .icon{
        vertical-align: top;
        margin: 0 .25rem 0 -.625rem;
        width:35px;
        height:31px;
        display:inline-block;
        background-size:100% 100%;
}
/* 等级星级排序按钮 */
.menu-sort {
    position: absolute;
    display: flex;
    flex-wrap:wrap;
    z-index: 100;
    top:0;
    left:0;
    border-left: 1px solid #e5e5e5;
    line-height: 2rem;
    font:22px/1.7 PingFangSC-Light,Microsoft Yahei,Heiti SC,miui,helvetica;
    width:240px;
    height:339px;
}
.menu-sort li{
    display: list-item;
    min-width:118px;
    min-height:58px;
    background: #fff;
    margin-top: -1px;
    border-top: 1px solid #e5e5e5;
    border-right: 1px solid #e5e5e5;
    border-bottom: 1px solid #e5e5e5;
    text-align: center;
    line-height: 58px;
}
.sanjiao{
    font-size:16px; 
    transition:all 0.5s;
    display: inline-block; 
    
}
.sanjiaotrans{
    transform:rotate(180deg);
}
.swiper-slide{
   border: 2px solid #8E6C46;
}
.popup-content{
  width:748px;
  height:395px;

}
.popup-content .yuhun-detail{
  height: 100%;
}
/* //御魂详情 */
.swiper-slide{
  z-index:500;
  height:397px !important; 
  position:fixed ;
  margin: auto; 
  bottom:0px;
}

.swiper-slide .containter{
    color: #1e1e1e;
    background: #d6c9b9;
    position: relative;
    height: 100%;

}
.swiper-slide .containter .popup-content .yuhun-detail{
      transition: all .2s;
      padding: 14px 21px;
      line-height: 1.3;
}
.swiper-slide .containter .popup-content .yuhun-detail header{
  position:relative;
  display: inline-block;
  width: 528px;
  height:68px;
  padding-left: 84px;
}
.swiper-slide .containter .popup-content .yuhun-detail .yuhun-detail-img{
   position: absolute;
    top:0px;
    left:0px;
    width: 76px;
    height: 76px;
    padding: 11px;

}
.swiper-slide .containter .popup-content .yuhun-detail .yuhun-detail-img img{
   width: 53px;
    height: 53px;
}
.swiper-slide .containter .popup-content .yuhun-detail .yuhun-detail-img .yvhun-detail-img-border{
    position: absolute;
    z-index: 2;
    width: 76px;
    height: 76px;
    top:0;
    left:0;
    color: #fff;
    
}
.swiper-slide .containter .popup-content .yuhun-detail  h2{
  font-size: 24px;
  font-weight: 400;
  vertical-align:top;
  padding-top:14px;
  margin:0;
}

.swiper-slide .containter .popup-content .yuhun-detail .star{
    display: inline-block;
    
}
.swiper-slide .containter .popup-content .yuhun-detail .star .level-icons img{
    width: 11px;
    height:14px;
    margin-top:9px;
    margin-right: 1px;
}
.swiper-slide .containter .popup-content .yuhun-attrs li{
   list-style: none;
   margin:7px 0;
   font-size: 19px;
}
.swiper-slide .containter .popup-content .yuhun-attrs li:nth-child(1){
   color: #d96932;
}
.swiper-slide .containter .popup-content .yuhun-attrs .pull-right{
  float: right;
}
.swiper-slide .containter .popup-content .desc{
  border-top: 1px solid #a68d70;
  padding-top:7px;
}
.swiper-slide .containter .popup-content .desc p{
  margin:7px 0;
  font-size:18px;
}
/* 式神动画 */
.flip-list-move{
    transition:all 0.5s;
}
.gongshi{
    height:21px;
    width: 21px;
    margin-left: 4px;
    vertical-align: middle;

}
/* 底部支付 */
 .bb-d-tabs{
     width:750px;height:67px;
     position:fixed;
     bottom:0px;left:auto;
     background: #fff;
     z-index:1000;
 }
.bb-d-tabs .bb-tab_gm{
     display: inline-block;
     width:50%;
     height:100%;
     text-align: center;
     background: #e74e4b;
     float:right;
 }
.bb-d-tabs .bb-tab_sc{
     display: inline-block;
     width:50%;
     height:100%;
     text-align: center;
 }
.bb-d-tabs .bb-tab_gm span{
    line-height: 67px;
    color:white;
    font-size:20px;
    font-weight: 600;
}
.bb-d-tabs .bb-tab_sc .bb-icon-collect{
    background-image: 
        url("data:image/svg+xml;charset=utf-8,<svg width='48' height='48' viewBox='0 0 48 48' xmlns='http://www.w3.org/2000/svg'><title>icon/nav/%E6%94%B6%E8%97%8F@2x</title><path d='M22.142 35.131a4.5 4.5 0 0 1 3.716 0l6.885 3.122a1.5 1.5 0 0 0 2.11-1.534l-.841-7.512a4.5 4.5 0 0 1 1.148-3.535l5.097-5.583a1.5 1.5 0 0 0-.806-2.48l-7.405-1.522a4.5 4.5 0 0 1-3.007-2.184L25.304 7.33a1.5 1.5 0 0 0-2.608 0l-3.735 6.573a4.5 4.5 0 0 1-3.007 2.184L8.55 17.61a1.5 1.5 0 0 0-.806 2.48l5.097 5.583a4.5 4.5 0 0 1 1.148 3.535l-.841 7.512a1.5 1.5 0 0 0 2.11 1.534l6.885-3.122z' stroke='%23333'  stroke-width='3' fill='none'  fill-rule='evenodd'/></svg>");
        width: 33px;
        height:33px;
        display: block;
        background-size: 100% 100%;
        margin: 0 auto;
}
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
