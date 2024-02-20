# Modifying API Request
Unfortunately, [Alternative.me](https://alternative.me/crypto/fear-and-greed-index/#api) does not support API requests for specific timeframes. </br>
Instead, we can only retrieve certain number of past data from today.</br></br>
For example, if it's **20th Febuary 2024** today, and we want data on time interval **10th ~ 20th Feburary 2024**, </br>
11 past data from today is requested as follows : 
```
https://api.alternative.me/fng/?limit=11format=json&date_format=kr
```

However this approach has limitations when it comes to requesting data not including today. </br> 
For instance, how would you request data on time interval **1st ~ 31st Oct 2023**?

To overcome this limitation, I came up with a new approach. </br>
For the sake of simplicity, let's assume today is  **20th Feburary of 2024**. </br>
We'd need to process our data as follows :
1. Get start and end date of desired timeframe
   - **1st Oct 2023 ~ 31st Oct 2023**
</br>

2. Calculate difference between today and each start and end date
   - **days_diff_start = today - start_date = 20th Feburary 2024 - October 31st 2023  = 143**
   - **days_diff_end = today - end_date =  20th Feburary 2024 - October 1st 2023 = 112**
</br>

3. Make API request for the calculated number of days until the end date
```
https://api.alternative.me/fng/?limit={days_diff_start}&format=json&date_format=kr
```
- For our example, days_diff_start = 112days hence we'd make the following API call
```
https://api.alternative.me/fng/?limit=112&format=json&date_format=kr
```
- This allows us to fetch all data from today until the start date (**1st Oct 2023 ~ 20th Feburary of 2024)**
</br>


4. Finally, data obtained from step 3 is cleansed by indexing from days_diff_end. </br>
This eliminates uneccessary data, (**31st Oct 2023 ~ 20th Feburary 2024**) </br>
and returns data from desired timeframe! (**1st Oct 2023 ~ 31st Oct 2023**)

By making adjusted API request and cleansing the data, fear and greed index data is obtained over specific timeframes.




    

</br></br>

# Diagram
![KakaoTalk_20240220_212633034](https://github.com/juho-creator/Crypto_AlgoTrading/assets/72856990/b0472066-491a-4fe0-83af-c22a9aa2912b)



