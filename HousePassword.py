def checkio(data):
    x=False
    if len(data) >= 10:
       if not data.isalpha() and not data.isdigit():
          if not data.islower() and not data.isupper():
             x=True
    return x
