from urllib.request import urlopen

story = urlopen('https://archive.org/stream/WingsOfFireAnAutobiographAPJAbdulKalam3873/Wings+of+Fire_+an+autobiograph+-+A+P+J+Abdul+Kalam_3873_djvu.txt')

story_words = []

for line in story:
    line_words = line.split()
    for word in line_words:
        story_words.append(word.decode())

story.close()

print(story_words[5000:])