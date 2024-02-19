# Modifying API Request
Unfortunately, [Alternative.me](https://alternative.me/crypto/fear-and-greed-index/#api) does not support API requests for specific timeframes. </br>
Instead, we can only retrieve data for a certain number of days until the end date.</br></br>
For example, to retrieve data at timeframe 26th~30th Oct 2023, we need to request 5 data until 30th Oct 2023.

To overcome this limitation, I adopted a new approach:
1. Get start and end date of desired timeframe
   - **1st Oct 2023 ~ 31st Oct 2023**
2. Calculate the number of days within the desired timeframe.
   - **31 days (October 31st, 2023 - October 1st, 2023)**
3. Fetch data from the API request for the calculated number of days until the end date.
     - **Request 31 data until 31st Oct 2023**
</br>
This adjusted API request method allows us to request fear and greed index data for specific timeframes.




    

</br></br>

# Diagram

![image](https://github.com/juho-creator/Crypto_AlgoTrading/assets/72856990/16a15404-f58e-48aa-8846-5a816d33e272)


