# :clipboard: README



### :slightly_smiling_face: 팀원

|  이름  |                     역할                      |             정보             |
| :----: | :-------------------------------------------: | :--------------------------: |
| 박상원 |            User 백엔드, JS, Vue.js            | 식품산업외식학 한국조리 전공 |
| 이해인 | 프로젝트 기본 틀, CSS, BootStrap,Movie 백엔드 |     미술대학 한국화 전공     |



****



*\# 목표서비스 구현 및 실제 구현 정도 (가능하다면 일자별 업무 진행 정도 포함)*

### :chart_with_upwards_trend: 진행 상황

#### 191122(금)

> - project 시작 : 환경변수와 라이브러리 설치, 프로젝트 시작 전 기본 틀 작성
>   **=>** *Django - settings, models, forms, urls, templates ...ect*
> - 소셜로그인 추가, 구글로 로그인 시도 시, `profile/` 이라는 알 수 없는 경로로 들어가게된다. **=>** settings.py 에 `LOGIN_REDIRECT_URL` 추가

#### 191123(토)

> - Model 수정
>   - User Model, Movie Model이 가지고 있어야 할 FIeid 재정의
> - 새로운 Model 정의
>   - 쪽지를 위한 Message Model 정의
>   - BLANK=True와 null=True를 헷갈릴 수 있다.
> - Movie DB API에서 필요한 정보를 추출해 영화 DB구축

#### 191124(일)

> - 메세지 기능 구현
> - 

#### 191125(월)

> - 유저 정보, 영화 정보, 댓글 달기, 댓글 수정 등 대부분의 백엔드 기능 구현
> - 댓글 수정 시 form 페이지로 다시 redirect하지 않고 댓글과 수정 form이 서로 번갈아가면서 display block과 display none을 가지며 전환되도록 JS코드 작성. 

#### 191126(화)

> - django와 javascript로만으로 짰던 평점 작성, 수정, 삭제를 Vue.js를 이용한 비동기 형태로 변경하는 과정에서 문법 충돌. 전체 페이지의 url 요청을 전부 수정할수도 있는 대작업이 예상됨.
> - Vue.js와 연동하는 과정에서 일어나는 충돌들을 해결하지 못하고 다시 동기로 전환. 비동기를 완전히 배제하고 짠 백엔드 코드에 프론트엔드를 붙이는건 매우 복잡하기 때문에 처음부터 프론트엔드를 염두에 두고 백엔드 코드를 짜야함.





****



###  :pushpin: ERD

- 데이터베이스 모델링 ([entity-relationship diagram)](http://www.terms.co.kr/ERD.htm))

- [ERD Design Site](https://www.erdcloud.com/)



****



### :pushpin: 핵심 기능

1. 



****



### :pushpin: 배포 서버

> - 
>
> #### [URL]()



****



### :pencil: 후기

| 박상원 |
| ------ |
|        |

| 이해인 |
| ------ |
|        |





