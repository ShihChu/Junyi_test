import sys

# Q1-A
words  = input("請輸入單字: ")

def Reverse(w):
    return w[len(w)::-1]

print(Reverse(words))

# Q1-B
sentence  = input("請輸入句子: ")

def Reverse_sentence(s):
    rev_sent = list()
    s = s.split(' ')

    for i in s:
        rev_sent.append(Reverse(i))
    
    return ' '.join(rev_sent)

print(Reverse_sentence(sentence))