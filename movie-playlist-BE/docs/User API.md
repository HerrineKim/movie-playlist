# πββοΈ User API

## π`/api/v1/accounts/signup/` 

### - νμκ°μ

| λ©μλ | μν μ½λ                    | νμ λ°μ΄ν°                    | μΈμ¦ μ¬λΆ |
| ------ | ---------------------------- | ------------------------------ | --------- |
| POST   | 201 (μ±κ³΅) / 400 (μμ²­ μ€λ₯) | username, password1, password2 | False     |


> Request μμ

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

## π`/api/v1/accounts/login/` 

### - λ‘κ·ΈμΈ

| λ©μλ | μν μ½λ                                     | νμ λ°μ΄ν°        | μΈμ¦ μ¬λΆ |
| ------ | --------------------------------------------- | ------------------ | --------- |
| POST   | 200 (μ±κ³΅) / 400 (μμ²­ μ€λ₯), 401 (μΈμ¦ μ€ν¨) | username, password | False     |


> Request μμ

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

## π`/api/v1/accounts/logout/` 

### - λ‘κ·Έμμ

| λ©μλ | μν μ½λ                    | νμ λ°μ΄ν° | μΈμ¦ μ¬λΆ |
| ------ | ---------------------------- | ----------- | --------- |
| POST   | 200 (μ±κ³΅) / 400 (μμ²­ μ€λ₯) |             | True      |

<br>



## π`/api/v1/accounts/profile/<username>/` 

### - νλ‘ν λ°μ΄ν° κ°μ Έμ€κΈ°

| λ©μλ | μν μ½λ                    | νμ λ°μ΄ν° | μΈμ¦ μ¬λΆ |
| ------ | ---------------------------- | ----------- | --------- |
| GET    | 200 (μ±κ³΅) / 404 (μ°Ύμ§ λͺ»ν¨) |             | True      |


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