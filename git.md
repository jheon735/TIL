# 소프트웨어 개발

1. 소프트웨어 개발 방법
    - Water-Fall 모델
        - 요구사항 분석 후 디자인, 개발, 검증, 유지보수 한 단계
        - CD 형태로 완성된 SW가 배포될 때 사용하던 방법
        - 개발 시간이 길어지면 요구사항이 변경되는데 대처가 불가능
    - 애자일(Agile) 개발
        - 1-3주 보통은 2주 이내의 짧은 사이클로 개발
        - 하나의 사이클을 스프린트라고 함
            - Backlog를 보고 일할 작업 결정(Planning)
            - 매일 Standup 미팅(5-10분)
                - 마지막 스탠드업 이후로 한 작업들
                - 오늘 하려고 하는 일이나 진행중인 일
                - 문제가 있거나 도움이 필요한 일 공유
            - 마지막날 Retrospective & Demo 미팅
        - Product Backlog를 작업별로 우선순위 결정
            - PM/PO(Product Manager, Product Owner)가 수행
            - 이를 Grooming이라고 함
            - 각 작업별 중요도와 복잡도를 Point로 결정
    - 스프린트 개발을 위한 툴
        - To do, In progress, In Review, Done 상태를 보여주는 툴
        - JIRA
            - 굉장히 많은 기능
            - 기업에서 사용
        - Trello
            - 단순하다
            - 무료
            - JIRA가 사서 JIRA의 서비스
            - 팀 프로젝트 기간에 사용
        - Github Porjects Board
        - 카드 예제
            - 타이틀
            - 세부설명
            - 포인트
                - 1 포인트면 하루 걸린다 이런 방식으로 약속하는 점수
                - 개인별 의견이 다르기 때문에 토론을 거쳐 수렴할때까지 진행
                - 점수가 너무 크면 업무를 쪼개야 한다
            - 성공의 정의 : 작업의 완료 기준을 명확히 설명해주어야 한다
            - 체크리스트 : 성공적으로 끝나는데 필요한 세부 작업들
            - 티켓 의존도 : 이 작업이 끝나면 가능한 다른 작업들
        
2. 소스 코드 버전 컨트롤
    - 소프트웨어 소스코드에 발생하는 변경사항들을 관리
    - 코드 공유와 변경이 용이
    - 코드리뷰도 지원
    - 코드 백업의 역할 수행
    - 소프트웨어 종류
        - CVS (Concurrent Version System)
        - SVN (SubVersionN)
        - Git/Github

3. 소프트웨어 테스트
    - TDD(Test Driven Development)
        - 테스트 코드부터 작성
    - Unit Test : 모듈의 특정 기능 테스트
    - Integration Test : 모듈을 통합하여 한 차원 위의 테스트
    - Acceptance Test : 트래픽이 몰릴 때 견딜 수 있는지 테스트
    - UI Test : Selenium등의 툴을 이용해 웹페이지 자체의 기능을 테스트하는 것이 대세

4. 빌드
    - 개발한 소프트웨어를 최종적으로 출시하기 위한 형태로 만드는 것
    - 테스트가 빌드의 중요한 일부로 포함
    - 코드가 변경될 때 마다 빌드를 하면 소프트웨어의 안정성 증대
        - CI : Continuous Integration 
    - CI
        - 소프트웨어 엔지니어링 Practice의 하나
        - 기본 원칙
            - 코드 Repository는 하나만 유지(Master or Main)
            - 코드 변경을 최대한 자주 반영
            - 테스트를 최대한 추가
            - 빌드를 계속적으로 수행 (자동화)
                - Commint Build vs 
    - CD (Continuous Delivery or Deployment) : 배포
    - DevOps
        - 개발자가 만든 코드를 시스템에 반영하는 프로세스 (CI/CD)
        - 시스템이 제대로 동작하는지 감시
    - MLOps
        - 머신러닝 모델을 관리하는 사람들
    - Jenkins
        - 오픈소스 CI 빌드 소프트웨어
        - CI와 관련한 모든 기능을 지원
    - 최근엔 Github에서 CI 기능을 부여해 Jenkins를 하지 않고 Github Actions 사용

5. GIT
    - 분산환경을 지원하는 소스 버전 컨트롤 시스템
    - SVN/CVS에 비해 현저하게 빠르나 사용법은 훨씬 복잡
    - 서버/클라이언트 모델
    - 장점
        - 다수의 개발자가 공동 개발
        - 코드 리뷰 가능
        - 코드 백업
        - 과거의 코드로 롤백 가능
        - 코드 충돌이 생기면 해결 가능
        - 모든 코드변경이 기록된다
        - 코드의 스냅샨을 잡아(버전) 나중에 필요시 버전간 이동 가능
        - 모든 테스트 파일에 사용 가능
    - 단점 : 어려움
    - 기본 기능
        - clone
        - init
        - add
        - commit
        - push
        - merge
        - branch
        - checkout
    - 고급 기능 : 시니어 단위에서 사용
        - rebase
        - cherry-pick
        - reset
        - revert
    - Mainline과 Branch
        - Mainline : github 이전엔 master라 불렀고 지금은 main이라 부르는 source of truth가 되는 원본. 특별한 branch
        - Branch : 특정한 기능을 구현하기 위해 만들어진 mainline의 복사본. 구현과 테스트가 이뤄진 후에 main branch와 머지됨
    - 용어
        - Repo : Repository의 준말로 Git으로 관리되는 소프트웨어 프로젝트를 지정
        - Push : 자기가 작업 중인 로컬 복사본(Local Repo)에서 서버(Remote Repo)로 변경사항들을 복사
        - Pull : Main과 같은 Remote Repository로부터 마지막 Pull이후 변경된 것을 다시 가져오는 작업. Main과 씽크
        - Merger : Pull이나 Push했을 경우 두 Branch간의 충돌을 해결하는 과정. 대부분 자동으로 되지만 몇몇 경우 손으로 직접 충돌 해결해야함
    - Git 작업 과정
        1. Main에서 remote branch를 하나 만든다 : `git checkout -b "브랜치 이름"`, `git branch "브랜치 이름"`
        2. Branch 공간으로 이동한다 : `git checkout "브랜치 이름`
        3. Local branch로 pull해온다
        4. Local에서 작업을 한다
        5. Commit으로 Local branch에 작업 내용을 반영한다 : `git commit -m "메세지" 파일이름1, 파일이름2, ...`
        6. Remote branch로 Push한다 : `git push -u origin 브랜치이름`
        7. Main에 merge를 위한 리뷰 요청(PR : Pull Request) : `git request-pull`

    - Github
        - Git repo 호스팅/클라우드 서비스
        - 웹 기반 인터페이스도 제공
        - 문서화를 위한 Wikis와 버그리포트와 트랙킹을 위한 Issues 기능 제공
        - 자신이 만든 repo들이 모두 public일 경우 사용이 무료
            - private repo 수에 따라 가격대 결정
        - Github Copilot 지원

    - 실습1 : Local에서 만든 후 github 리포 생성
        - `git init`으로 빈 repo 생성
        - `git add 파일이름`으로 추가
        - `git commit -m "메세지" 파일이름`으로 커밋 
        - 로컬에서 이미 만든 파일을 연결하기 위해서는 빈 리포를 만들어야 한다. Readme file 등 기타 파일 생성 안됨
        - `git remote add origin 생성한원격github주소`로 git으로 만든 리포와 연결
        - github의 메인은 main이지만 local의 main은 초기에 master로 설정되기 때문에 `git branch -M main`으로 이름을 맞춘다
        - `git branch`로 브랜치 이름 확인
        - `git push -u origin main`으로 push
    - 실습2 : github에서 다운로드
        - `git clone 깃링크`로 가져온다
    - 실습3 : 브랜치 생성 및 작업
        - `git branch 브랜치이름`으로 브랜치 만들기
        - `git checkout 브랜치이름`으로 브랜치 이동
        - 파일 수정
        - `git commit -m "메세지" 파일이름`으로 커밋 
        - `git push -u origin 브랜치이름`으로 푸쉬
        - github사이트에서 compare & pull request 클릭
        - 내용을 작성한 후 오른쪽에 Reviewers를 지정하여 리뷰어 요청
        - Pull request 탭에 Files changed로 파일 변경 내용 보고 Review change를 눌러 반영