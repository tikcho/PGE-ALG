import sys
import copy

def main():
    # we read the input and make a list of words
    number = int(input())
    text = []
    words = []
    lines = sys.stdin.readlines()

    for i in lines:
        text.append(i.rstrip('\n'))

    for j in text:
        for k in j.split():
            words.append(k)
# ----------------------------------------
    words = list(filter(None, words))  # list of all elements
    N = 0
    size = len(words[0])  # sorting number, by current size
    tile_words = []  # tiles
    draw_tiles = []  # list of tiles
# ----------------------------------------
    for word in words:
        N += 1
        # we get list of all tiles, to order them on lines
        if len(word) <= size:
            tile_words.append(word)
            size = len(word)
            if N == len(words):
                tile_words.reverse()
                draw_tiles.append(tile_words)

        elif len(word) > size:
            size = len(word)
            tile_words.reverse()
            draw_tiles.append(tile_words)
            tile_words = [word]
            if N == len(words):
                tile_words.reverse()
                draw_tiles.append(tile_words)
    #print(draw_tiles)
# ----------------------------------------
    M = 0
    line = []
    #lines = []
    tile_length = 1
    max_widths = []
    prv_max = copy.copy(max_widths)
    ok =[]
# ----------------------------------------
    for tile in draw_tiles:
        # print(len(draw_tiles))
        # print(tile)
        # sorting tiles on lines according to initial number --> max size of a line
        M += 1
        #print(M)

        tl = list(map(len, tile))  # list of element sizes in a tile
        t_width = max(tl)

        tile_length = tile_length + t_width + 1
        if tile_length <= number:
            #print(tile)
            max_widths.append(t_width)
            line.append(tile)
            if M == len(draw_tiles):
                draw(line, max_widths, prv_max)
            # else:
            #     ok.append()

        if tile_length > number:  # whole sum on the line is > number (19, ...)
            # code to draw the next line
            # lines.append(line)
            # print(">", tile)

            draw(line, max_widths, prv_max)   # middle part: words/tiles...
            prv_max = copy.copy(max_widths)
            max_widths = [t_width]
            line = [tile]
            tile_length = 1 + t_width + 1
            if M == len(draw_tiles):
                draw(line, max_widths, prv_max)
    print(draw_top(max_widths) + '+')


def draw_top(max_widths):
    top = ''
    for w in max_widths:
        top = top + '+' + '-' * w
    return top


def draw(line, max_widths, prv_max):
    u = list(map(len, line))  # number of elements in each tile, in one line
    height = max(u)  # max number of elements in a given line

    top = draw_top(max_widths)
    new = top + '+'
    oldtop = draw_top(prv_max)
    old = oldtop + '+'

    if new == old:
        print(new)
    else:
        n = list(new)
        o = list(old)
        if len(new) < len(old):
            for p in range(len(n)):
                if n[p] == '+' and o[p] == '-':
                    o[p] = '+'
            print(''.join(o))
        else:
            for p in range(len(o)):
                if o[p] == '+' and n[p] == '-':
                    n[p] = '+'
            print(''.join(n))

    for y in range(height):
        middle = ''
        for x in range(len(line)):
            tile = line[x]
            for z in range(height-u[x]):
                tile = [''] + tile
            word = tile[y]
            d = max_widths[x] - len(word)
            middle = middle + '|' + ' '*d + word

        print(middle + '|')

main()
