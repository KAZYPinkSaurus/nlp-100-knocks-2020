#%%
# 00 文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
"stressed"[::-1]

# %%
# 01 「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
"パタトクカシーー"[::2]


# %%
# 02 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．

a = "パトカー"
b = "タクシー"
"".join([_a + _i for _a, _i in zip(a, b)])

#
# %%
# 01 “Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.”という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
a = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
[len(word) for word in a.replace(",", "").replace(".", "").split()]


# %%
