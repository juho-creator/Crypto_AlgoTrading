# Crypto AlgoTrading

- 이 코드는 [파트 타임 래리의 바이낸스 API 튜토리얼 시리즈](https://www.youtube.com/watch?v=rvhnz1yBHgQ&list=PLvzuUVysUFOuB1kJQ3S2G-nB7_nHhD7Ay)를 기반으로 개발됬습니다.
- BTC 가격 데이터를 수집한 후 RSI 전략에 기반한 백테스트 및 포워드 테스트를 수행할 수 있습니다.
- 코드는 사용 편의성을 위해 더 많은 기능으로 구성되어 있습니다.</br></br></br>

### 데이터 수집
- **get_data.py** : 가격 이력의 CSV 파일 생성
- **back_test.py** : get_data.py에서 수집한 가격 기록을 사용하여 간단한 RSI 전략을 백테스트합니다.
- **config.py** : 바이낸스 자격 증명 (API KEY)
- **wscat** : 바이낸스 웹소켓에서 가격 데이터 수집을 위한 wscat 명령어
</br></br>

### 라이브 차트
 - 비트코인의 실시간 가격 차트를 표시하기 위한 Flask
</br></br></br>

### 기술적 분석
- **AlgoTrading.py** : 주문 조정 기능 (TPSL, 레버리지) 및 잔액 확인을 위한 함수
- **TechnicalAnalysis.py** : SMA 및 RSI 값을 확인하고 테스트하기 위한 파일
- **bot.py** : 간단한 RSI 전략으로 라이브 트레이딩
</br></br></br>

## 진행해야 할 작업
- [X] [공포탐욕 지수 수집](https://github.com/juho-creator/fear_greed/blob/main/dataCreator.py)
- [ ] Fear & Greed 지수를 기반으로 한 트레이딩 전략 생성
- [ ] Fear & Greed 지수 트레이딩 전략의 백테스트 및 포워드 테스트

암호화폐 시장과 알고리즘 트레이딩에 대해 더 공부하면 수익이 매우 불안정적인 것을 알 수 있습니다. </br>
현재 저는 안정적인 이익 창출을 위한 암호화폐 재정거래 알고리즘을 만들고 있습니다 (개인 프로젝트 - 아직 공유되지 않음).
하지만 추가 수익을 위해 이 프로젝트를 다시 진행할 의향이 있습니다.

 재정거래를 먼저 공부하는 이유는 :
- 알고리즘 트레이딩은 안정적인 수익이 발생하지 않습니다. 수익성 있는 전략을 찾을 때까지 기다려야 합니다.
- 재정거래 알고리즘은 거래소 간의 시세 차이를 신속히 감지한 후, 암호화폐를 즉각적으로 매매할 수 있을 경우 보장된 수익을 제공합니다.