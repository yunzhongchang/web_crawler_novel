import requests
from bs4 import BeautifulSoup
import os


# web_url = "http://biquw.net/book/82286/"


def get_web_url(web_url):

    resp = requests.get(web_url)
    resp.encoding = 'utf-8'
    html_doc = resp.text
    return html_doc

def parse_and_novel_download(html_doc):

    soup = BeautifulSoup(html_doc, 'html.parser')

    a_list = soup.find('ul',attrs={'class': 'dirlist three clearfix'}).find_all('a')


    for a in a_list:
        print("正在下载"a["href"])
        file_name = os.path.basename(a["href"])
        novel_url = f"http://biquw.net/book/82286/{file_name}"
        with open(f"D:\爬取小说/{file_name}.txt", "wt") as f:
            novel_url = requests.get(novel_url)
            novel_doc = novel_url.text
            soup = BeautifulSoup(novel_doc, 'html.parser')
            div_node = soup.find('div',class_="content")

            p_nodes = div_node.find_all('p')
            for p in p_nodes:
             f.write(p.get_text())

url =   get_web_url("http://biquw.net/book/82286/")
parse_and_novel_download(url)