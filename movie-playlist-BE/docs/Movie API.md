# III. Movie API

<br>



## 🔗`/api/v1/articles/movies/actors/` 

### - 전체 배우 목록 조회

| 메서드 | 상태 코드                           | 필수 데이터 | 인증 여부 |
| ------ | ----------------------------------- | ----------- | --------- |
| GET    | 200 (성공) / 400 Bad Request (실패) |             | True      |

<hr>

> Response Data

```python
[
    {
        "id": 2,
        "name": "Mark Hamill",
        "profile_path": "/9Wws35pCsT0KoZpiV4Gk5nbn9ZD.jpg"
    },
    ...
]
```

<br>

## 🔗`/api/v1/articles/movies/actors/<int:actor_pk>/` 

### - 단일 배우 조회

| 메서드 | 상태 코드                           | 필수 데이터 | 인증 여부 |
| ------ | ----------------------------------- | ----------- | --------- |
| GET    | 200 (성공) / 400 Bad Request (실패) |             | True      |

<hr>

> Response Data

```python
{
    "name": "Tom Hanks",
    "profile_path": "/xndWFsBlClOJFRdhSt4NBwiPq2o.jpg",
    "movies": [
        {
            "title": "포레스트 검프",
            "poster_path": "/xdJxoq0dtkchOkUz5UVKuxn7a2V.jpg"
        },
        {
            "title": "심슨 가족: 더 무비",
            "poster_path": "/ibamiFS4ifL7jtMfi5yDoPERC6p.jpg"
        },
        {
            "title": "그린 마일",
            "poster_path": "/yuSpRhrTIJa5JN8oESrfD2bndp1.jpg"
        }
        ...
}       
```

<br>

## 🔗`/api/v1/articles/movies/genre/<int:genre_pk>/` 

### - 장르별 영화 데이터 가져오기

| 메서드 | 상태 코드                           | 필수 데이터 | 인증 여부 |
| ------ | ----------------------------------- | ----------- | --------- |
| GET    | 200 (성공) / 400 Bad Request (실패) |             | True      |

<hr>

>Response Data

```python
{
    "id": 28,
    "movies": [
        {
            "title": "스타워즈 에피소드 4: 새로운 희망",
            "poster_path": "/7XFfURIFCJxN1mfBg0SAjk5yGzg.jpg",
            "tagline": "아주 오래 전 멀고 먼 은하계에서..."
        },
        {
            "title": "제5원소",
            "poster_path": "/npcHgyp5MmKMe4lWqJi2ma1CuhC.jpg",
            "tagline": "사라진 4개 원소를 되찾고 제 5원소의 비밀을 밝혀라"
        }
        ...
}
```



<br>

## 🔗`/api/v1/articles/movies/moodtag/<int:moodtag_pk>/` 

### - 기분별 영화 데이터 가져오기

| 메서드 | 상태 코드                           | 필수 데이터 | 인증 여부 |
| ------ | ----------------------------------- | ----------- | --------- |
| GET    | 200 (성공) / 400 Bad Request (실패) |             | True      |

<hr>

>Response Data

```python
{
    "id": 7,
    "movies": [
        {
            "title": "비포 선라이즈",
            "poster_path": "/o7mLGNdzY1z6w2bQv0NJNOoVKks.jpg",
            "tagline": "단 하루, 사랑에 빠지기 충분한 시간"
        },
        {
            "title": "노팅 힐",
            "poster_path": "/1AbAtQSgN4KKVODiiX2452dlDJD.jpg",
            "tagline": "\"난 오늘, 오르지 못할 나무를 처다봤다!\""
        },
        ...
}
```



<br>

## 🔗`/api/v1/articles/movies/casetag/<int:casetag_pk>/` 

### - 상황별 영화 데이터 가져오기

| 메서드 | 상태 코드                           | 필수 데이터 | 인증 여부 |
| ------ | ----------------------------------- | ----------- | --------- |
| GET    | 200 (성공) / 400 Bad Request (실패) |             | True      |

<hr>

>Response Data

```python
{
    "id": 7,
    "movies": [
        {
            "title": "죽은 시인의 사회",
            "poster_path": "/41AJ4X5TRWpECsiMIKS8so4MSsD.jpg",
            "tagline": "“오 캡틴, 나의 캡틴”"
        },
        {
            "title": "해리가 샐리를 만났을 때",
            "poster_path": "/m4IfPfmR3LELJgu5aa03CIennTF.jpg",
            "tagline": ""
        },
}
```

<br>

## 🔗`/api/v1/articles/movies/<int:movie_pk>/` 

### - 영화 상세 데이터 가져오기

| 메서드 | 상태 코드                           | 필수 데이터 | 인증 여부 |
| ------ | ----------------------------------- | ----------- | --------- |
| GET    | 200 (성공) / 400 Bad Request (실패) |             | True      |

> Response Data

```python
{
    "id": 100,
    "genres": [
        {
            "name": "코미디"
        },
        {
            "name": "범죄"
        }
    ],
    "actors": [
        {
            "name": "Jason Flemyng"
        },
        {
            "name": "Jason Statham"
        }
    ],
    "ratings": [],
    "title": "록 스탁 앤 투 스모킹 배럴즈",
    "overview": "베이컨(제이슨 스테덤), 소프(덱스터 플렛쳐), 톰(제이슨 플레밍)과 에디(닉 모란) 패거리는 포르노 거물 해리가 여는 포커판에 끼려는 에디에게 가진 돈을 모두 준다. 그러나 이길 줄 알았던 에디가 졌을 뿐만 아니라 해리에게 빚까지 지게 된다. 일주일 안에 돈을 갚지 않으면 손가락이 잘릴 위기에 처한 에디는 대마초 패거리를 털려는 덕의 계획을 알고 덕 일당의 돈을 뺏기로 한다. 덕 일당이 돈과 대마초를 털어오자 집에서 기다린 에디 일당이 돈과 대마초를 빼앗는다. 에디 일당은 해리에게 빚을 갚고 대마초를 팔아 돈을 챙기기만 하면 된다고 기뻐하지만...",
    "budget": 1350000,
    "poster_path": "/pmnmU1BVt58y2HLyvWFYnC3F6ma.jpg",
    "release_date": "1998-08-28",
    "revenue": 28356188,
    "runtime": 105,
    "moodtag": [],
    "casetag": [],
    "like_users": []
}
```

<br>

## 🔗`/api/v1/articles/movies/<int:movie_pk>/like/` 

### - 영화 좋아요 / 좋아요 취소

| 메서드 | 상태 코드                                      | 필수 데이터 | 인증 여부 |
| ------ | ---------------------------------------------- | ----------- | --------- |
| POST   | 204 No Content (성공) / 400 Bad Request (실패) |             | True      |

<hr>

> Response Data

```python
{
    "id": 100,
    "genres": [
        {
            "name": "코미디"
        },
        {
            "name": "범죄"
        }
    ],
    "actors": [
        {
            "name": "Jason Flemyng"
        },
        {
            "name": "Jason Statham"
        }
    ],
    "ratings": [],
    "title": "록 스탁 앤 투 스모킹 배럴즈",
    "overview": "베이컨(제이슨 스테덤), 소프(덱스터 플렛쳐), 톰(제이슨 플레밍)과 에디(닉 모란) 패거리는 포르노 거물 해리가 여는 포커판에 끼려는 에디에게 가진 돈을 모두 준다. 그러나 이길 줄 알았던 에디가 졌을 뿐만 아니라 해리에게 빚까지 지게 된다. 일주일 안에 돈을 갚지 않으면 손가락이 잘릴 위기에 처한 에디는 대마초 패거리를 털려는 덕의 계획을 알고 덕 일당의 돈을 뺏기로 한다. 덕 일당이 돈과 대마초를 털어오자 집에서 기다린 에디 일당이 돈과 대마초를 빼앗는다. 에디 일당은 해리에게 빚을 갚고 대마초를 팔아 돈을 챙기기만 하면 된다고 기뻐하지만...",
    "budget": 1350000,
    "poster_path": "/pmnmU1BVt58y2HLyvWFYnC3F6ma.jpg",
    "release_date": "1998-08-28",
    "revenue": 28356188,
    "runtime": 105,
    "moodtag": [],
    "casetag": [],
    "like_users": [
        4
    ]
}
```

<br>

## 🔗`/api/v1/articles/movies/<int:user_pk>/recommendation/` 

### - 사용자가 좋아요 누른 영화와 유사한 영화 데이터 가져오기

| 메서드 | 상태 코드                                      | 필수 데이터 | 인증 여부 |
| ------ | ---------------------------------------------- | ----------- | --------- |
| GET    | 204 No Content (성공) / 400 Bad Request (실패) |             | True      |

<hr>

> Response Data

```python
[
    {
        "title": "비버리 힐빌리즈",
        "poster_path": "/refYLEQvzkY63i2IHronCPQODex.jpg",
        "pk": 11041
    },
    {
        "title": "The Lost Skeleton of Cadavra",
        "poster_path": "/nGUjqu7DotLx6yfakAeqaj8D1FO.jpg",
        "pk": 18841
    },
	...
]
```

<br>

## 🔗`/api/v1/articles/movies/<int:movie_pk>/similar/` 

### - 특정 영화와 유사한 영화 데이터 가져오기

| 메서드 | 상태 코드                                      | 필수 데이터 | 인증 여부 |
| ------ | ---------------------------------------------- | ----------- | --------- |
| GET    | 204 No Content (성공) / 400 Bad Request (실패) |             | True      |

<hr>

> Response Data

```python
[
    {
        "title": "The R.M.",
        "poster_path": "/OQ3X7k13koP833iZx1PRIPngZ8.jpg",
        "pk": 36825
    },
    {
        "title": "하쉬 타임",
        "poster_path": "/raBWBnGz2X6FQ3iUwPwYQE4FrkY.jpg",
        "pk": 7873
    },
	...
]
```

<br>

## 🔗`/api/v1/articles/movies/<int:movie_pk>/rating/` 

### - 영화 평점 등록

| 메서드 | 상태 코드                                      | 필수 데이터 | 인증 여부 |
| ------ | ---------------------------------------------- | ----------- | --------- |
| POST   | 204 No Content (성공) / 400 Bad Request (실패) | rate        | True      |

<hr>

> Request 예시

```python
{
    "rate" : 7
}
```

> Response Data

```python
[
    {
        "id": 1,
        "user": {
            "pk": 4,
            "username": "admin123456"
        },
        "rate": 7,
        "review": null,
        "movie": 5
    }
]
```

<br>

## 🔗`/api/v1/articles/movies/<int:movie_pk>/rating/<int:rating_pk>`/ 

### - 영화 평점 수정

| 메서드 | 상태 코드                                      | 필수 데이터 | 인증 여부 |
| ------ | ---------------------------------------------- | ----------- | --------- |
| PUT    | 204 No Content (성공) / 400 Bad Request (실패) | rate        | True      |

<hr>

> Request 예시

```python
{
    "rate" : 8
}
```

> Response Data

```python
[
    {
        "id": 1,
        "user": {
            "pk": 4,
            "username": "admin123456"
        },
        "rate": 8,
        "review": null,
        "movie": 5
    }
]
```

<br>

### - 영화 평점 삭제

| 메서드 | 상태 코드                                      | 필수 데이터 | 인증 여부 |
| ------ | ---------------------------------------------- | ----------- | --------- |
| DELETE | 204 No Content (성공) / 400 Bad Request (실패) |             | True      |

<br>

## 🔗`/api/v1/articles/movies/<str:movie_name>/` 

### - 검색한 영화와 유사한 영화 데이터 가져오기

| 메서드 | 상태 코드                                      | 필수 데이터 | 인증 여부 |
| ------ | ---------------------------------------------- | ----------- | --------- |
| DELETE | 204 No Content (성공) / 400 Bad Request (실패) |             | True      |

<hr>

> Response Data

```python
[
    {
        "pk": 506528,
        "title": "해리엇",
        "poster_path": "/bNmuY9vOx1AEh3G8G1IUppFKAgj.jpg",
        "similarity": 0.75
    },
    {
        "pk": 674,
        "title": "해리 포터와 불의 잔",
        "poster_path": "/h6BhNwNXg0IEbs2PoWfCX9QEvgl.jpg",
        "similarity": 0.7340909090909091
    },
    ...
]
```

