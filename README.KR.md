[![English](https://img.shields.io/badge/lang-English-blue.svg)](https://github.com/juho-creator/Crypto_AlgoTrading/blob/master/README.md)

# 암호화폐 자동매매 알고리즘

- 이 코드는 [파트 타임 래리의 바이낸스 API 튜토리얼 시리즈](https://www.youtube.com/watch?v=rvhnz1yBHgQ&list=PLvzuUVysUFOuB1kJQ3S2G-nB7_nHhD7Ay)를 기반으로 개발됬습니다.
- BTC 가격 데이터를 수집한 후 RSI 전략에 기반한 백테스트 및 포워드 테스트를 수행할 수 있습니다.
- 코드는 사용 편의성을 위해 더 많은 기능으로 구성되어 있습니다.</br></br></br>

### 데이터 수집
- **get_data.py** : 비트코인 가격 데이터 CSV 파일 생성
- **back_test.py** : get_data.py에서 수집한 가격 데이터(CSV파일)를 사용하여 간단한 RSI 전략을 백테스팅
- **config.py** : 바이낸스 API키 
- **wscat** : 바이낸스/업비트 웹소켓에서 실시갼 가격 데이터 수집을 위한 wscat 명령어
- **fear_and_greed_index**: 특정 기간 동안의 공포 탐욕 지수에 대한 CSV 파일과 그래프를 생성합니다. </br>
[(API 요청이 어떻게 변형됬는지 자세히 읽으려면 여기를 클릭하세요)](https://github.com/juho-creator/Crypto_AlgoTrading/blob/master/README.modified-api.KR.md)

</br></br>

### 실시간 차트
 - 비트코인의 실시간 가격 차트를 표시하기 위한 Flask
</br></br></br>

### 기술적 분석
- **AlgoTrading.py** : 주문 조정 기능 (TPSL, 레버리지) 및 잔액 확인을 위한 함수
- **TechnicalAnalysis.py** : SMA 및 RSI 값을 확인하고 테스트하기 위한 파일
- **bot.py** : 간단한 RSI 전략으로 실시간 트레이딩
</br></br></br>

## 현재 진행 상황
- [X] [공포탐욕 지수 수집](https://github.com/juho-creator/fear_greed/blob/main/dataCreator.py)
- [ ] Fear & Greed 지수를 기반으로 한 트레이딩 전략 생성
- [ ] Fear & Greed 지수 트레이딩 전략의 백테스트 및 포워드 테스트

암호화폐 시장 및 알고리즘 트레이딩에 대한 공부를 통해 수익이 매우 불안정적임을 알 수 있습니다. </br>
현재로서는 안정적인 수익을 창출하기 위해 암호화폐 재정거래 알고리즘을 개발하고 있습니다. **(개인 프로젝트 - 아직 공유되지 않음)** </br>
하지만 추가 수익을 위해 이 프로젝트를 다시 진행할 의향이 있습니다. </br>

 재정거래를 먼저 공부하는 이유는 :
- 트레이딩 알고리즘은 수익성 있는 전략을 찾을 때까지 안정적인 수익이 발생하지 않습니다.
- 재정거래 알고리즘은 거래소 간의 시세 차이를 신속히 감지한 후, 암호화폐를 즉각적으로 매매할 수 있을 경우 수익이 보장됩니다.</br>
따라서 실행속도만 빠르면 비교적 간단한 얄고리즘으로 안정적인 수익을 추구할 수 있습니다.
