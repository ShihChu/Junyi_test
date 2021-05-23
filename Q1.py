import sys

words  = input("請輸入單字: ")
sentence  = input("請輸入句子: ")

# Q1-A
def Reverse(w):
    return w[len(w)::-1]

print(Reverse(words))

# Q1-B
sentence = sentence.split(' ')
rev_sent = list()

for i in sentence:
    rev_sent.append(Reverse(i))

print(' '.join(rev_sent))