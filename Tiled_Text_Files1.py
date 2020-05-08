import sys

def main():

    # 1.
    # we read the input and make a list of words

    text = []
    words = []
    lines = sys.stdin.readlines()

    for i in lines:
        text.append(i.rstrip('\n'))

    for j in text:
        for k in j.split():
            words.append(k)

    words = list(filter(None, words))
    print(words)
    print(len(words))
    print(words[len(words)-1])

    # 2.
    # now we need a loop, which will start at 1 Tile and continue till last tile
    # inside we also count:
    # Width --> length of longest word in a given Tile and,
    # Height --> amount of words in a Tile

    #list_length = len(words)
    tile = 0
    max_width = len(words[0])
    height = 0
    width = 0
    tile_words = []

    for word in words:

        if len(word) <= max_width:
            # code that continues collecting tile info
            tile_words.append(word)
            max_width = len(word)

        if len(word) > max_width:
            # if word == words[len(words)-1]:
            #     tile_words.append(word)
            # if word == words[len(words)-1]:
            #     tile_words = [word]
            tile +=1
            if tile_words != []:
                height = len(tile_words)
                width = max(list(map(len, tile_words)))
            max_width = len(word)

            # 3.
            # we draw Tile borders '-', '|' and corners '+'

            tile_words.reverse()
            M = max(len(str(tile)), len(str(height)), len(str(width)))
            #top = "+-----------+"
            top = '+' + '-'*len('| Tile:  ') + '-'*(M+1) + '+'
            bottom = '+'+'-'*width+'+'
            print(top)
            print('| Tile:  ' + str(' ')*(M-len(str(tile))), tile, '|')
            print('| Width: ' + str(' ')*(M-len(str(width))), width, '|')
            print('| Height:' + str(' ')*(M-len(str(height))), height, '|')

            if len(top) > len(bottom):
                d = len(top) - len(bottom) - 1
                print(bottom + '-' * d + '+')
            if len(top) < len(bottom):
                d = len(bottom) - len(top) - 1
                print(top + '-' * d + '+')
            if len(top) == len(bottom):
                print(top)

            for w in tile_words:
                m = width - len(w)
                print('|'+' '*m + w +'|')
            #print(tile_words)
            print(bottom)
            if tile >= 500:
                return

            tile_words = [word]

main()