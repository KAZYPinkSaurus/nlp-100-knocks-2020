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


# read_text()

# # %%
# import re

# text = read_text()
# results = re.findall(r"\[\[Category:.*?\n", text)
# print("".join(results))


# # %%
# import re

# text = read_text()
# results = re.findall(r"\[\[Category:.*?\n", text)
# result = re.sub(r"\[\[Category:", "", "".join(results))
# result = re.sub(r"\]\]", "", "".join(result))
# print(result)


# # %%
# import re

# text = read_text()
# results = re.findall(r"\n=+.*=+\n", text)
# func = lambda x: (re.sub(r"\n?=+\n?", "", x), len(re.search(r"=+", x).group()) - 1)
# for result in results:
#     title, level = func(result)
#     print(f"{title}:{level}")


# # %%
# import re

# text = read_text()
# results = re.findall(r"ja", text)
# results

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
    print(field_name)

    field_value_search = re.search(r"=([\s\S]*)", base_info)
    if field_value_search is None:
        continue
    field_value = field_value_search.group(1)

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
a = "[[ファイル:Wikipedia-logo-v2-ja.png|thumb|説明文]]"
b = "[[Category:ヘルプ|はやみひよう]]"
c = "[[記事名#節名|表示文字]]"
d = "[[記事名|表示文字]]"
e = "[[記事名]]"


for func in funcs27:
    assert func(a) == "[[ファイル:Wikipedia-logo-v2-ja.png|thumb|説明文]]"
    assert func(b) == "[[Category:ヘルプ|はやみひよう]]"
    assert func(c) == "表示文字"
    assert func(d) == "表示文字"
    assert func(e) == "記事名"
# %%
a = "[[[[ファイル:Wikipedia-logo-v2-ja.png|thumb|説明文]]]]"
b = "[[[[Category:ヘルプ|はやみひよう]]]]"
c = "[[記事名#節名|表示文字]]"
d = "[[記事名|表示文字]]"
e = "[[記事名]]"
f = "#REDIRECT [[記事名]]]]"
g = "#REDIRECT [[記事名#節名]]]]"
h = "<!-- コメントアウトしたいテキスト -->a<!-- コメントアウトしたいテキスト -->"


func28_1 = lambda x: re.sub(r"\[\[ファイル:.*?\]\]", r"", x)
func28_2 = lambda x: re.sub(r"\[\[Category:.*?\]\]", r"", x)
func28_3 = lambda x: re.sub(r"#REDIRECT \[\[.*?\]\]", r"", x)
func28_4 = lambda x: re.sub(r"<!--.*?-->", r"", x)


assert func28_1(a) == "[[]]"
assert func28_1(b) == "[[[[Category:ヘルプ|はやみひよう]]]]"
assert func28_1(c) == "[[記事名#節名|表示文字]]"
assert func28_1(d) == "[[記事名|表示文字]]"
assert func28_1(e) == "[[記事名]]"
assert func28_1(f) == "#REDIRECT [[記事名]]]]"
assert func28_1(g) == "#REDIRECT [[記事名#節名]]]]"

assert func28_2(a) == "[[[[ファイル:Wikipedia-logo-v2-ja.png|thumb|説明文]]]]"
assert func28_2(b) == "[[]]"
assert func28_2(c) == "[[記事名#節名|表示文字]]"
assert func28_2(d) == "[[記事名|表示文字]]"
assert func28_2(e) == "[[記事名]]"
assert func28_2(f) == "#REDIRECT [[記事名]]]]"
assert func28_2(g) == "#REDIRECT [[記事名#節名]]]]"

assert func28_3(a) == "[[[[ファイル:Wikipedia-logo-v2-ja.png|thumb|説明文]]]]"
assert func28_3(b) == "[[[[Category:ヘルプ|はやみひよう]]]]"
assert func28_3(c) == "[[記事名#節名|表示文字]]"
assert func28_3(d) == "[[記事名|表示文字]]"
assert func28_3(e) == "[[記事名]]"
assert func28_3(f) == "]]"
assert func28_3(g) == "]]"


assert func28_4(h) == "a"


print("ok")

# %%
func28_6 = lambda x: re.sub(r"<ref[\s\S]*?ref>", r"", x)
func28_6("aa<ref>h\noge\nfafa</ref>aa")

# %%
