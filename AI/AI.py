import textwrap
import urllib
import google.generativeai as genaiL
import json
import datetime
from IPython.display import Markdown
from openai import OpenAI
from pathlib import Path
from base64 import b64decode
import datetime as dt
import os


# 디렉토리 이름
DATA_DIR = "C:\\Users\\minqu\\"
today = dt.date.today()
DIR_NAME = f"newsis_{today.year}-{today.month}-{today.day}\\"
secret_file = ["naver_id", "naver_password", "openai_key", "genai_key"]
for file_name in secret_file:

    with open(DATA_DIR + "api_key\\" + file_name + ".txt", "r") as fp:
        match file_name:
            case "naver_id":
                naver_id = fp.readline()
            case "naver_password":
                naver_Key = fp.readline()
            case "openai_key":
                openai_Key = fp.readline()
            case "genai_key":
                genai_key = fp.readline()
            case _:
                print("error")

# API key
genaiL.configure(api_key=genai_key)
client = OpenAI(api_key=openai_Key)


def getRequestUrl(url):
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", naver_id)
    req.add_header("X-Naver-Client-Secret", naver_Key)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s]Url Request Success" % datetime.datetime.now())
            return response.read().decode("utf-8")
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None


def getNaverSearch(node, srcText, start, display):
    base = "https://openapi.naver.com/v1/search"
    node = "/%s.json" % node
    parameters = "?query=%s&start=%s&display=%s" % (
        urllib.parse.quote(srcText),
        start,
        display,
    )

    url = base + node + parameters
    responseDecode = getRequestUrl(url)  # [CODE 1]

    if responseDecode == None:
        return None
    else:
        return json.loads(responseDecode)


def to_markdown(text):
    text = text.replace("•", "  *")
    return Markdown(textwrap.indent(text, "> ", predicate=lambda _: True))


# 디렉토리 만들기
try:
    os.mkdir(DATA_DIR + DIR_NAME)
except:
    print("디텍토리 만들 때 오류 발생")


node = "news"  # 크롤링한 대상
srcText = input("검색어를 입력하세요: ")
cnt = 0
jsonResult = []
jsonResponse = getNaverSearch(node, srcText, 1, 10)  # [CODE 2]

print(jsonResponse["items"])


model = genaiL.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(history=[])
response = chat.send_message(
    """뉴스 기사 10가지의 인터넷 주소를 첨부 할테니 이를 4가지로 나누고 나눈 기사들을 기준으로 내용을 합쳐서 4가지의 새로운 뉴스 기사를 만들어줘 이때, 분량은 한 기사당 400자 이상으로! 그리고 새로 만든 뉴스 기사의 마지막에는 참조한 그 인터넷 기사의 링크를 밝혀줘"
    이 뉴스 기사 리스트는 json형태로 되어 있어, 'title'은 이 기사의 제목이고, 'originallink'는 기사의 실제 링크, 'description'은 기사를 간단히 요약한 것이야, 'pubDate'은 출판 날짜야
    그리고 결과는 Json형태로 만들어줘 'title'의 뉴스 기사의 제목이고, 'text'는 너가 직접 만든 뉴스 기사 내용을 적어줘, 'reference'는 이 기사의 출처를 리스트 형태로 만들어 줘 그리고 json형태 말고 아무런 말하지 마"""
    + "다음은 뉴스 기사 리스트야 : "
    + str(jsonResponse["items"])
)
try:
    print(response.text)
except Exception as e:
    print(f"{type(e).__name__}: {e}")
text = response.text
text = text.replace("`", "")
text = text.replace("'", "")
text = text.replace("\t", "")
text = text.replace("\n", "")
text = text.replace("json", "")

n_json = json.loads(str(text))
with open(DATA_DIR + DIR_NAME + f"{srcText}.json", mode="w", encoding="utf-8") as fp:
    json.dump(n_json, fp, ensure_ascii=False)
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
        image_file = DATA_DIR + DIR_NAME + f"{srcText}-{i}.png"
        with open(image_file, mode="wb") as png:
            png.write(image_data)