# :clipboard: README



### :slightly_smiling_face: 팀원

|  이름  |                        역할                         |             정보             |
| :----: | :-------------------------------------------------: | :--------------------------: |
| 박상원 |       User 백엔드, Movie 백엔드, JavaScript,        | 식품산업외식학 한국조리 전공 |
| 이해인 | 프로젝트 기본 틀, CSS, BootStrap,Movie 백엔드, 배포 |     미술대학 한국화 전공     |



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

> - 메세지 기능 구현 중
> - git branch를 잘못 선택하여 약 7시간의 작업물 모두 사라짐.

#### 191125(월)

> - 유저 정보, 영화 정보, 댓글 달기, 댓글 수정 등 대부분의 백엔드 기능 구현
>
> - 댓글 수정 시 form 페이지로 다시 redirect하지 않고 댓글과 수정 form이 서로 번갈아가면서 display block과 display none을 가지며 전환되도록 JS코드 작성. 
>
> - 댓글 수정 form 클릭시 스크롤 최상단 이동 -> display 변경 함수에 return false를 주어 스크롤 이동 방지.
>
> - 메세지 기능 구현을 위해 z-index와 modal을 이용해 주위 화면은 반투명해지며 클릭이 안되게, modal만 z-index를 크게 주어 메세지를 보내는 창을 만들었으나 이미 bootstrap의 modal에서 전부 제공해주는 기능이었음. 
>
>   ```html
>   <a id="sendBtn" class="btn btn-primary mt-3" href="#">메세지 보내기</a>
>   ```
>
>   ```javascript
>   const modal = document.querySelector('#modal')
>       const sendBtn = document.querySelector('#sendBtn')
>       const dimm = document.createElement('div')
>       const closeBtn = document.querySelector('.close')
>       sendBtn.onclick = function(){
>         document.body.appendChild(dimm)
>         dimm.setAttribute('class','dimm');
>         dimm.style.display = 'block'
>         modal.style.display = 'block'
>         modal.style.zIndex = '1'
>       }
>   ```
>
>   편하고 간결하게 modal에서 제공해주는 기능을 쓰기로 함.

​	

#### 191126(화)

> - django와 javascript로만으로 짰던 평점 작성, 수정, 삭제를 Vue.js를 이용한 비동기 형태로 변경하는 과정에서 문법 충돌. 전체 페이지의 url 요청을 전부 수정할수도 있는 대작업이 예상됨.
> - Vue.js와 연동하는 과정에서 일어나는 충돌들을 해결하지 못하고 다시 동기로 전환. 비동기를 완전히 배제하고 짠 백엔드 코드에 프론트엔드를 붙이는건 매우 복잡하기 때문에 처음부터 프론트엔드를 염두에 두고 백엔드 코드를 짜야함.

#### 191127(수)

> - 배포시 일어나는 에러가 어디서부터 어디까지인지 확인불가. 배포는 한번도 해본적 없기 때문에 에러 수정이 매우 어려움.
>
> - 자바스크립트 문법 또한 django template 문법과 충돌 발생 (url namespace의 경우 "" 안에 '' 가 들어가 있는데 자바스크립트는 이를 허용하지 않음. "" 안에 ''가 없는 url 접근으로 해결)
>
>   ```javascript
>   moreInfo.href = `/movies/movie_detail/${movieId}/` ----> ok
>   moreInfo.href = `{% url 'movies:movie_modify' ${movieId} %}` ----> error
>   ```
>
> -  편하다고 그 방법밖에 알지 못하면 여러 상황을 해결하는 능력이 부족해진다. 기본적으로 여러가지 방법을 안 상태에서 가장 편한 방법을 찾아 쓰도록 하자.
> - 백엔드와 Vue.js를 연동해서 썼다면 더 효율적인 코드가 되었을텐데 자바스크립트만으로는 백엔드(db)에 접근하는게 한계가 있어서 비효율적인 코드가 짜여질 수 밖에 없음. 

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





