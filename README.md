# API-AUT 
- HTTP API Application Under Testing
- 基于Python Flask
- 为了展示如何使用自动化测试框架而创建的待测应用，相当于一个Mock Server

# 运行
- python manage.py


# 数据结构
- 用户信息存储在内存中，用列表存储
- 用户基本信息包含：用户ID，用户名，用户年龄，参见user.py


# 接口列表
- 一共4个接口
- 用户创建: POST(非幂等操作)
- 用户查询: GET
- 用户更新: PUT(幂等操作，提供更新后的完整信息)
- 用户删除: DELETE

## 用户创建
###  请求格式
    POST /user
    Content-Type:application/json
    ACCEPT: application/json	
### 请求体
```json
{  
  "name": "string",
  "age": "int"
}
```
### 请求参数含义
    name, string, 用户名
    age, int, 用户年龄
    userID, int, 用户唯一标识
### 响应格
    HTTP/1.1 status_code
    Content-Type:application/json
### 响应状态码
    200
### 响应body
```json
{  
    "userID": "int"
}
```

## 用户查询
###  请求格式
    GET /user/{userID}
    ACCEPT: application/json	
### 请求体
    无
### 请求参数含义
    userID, int, 用户唯一标识, 必选
### 响应格
    HTTP/1.1 status_code
    Content-Type:application/json
### 响应状态码
    200
### 响应body
```json
{
  "userName": "tester"
}
``` 



## 用户信息更新
###  请求格式
    PUT /user/{userID}
    Content-Type:application/json
    ACCEPT: application/json	
### 请求体
```json
{  
  "name": "string",
  "age": "int"
}
```
### 请求参数含义
    userID, int, 用户唯一标识, 必选
    name, string, 更新后的用户名
### 响应格
    HTTP/1.1 status_code
    Content-Type:application/json
### 响应状态码
    200
### 响应body
```json
{  
}
```

## 用户删除
###  请求格式
    DELETE /user/{userID}
    ACCEPT: application/json	
### 请求体
    无
### 请求参数含义
    userID, int, 用户唯一标识, 必选
### 响应格
    HTTP/1.1 status_code
    Content-Type:application/json
### 响应状态码
    200
### 响应body
```json
{  
}
```


