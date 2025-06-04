import google.generativeai as genaiL
import json
from openai import OpenAI
from base64 import b64decode
import datetime as dt
from datetime import timedelta
import os
from openai import OpenAI
from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import requests
import bs4
from bs4 import BeautifulSoup
import base64

def find_week():
    firstday = today.replace(day=1) # 5
    while firstday.weekday() != 6: # 6
      firstday += timedelta(days=1)
      
    if today < firstday: # 7
      return 0
  
    return (today - firstday).days // 7 + 1 # 8

def find_news():
    urls = []
    for pagenum in range(1, 30):
        url = "https://news.hada.io/new?page={}".format(pagenum)

        response = requests.get(url)

        if response.status_code == 200:
            html = response.text
            soup = BeautifulSoup(html, "html.parser")
            for div_index in range(1, 20):
                cssstring = "body > main > article > div > div:nth-child({}) > div.topictitle > a".format(
                    div_index
                )
                temp_orgin_url = soup.select_one(cssstring)
                cssstring = "body > main > article > div > div:nth-child({}) > div.topicdesc > a".format(
                    div_index
                )
                temp_summarized_url = soup.select_one(cssstring)
                if temp_orgin_url:
                    if temp_orgin_url.attrs["href"].find("https") != -1 and temp_orgin_url.attrs["href"].find("youtube") == -1:
                        urls.append(
                            [
                                temp_orgin_url.attrs["href"],
                                pagenum * 100 + div_index,
                                temp_summarized_url.attrs["href"],
                            ]
                        )
        else:
            print(response.status_code)
    return urls


def urltodocument(url, ishada: bool, isgithub : bool):
    text_splitter = CharacterTextSplitter(
        separator="\n\n",
        chunk_size=3000,
        chunk_overlap=500,
    )
    if ishada:
        classifiers = dict(parse_only=bs4.SoupStrainer(class_=("topic_contents")))
    elif isgithub:
        classifiers = dict(parse_only=bs4.SoupStrainer(class_=("markdown-body entry-content container-lg")))
    else :
        classifiers = None
    docs = WebBaseLoader(
        url,
        bs_kwargs=classifiers,
    ).load_and_split(text_splitter)
    for document in docs:
        document.page_content = (
            document.page_content.replace("\n", "")
            .replace("\t", "")
            .replace("  ", "")
            .replace("\r", "")
            .replace("\\", " ")
        )
    return docs

DATA_DIR = "/docker/Newsis-Newsletter/"
today = dt.date.today()
cur_week = find_week()
DIR_NAME = f"WEB/Back-end/media/{today.year}-{today.month}-{cur_week}/"
secret_file = ["naver_id", "naver_password", "openai_key", "genai_key"]

for file_name in secret_file:

    with open(DATA_DIR + "api_key/" + file_name + ".txt", "r") as fp:
        if file_name == "naver_id":
            naver_id = fp.readline()
        elif file_name == "naver_password":
            naver_Key = fp.readline()
        elif file_name == "openai_key":
            openai_Key = fp.readline()
        elif file_name == "genai_key":
            genai_key = fp.readline()

# API key
genaiL.configure(api_key=genai_key)
client = OpenAI(api_key=openai_Key)

try:
    os.mkdir(DATA_DIR + DIR_NAME)
except:
    print("디텍토리 만들 때 오류 발생")


urls = find_news()

result = []

for url in urls:
    print(dt.datetime.now(), url)
    llm = ChatOllama(
    model="gemma3:12b",  # 사용할 언어 모델을 지정합니다.
    format="json",  # 입출력 형식을 JSON으로 설정합니다.
    temperature=0,
    )
    isgithub = False
    summarized_docs = urltodocument("https://news.hada.io/" + url[2], True, isgithub)
    if not url[0].find("github"):
        isgithub = True
    else :
        isgithub = False
    origin_docs = urltodocument(url[0], False, isgithub)
    prompt = ChatPromptTemplate.from_messages(
        [
            """Create a new news article with a summary and original of some Tech in Korean with more than 200 characters. \n Article with a summary : {sum_text} \n article with original : {origin} \n`title` : Topic of this article, `text` : Summarized text \n key: `title`, `text`. respose in JSON format"""
        ]
    )
    chain = prompt | llm | StrOutputParser()
    result_stuff = chain.invoke({"sum_text": summarized_docs, "origin" : origin_docs})
    result_stuff.replace("\n", "").replace("\t", "").replace("\r", "").replace("\\", "").replace("`", "").replace("'", "")
    try : 
        sample_text = json.loads(result_stuff)
    except :
        print(result_stuff)
        continue
    sample_text["url"] = url[0]
    result.append(sample_text)

with open(DATA_DIR + DIR_NAME + "temp.json", "w", encoding="UTF-8") as f:
    json.dump(result, f, indent=4, ensure_ascii=False)


model = genaiL.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(history=[])
response = chat.send_message(
    """뉴스 기사 10가지의 인터넷 주소를 첨부 할테니 이를 4가지로 나누고 나눈 기사들을 기준으로 내용을 합쳐서 4가지의 새로운 뉴스 기사를 한국어로 만들어줘 이때, 분량은 한 기사당 400자 이상으로! 그리고 새로 만든 뉴스 기사의 마지막에는 참조한 그 인터넷 기사의 링크를 밝혀줘"
    이 뉴스 기사 리스트는 json형태로 되어 있어, 'title'은 이 요약한 기사의 제목이고, 'url'는 기사의 실제 링크, 'description'은 기사를 간단히 요약한 것이야, 'pubDate'은 출판 날짜야
    그리고 결과는 Json형태로 만들어줘 'title'의 뉴스 기사의 제목이고, 'text'는 너가 직접 만든 뉴스 기사 내용을 적어줘, 'reference'는 이 기사를 만들면서 참고했던 출처들을 리스트 형태로 만들어 줘 그리고 json형태 말고 아무런 말하지 마"""
    + "다음은 뉴스 기사 리스트야 : "
    + str(result)
)

try:
    print(response.text)
except Exception as e:
    print(f"{type(e).__name__}: {e}")
    exit(1)

text = response.text
text = text.replace("`", "")
text = text.replace("'", "")
text = text.replace("\t", "")
text = text.replace("\n", "")
text = text.replace("json", "")
try:
    n_json = json.loads(str(text))
except:
    exit(1)

with open(DATA_DIR + DIR_NAME + "news.json", mode="w", encoding="utf-8") as fp:
    json.dump(n_json, fp, ensure_ascii=False, indent=4)
print(n_json)

for i in range(0, 4):
    response = client.images.generate(
        model="dall-e-3",
        prompt="위의 기사를 토대로 이미지를 하나 만들어줘. 그리고 이미지를 생성할 때 글자처럼 보이는 것은 다 제거해줘"
        + "기사 내용 : "
        + n_json[i]["text"],
        size="1024x1024",
        quality="standard",
        n=1,
        response_format="b64_json",
    )

    # png 파일로 저장
    for index, image_dict in enumerate(response.data):
        image_data = b64decode(image_dict.b64_json)
        image_file = DATA_DIR + DIR_NAME + f"{i}.png"
        with open(image_file, mode="wb") as png:
            png.write(image_data)

obj = []
with open(DATA_DIR+DIR_NAME+"news.json", "r+") as fp:
    obj = json.load(fp)
data = {}

for i in range(0, 4):
    img_in = open(DATA_DIR+DIR_NAME+f"{i}.png", 'rb')
    base64_str = base64.b64encode(img_in.read()).decode('utf-8')
    data["image"] = "blank"
    data["news"] = str(obj[i])
    data["index"] = i
    data["weeks"] = f"{today.year}-{today.month}-{cur_week}"
    responds = requests.post("http://localhost:9000/data/", json=data)
    print(responds.text)