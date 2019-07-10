import Vue from 'vue'
import Router from 'vue-router'
import EquipContainer from "./components/equip.vue"
import MwebContainer from "./components/mweb.vue"
import HomeContainer from "./components/Home.vue"
import Register from "./components/register.vue"
import Home from "./components/Home.vue"
import ShopList from "./components/ShopList.vue"
import shoucang from './components/shoucang.vue'
import pf from './components/pf.vue'
import my from './components/my.vue'
import yjfk from './components/yjfk.vue'
import shouji from './components/shouji.vue'
import help from './components/help.vue'
import myshop from './components/myshop.vue'
import mydj from './components/mydj.vue'
import mycollect from './components/mycollect.vue'
import wyzf from './components/wyzf.vue'


Vue.use(Router)

export default new Router({
  routes: [
    {path:'/',redirect:"/Home"},
    {path:'/',component:MwebContainer},
    {path:'/mweb',component:MwebContainer},
    {path:'/equip/:Id',component:EquipContainer},
    {path:'/home',component:Home},
    {path:'/register',component:Register},
    {path:'/ShopList',component:ShopList},
    {path:'/shoucang',component:shoucang},
    {path:'/pf',component:pf},
    {path:'/my',component:my},
    {path:'/yjfk',component:yjfk},
    {path:'/shouji',component:shouji},
    {path:'/help',component:help},
    {path:'/myshop',component:myshop},
    {path:'/mycollect',component:mycollect},
    {path:'/mydj',component:mydj},
    {path:'/wyzf',component:wyzf},

  ]
})
