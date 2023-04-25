import requests
# 臺灣各縣市天氣預報資料及國際都市天氣預報
# 一般天氣預報-今明36小時天氣預報
"""
Wx(天氣現象)
MaxT(最高溫度)
MinT(最低溫度)
CI(舒適度)
PoP(降雨機率)
"""

url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001"
params = {
    "Authorization" : "Your api_key.",
}

response = requests.get(url, params=params)
data = response.json()
print("起始時間: ", data["records"]["location"][0]["weatherElement"][0]["time"][0]["startTime"])
print("結束時間: ", data["records"]["location"][0]["weatherElement"][0]["time"][0]["endTime"])
for locationOrdinal in range(0, 22):
    print("項次:", locationOrdinal)
    print("地區: ", data["records"]["location"][locationOrdinal]["locationName"])
    print("天氣: ", data["records"]["location"][locationOrdinal]["weatherElement"][0]["time"][0]["parameter"]["parameterName"])

