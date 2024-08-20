import requests
from bs4 import BeautifulSoup
import gradio as gr
def do(url):
    ans = []
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    job = soup.find_all('article', class_='b-block--top-bord job-list-item b-clearfix js-job-item')
    for i in job:
        title = i.find('a', class_='js-job-link').text.strip()
        com = i.get('data-cust-name')
        ans.append(f'職位: {title}, 公司: {com}')
    return '\n'.join(ans)

iface = gr.Interface(fn=do, title='104人力銀行爬蟲', description='請在下面貼上要爬的網址(104人力銀行)，使用時請注意不要給網頁帶來過多付擔。', inputs='text', outputs='text')
iface.launch(share=True)
