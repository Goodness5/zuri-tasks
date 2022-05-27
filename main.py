# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here
    f = open("story.txt", "r")
    print(f.read())
    lines = []
with open('story.txt') as f:
    lines = f.readlines()

count = 0
for line in lines:
    count += 1
    print(f'line {count}: {line}')


def count_words(*args):
    with open("story.txt") as f:
        for i in f:
            print("water")
        x = len("water")
        print(x)
        
    # [assignment] Add your code here
    
    

   # return {"as": 10, "would": 20}
