import requests
from bs4 import BeautifulSoup


def check_available(received_text: str) -> bool:
    return received_text.startswith("나무위키 검색:")

def make_response(received_text: str) -> str:
    query = received_text[7:]
    post_list = naver_search(query)

    # response_text = ""
    # for post in post_list:
    #     response_text += post["title"] + "\n"

    response_text = "\n".join([
        post["title"]for post in post_list])

    return response_text

def naver_search(query):
    naver_search_url = "https://namu.wiki/w/"
    params = {
        query,  # 검색어
    }
    res = requests.get(naver_search_url, params=params)
    soup = BeautifulSoup(res.text, "html.parser")
    return [{"title": tag.text} for tag in soup.select(".lst_total .total_tit")]