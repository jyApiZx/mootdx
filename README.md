# mootdx

# 通达信/同花顺纯协议接口

**产品介绍见 [thsapi.com](https://thsapi.com/)。提供通达信/同花顺纯协议接口，直连券商，无需启动客户端，支持大部分券商。接入请联系 Telegram：`JyApi888`。**

完整函数表和各语言示例见 [stockapi](https://github.com/jyApiZx/stockapi)。

按 mootdx 的 `Quotes` 用法取在线行情。K 线、分时、报价和逐笔改由 `Api.dll` 提供。本地 `Reader` 仍读取本机通达信数据文件。

已有 mootdx 脚本只需换行情地址和授权账号。交易、L2 十档和逐笔也使用同一份 DLL。

## Api.dll

面向 A 股的交易和行情库，支持大部分券商。

| 能力 | 说明 |
| --- | --- |
| 券商交易 | 登录、资金、持仓、当日委托、当日成交、买入、卖出、撤单 |
| 在线行情 | K 线、指数、分时、实时报价、财务、除权除息、板块 |
| L2 | 十档、逐笔成交、逐笔委托 |
| 扩展行情 | `market="ext"`，期货、期权等 |

DLL 与函数说明见 [stockapi](https://github.com/jyApiZx/stockapi)。

进程位数须与 `Api.dll` 一致。

## 在线行情

```python
from mootdx.quotes import Quotes

client = Quotes.factory(
    market="std",
    server=("YOUR_HQ_HOST", 7709),
    account="YOUR_ACCOUNT",
    password="YOUR_PASSWORD",
)

client.bars(symbol="600036", frequency=9, offset=10)
client.quotes(symbol=[(1, "600036")])
client.minute(symbol="000001")
client.transaction(symbol="000001", start=0, offset=100)
```

市场：`0` 深圳，`1` 上海，`2` 北京。L1 常见端口 `7709`，L2 常见端口 `7719`。

十档、逐笔成交、逐笔委托：

```python
client.client.get_security_quotes10([(1, "600036")])
client.client.get_detail_transaction_data(1, "600036", 0, 100)
client.client.get_detail_order_data(1, "600036", 0, 100)
```

扩展行情把 `market` 设为 `"ext"`，端口常用 `7727`。

## 本地文件

`Reader` 不经过 DLL，只读本机通达信目录里的日线和分钟文件。

```python
from mootdx.reader import Reader

reader = Reader.factory(market="std", tdxdir="C:/new_tdx")
reader.daily(symbol="600036")
```

## 说明

调用风格来自 mootdx。在线行情由 `Api.dll` 完成。许可证见 [LICENSE](LICENSE)。
