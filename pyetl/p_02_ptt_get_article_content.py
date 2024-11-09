import os

import requests
from bs4 import BeautifulSoup

from test_extract_article_content import get_article_string


PTT_FOLDER_PATH = "ptt_article"

# Create folder
if not os.path.exists(PTT_FOLDER_PATH):
    os.mkdir(PTT_FOLDER_PATH)

# url = "https://ptt-discussion.tw/bbs/Gossiping/index.html"
url = "https://www.ptt.cc/bbs/Gossiping/index.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
}
cookies = {
    "over18": "1",
}

response = requests.get(url, headers=headers, cookies=cookies)
soup = BeautifulSoup(response.text, "html.parser")

articles = soup.find_all("div", class_="title")
print(articles)
for article in articles:
    # Each article be like:
    # <div class="title">
    # <a href="/bbs/Gossiping/M.1731081383.A.48A.html">[新聞] 川普勝選太傷心？哈佛大學隔天取消課程</a>
    # </div>
    title = article.text.strip()  # article.find("a").text.strip()
    link = article.find("a")  # <a href="/bbs/Gossiping/M.1731081383.A.48A.html">[新聞] 川普勝選太傷心？哈佛大學隔天取消課程</a>
    if link:
        article_url = "https://www.ptt.cc" + link["href"]
        print(f"Title: {title}, URL: {article_url}")

        # Get article content "string"
        article_string = get_article_string(article_url)

        for replace_word in ["/", "?", "@", "#", "*", ":"]:
            title = title.replace(replace_word, "")

        with open(f"{PTT_FOLDER_PATH}/{title}.txt", "w", encoding="utf-8") as f:
            f.write(article_string)
