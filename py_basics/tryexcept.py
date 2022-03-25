from unicodedata import name


try:
    x = int(input('Input an integer'))
    print(x)
    
except ValueError:
    print("Value not a integer!!!!")

else:
    print("Nothing went wrong success!!")