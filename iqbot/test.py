from iqoptionapi.stable_api import IQ_Option
import numpy as np
from multiprocessing import Process
import pandas as pd
from stockstats import StockDataFrame

iq = IQ_Option("autisticmaster69@gmail.com", "FAKErayan106")
iq.connect()

asset = "EURUSD-OTC"
size = 120
maxdict = 30
money = 5
expiration_mode = 2

iq.start_candles_stream(asset, size, maxdict)


def get_stockstats_df(asset, size):
    #get real time candles from iqoptions
    candles = iq.get_realtime_candles(asset, size)
    data = []

    #convert the dictionary of dictionaries from the candles into a list
    for i, k in candles.items():
        data.append(k)

        #convert the list into a padas Dataframe
        df = pd.DataFrame(data=data)
        df.drop(labels=["id", "from", "at"], axis=1)
        #convert the pandas dataframe into a stockstats dataframe (still works with pandas)
        stock = StockDataFrame.retype(df)

        return stock


def get_macd_stockstats_df():
    stock = get_stockstats_df(asset, size)
    stock["macd"]
    return stock


def get_macd():
    stock = get_macd_stockstats_df()
    last_row = stock.tail(1)

    macd = last_row.get("macd")
    macd = float(macd)
    macd = np.around(macd, decimals=5)

    return macd


def get_macds():
    stock = get_macd_stockstats_df()
    last_row = stock.tail(1)

    macds = last_row.get("macds")
    macds = float(macds)
    macds = np.around(macds, decimals=5)

    return macds


def buy():
    print("Buy process started")
    macd_first_trigger = False
    macd_second_trigger = False
    macd_third_trigger = False
    ACTION = "call"

    while True:
        macd = get_macd()
        macds = get_macds()

        if not macd_first_trigger:
            if (macd < macds) and (abs(macd - macds) >= 0.0001):
                macd_first_trigger = True

        if not macd_second_trigger:
            if macd_first_trigger and (macd == macds):
                macd_second_trigger = True

        if not macd_third_trigger:
            if macd_second_trigger and (macd > macds) and (abs(macd - macds) >= 0.0001):
                macd_third_trigger = True

        if macd_third_trigger:
            id = iq.buy(money, asset, ACTION, expiration_mode)
            macd_first_trigger = False
            macd_second_trigger = False
            macd_third_trigger = False
            check_win = iq.check_win_v3(id)


def sell():
    print("Sell process started")
    macd_first_trigger = False
    macd_second_trigger = False
    macd_third_trigger = False
    ACTION = "put"

    while True:
        macd = get_macd()
        macds = get_macds()

        if not macd_first_trigger:
            if (macd > macds) and (abs(macd - macds) >= 0.0001):
                macd_first_trigger = True

        if not macd_second_trigger:
            if macd_first_trigger and (macd == macds):
                macd_second_trigger = True

        if not macd_third_trigger:
            if macd_second_trigger and (macd < macds) and (abs(macd - macds) >= 0.0001):
                macd_third_trigger = True

        if macd_third_trigger:
            id = iq.buy(money, asset, ACTION, expiration_mode)
            macd_first_trigger = False
            macd_second_trigger = False
            macd_third_trigger = False
            check_win = iq.check_win_v3(id)


if __name__ == '__main__':
    p1 = Process(target=buy)
    p2 = Process(target=sell)

    p1.start()
    p2.start()
