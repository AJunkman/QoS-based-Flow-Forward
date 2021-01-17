import numpy as np
import time

# 定义光交换机参数
class OCSInit:
    def __init__(self,bandwidth,forwardingRate):
        self.bandwidth = bandwidth
        self.forwardingRate = forwardingRate

# 使用光交换机处理数据流队列
def OCS(flowList,OCSInit):
    rate = OCSInit.forwardingRate
    forwardTime = 0
    for i in range(len(flowList)):
        forwardTime += flowList[i].dataSize / rate
        flowList[i].src = flowList[i].dst
    return forwardTime

'''
定义光交换机的连接矩阵，周期为cycle,TOR数量为r,光交换机个数为OCS
则重配置的时间周期内可连接OCS对TOR
'''
def ConnMatrix(r):
    #while True:
    ConnMatrixList1 = {}
    ConnMatrixList2 = {}
    k = 0
    # l = 0
    for i in range(r - 1):
        matrix1 = np.zeros([r, r], dtype=int)
        matrix2 = np.zeros([r, r], dtype=int)
        for j in range(r):
            matrix1[j][(i+j+1)%r] = 1
            matrix2[(i+j+1)%r][j] = 1
        ConnMatrixList1[k] = matrix1
        ConnMatrixList2[k] = matrix2
        k += 1
            # if i < j:
            #     matrix1[i][j] = 1
            #     ConnMatrixList1[k] = matrix1
            #     k += 1
            #     continue
            # elif r - i - 1 < r - j - 1:
            #     matrix2[r - i - 1][r - j - 1] = 1
            #     ConnMatrixList2[l] = matrix2
            #     l += 1
            #     continue
            # else:
            #     continue
            # print(matrix)
            # return matrix
            # time.sleep(cycle)
    return ConnMatrixList1,ConnMatrixList2

# 查找连接矩阵，返回当前连接的TOR
def FindConnMatrix(time, r):
    con1, con2 = ConnMatrix(r)
    con1 = con1[time]
    con2 = con2[time]
    conNum1 = {}
    conNum2 = {}
    k ,l = 0, 0
    for i in range(r):
        for j in range(r):
            if con1[i][j] > 0:
                conNum1[k] = [i, j]
                k += 1
            elif con2[i][j] > 0:
                conNum2[l] = [i, j]
                l += 1
            else:
                pass
    return conNum1,conNum2



# 仿真参数：数据流个数N = 10000 TOR个数 r = 5 EPS = 2 OCS = 2 cycle = 5s 当前时间time
if __name__ == '__main__':
    time = 3
    cycle = 5
    r = 5
    OCS = 2
    conn1,conn2 = ConnMatrix(r)
    for i in range(len(conn1)):
        print(conn1[i])
        print(conn2[i])
    connNum1,connNum2 = FindConnMatrix(time%(r - 1), r)
    for i in range(len(connNum1)):
        print(connNum1[i])
        print(connNum2[i])

