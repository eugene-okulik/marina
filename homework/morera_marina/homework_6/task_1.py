text = ("Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, "
        "dignissim vitae libero")

words = text.split()
text_new = []
for word in words:
    if not (word.endswith(",") or word.endswith(".")):
        text_new.append(word + "ing")
        continue
    else:
        text_new.append(word[:-1] + "ing" + word[-1])
print(" ".join(text_new))
