from bs4 import BeautifulSoup
import requests

page = requests.get("https://www.roblox.com/games/286090429/Arsenal")
soup = BeautifulSoup(page.text, "html.parser")

title = soup.findAll("h1", attrs={"class":"game-name"})
dev = soup.findAll("a", attrs={"class":"text-name text-overflow"})


for t in title:
    print(t.text)
for d in dev:
    print(d.text)