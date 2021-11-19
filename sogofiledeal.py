# -*- coding:utf8 -*-

import re

file = open('news_tensite_xml.dat','r',encoding='gb18030')
data = file.read()
doc_items = data.split('</doc>')
text_list = []

for num, text in enumerate(doc_items):
    middle_result = text.split('</content>')[0]
    middle_result = middle_result.split('<content>')
    if len(middle_result) > 1:
        text_list.append(middle_result[1])

length_doc = len(text_list)
print(length_doc)
word_num_txt = 10000
file_num = length_doc / word_num_txt
print(file_num)
file_num = round(file_num)
print(file_num)
file_num = round(length_doc * 1.0 / word_num_txt) + 1
print(file_num)
import os
if not os.path.exists('news_tensite_xml_qiefen'):
    os.mkdir('news_tensite_xml_qiefen')
for num in range(0, file_num):
    file_name = "./news_tensite_xml_qiefen/" + str(num) + ".txt"
    with open(file=file_name,mode='w',encoding='utf-8') as f:
        start = num * word_num_txt
        end = min((num + 1) * word_num_txt, length_doc)
        for _ in range(start, end):
            word = text_list[_].replace(' ', '')
            word = re.sub("([“。，？：；”、])", "", word)
            f.write(word)
        f.close()
