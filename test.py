# -*- encoding: utf-8 -*-

import base64
import json
import requests
import pandas as pd
from bs4 import BeautifulSoup
import time
from common.const import CConst



str_base64 = "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"
bstr = base64.b64decode(str_base64)
bstr.decode('utf-8')
str(bstr, 'utf-8')
cstr = bstr[:19]
print(str(cstr, 'utf-8'))
print(bstr)

session = requests.session()
s = session.get("https://explorer.binance.org/api/v1/txs?page=10&rows=100&address=bnb1amwztd76ykx4hhgh52r6lfueks0t32lw5ydgqh")
mapPage = json.loads(s.text)

mapPage['txNums']
len(mapPage['txArray'])
mapPage['txArray'][-1]


def get_txs_content(address, save_name='binance_trans.xlsx', save=True, size_per_page=50):
    str_url = "https://explorer.binance.org/api/v1/txs?page=%d&rows=%d&address=" + address
    lsTxArray = 1
    page = 1
    session = requests.session()
    lsAllData = []
    total = 0
    while lsTxArray:
        this_url = str_url % (page, size_per_page)
        time.sleep(1)
        s = session.get(this_url)
        mapPage = json.loads(s.text)
        lsTxArray = mapPage['txArray']
        this_length = len(lsTxArray)
        if this_length == 0:
            print("No more data, total: %d" % (total))
            break
        total += this_length
        lsAllData += lsTxArray
        print('Page: %d,\tpage size: %d,\ttotal: %d' % (page, len(lsTxArray), total))
        page += 1
    dfAllData = pd.DataFrame(lsAllData)
    if save:
        dfAllData.to_excel(CConst.M_RESULT_PATH + save_name, sheet_name='sheet1')
    return dfAllData


def get_block_data(block):
    str_url = "https://explorer.binance.org/block/" + block
    session = requests.session()
    s = session.get(str_url)
    bsObj = BeautifulSoup(s.text, 'lxml')
    reward_table = bsObj.find('table')
    # reward = bsObj.find("div", {"class": "DetailCard__Row-sc-1gna34z-3 FeeRewardRow__StyledRow-sc-1afbm3f-0 primary-color IgsUY FlexBox__StyledFlexBox-ixcd3u-0 cxfWkp"})
    # reward_table = reward.find("table")
    if not reward_table:
        return -1
    table_rows = reward_table.find_all('tr')
    l = []
    for tr in table_rows:
        td = tr.find_all('td')
        row = [tr.text for tr in td]
        l.append(row)
    return pd.DataFrame(l, columns=["rewardTo", 'Fee']).dropna().reset_index(drop=True)


if __name__ == "__main__":
    address = "bnb1amwztd76ykx4hhgh52r6lfueks0t32lw5ydgqh"
    content_data = get_txs_content(address)

    block = '20131911'
    block = '21169224'  # 这个是没有reward的
    get_block_data('21169224')

