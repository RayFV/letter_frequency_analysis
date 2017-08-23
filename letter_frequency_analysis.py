import numpy as np
from matplotlib import pyplot as plt
import collections
import sys,re

def menu():
    print("Welcome, what can I help?")
    print("[1]:Read from file")
    print("[2]:Enter text")
    print("[0]Exit")
    return input('::: ')

def main():
    pattern = re.compile(r'[^a-z]+') #regex, for remove all lettes except a-z
    while True:
        chosen = menu()
        if chosen == '1':
            # for file
            path = input('Input your file path:')
            file = open(path,"r")
            # replace all letters to "" except a-z
            # read whole file
            text = re.sub(pattern,"",file.read().lower())  
            file.close()
        elif chosen == '2':
            # for self enter text
            text = re.sub(pattern,"",input('Input Text : ').lower())  
        elif chosen == '0':
            sys.exit()
        text = collections.Counter(text) # count it dude!
        # sorted a-z
        obj = sorted(text.keys())
        # x = height
        x = np.arange(len(obj))
        # y = weight
        y = list(text[i] for i in obj) #example: text['a'] will return counted value
        plt.bar(x, y)
        # display value
        for v,w in zip(x,y):
            plt.text(v,w,str(w),color='red', fontweight='bold')
        plt.xticks(x, obj)
        # show result with bar
        plt.show()

if __name__ == "__main__":
    main()
