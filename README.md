# Readme.md

## 조원 소개



## 프로젝트 개요



## 실행 화면



## 기능 소개



## 클라이언트 실행 방법

```bash
# IDE 터미널에서 실행

npm install

npm run serve
```



## 서버 실행 방법

```bash
# 개인 Djnago 시크릿 키 추가
# IDE 터미널에서 실행

# 가상환경 생성

python -m venv venv

# 가상환경 활성화

source venv/Scripts/activate

# requirements 설치

pip install -r requirements.txt

# make migrations

python manage.py makemigrations

# migrate

python manage.py migrate

# fixture 데이터를 로드

python manage.py loaddata moodtag.json casetag.json genre.json actor.json movie.json

# 서버 실행

python manage.py runserver
```





## 🌵git branch convention

#### frontend/

프론트엔드 관련 기능 (ex: frontend/login)

#### backend/

백엔드 관련 기능 (ex: backend/fixture)

#### README

리드미 수정, 개발일지 작성





## 🖋️git commit message convention

#### 참고

https://blog.ull.im/engineering/2019/03/10/logs-on-git.html



#### Fix

> 올바르지 않은 동작을 고친 경우

#### Add

> 코드나 테스트, 예제, 문서 등의 추가가 있을 때

#### Remove

> 코드의 삭제가 있을 때

#### Refactor

> 전면 수정이 있을 때

#### Simplify

> 복잡한 코드를 단순화 할 때

#### Improve

> 향상이 있을 때(호환성, 테스트 커버리지, 성능, 접근성...)

#### Make

> 기존 동작의 변경을 명시

#### Implement

> 모듈, 클래스 등 구현체를 완성시켰을 때

#### Correct

> 문법의 오류나 타입의 변경, 이름 변경에 사용

#### Ensure

> 무엇인가 확실하게 보장받도록 할 때

#### Prevent

> 특정한 처리를 못하게 막을 때

#### Avoid

> 특정한 상황을 회피할 때

#### Move

> 코드의 이동이 있을 때

#### Rename

> 이름 변경이 있을 때

#### Allow

> 무언가를 허용할 때

#### Verify

> 검증 코드를 넣을 때

#### Set

> 변수 값을 변경하는 등 작은 수정

#### Pass

> 파라미터를 넘기는 처리를 할 때



## 프로젝트 소감