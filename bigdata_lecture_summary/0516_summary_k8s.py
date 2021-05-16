# 쿠버네티스란? 해석하자면 조타수, 파일럿 다른이름으로 k8s, kube라고도 부른다.
## AWS나 AZURE 같은 관리형 서비스와 유사하다.
## OS에 접속해서 프로그램 하나하나 설치하는 것이아니라, 쿠버네티스를 활용하여 컨테이너를 배포하고 다운받는다.

### 컨테이너란? 무언갈 실행하기 위해 필요한 요소나 환경들을 모두 포함하는 소프트웨어 패키지. 해운업계에서 컨테이너로 물건을 배송하듯, 소프트웨어 개발기술도 컨테이너화한다.
### 애플리케이션의 구성파일, 라이브러리 등 모든것을 번들로 제공하는 것을 컨테이너라고 한다.
### 컨테이너는 os단계에서 나눠주는 거고, vm은 하드웨어단계에서 나눠주는 것이다.

### 컨테이너오케스트레이션(container ochestration) 이란? 
### 서버를 관리한다는 것은 상태를 유지시키는 것. 어떻게 하면 쉽게할까? 문서화를 잘해보자 즉, 메모하자. 하지만 버전이 바뀌면 오류가 날수밖에 없다.
### 한 서버에 다양한 버전의 프로그램을 돌리는 것. 그거 너무 복잡해, 그래서 vm이 생겼다. 조금 느리지만 좋다.
### 클라우드에서는 어렵네 그래서 도커가 생겼어!! 도커와 컨테이너는 개발환경과 배포환경 전부 컨트롤 가능 그래서 문제 생길확률 낮다.
### 특정 클라우드에 종속적이지 않아서 서로 호환도 된다. 이거 이제 좀 쉽네???
### 모든앱을 컨테이너화 한다. 그런데 컨테이너가 막 100개 씩 많아지기 시작한다. 점점 손이 많이 가는데?
### 서버관리자는 많이진 컨테이너를 관리하는데 어려움을 겪는다. 그래서 컨테이너 오케스트레이션이라는 복잡한 컨테이너환경을 효과적으로 관리하기 위한 도구가 만들어진다.
### 이러한 오케스트레이션 도구 중 1개가 쿠버네티스 이다.

### 이제 쿠버네티스가 무엇인지 어느정도는 이해할 수 있다. 컨테이너를 쉽고 빠르게 배포/확장 관리를 자동화해주는 오픈소스 플랫폼이다.
### 쿠버네티스는 구글이 만들었다. 참고로 구글은 당시 1주일에 20억개의 컨테이너를 생성하고 있었다.(2015)
### 아마존 애저 구글 클라우드 전부 쿠버네티스 매니지드 서비스 지원


### 빅데이터에는 쿠버네티스가 어떻게 사용될까?
### kubeflow 라는 머신러닝이 여기서 구동한다.
### 이제 리눅스는 필요없다? 쿠버네티스라는 새로운 os가 있기 때문, 도커도 쿠버네티스를 지원.

### Azure kubernetes service
### AKS라고한다. AKS를 통해 서버구축 가능, 머신러닝을 쿠버네틱스위에서 구동한다.
### 웨이브에선 추천서비스 구동을 위해 머신러닝을 kubeflow에서 돌리고, 바로 추천하는 엣지ai화도 진행중이다.

### 쿠버네티스와 하둡??
### 하둡에코시스템은 각기다른 컴포넌트들이 엮여 있어 관리가 어렵다.
### 그것을 효과적으로 관리할 수 있게 해주는 것이 쿠버네티스다.

## 쿠버네티스는 자동화, 가상머신이 5개가 있으면 그것들이 문제가 생기면 자동으로 문제를 해결.
## 문제에는 전원이 종료된다거나, 갑자기 트래픽이 늘어나서 스케일업해주는 것들을 포함


