if __name__ == "__main__":
    try:
        import discum
        import requests
        from pathlib import Path
        import os
        import json
        import random
        from time import sleep
        os.path.isfile("token.txt")
    except Exception as e:
        os.system("pip install discum")
        os.system("pip install requests")
        os.system("pathlib")
        input("모듈 설치를 완료 하였습니다.\ntoken.txt 를 만들고 안에 토큰을 넣어 주세요.")
    else:
        count = int(input("만드실 횟수를 입력 해 주세요 >> "))
        token = Path("token.txt").read_text()
        if "." in token:
            def header():
                headers = {
                    'authority': 'discord.com',
                    'accept': '*/*',
                    'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
                    'authorization': token,
                    'referer': 'https://discord.com/channels/@me',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
                }
                return headers
            random_name = open('keywords.txt','r',encoding="UTF-8")
            name = random.choice(random_name.read().split("\n"))
            print(name)
            try:
                for _ in range(1,count+1):
                    sleep(0.4)
                    #print(token)
                    payload = {
                        "recipients": []
                    }
                    r = requests.post('https://discord.com/api/v10/users/@me/channels', headers=header(), json=payload)
                    data = json.loads(r.content)
                    bot = discum.Client(token = token,log=False)
                    bot.setDmGroupIcon(data['id'], "./img/None.png")
                    js = {
                        'name': name
                    }
                    res = requests.patch(f'https://discord.com/api/v9/channels/{data["id"]}', headers=header(),json=js)

                    if res.status_code == 200 or res.status_code == 204 or res.status_code == 201:
                        print("SUCCESS | {}".format(name))
                    else:
                        print("FAIL | {}".format(name))

            except Exception as e:
                print(e)
                input(f"{data['retry_after']}초 후에 다시 이용 해 주세요.")
        else:
            input("토큰을 제대로 입력 해 주세요.")
