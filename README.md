# API-AUT 
- HTTP API Application Under Testing
- 基于Python Flask
- 为了展示如何使用自动化测试框架而创建的待测应用，相当于一个Mock Server

# 接口列表

## 用户查询
###  请求格式
    GET /users/{userID}
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

## 用户删除
###  请求格式
    DELETE /users/{userID}
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

## 用户信息更新
###  请求格式
    POST /users/{userID}
    Content-Type:application/json
    ACCEPT: application/json	
### 请求体
```json
{  
  "name": string
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

## 用户创建
###  请求格式
    POST /users
    Content-Type:application/json
    ACCEPT: application/json	
### 请求体
```json
{  
  "name": string,
  "age": int
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
    "userID": int
}
```
