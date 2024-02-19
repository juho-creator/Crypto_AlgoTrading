# 변형된 API 요청 
안타깝게도 Alternative.me은 특정 시간대에 대한 API 요청을 지원하지 않습니다. </br>
대신에 종료 날짜까지의 특정 일수만큼의 데이터만을 가져올 수 있습니다. </br>
이러한 제한을 극복하기 위해 새로운 방법을 채택했습니다:
1. 원하는 시간대 내의 날짜 수를 계산합니다. 
2. 계산된 날짜 수만큼의 데이터를 API 요청으로부터 가져옵니다.
</br>

# 다이어그램
![수정된 API 요청](https://github.com/juho-creator/Crypto_AlgoTrading/assets/72856990/abb0fb56-7b32-4431-b74d-d5f9d8e19c18)
