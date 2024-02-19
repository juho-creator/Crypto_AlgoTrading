# Modifying API Request
Unfortunately, [Alternative.me](https://alternative.me/crypto/fear-and-greed-index/#api) does not support API requests for specific timeframes. </br>
Instead, we can only retrieve data for a certain number of days until the end date.</br>
To overcome this limitation, I adopted a new approach:
1. Calculate the number of days within the desired timeframe.
2. Fetch data from the API request for the calculated number of days until the end date.

</br></br>

# Diagram
![Modified API Request](https://github.com/juho-creator/Crypto_AlgoTrading/assets/72856990/abb0fb56-7b32-4431-b74d-d5f9d8e19c18)
