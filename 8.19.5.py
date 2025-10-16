lyrics = """Healing hands, of God have mercy on our unclean souls, once again. Jesus Christ, light of the world, burning bright, within our hearts forever. Freedom, means love without condition, Without a beginning or an end. Here's my heart, let it be forever Yours. Only You can make every new day seem so new."""

count = 0
wordcount= 0
cancount = 0

for char in lyrics:
    if cancount == 0:
        if char == " ":
            wordcount += 1
            cancount = 1
    if cancount == 1:
        if char == "e":
            count += 1
            cancount = 0
        if char == " ":
            wordcount += 1
wordcount += 1
countstring = str(count)
wordcountstring = str(wordcount)
percentage = str(count/wordcount*100)

print("there are " + wordcountstring  +" words, and 'e' shows up in " + countstring+" words, " + percentage + " percent of total words.")
