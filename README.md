# HTTP API Application Under Test
- 为了开发自动化测试框架，常常需要一个靶子，也就是待测应用。
- http-api-aut是一个非常简单的HTTP接口待测应用，实现了用户信息的增删改查，相当于Mock Server。
- 支持POST,GET,PUT,DELETE等基本HTTP请求方法。
- 请求体和响应体为application/json类型。
- 基于Python Flask开发。
- 使用简单，一键启动。

# 运行
- python main.py

# 数据结构
- 用户信息存储在内存中，用列表存储
- 用户基本信息包含：用户ID，用户名，用户年龄，参见user.py

# 接口列表
- 4个接口用于用户管理
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
  "name": "python",
  "age": 24
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
    "userID": 1
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
  "userName": "python",
  "age": 24
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
  "name": "python",
  "age": 24
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


