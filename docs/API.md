# REST API

> 이 문서는 Newsis-Newsletter의 백엔드 API 구현을 소개합니다
> 해당 사이트는 한 주 동안 있었던 개발 관련 뉴스의 요약본을, 자체 생성한 이미지와 함께 뉴스레터로 정리하여 이용자에게 보여줍니다
> 구독을 통해, 주차별 뉴스레터를 이메일로 받아볼 수 있습니다

## 시작하기 전에
- API 요청 시 데이터 형식은 `application/json`으로 통일하였고, 응답에 대해서는 http 상태코드(http status)를 제공하였습니다. 200번대는 성공, 400번대는 오류입니다.
- 해당 API를 사용하는 경우, 이에 대하여 인증 등의 사전 작업이 필요하지 않습니다.
- API들 간의 종속성은 없습니다. 게시글을 가져오는 경우에도, 시스템에 의해 매주 생성되기에 API 간 종속성은 없습니다.


## API 리스트업
| API 종류 | 설명           |
|---------|:-------------:|
| 게시물    | [게시물 목록 조회](#게시물_목록_조회) |
|         | [게시물 세부내용 및 이미지 조회](#게시물_세부내용_및_이미지_조회)  |
|         | [게시물 등록](#게시물_등록)      |
| 이용자    | [이용자 목록 조회](#이용자_목록_조회)  |
|         | [이용자 등록](#이용자_등록)      |



## API들
### 게시물_목록_조회
메인페이지에서 주차별 게시물(뉴스레터) 목록을 확인하는 기능입니다

| 기능 | 세부 기능 | method | Request path | Request element | Response | 접근 범위 |
|:---:|:-------:|:------:|:------------:|:---------------:|:--------|:-------:|
|게시물	|게시물 목록 조회	|GET	|/post		| |"200 OK<br>[<br>&nbsp;&nbsp;&nbsp;&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;""weeks"": ""2025-5-4"",<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;""index"": 0,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;""news"": ""{'title': 'title example1', 'text': 'text example1', 'reference': ['https://refexample1.com]}"",<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;""image"": ""Blank""<br>&nbsp;&nbsp;&nbsp;&nbsp;},<br>&nbsp;&nbsp;&nbsp;&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;""weeks"": ""2025-6-1"",<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;""index"": 0,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;""news"": ""{'title': 'title example2', 'text': 'text example2', 'reference': ['https://refexample2.com]}"",<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;""image"": ""Blank""<br>&nbsp;&nbsp;&nbsp;&nbsp;},<br>]"|	전체|



### 게시물_세부내용_및_이미지_조회
게시물 목록에서 한 게시물을 누르면 세부 정보를 볼 수 있습니다
개발 관련 뉴스 요약본을, 자체 생성한 이미지와 함께 볼 수 있습니다

| 기능 | 세부 기능 | method | Request path | Request element | Response | 접근 범위 |
|:---:|:-------:|:------:|:------------:|:---------------:|:--------|:-------:|
|게시물 |	게시물 세부 조회|	GET	|/post/?weeks=2025-5-4|		|"200 OK<br>[<br>&nbsp;&nbsp;&nbsp;&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        ""weeks"": ""2025-5-4"",<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        ""index"": 0,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        ""news"": ""{'title': 'title example1', 'text': 'text example1', 'reference': ['https://refexample1.com]}"",<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;""image"":""Blank""<br>&nbsp;&nbsp;&nbsp;&nbsp;    },<br>&nbsp;&nbsp;&nbsp;&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;     ""weeks"": ""2025-5-4"",<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        ""index"": 1,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        ""news"": ""{'title': 'title example2', 'text': 'text example2', 'reference': ['https://refexample2.com]}"",<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;""image"": ""Blank""<br>&nbsp;&nbsp;&nbsp;&nbsp;    }<br>]"|	전체|

### 게시물_등록
시스템에서 뉴스를 요약하고 이미지를 생성한 뒤, 사이트에 등록합니다
외부에서는 접근이 불가합니다

| 기능 | 세부 기능 | method | Request path | Request element | Response | 접근 범위 |
|:---:|:-------:|:------:|:------------:|:---------------|:--------|:-------:|
|게시물|게시물 등록|POST|/data|"{<br>&nbsp;&nbsp;&nbsp;&nbsp;""weeks"": ""2025-5-4"",<br>&nbsp;&nbsp;&nbsp;&nbsp;""index"": 0,<br>&nbsp;&nbsp;&nbsp;&nbsp;""news"": ""{'title': 'title example1', 'text': 'text example1', 'reference': ['https://refexample1.com]}"",<br>&nbsp;&nbsp;&nbsp;&nbsp;""image"": ""Blank""<br>}"| |내부만|

### 이용자_목록_조회
시스템에서 주차별 뉴스레터를 구독자에게 보낼 때 참고할 이용자 정보로, 외부에선 접근이 불가합니다
| 기능 | 세부 기능 | method | Request path | Request element | Response | 접근 범위 |
|:---:|:-------:|:------:|:------------:|:---------------:|:--------|:-------:|
|이용자|이용자 목록 조회|GET|/user| |"200 OK<br>[<br>&nbsp;&nbsp;&nbsp;&nbsp;{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;""email"": ""example01.gmail.com"",<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;""name"": ""example01""<Br>&nbsp;&nbsp;&nbsp;&nbsp;},<br>]"|내부만|

### 이용자_등록
구독페이지에서 이름과 이메일을 등록할 수 있습니다. 추후 뉴스레터가 발행될 때마다, 등록한 이메일로 뉴스레터를 받아볼 수 있습니다
| 기능 | 세부 기능 | method | Request path | Request element | Response | 접근 범위 |
|:---:|:-------:|:------:|:------------:|:---------------|:--------|:-------:|
|이용자|이용자 등록|POST|/user|"{<br>&nbsp;&nbsp;&nbsp;&nbsp;""email"": ""example01.gmail.com"",<br>&nbsp;&nbsp;&nbsp;&nbsp;""name"": ""example01""<br>}"| |전체|