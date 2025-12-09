def Clean_text(text):
    symbols = ".?!,\n"
    clean_text = ""
    for s in symbols:
        text = text.replace(s, '')
    for i in range(len(text) - 1):
        if text[i] == " " and text[i + 1] == " ":
            i += 1
        else:
           clean_text += text[i]
    return clean_text

text2 = """
    Python is a powerful programming language.

    It is used in data science, web devolepment,
   automation, and many other fields!

   PYTHON is easy to learn, yet very versatile
"""
text2 = text2.strip().lower()
text2 = text2.replace("!", ".")
text2 = text2.split(".")
print(text2)
text1 = text2[0]
text1 = text1.strip()
text1 = text1.lower()
print(text1)
print(text1.count("python"))
print(text1.startswith("python"), text1.endswith("language"))
print(len(text1), text1.count("a"), text1.find("data"))

text = """
    Python is a powerful programming language.

    It is used in data science, web devolepment,
   automation, and many other fields!

   PYTHON is easy to learn, yet very versatile
"""
dict_of_words = {}
clean_text = Clean_text(text.strip())
words1 = clean_text.split(" ")
for i in (words1):
    dict_of_words[i] = words1.count(i)
joined_text = ''
for i in range(len(words1)- 1):
    joined_text = joined_text + words1[i] + '-'
joined_text += words1[-1]
print(dict_of_words)
print(joined_text)