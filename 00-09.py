#%%
# 00 文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
"stressed"[::-1]

# %%
# 01 「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
"パタトクカシーー"[::2]


# %%
# 02 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．

word1 = "パトカーbbb"
word2 = "タクシーaaa"
"".join([_word1 + _word2 for _word1, _word2 in zip(word1, word2)])

#
# %%
# 03 “Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.”という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
import re

[len(word) for word in text.split()]


# %%
# 04 “Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.”という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．

text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
words = text.split()
b = [1, 5, 6, 7, 8, 9, 15, 16, 19]

dic = {}
for idx, word in enumerate(words):
    c = 2
    if idx + 1 in b:
        c = 1
    dic[word[:c]] = idx + 1

dic

# %%
# 05 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，”I am an NLPer”という文から単語bi-gram，文字bi-gramを得よ．

text = "I am an NLPer"


def n_gram(text, n=2, mode="tango"):
    if mode == "tango":
        text = text.split()
    if len(text) < n:
        return []
    return [text[idx : idx + n] for idx in range(len(text) - n + 1)]


print(n_gram(text, mode="tango"))
print(n_gram(text, mode="moji"))


# %%
# 06 “paraparaparadise”と”paragraph”に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．さらに，’se’というbi-gramがXおよびYに含まれるかどうかを調べよ
text1 = "paraparaparadise"
text2 = "paragraph"

text1 = n_gram(text1, mode="moji")
text2 = n_gram(text2, mode="moji")
print(f"和集合:{set(text1) | set(text2)}")
print(f"積集合:{set(text1) & set(text2)}")
print(f"差集合:{set(text1) - set(text2)}")
print(f"差集合:{set(text2) - set(text1)}")

"se" in set(text1) & set(text2)

# %%
# 07 引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．さらに，x=12, y=”気温”, z=22.4として，実行結果を確認せよ．

func1 = lambda x, y, z: f"{x}時の{y}は{z}"

x = 12
y = "気温"
z = 22.4

func1(x, y, z)


# %%
# 08 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
# 英小文字ならば(219 - 文字コード)の文字に置換
# その他の文字はそのまま出力
# この関数を用い，英語のメッセージを暗号化・復号化せよ


def cipher(text, mode="encode"):
    if mode == "decode":
        return "".join([chr(219 - ord(txt)) if txt.islower() else txt for txt in text])
    return "".join([chr(219 - ord(txt)) if txt.islower() else txt for txt in text])


a = "I am KAZY from Japan"
a = cipher(a, mode="encode")
print(a)
a = cipher(a, mode="decode")
print(a)


# %%
# 09 スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文（例えば”I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .”）を与え，その実行結果を確認せよ．

text = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
import random


def func2(text):
    shuffle = (
        lambda x: f"{x[0]}{''.join(random.sample([_x for _x in x[1:-1]],len(x[1:-1])))}{x[-1]}"
    )
    return " ".join([shuffle(txt) if len(txt) > 4 else txt for txt in text.split()])


print(text)
func2(text)

# %%
