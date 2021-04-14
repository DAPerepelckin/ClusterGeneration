import os

import Cluster

if __name__ == '__main__':
    # просто создаем кластер и выводим 20 раз
    c = Cluster.cluster()
    print('generating colors')
    c.printColors('colors.tiff')

    k = 1

    if not os.path.exists('Folder-1-20'):
        os.mkdir('Folder-1-20')
        for i in range(1, 21):
            c = Cluster.cluster()
            c.printfTIFF('Folder-1-20//cluster{}.tiff'.format(i))
            c.printf('Folder-1-20//cluster{}.txt'.format(i))
            print('generating cluster {}'.format(k))
            k += 1

    if not os.path.exists('Folder-5-4'):
        os.mkdir('Folder-5-4')
    for i in range(1, 21):
        c = Cluster.cluster()
        c.printfTIFF('Folder-5-4//cluster{}.tiff'.format(i))
        c.printf('Folder-5-4//cluster{}.txt'.format(i))
        print('generating cluster {}'.format(k))
        k += 1

    if not os.path.exists('Folder-10-2'):
        os.mkdir('Folder-10-2')
    for i in range(1, 21):
        c = Cluster.cluster()
        c.printfTIFF('Folder-10-2//cluster{}.tiff'.format(i))
        c.printf('Folder-10-2//cluster{}.txt'.format(i))
        print('generating cluster {}'.format(k))
        k += 1

    if not os.path.exists('Folder-15-1'):
        os.mkdir('Folder-15-1')
    for i in range(1, 16):
        c = Cluster.cluster()
        c.printfTIFF('Folder-15-1//cluster{}.tiff'.format(i))
        c.printf('Folder-15-1//cluster{}.txt'.format(i))
        print('generating cluster {}'.format(k))
        k += 1

    if not os.path.exists('Folder-20-1'):
        os.mkdir('Folder-20-1')
    for i in range(1, 21):
        c = Cluster.cluster()
        c.printfTIFF('Folder-20-1//cluster{}.tiff'.format(i))
        c.printf('Folder-20-1//cluster{}.txt'.format(i))
        print('generating cluster {}'.format(k))
        k += 1

    if not os.path.exists('Folder-50-1'):
        os.mkdir('Folder-50-1')
    for i in range(1, 51):
        c = Cluster.cluster()
        c.printfTIFF('Folder-50-1//cluster{}.tiff'.format(i))
        c.printf('Folder-50-1//cluster{}.txt'.format(i))
        print('generating cluster {}'.format(k))
        k += 1

    print('finish')