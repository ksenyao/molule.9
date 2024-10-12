def all_variants(text):
    len_text = len(text)
    for i in range(len_text):
        for j in range(len_text - i):
            str_txt = text[j:j+i+1:1]
            yield str_txt


a = all_variants("abc")
for i in a:
    print(i)