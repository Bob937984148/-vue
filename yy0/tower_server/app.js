//vue_app_server 服务器
const express = require("express");
//导入querystring模块（解析post请求）
const querystring = require("querystring");
var app = express();
app.use(express.static("public"));
app.listen(3000);
const pool = require("./pool");

// request = require('request-json');
//引入body-parser中间件
const bodyParser=require('body-parser');
app.use(bodyParser.urlencoded({
	extended:false//不适用扩展而是使用node.js提供的querystring
}));
app.use(bodyParser.json());
//使用路由器来管理文件，路由里面可以使用了body-parser

//express mysql 参数 request;response
//跨域访问配置
//1:加载模块cors
const cors = require("cors");
//2:配置cors
app.use(cors({
  origin:["http://127.0.0.1:3001",
         "http://localhost:3001"],//允许列表
  credentials:true   //是否验证
}));
//3:加载第三方模块: express-session
const session = require("express-session");
//4:对模块配置
app.use(session({
  secret:"128位随机字符串",   //安全令牌
  resave:false,              //请求保存
  saveUninitialized:true,    //初始化
  cookie:{                   //sessionid保存时
    maxAge:1000*60*60*24     //间1天 cookie
  }
}));
//功能十一:用户登录
app.get("/login",(req,res)=>{
  //1:获取登录参数
  var name = req.query.name;
  var pwd = req.query.pwd;
  //2:正则
  //3:创建sql
  var sql =" SELECT count(id) as c,id";
     sql +=" FROM xz_login";
     sql +=" WHERE name = ? AND pwd = md5(?)";
  //4:如果参数匹配成功将用户id保存session对象
  pool.query(sql,[name,pwd],(err,result)=>{
       if(err)throw err;
       var c = result[0].c;
       if(c == 1){
         req.session.uid = result[0].id
         res.send({code:1,msg:"登录成功"});
       }else{
         res.send({code:-1,msg:"用户名或密码有误"})
       }
  });
  //5:返回结果
  //  {code:1,msg:"登录成功"}
  //  {code:-1,msg:"用户名或密码错误"}
});

//御魂查询
app.get("/yv",(req,res)=>{
  var user_id = req.query.userId;
  var yh_site = req.query.yh_site;
  
  var sql = "SELECT * FROM user_yh WHERE user_id=? AND yh_site=? ";
  pool.query(sql,[user_id,yh_site],(err,result)=>{
  if(err) throw err;
  res.send(result);
  })
});

app.get("/yvattr",(req,res)=>{
  var user_id = req.query.userId;
  var yh_site = req.query.yh_site;
  var attr = req.query.attr;
  var sql = `SELECT * FROM user_yh WHERE user_id=${user_id} AND yh_site=${yh_site} ORDER BY ${attr} DESC`;
 
  pool.query(sql,(err,result)=>{
    if(err) throw err;
    res.send(result);
    
  })
})
app.get("/sh",(req,res)=>{
    var user_id = req.query.userId;
    var ss = req.query.ss;
    var sql = `SELECT * FROM user_ss WHERE user_id=${user_id} ORDER BY ${ss} DESC`;
    pool.query(sql,(err,result)=>{
      if(err) throw err;
      res.send(result);
    })
})
app.get("/User",(req,res)=>{
  var id = req.query.userId;
  var sql = `SELECT * FROM user WHERE id=${id}`;
  pool.query(sql,(err,result)=>{
    if(err) throw err;
    res.send(result);
  })
})
app.post("/register",(req,res)=>{
  var obj = req.body;
  var email = obj.email;
  var pwd = obj.upwd;
  var phone = obj.phone;
  
   //1.1:验证
   var sql = "INSERT INTO log_user VALUES(";
      sql +="null,?,?,?)";
      console.log(email);
      console.log(pwd);
   pool.query(sql,[email,pwd,phone],(err,result)=>{
          if(err)throw err;
          if(result.affectedRows>0){
            res.send({code:1,msg:"注册成功"})
          }else{
            res.send({code:-1,msg:"注册失败"});
          }
   })
})
app.get("/home",(req,res)=>{
  var id=req.query.id;
  // console.log(id);
  var sql="SELECT * FROM user INNER JOIN user_ss ON user.id =? and user_ss.user_id=? limit 5";
  pool.query(sql,[id,id],(err,result)=>{
    if(err) throw err;
    res.send(result)
  })
})
app.get('/getpf',(req,res)=>{
  var sql=`select * from pf`
  pool.query(sql,(err,result)=>{
      if(err) throw err;
      res.send(result);
  })
})
app.get('/getyyspf',(req,res)=>{
  var sql=`select * from yyspf`;
  pool.query(sql,(err,result)=>{
      if(err) throw err;
      res.send(result);
  })
})
app.get('/txk',(req,res)=>{
  var sql=`select * from txk`;
  pool.query(sql,(err,result)=>{
      if(err) throw err;
      res.send(result);
  })
})
app.get('/gethz',(req,res)=>{
  var sql=`select * from hz`;
  pool.query(sql,(err,result)=>{
      if(err) throw err;
      res.send(result);
  })
})
app.get('/getImages',(req,res)=>{
  res.send('成功');
})

app.get('/getuser',(req,res)=>{
  var uid=1;
  var reg=/^[0-9]{1,2}$/;
  if(reg.test(uid)){
    sql='select id,nickname,phone,uimg from us where id=?';
    pool.query(sql,[uid],(err,result)=>{
      if(err) throw err;
      res.send(result);
    })
  }else{
    res.send([{id:'-1'}]);
  }
})
