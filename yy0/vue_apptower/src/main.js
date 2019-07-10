import Vue from 'vue'
import App from './App.vue'
import router from './router'

import'mint-ui/lib/style.css'

Vue.config.productionTip = false
//5: 设置请求的根路径 
//Vue.http.options.root = "http://127.0.0.1/vue_ser/";
//6:全局设置post 时候表音的数据组织格式为 application/x-www-form-urlencoded
//Vue.http.options.emulateJSON = true;
// 导入 MUI 的样式表， 和 Bootstrap 用法没有差别
import './lib/mui/css/mui.css'
// 导入 MUI 的样式表，扩展图标样式，购物车图标
// 还需要加载图标字体文件
import './lib/mui/css/icons-extra.css'

// 1.引入mint-ui组件库
// （1）引入制定组件Header
// （2）注册指定组件（注册一个组件）
// （3）在Home.vue中使用组件
import axios from "axios";
// 修改配置信息 跨域保存session值
axios.defaults.withCredentials=true;
Vue.prototype.axios=axios;
import {Header,Swipe,SwipeItem} from "mint-ui";
Vue.component(Header.name,Header);
Vue.component(Swipe.name,Swipe);
Vue.component(SwipeItem.name,SwipeItem);
// 引入
import Vuex from "vuex";
// 注册vuex
Vue.use(Vuex);
//在main.js中配置Vuex
var store = new Vuex.Store({
  state:{
    cartCount:0,
    shoplist1:[],
  },//属性保存共享全局数据
});
new Vue({
  router,
  render: h => h(App),
  store,
}).$mount('#app')
