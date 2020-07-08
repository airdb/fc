Function Compute

[以函数计算作为 API 网关后端服务](https://fc.console.aliyun.com/fc/service)
[迁移 Gin 到函数计算](https://help.aliyun.com/document_detail/159157.html?spm=a2c4g.11186623.6.751.7c145578cRq5OC)

head头中带X-Ca-Stage参数, 区分不同的环境。
测试环境： X-Ca-Stage: TEST
预发环境： X-Ca-Stage: RELEASE
生产环境： 直接调用，无需参数


```bash
go build                   
fun deploy -y
```
