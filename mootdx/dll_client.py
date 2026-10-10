# coding=utf-8
import pandas as pd

from mootdx.dll_backend import HqDll, ExHqDll


class _Sock(object):
    _closed = False


class HqClient(object):
    def __init__(self, account="YOUR_ACCOUNT", password="YOUR_PASSWORD", **kwargs):
        self.account = account
        self.password = password
        self._hq = None
        self.client = _Sock()

    def connect(self, ip, port, time_out=15, **kwargs):
        self._hq = HqDll()
        cid = self._hq.connect(ip, port, kwargs.get("account", self.account), kwargs.get("password", self.password))
        self.client._closed = cid < 0
        return cid >= 0

    def close(self):
        if self._hq is not None:
            self._hq.disconnect()
            self.client._closed = True

    def disconnect(self):
        self.close()

    def to_df(self, value):
        if isinstance(value, list):
            return pd.DataFrame(value)
        if isinstance(value, dict):
            return pd.DataFrame([value])
        return pd.DataFrame([{"value": value}])

    def get_traffic_stats(self):
        return {}

    def get_security_quotes(self, symbol):
        return self._hq.quotes(symbol)

    def get_security_bars(self, frequency, market, symbol, start, offset):
        return self._hq.bars(frequency, market, symbol, start, offset)

    def get_security_count(self, market):
        return self._hq.security_count(market)

    def get_security_list(self, market, start):
        return self._hq.security_list(market, start)

    def get_index_bars(self, frequency, market, symbol, start, offset):
        return self._hq.bars(frequency, market, symbol, start, offset, index=True)

    def get_history_minute_time_data(self, market, code, date):
        return self._hq.minute(market, code, date)

    def get_transaction_data(self, market, symbol, start, offset):
        return self._hq.ticks(market, symbol, start, offset)

    def get_history_transaction_data(self, market, symbol, start, offset, date):
        return self._hq.ticks(market, symbol, start, offset, date)

    def get_company_info_category(self, market, symbol):
        return self._hq.company(market, symbol)

    def get_company_info_content(self, market, symbol, filename, start, length):
        return self._hq.company_content(market, symbol, filename, start, length)

    def get_xdxr_info(self, market, symbol):
        return self._hq.xdxr(market, symbol)

    def get_finance_info(self, market, code):
        return self._hq.finance(market, code)

    def get_and_parse_block_info(self, blockfile):
        return self._hq.block(blockfile)

    def get_security_quotes10(self, symbol):
        return self._hq.quotes(symbol, level2=True)

    def get_detail_transaction_data(self, market, symbol, start=0, count=100):
        return self._hq.detail(market, symbol, start, count)

    def get_detail_order_data(self, market, symbol, start=0, count=100):
        return self._hq.detail(market, symbol, start, count, orders=True)


class ExClient(object):
    def __init__(self, account="YOUR_ACCOUNT", password="YOUR_PASSWORD", **kwargs):
        self.account = account
        self.password = password
        self._ex = None
        self.client = _Sock()

    def connect(self, ip, port, time_out=15, **kwargs):
        self._ex = ExHqDll()
        cid = self._ex.connect(ip, port, kwargs.get("account", self.account), kwargs.get("password", self.password))
        self.client._closed = cid < 0
        return cid >= 0

    def close(self):
        if self._ex is not None:
            self._ex.disconnect()
            self.client._closed = True

    def to_df(self, value):
        if isinstance(value, list):
            return pd.DataFrame(value)
        if isinstance(value, dict):
            return pd.DataFrame([value])
        return pd.DataFrame([{"value": value}])

    def get_markets(self):
        return self._ex.markets()

    def get_instrument_count(self):
        return self._ex.instrument_count()

    def get_instrument_info(self, start, count=100):
        return self._ex.instrument_info(start, count)

    def get_instrument_quote(self, market, symbol):
        return self._ex.quote(market, symbol)

    def get_minute_time_data(self, market, symbol):
        return self._ex.minute(market, symbol)

    def get_history_minute_time_data(self, market, symbol, date):
        return self._ex.minute(market, symbol, date)

    def get_instrument_bars(self, category, market, code, start=0, count=700):
        return self._ex.bars(category, market, code, start, count)

    def get_transaction_data(self, market, code, start=0, count=1800):
        return self._ex.ticks(market, code, start, count)

    def get_history_transaction_data(self, market, code, date, start=0, count=1800):
        return self._ex.ticks(market, code, start, count, date)
