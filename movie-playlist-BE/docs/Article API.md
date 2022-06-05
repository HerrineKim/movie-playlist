# II. Article API

<br>

## 🔗`/api/v1/articles/` 

### - 게시글 작성

| 메서드 | 상태 코드                           | 필수 데이터    | 인증 여부 |
| ------ | ----------------------------------- | -------------- | --------- |
| POST   | 200 (성공) / 400 Bad Request (실패) | title, content | True      |

<hr>

> Request 예시

```python
{
  title: 'Test Title',
  content: 'Test Content',
}
```

> Response Data

```python
{
    "pk": 1,
    "user": {
        "pk": 4,
        "username": "TestId"
    },
    "title": "Test Title",
    "content": "Test Content",
    "comments": [],
    "created_at": "2022-06-05T22:45:09.233770+09:00",
    "updated_at": "2022-06-05T22:45:09.233770+09:00",
    "like_users": [],
    "like_count": 0,
    "comment_count": 0
}
```

### - 전체 게시글 조회

| 메서드 | 상태 코드                           | 필수 데이터 | 인증 여부 |
| ------ | ----------------------------------- | ----------- | --------- |
| GET    | 200 (성공) / 400 Bad Request (실패) |             | True      |

>Response Data

```PYTHON
[
    {
        "pk": 1,
        "title": "Test Title",
        "user": {
            "pk": 4,
            "username": "TestId"
        },
        "comment_count": 0,
        "like_count": 0,
        "created_at": "2022-06-05T22:45:09.233770+09:00"
    }
]
```

<br>



## 🔗`/api/v1/articles/<int:article_pk>/` 

### - 단일 게시글 조회

| 메서드 | 상태 코드                           | 필수 데이터 | 인증 여부 |
| ------ | ----------------------------------- | ----------- | --------- |
| GET    | 200 (성공) / 400 Bad Request (실패) |             | True      |

<hr>

>Response Data

```PYTHON
{
    "pk": 1,
    "user": {
        "pk": 4,
        "username": "admin123456"
    },
    "title": "Test Title",
    "content": "Test Content",
    "comments": [],
    "created_at": "2022-06-05T22:45:09.233770+09:00",
    "updated_at": "2022-06-05T22:45:09.233770+09:00",
    "like_users": [],
    "like_count": 0,
    "comment_count": 0
}
```

<br>

### - 단일 게시글 수정

| 메서드 | 상태 코드 | 필수 데이터    | 인증 여부 |
| ------ | --------- | -------------- | --------- |
| PUT    |           | title, content | True      |

<hr>

> Response Data

```python
{
    "pk": 1,
    "user": {
        "pk": 4,
        "username": "admin123456"
    },
    "title": "New Title",
    "content": "New Content",
    "comments": [],
    "created_at": "2022-06-05T22:45:09.233770+09:00",
    "updated_at": "2022-06-06T00:43:22.245019+09:00",
    "like_users": [],
    "like_count": 0,
    "comment_count": 0
}
```

<br>

### - 단일 게시글 삭제

| 메서드 | 상태 코드                                      | 필수 데이터 | 인증 여부 |
| ------ | ---------------------------------------------- | ----------- | --------- |
| DELETE | 204 No Content (성공) / 400 Bad Request (실패) |             | True      |

<br>



## 🔗`/api/v1/articles/<int:article_pk>/like/` 

### - 게시글 좋아요/좋아요 취소

| 메서드 | 상태 코드                                      | 필수 데이터 | 인증 여부 |
| ------ | ---------------------------------------------- | ----------- | --------- |
| POST   | 204 No Content (성공) / 400 Bad Request (실패) |             | True      |

<br>

> Response Data

```python
{
    "pk": 2,
    "user": {
        "pk": 4,
        "username": "admin123456"
    },
    "title": "New Title",
    "content": "New Content",
    "comments": [],
    "created_at": "2022-06-06T00:59:38.712131+09:00",
    "updated_at": "2022-06-06T00:59:38.712131+09:00",
    "like_users": [
        {
            "pk": 4,
            "username": "admin123456"
        }
    ],
    "like_count": 1,
    "comment_count": 0
}
```

<br>

## 🔗`/api/v1/articles/<int:article_pk>/comments/` 

### - 댓글 생성

| 메서드 | 상태 코드                           | 필수 데이터 | 인증 여부 |
| ------ | ----------------------------------- | ----------- | --------- |
| POST   | 200 (성공) / 400 Bad Request (실패) |             | True      |

<hr>

> Request 예시

```python
{
  content: 'New comments',
}
```

> Response Data

```python
[
    {
        "pk": 1,
        "user": {
            "pk": 4,
            "username": "admin123456"
        },
        "content": "New comments",
        "article": 2,
        "created_at": "2022-06-06T01:04:29.020653+09:00",
        "updated_at": "2022-06-06T01:04:29.020653+09:00"
    }
]
```

<br>

## 🔗`/api/v1/articles/<int:article_pk>/comments/<int:comment_pk>/` 

### - 댓글 수정

| 메서드 | 상태 코드                           | 필수 데이터 | 인증 여부 |
| ------ | ----------------------------------- | ----------- | --------- |
| PUT    | 200 (성공) / 400 Bad Request (실패) | content     | True      |

<hr>

> Request 예시

```python
{
  content: 'PUT comments',
}
```

> Response Data

```python
[
    {
        "pk": 1,
        "user": {
            "pk": 4,
            "username": "admin123456"
        },
        "content": "PUT comments",
        "article": 2,
        "created_at": "2022-06-06T01:04:29.020653+09:00",
        "updated_at": "2022-06-06T01:04:29.020653+09:00"
    }
]
```

<br>

### - 댓글 삭제

| 메서드 | 상태 코드                           | 필수 데이터 | 인증 여부 |
| ------ | ----------------------------------- | ----------- | --------- |
| DELETE | 200 (성공) / 400 Bad Request (실패) |             | True      |