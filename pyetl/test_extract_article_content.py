import requests
from bs4 import BeautifulSoup


def get_article_string(article_url: str) -> str:
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
    }
    cookies = {
        "over18": "1",
    }

    res_article = requests.get(
        article_url,
        headers=headers,
        cookies=cookies,
    )

    soup_article = BeautifulSoup(res_article.text, "html.parser")
    soup_article_content = soup_article.select(
        'div[id="main-content"]',
    )[0]
    # print(type(soup_article))

    # div_article_metaline_tags = soup_article_content.select(
    #     'div[class="article-metaline"]',
    # )
    # reply_tags = soup_article_content.select(".push")

    # # print(div_article_metaline_tags)
    # for div_article_metaline_tag in div_article_metaline_tags:
    #     div_article_metaline_tag.extract()

    # for reply_tag in reply_tags:
    #     reply_tag.extract()

    extract_attr_list = [
        ".article-metaline",
        ".push",
        ".richcontent",
        ".article-metaline-right",
        ".f2",
    ]
    for attr in extract_attr_list:
        for tag in soup_article_content.select(attr):
            # print(type(tag))
            tag.extract()

    # print(soup_article_content.text)
    return soup_article_content.text

if __name__ == "__main__":
    article_url = "https://www.ptt.cc/bbs/Gossiping/M.1731081383.A.48A.html"
    print(get_article_string(article_url))