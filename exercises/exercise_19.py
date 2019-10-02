# Exercise 19:
# ======================
# 99 Bottles of Beer" is a traditional song in the United States and Canada. It is popular to sing on long trips,
# as it has a very repetitive format which is easy to memorize, and can take a long time to sing. The song's
# simple lyrics are as follows:
# 99 bottles of beer on the wall, 99 bottles of beer.
# Take one down, pass it around, 98 bottles of beer on the wall.
# The same verse is repeated, each time with one fewer bottle. The song is completed when the singer or
# singers reach zero.
# Your task here is write a Python program capable of generating all the verses of the song.

def generate_beer_song(n):
    if n == 0: #stop condition
        return #end point - return.
    else:
        print(f'{n} bottles of beer on the wall, {n} bottles of beer')
        print(f'Take one down, pass it around, {n-1} bottles of beer on the wall')
        generate_beer_song(n-1) #recursion


if __name__ == "__main__":
    generate_beer_song(4)
    #generate_beer_song(10)
    #generate_beer_song(99)