def count_words(text, words):
    text=text.lower()
    i=0
    w=list(words)
    for item in w:
        try:
          text.index(item)
          i=i+1;
        except ValueError:
          i=i   
    return i
