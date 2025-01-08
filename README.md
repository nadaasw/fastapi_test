# :tiger: Fastapi를 사용해 비동기식 웹사이트 만들기

- 목표: fastapi를 이용해 간단한 게시판 및 로그인 기능이 있는 웹사이트를 만들고자 한다.

## :clipboard: 게시판 CRUD 기능 구현
1. board 스키마
* NewPost
> writer, title, content
* PostLitst
> no, writer, title, date
* Post
> no, writer, tittle, content(optional), date
* ErrorResponse
> error, msg
* UpdatePost
> no, title, content(optional)


2. board_crud.py
* 게시판에서 crud기능을 구현하기 위한 함수들을 구현해놨다.
3. board_router.py
* 라우터를 사용하여 기능별로 구현할 수 있도록 하였다.
## :lock: 로그인 기능 구현
1. user_schema.py
* NewUserForm
> email, name, phone, password
* Token
> access_token, token_type
2. user_crud.py
* 로그인에서 crud기능을 구현하기 위한 함수들을 구현해놨다.

3. user_router.py
* 라우터를 사용하여 기능별로 구현할 수 있도록 하였다.

### :hammer: 개발 환경
1. python : 3.10.6
2. DB     : SQLite3
3. IDE    : VScode
