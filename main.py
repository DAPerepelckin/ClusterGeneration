import Cluster

if __name__ == '__main__':
    # просто создаем кластер и выводим 20 раз
    for i in range(1, 21):
        c = Cluster.cluster()
        c.printf('ClustersText//cluster{}.txt'.format(i))
        c.printfJPG('ClustersPictures//cluster{}.jpg'.format(i))
