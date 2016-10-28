import numpy as np
import matplotlib.pyplot as plt
def randomWaitScheme(nodes, len_n):
    cnt = 0
    ch_timer = 0
    channel = 1
    served = []
    while True:
        # print 'ch_timer ', ch_timer
        for key in nodes.keys():
            # print 'node', node[key]
            if key not in served:
                # print 'node', node[key]
                if nodes[key]['timer'] == 0: # node timer is out
                    if channel == 1: #if channel is avaliable
                        ch_timer = nodes[key]['need']
                        served.append(key)
                        channel = 0 # turn off channel access
                    else:
                        new_timer = np.random.randint(32, size=(1))[0]
                        # print 'new_timer',new_timer
                        nodes[key]['timer'] = new_timer
                        if nodes[key]['type']:
                            nodes[key]['cnt'] += new_timer
                else:
                    nodes[key]['timer'] -= 1 #node waiting

        if channel == 0:
            if ch_timer >0:
                ch_timer -= 1 # channel flag
            if ch_timer == 0:
                channel = 1

        cnt += 1 # total timer

        if ch_timer == 0 and len(served) == len_n:
            break
    urgent_cnt = 0
    for key in nodes.keys():
        if nodes[key]['type']:
            urgent_cnt += nodes[key]['cnt']
    return cnt, urgent_cnt

def priorityScheme(nodes, len_n):
    cnt = 0
    ch_timer = 0
    channel = 1
    served = []
    queue = []
    wait = 0
    while True:
        # print 'ch_timer ', ch_timer
        for key in nodes.keys(): # reset each nodes
            # print 'node', node[key]
            if key not in served:
                # print 'node', node[key]
                if nodes[key]['timer'] == 0: # node timer is out
                    if nodes[key]['type']:
                        queue.append((key, cnt))
                        served.append(key)
                    else:
                        new_timer = np.random.randint(32, size=(1))[0]
                        nodes[key]['timer'] = new_timer
                    if channel == 1: #if channel is avaliable
                        if queue:
                            key,s = queue.pop(0)
                            ch_timer = nodes[key]['need']
                            wait += (cnt-s)
                            channel = 0
                        else:
                            ch_timer = nodes[key]['need']
                            served.append(key)
                            channel = 0 # turn off channel access

                else:
                    nodes[key]['timer'] -= 1 #node waiting

        if channel == 0:
            if ch_timer >0:
                ch_timer -= 1 # channel flag
            if ch_timer == 0:
                channel = 1

        cnt += 1 # total timer

        if ch_timer == 0 and len(served) == len_n:
            break

    return cnt, wait

def initialNodes(len_n):
    # initial the node status
    timer = np.random.randint(len_n, size=(len_n))
    need = np.random.randint(10, size=(len_n))
    nodes = {}
    for i in range(len(timer)):
        if timer[i] % 2 == 0:
            type_ = True
        else:
            type_ = False
        nodes[i] = {}
        nodes[i]['index'] = i
        nodes[i]['timer'] = timer[i]
        nodes[i]['need'] = need[i]
        nodes[i]['type'] = type_
        nodes[i]['cnt'] = 0
    return nodes

if __name__ == '__main__':
    r, p = [], []
    r_u, p_u = [] , []
    num = range(1,32,2)
    # num = [16]
    for i in num:
        len_n = i
        k, k_u, q, q_u = 0, 0 ,0 ,0
        for j in range(10):
            nodes = initialNodes(len_n)
            # print len(nodes)
            r_cnt, r_urgent = randomWaitScheme(nodes, len_n)
            k += r_cnt
            k_u += r_urgent
            p_cnt, p_urgent = priorityScheme(nodes, len_n)
            q += p_cnt
            q_u += p_urgent
        r.append(k/10)
        r_u.append(k_u/10)
        p.append(q/10)
        p_u.append(q_u/10)

    plt.figure(1)
    plt.plot(num, r, 'r-o', label='CSMA/CA')
    plt.plot(num, p, 'b-o', label='P-CSMA/CA')
    plt.xlabel('Number of nodes')
    plt.ylabel('Time counter')
    plt.title('Over all time consme betwee CSMA/CA and P-CSMA/CA')
    plt.legend(loc='upper left')
    plt.grid()
    plt.show()

    plt.figure(2)
    plt.plot(num, r_u, 'r-o', label='CSMA/CA urgent node waiting time')
    plt.plot(num, p_u, 'b-o', label='P-CSMA/CA urgent node waiting time')
    plt.title('Over all urgent nodes waiting time betwee CSMA/CA and P-CSMA/CA')
    plt.xlabel('Number of nodes')
    plt.ylabel('Time counter')
    plt.legend(loc='upper left')
    plt.grid()
    plt.show()
