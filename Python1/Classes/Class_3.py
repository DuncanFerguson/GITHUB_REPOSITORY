def audioSetting(volume, bass=0, treble=0):
    '''This is a function that returns the Volume Settings'''
    print("Volume: ", volume)
    print("Bass: ", bass)
    print("Treble: ", treble)
    return

def max(x,y):
    if x > y:
        return y
    return y

x = 100
y = int(input("Enter Volume:"))
max(x, y)

audioSetting(y or x, 10, -20)

