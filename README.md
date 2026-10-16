# mootdx

通达信行情的另一套 Python 接口。`Quotes.factory(market="std")` 仍读取在线 7709 行情，本地 `Reader` 仍读本机通达信数据文件。

老的 `TdxHqApi` 已经没人维护。要心跳、断线重连和后来补上的函数时，用 `market="hqapi"`，加载 [HqApi.dll](https://github.com/jyApiZx/stockapi)。公开这一版是 L1：实时行情、Tick、买卖五档，以及一分钟、五分钟 K 线。断线由 DLL 自己重连。

行情包：[64 位](https://github.com/jyApiZx/stockapi/releases/download/v1.1.0/HqApi-x64.zip)、[32 位](https://github.com/jyApiZx/stockapi/releases/download/v1.1.0/HqApi-x32.zip)。

## 原来的在线行情

```python
from mootdx.quotes import Quotes

client = Quotes.factory(market="std")
client.bars(symbol="600036", frequency=9, offset=10)
```

## HqApi

```python
from mootdx.quotes import Quotes

client = Quotes.factory(market="hqapi", server=("101.227.73.20", 7709), account="L1*YOUR_ACCOUNT", password="YOUR_PASSWORD")
client.bars(symbol="600036", frequency=9, offset=10)
```

账号写成 `L1*账号`。程序位数要和 `HqApi.dll` 一致。
