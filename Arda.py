import requests

url = "https://www.tuttosport.com/api-live/poll/109339784"
headers = {
    "Host": "www.tuttosport.com",
    "Sec-Ch-Ua": "",
    "Sec-Ch-Ua-Platform": "\"\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Content-Type": "application/json",
    "Accept": "*/*",
    "Origin": "https://www.tuttosport.com",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://www.tuttosport.com/sondaggi/calcio/golden-boy/2023/06/21-109339784/vota_il_golden_boy_2023_ecco_la_lista_dei_100_candidati_sondaggio_aperto_",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7"
}
data = {
    "selected": ["77"]
}

while True:
    response = requests.post(url, headers=headers, json=data)
    print(response.status_code)
    print(response.text)

