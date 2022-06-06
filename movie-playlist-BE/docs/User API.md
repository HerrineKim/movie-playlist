# 👤 User API

## 🔗`/api/v1/accounts/signup/` 

### - 회원가입

| 메서드 | 상태 코드                    | 필수 데이터                    | 인증 여부 |
| ------ | ---------------------------- | ------------------------------ | --------- |
| POST   | 201 (성공) / 400 (요청 오류) | username, password1, password2 | False     |


> Request 예시

```python
{
  username: 'TestId',
  password1: 'TestPassword',
  password2: 'TestPassword',
}
```

> Response Data

```python
{
  token: String,
  user: {
    id: Number,
    username: String,
  }
}
```

<br>

## 🔗`/api/v1/accounts/login/` 

### - 로그인

| 메서드 | 상태 코드                                     | 필수 데이터        | 인증 여부 |
| ------ | --------------------------------------------- | ------------------ | --------- |
| POST   | 200 (성공) / 400 (요청 오류), 401 (인증 실패) | username, password | False     |


> Request 예시

```python
{
  username: 'TestId',
  password: 'TestPassword',
}
```

> Response Data

```python
{
  token: String,
  user: {
    id: Number,
    username: String,
  }
}
```

<br>

## 🔗`/api/v1/accounts/logout/` 

### - 로그아웃

| 메서드 | 상태 코드                    | 필수 데이터 | 인증 여부 |
| ------ | ---------------------------- | ----------- | --------- |
| POST   | 200 (성공) / 400 (요청 오류) |             | True      |

<br>



## 🔗`/api/v1/accounts/profile/<username>/` 

### - 프로필 데이터 가져오기

| 메서드 | 상태 코드                    | 필수 데이터 | 인증 여부 |
| ------ | ---------------------------- | ----------- | --------- |
| GET    | 200 (성공) / 404 (찾지 못함) |             | True      |


> Response Data

```python
{
    "articles": [],
    "pk": 4,
    "username": "TestId",
    "like_articles": [],
    "like_movies": []
}
```