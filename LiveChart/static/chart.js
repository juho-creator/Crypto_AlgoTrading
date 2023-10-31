var chart = LightweightCharts.createChart(document.getElementById('charts'), {
	width: 600,
  height: 300,
	layout: {
		background: {
            type: 'solid',
            color: '#000000',
        },
		textColor: 'rgba(255, 255, 255, 0.9)',
	},
	grid: {
		vertLines: {
			color: 'rgba(197, 203, 206, 0.5)',
		},
		horzLines: {
			color: 'rgba(197, 203, 206, 0.5)',
		},
	},
	crosshair: {
		mode: LightweightCharts.CrosshairMode.Normal,
	},
	rightPriceScale: {
		borderColor: 'rgba(197, 203, 206, 0.8)',
	},
	timeScale: {
		borderColor: 'rgba(197, 203, 206, 0.8)',
	},
});

var candleSeries = chart.addCandlestickSeries({
  upColor: '#00ff00',
  downColor: '#ff0000',
  borderDownColor: 'rgba(255, 144, 0, 1)',
  borderUpColor: 'rgba(255, 144, 0, 1)',
  wickDownColor: 'rgba(255, 144, 0, 1)',
  wickUpColor: 'rgba(255, 144, 0, 1)',
});


// Create chart based off historical data
fetch('http://127.0.0.1:4000/history')
	.then((r) => r.json())
	.then((response)=>{
		candleSeries.setData(response)
	})


var binanceSocket = new WebSocket("wss://stream.binance.com:9443/ws/btcusdt@kline_5m")

binanceSocket.onmessage = function (event){
	var message = JSON.parse(event.data);
	var candlestick = message.k;
	
	console.log(candlestick)

// Update chart based off live data
	candleSeries.update({
		time: candlestick.t / 1000,
		open: candlestick.o,
		high: candlestick.h,
		low: candlestick.l,
		close: candlestick.c
	})
}