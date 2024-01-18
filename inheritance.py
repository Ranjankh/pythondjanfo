# # inheritance
class Music:
    def playMusic(self):
        return"Music has been started"
    
class Guitar(Music):
    def guitarMusic(self):
        return "jing jing jack"

guitar =Guitar()
print(guitar.guitarMusic())
print(guitar.playMusic())

# static method
class StaticExample():
    @staticmethod
    def guitarMusic():
        return"jaz jaz"
print(StaticExample.guitarMusic())
