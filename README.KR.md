[![English](https://img.shields.io/badge/lang-English-blue.svg)](https://github.com/juho-creator/CryptoCompass/blob/main/README.md)

# Crypto AlgoTrading

- [Part Time Larry의 바이낸스 API 튜토리얼 시리즈](https://www.youtube.com/watch?v=rvhnz1yBHgQ&list=PLvzuUVysUFOuB1kJQ3S2G-nB7_nHhD7Ay)의 코드를 기반으로 개발되었습니다.
- BTC 가격 데이터를 수집한 후 RSI 전략에 기반한 백테스트와 포워드 테스트를 수행할 수 있습니다.
- 코드는 사용 편의성을 위해 더 많은 기능으로 구성되어 있습니다.

### 데이터 수집
- **get_data.py** : 가격 이력의 CSV 파일 생성
- **back_test.py** : get_data.py에서 수집한 가격 이력을 기반으로 간단한 RSI 전략의 백테스트
- **config.py** : 바이낸스 자격 증명 (API 키)
- **wscat** : 바이낸스 웹소켓에서 가격 데이터 수집을 위한 wscat 명령
</br></br>

### 실시간 차트
- 비트코인의 실시간 가격 차트를 표시하기 위한 Flask

</br></br></br>

### 기술적 분석
- **AlgoTrading.py** : 주문 조정 (TPSL, 레버리지) 및 잔액 확인을 위한 기능
- **TechnicalAnalysis.py** : SMA 및 RSI 값을 확인하고 테스트하는 기능
- **bot.py** : 간단한 RSI 전략으로 실시간 거래

</br></br></br>

## 필수 작업
- [X] [공포 및 욕망 지수 수집](https://github.com/juho-creator/fear_greed/blob/main/dataCreator.py)
- [ ] 공포 및 욕망 지수에 기반한 거래 전략 생성
- [ ] 공포 및 욕망 지수 거래 전략의 백테스트 및 포워드 테스트

암호화폐 시장 및 알고트레이딩에 대해 더 공부하면 보장된 수익에 대한 많은 요구 사항이 있음을 알 수 있습니다.
현재 이 프로젝트는 유예되어 있으며, 대신 암호화폐 아비트리지 거래 알고리즘을 만들고 있습니다 (개인 프로젝트 - 아직 공유되지 않음).
