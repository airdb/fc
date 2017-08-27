

[以函数计算作为 API 网关后端服务](https://help.aliyun.com/document_detail/54788.html)

head头中带X-Ca-Stage参数, 区分不同的环境。
测试环境： X-Ca-Stage: TEST
预发环境： X-Ca-Stage: RELEASE
生产环境： 直接调用，无需参数

