# -*- coding: utf-8 -*-
import os, glob, json
# dic_file = './newstext/word-dic.json'
# dic_file = './word-dic.json'
# word_dic= {'_MAX': 0}
# json.dump(word_dic, open(dic_file, "w"))
word_dic = { "_MAX": 0 }
def text_to_ids(text):
    text = text.strip()
    words = text.split(" ")
    result = []
    for n in words:
        n = n.strip()
        if n == "": continue
        if not n in word_dic:
            wid = word_dic[n] = word_dic["_MAX"]
            word_dic["_MAX"] += 1
            print(wid, n)
        else:
            wid = word_dic[n]
        result.append(wid)
    return result

# cnt=[]
# for n in range(word_dic["_MAX"]):
#     cnt.append(n)
cnt=[]
with open('hong.txt', "r", encoding='utf-8') as f:
    text = f.read().strip()
    ids = text_to_ids(text)
    # cnt = [0 for n in range(word_dic["_MAX"])]
    for n in range(word_dic["_MAX"]):
        cnt.append(0)
    print(cnt)
    print()
    for wid in ids:
        cnt[wid] += 1
        print('wid: %d, cnt[%d]: %d'%(wid,wid,cnt[wid]))
