[![English](https://img.shields.io/badge/lang-English-blue.svg)](https://github.com/juho-creator/Crypto_AlgoTrading/blob/master/README.md)
[![한국어](https://img.shields.io/badge/lang-한국어-red.svg)](https://github.com/juho-creator/Crypto_AlgoTrading/blob/master/README.KR.md)



# 加密货币算法交易
- 以下内容是基于 [Part Time Larry 的币安 API 教程系列](https://www.youtube.com/watch?v=rvhnz1yBHgQ&list=PLvzuUVysUFOuB1kJQ3S2G-nB7_nHhD7Ay) 的代码开发的。
- 在收集了 BTC 价格数据之后，您可以基于 RSI 策略进行回测和实盘测试。
- 代码经过组织，具有更多功能以提高易用性。</br></br></br>


### 数据收集
- **get_data.py**：创建价格历史记录的 CSV 文件
- **back_test.py**：对从 get_data.py 收集的价格历史记录进行简单 RSI 策略的回测
- **config.py**：您的币安凭据（API 密钥）
- **wscat**：从币安 websocket 收集价格数据的 wscat 命令
- **fear_and_greed_index.py**：在特定时间段内创建恐惧和贪婪指数的 CSV 文件和图表。</br>
[(点击此处了解如何修改 API 请求的更多信息)](https://github.com/juho-creator/Crypto_AlgoTrading/blob/master/README.modified-api.md)
</br></br>

### 实时图表
 - 使用 Flask 显示比特币的实时价格图表
</br></br></br>

### 技术分析
- **AlgoTrading.py**：用于调整订单（TPSL、杠杆）和检查剩余余额的功能。
- **TechnicalAnalysis.py**：用于检查和测试 SMA 和 RSI 值
- **bot.py**：使用简单 RSI 策略进行实时交易
</br></br></br>

## 必须处理的事项
- [X] [收集恐惧与贪婪指数](https://github.com/juho-creator/Crypto_AlgoTrading/blob/master/DataCollection/fear_and_greed_index.py)
- [ ] 根据恐惧与贪婪指数创建交易策略
- [ ] 回测/实盘测试基于恐惧与贪婪指数的交易策略

随着我对加密货币市场和算法交易的研究越来越深入，似乎存在很多对利润的要求。</br>
目前，我将此项目搁置，转而创建加密货币套利交易算法。</br>
（个人项目 - 尚未分享）


这样做的原因是：
- 算法交易在找到盈利策略之前不会产生任何利润
- 套利交易如果程序能够检测到交易所之间的价格差异并迅速转移加密货币并以更高的价格出售，将提供保证利润。

一旦我能够使用套利交易算法产生保证利润，我将返回此项目以获取额外的利润。
