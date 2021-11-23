import os

for item in os.listdir(path='.'):
    if item.endswith(".jpg"):
        print(item)
        cmd = 'ffmpeg -y -i ' + item + ' ' + item + '.png'
        print(cmd)
        output = os.popen(cmd).read()
        print(output)
