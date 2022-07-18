import subprocess

suffix = ['mp4', 'mkv', 'vod']

def movie_list():
    l = subprocess.check_output('ls')
    l = str(l)
    l = l.split('\\')
    f = []

    x = []
    for i in l:
        i = i[1:]
        x.append(i)

    for i in x:
        l = i.split('.')
        try:
            if l[1] in suffix:
                f.append(i)
        except:
            pass

    return f

def tmovie_list():
    x = []
    l = movie_list()
    for i in l:
        i = i.split('.')
        x.append(i[0])
    return x

tmovie_list()