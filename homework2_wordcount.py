'''Please write a program that reads a text file containing some text and for each word in the file counts how many times it
appears. Please note you can use a dictionary structure. Before starting to count words it might be necessary to delete
all punctuation and special symbols (new line, tab etc.) and put all words in lower case.'''

print("Count the number of words directly: ")
import time
start = time.process_time()

with open("C:\\Users\\Yuqing\\Desktop\\Sample.txt", "r") as fp:
    # read the file
    datas = fp.readlines()
    # merge
    datas = " ".join(datas)
    # split
    datas = datas.split()
    # word count
    wordcount = len(datas)
    print(wordcount)

end = time.process_time()
print(end - start)
