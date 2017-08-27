module.exports.handler = function(event, context, callback) {
    var responseCode = 200;
    console.log("request: " + JSON.stringify(event.toString()));
    //将event转化为JSON对象
    event=JSON.parse(event.toString());
    var isBase64Encoded=false;
    //根据用户输入的statusCode返回，可用于测试不同statusCode的情况
    if (event.queryParameters !== null && event.queryParameters !== undefined) {
        if (event.queryParameters.httpStatus !== undefined && event.queryParameters.httpStatus !== null && event.queryParameters.httpStatus !== "") {
            console.log("Received http status: " + event.queryParameters.httpStatus);
            responseCode = event.queryParameters.httpStatus;
        }
    }
    //如果body是Base64编码的，FC中需要对body内容进行解码
    if(event.body!==null&&event.body!==undefined){
        if(event.isBase64Encoded!==null&&event.isBase64Encoded!==undefined&&event.isBase64Encoded){
            event.body=new Buffer(event.body,'base64').toString();
        }
    }
    //input是API网关给FC的输入内容
    var responseBody = {
        message: "Hello World!",
        input: event
    };
    //对body内容进行Base64编码，可根据需要处理
    var base64EncodeStr=new Buffer(JSON.stringify(responseBody)).toString('base64');
    //FC给API网关返回的格式，须如下所示。isBase64Encoded根据body是否Base64编码情况设置
    var response = {
        isBase64Encoded:true,
        statusCode: responseCode,
        headers: {
        "x-custom-header" : "header value"
        },
        body: base64EncodeStr
    };
    console.log("response: " + JSON.stringify(response));
    callback(null, response);
};
