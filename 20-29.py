# %%
# 20
from pathlib import Path
import gzip
import json


def read_text():
    file_path = Path("files/jawiki-country.json.gz")
    with gzip.open(file_path) as f:
        for line in f:
            title_contents = json.loads(line)
            if title_contents["title"] == "イギリス":
                return title_contents["text"]


read_text()

# %%
# 21
import re

text = read_text()
results = re.findall(r"\[\[Category:.*?\]\]", text)
print("\n".join(results))


# %%
# 22
import re

text = read_text()
results = re.findall(r"\[\[Category:.*?\]\]", text)
result = re.sub(r"\[\[Category:|(\|.*)?\]\]", "", "\n".join(results))
print(result)


# %%
# 23
import re

text = read_text()
results = re.findall(r"==+.*?==+", text)
print(results)
func = lambda x: (re.sub(r"==+|\s", "", x), len(re.search(r"==+", x).group()) - 1)
for result in results:
    title, level = func(result)
    print(f"{title}:{level}")


# %%
# 24
# ref :https://ja.wikipedia.org/wiki/Help:%E7%94%BB%E5%83%8F%E3%81%AA%E3%81%A9%E3%81%AE%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%81%AE%E3%82%A2%E3%83%83%E3%83%97%E3%83%AD%E3%83%BC%E3%83%89%E3%81%A8%E5%88%A9%E7%94%A8
import re

text = read_text()
# results = re.findall(r"\[\[ファイル:.*?\]\]", text)
# print(results)
results = re.findall(r".*?(?:png|gif|jpg|jpeg|xcf|pdf|mid|ogg|svg|djvu)", text)
for result in results:
    result = re.sub(r".*ファイル:(.+)", r"\1", result)
    result = re.sub(
        r".*(http:[a-zA-Z0-9_/\-\.~:]+\.)(png|gif|jpg|jpeg|xcf|pdf|mid|ogg|svg|djvu)",
        r"\1\2",
        result,
    )
    result = re.sub(r".+=\ ?", r"", result)
    print(result)

# 

# %%
import re

# 26用
func26_1 = lambda x: re.sub(r"(^|[^'])''([^']+)''([^']|$)", r"\1\2\3", x)
func26_2 = lambda x: re.sub(r"(^|[^'])'''([^']+)'''([^']|$)", r"\1\2\3", x)
func26_3 = lambda x: re.sub(r"(^|[^'])'''''([^']+)'''''([^']|$)", r"\1\2\3", x)
funcs26 = [func26_1, func26_2, func26_3]

# 27用
func27_1 = lambda x: re.sub(r"\[\[([^:\]]+\|)?([^:\]]+)\]\]", r"\2", x)
funcs27 = [func27_1]

# 28用
func28_1 = lambda x: re.sub(r"\[\[ファイル:.*?\]\]", r"", x)
func28_2 = lambda x: re.sub(r"\[\[Category:.*?\]\]", r"", x)
func28_3 = lambda x: re.sub(r"#REDIRECT \[\[.*?\]\]", r"", x)
func28_4 = lambda x: re.sub(r"<!--.*?-->", r"", x)
func28_5 = lambda x: re.sub(r"<references/>", r"", x)
func28_6 = lambda x: re.sub(r"<ref[\S\s]*?ref>", r"", x)
func28_7 = lambda x: re.sub(r"<ref[\s\S]*?/>", r"", x)
func28_8 = lambda x: re.sub(r"\{\{0\}\}", r"", x)
func28_9 = lambda x: re.sub(r"\{\{.*?\}\}", r"", x)

funcs28 = [
    func28_9,
    func28_6,
    func28_7,
    func28_1,
    func28_2,
    func28_3,
    func28_4,
    func28_5,
    func28_8,
]


text = read_text()
result = re.search(r"\{\{基礎情報 国\n([\S\s]+?)\}\}\n\n", text).group(1)

result_dic = {}
for base_info in result.split("\n|"):
    base_info = re.sub(r"\n", "", base_info)
    field_name_search = re.search(r"^\|?(.*?)=", base_info)
    if field_name_search is None:
        continue
    field_name = field_name_search.group(1)

    field_value_search = re.search(r"=([\s\S]*)", base_info)
    if field_value_search is None:
        continue
    field_value = field_value_search.group(1)
    print([field_value])
    field_name = re.sub(r"[\s=]", "", field_name)
    field_value = re.sub(r"^=", "", field_value)
    # 26用

    if "'" in field_value:
        # print(f"before:\n{field_value}\n")
        for func in funcs26:
            field_value = func(field_value)
        # print(f"after\n:{field_value}\n")

    for func in funcs28:
        field_value = func(field_value)

    if "[[" in field_value:
        # print(f"before:\n{field_value}\n")
        for func in funcs27:
            field_value = func(field_value)
        # print(f"after\n:{field_value}\n")

    result_dic[field_name] = field_value


for key, value in result_dic.items():
    print("--------")
    print(f"key :{key}")
    print(f"value :{value}")
    print("--------")


# %%
# 29

import requests

S = requests.Session()

URL = "https://jp.wikipedia.org/w/api.php"


PARAMS = {
    "action": "query",
    "format": "json",
    "prop": "imageinfo",
    "titles": f"ファイル:{result_dic['国旗画像']}",
    "iiprop":"url"
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()
PAGES = DATA['query']['pages']['-1']['imageinfo'][0]['url']
print(PAGES)


# %%
