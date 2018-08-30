import requests


if __name__ == "__main__":
    r = requests.get("https://www.kuaidaili.com/free/")
    print(r.status_code)
    print(r.text)