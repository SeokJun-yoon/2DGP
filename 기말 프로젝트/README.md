## 1.  게임의 소개
### - 제목 : 무한의 계단
* NFLY STUDIO에서 개발한 아케이드 장르의 게임으로 2015년 1월에 출시되었던 게임이다.
* 원작은 모바일 게임이지만, PC로 모작을 만들어보고자 한다.

### - Screenshots
---------------

<div>
<img width="200" src="https://user-images.githubusercontent.com/70671442/94278519-de16f080-ff85-11ea-85d1-04116ba2e0f0.jpg">
<img width="200" src="https://user-images.githubusercontent.com/70671442/94278530-e2430e00-ff85-11ea-8cec-ae84cb6c5be3.jpg">
<img width="200" src="https://user-images.githubusercontent.com/70671442/94278540-e96a1c00-ff85-11ea-8132-9168fc54a566.jpg">
<div>

### # 게임의 목적 및 방법 : 
* 캐릭터와 계단으로 이루어진 화면에서 '오르기' 버튼과 '방향전환' 버튼을 이용하여 최대한 높이 올라가며 높은 점수를 기록하는 것이 목적이다.
* '오르기' 버튼을 누르면 캐릭터가 진행방향으로 한 칸 올라가고, '방향전환' 버튼 누르면 방향으르 바꿔서 한 칸 올라가게 된다.
* 위 두 버튼을 이용하여 계단에 맞게 올라가지 못하면 게임이 종료된다.
* 한 칸씩 지그재그로 되어있을 경우에는 '방향전환' 버튼을 연속으로 누르면 된다.
* 올라간 계단 수 위에 게이지가 존재하고 게이지는 시간이 지날수록 소모된다. 이 게이지가 다 닳게되면 게임이 오버된다.
* 계단을 한 층 한 층 올라갈 때마다, 점점 게이지가 닳는 속도가 빨라지게된다.
* 이는 시간 제한이 없을 경우, 게임의 난이도가 너무 쉬울 수 있기 때문에 난이도 조절을 위한 것이다.
<img width="500" height="400" src="https://user-images.githubusercontent.com/70671442/95722149-83cc9e00-0cae-11eb-90a5-75f32efac9d5.PNG">
<img width="500" height="400" src="https://user-images.githubusercontent.com/70671442/95722157-85966180-0cae-11eb-84a3-f083b5e5c5fd.PNG">

## 2. GameState(Scene)의 수 및 각각의 이름
### 1. MainState
### 2. GameState
### 3. PauseState
### 4. GameOverState
### 5. RankingState
### 6. OptionState  

## 3. 각 GameState 별 다음 항목
### - GameState 한줄 설명
#### 1. MainState : 게임을 실행하면 처음에 출력되는 화면으로 'Start' 버튼 및 'Option' 버튼을 선택할 수 있고 캐릭터가 중앙에 등장하는 메인 화면이다.
#### 2. GameState : 게임이 진행되는 화면으로 중앙에 캐릭터와 캐릭터 주변으로 계단이 생성되며 화면 중앙상단에 게이지바와 '오르기', '방향전환' 버튼이 존재한다.
#### 3. PauseState : 게임 진행 도중, 일시 정지를 위해 사용되는 화면으로 게임으로 돌아가는 버튼, 게임 재시작 버튼, 메인화면으로 돌아가는 버튼이 존재한다.
#### 4. GameOverState : 게임이 종료 되면 스코어와 게임오버 멘트가 등장하는 종료창이다.
#### 5. RankingState : 플레이어들의 순위가 나오는 랭킹창이다.
#### 6. OptionState : 소리 및 기본 설정을 할 수 있는 옵션 설정창이다.  


### - 화면에 표시할 객체들의 목록
*  : Logo, Play Button, Character 및 Stairs
* 게임 플레이 화면 : '오르기' 버튼, '방향 전환' 버튼, 게이지 바, 일시 중지 버튼, 계단, 메인 캐릭터
* 일시 정지 화면 : '홈'버튼, '소리 끄기' 버튼, '재시작' 버튼, '돌아가기' 버튼
* 게임 오버 화면 : 게임 오버 글씨, 최고 점수, 현재 점수, 재시작 버튼, 설정 버튼
* 랭킹창 : 각 플레이어별 점수
* 설정창 : 소리 설정 및 좌우측 버튼 방식 변경 버튼  


### - 처리할 키 / 마우스 이벤트
* '오르기' 버튼 : 키보드 'P'
* '방향전환' 버튼 : 키보드 'Q'
* 이유 : 키보드의 양끝에 위치한 버튼을 사용하기 위함
* 마우스 이벤트 : 
* 메인 화면의 '게임플레이' 버튼, '랭킹' 버튼, '설정' 버튼   


### - 다른 State로 이동한다면, 각 이동에 대한 조건 및 방법
* MainState -> GameState : 메인화면에서 'PLAY' 버튼 마우스 클릭
* MainState -> RankingState : 메인화면에서 'RANKING' 버튼 마우스 클릭
* MainState -> OptionState : 메인화면에서 '설정' 버튼 마우스 클릭
* GameState -> GameOverState : 게임 종료시 팝업 형식으로 등장
* GameState -> PauseState : 화면 우측 끝의 '일시 정지' 버튼 마우스 클릭
* GameOverState -> MainState : '홈' 버튼 마우스 클릭
* GameOverState -> GameState : '재시작' 버튼 마우스 클릭  

### - 개발 범위
<img width="600" height="400" src="https://user-images.githubusercontent.com/70671442/95722162-88915200-0cae-11eb-9567-4361c3048f63.PNG">

### - 개발 일정
<img width="700" height="500" src="https://user-images.githubusercontent.com/70671442/95722170-89c27f00-0cae-11eb-959e-5047abf3dbfe.PNG">

## 4. 필요한 기술
* 계단이 캐릭터 좌우 한칸 중 랜덤으로 맵을 벗어나지 않는 범위내에서 생성되도록 하는 기술
* 캐릭터가 계단을 벗어날 경우 게임이 종료되도록 하는 충돌체크
