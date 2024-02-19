# 변형된 API 요청 
안타깝게도 [Alternative.me](https://alternative.me/crypto/fear-and-greed-index/#api)는 특정 시간대에 대한 API 요청을 지원하지 않습니다. </br>
대신에 종료 날짜까지의 특정 일수만큼의 데이터만을 가져올 수 있습니다. </br></br>
예를 들어 2023년 10월 30일까지 5개 데이터를 요청하면 </br>
2023년 10월 26~30일까지 요청하게 되는거죠. </br> </br>
이러한 제한을 극복하기 위해 새로운 방법을 생각했습니다:
1. 원하는 시간대 내의 날짜 수를 계산한다
   - **2023년 10월 31일 - 2023년 10월 1일 = 31일**
3. 계산된 날짜 수만큼의 데이터를 API 요청으로부터 가져옵니다.
   - **2023년 10월 31일까지 31개의 데이터 요청**
</br>

# 다이어그램
![image](https://github.com/juho-creator/Crypto_AlgoTrading/assets/72856990/2eae6a0e-b671-44fe-9874-ed8c3c3c17cc)
