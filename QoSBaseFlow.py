import random
import numpy as np
import datetime
import time

'''
定义数据流结构
    时间戳timeStamp 生成数据流时的时间
    源地址src 用TOR的标号表示
    目的地址dst 用TOR的标号表示
    时延敏感流最长时延忍耐delayTolerance [0, 5]之间随机生成整数 单位ms
    优先级priority 随机生成整数 数值越小优先级越高
    类型type 代表数据流的类型，进行QoS分类时所得，0代表时延敏感数据流，1代表时延不敏感数据流
    数据大小dataSize 数据流个大小，依据二八定律随机生成大象流和老鼠流 单位M
    延迟叠加delay 表示滞留的周期数，最后乘周期得到延迟时间,初始值都为0 
'''
class Flow:
    def __init__(self):
        self.timeStamp = int
        self.src = int
        self.dst = int
        self.delayTolerance = int
        self.priority = int
        self.type = int
        self.dataSize = float
        self.delay = int

# 生成数据流，r：TOR数量
def CreatFlow(flow, r):
    # flow.timeStamp = time.mktime(datetime.datetime.now().timetuple())
    flow.timeStamp = random.randint(0, r - 2)
    flow.src = random.randint(0, r-1)
    flow.dst = random.randint(0, r-1)
    flow.priority = 4
    # if random.random() < 0.3:
    #     flow.type = 1
    # else:
    #     flow.type = 0
    flow.type = random.randint(0, 1)
    flow.delay = 0
    if flow.type == 0:
        flow.delayTolerance = random.randint(0, 5)
    else:
        flow.delayTolerance = 20
    P = random.random()
    if P < 0.8:
        flow.dataSize = round(random.uniform(0, 100), 3)
    else:
        flow.dataSize = round(random.uniform(100, 10000), 3)
    return flow

# 打印每一条数据流参数
def printFlow(flow):
    print("{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}\t\t{}".format(flow.timeStamp,flow.src, flow.dst, flow.delayTolerance, flow.priority, flow.type, flow.delay, flow.dataSize))

# 生成数据流列表，数据流的个数为N
def CreateFlowList(N, r):
    flowList = {}
    for i in range(N):
        flow = Flow()
        flowList[i] = CreatFlow(flow,r)
    return flowList

# 生成数据流数量矩阵，每个元素代表源TOR到目的TOR的数据流个数
def CreatFlowMatrix(flowList, time, r):
    matrix = np.zeros([r, r], dtype=int) # 初始化一个零矩阵
    for i in range(len(flowList)):
        if flowList[i].timeStamp == time:
            if flowList[i].src != flowList[i].dst:
                matrix[flowList[i].src][flowList[i].dst] += 1
    return matrix

# 生成对应连接TOR的流量列表
def FlowMatrixList(flowList, time, r):
    flowMatrixList = {}
    for i in range(r * r):
        flowMatrixList[i] = set()
    for i in range(len(flowList)):
        # if len(FlowListMatrix[flowList[k].src][flowList[k].dst]) == 0:
        #     FlowListMatrix[flowList[k].src][flowList[k].dst] = []
        # else:
        #     FlowListMatrix[flowList[k].src][flowList[k].dst].append((flowList[k]))
        k = flowList[i].src * r + flowList[i].dst % r
        if flowList[i].timeStamp == time:
            if flowList[i].src != flowList[i].dst:
                flowMatrixList[k].add(flowList[i])
            else:
                pass
    return flowMatrixList


'''
根据OCS提供的TOR连接矩阵，查找流量矩阵
返回当前连接TOR流量队列
'''
def FindFlowMatrix(i, j, r, time, flowList):
    flowMatrixList = FlowMatrixList(flowList,time, r)
    currentFlowList = {}
    k = 0
    for flow in flowMatrixList[i * r + j]:
        currentFlowList[k] = flow
        # printFlow(TORFlowList[k])
        k += 1
    return currentFlowList

# TOR之间传输数据流列表按照优先级排序,三个优先级
def SortQueue(TORFlowList):
    priority1,priority2,priority3,priority4 = {}, {}, {}, {}
    k, m, n, l= 0, 0, 0, 0
    for i in range(len(TORFlowList)):
        if TORFlowList[i].priority == 1:
            priority1[k] = TORFlowList[i]
            k += 1
        elif TORFlowList[i].priority == 2:
            priority2[m] = TORFlowList[i]
            m += 1
        elif TORFlowList[i].priority == 3:
            priority3[n] = TORFlowList[i]
            n += 1
        else:
            priority4[l] = TORFlowList[i]
            l += 1
    for i in range(k):
        TORFlowList[i] = priority1[i]
    for i in range(m):
        TORFlowList[k + i] = priority2[i]
    for i in range(n):
        TORFlowList[k + m + i] = priority3[i]
    for i in range(l):
        TORFlowList[k + m + n + i] = priority4[i]
    return TORFlowList

# 仿真参数：数据流个数N = 10000 TOR个数 r = 5 EPS = 2 OCS = 2
if __name__ == '__main__':
    N = 10000
    r = 5
    time = 0
    flowList = CreateFlowList(N, r)
    flowListMatrix = CreatFlowMatrix(flowList, time, r)
    print(flowListMatrix)
    m,n=0,0
    print("到达时间\t源地址\t目的地址\t时延忍耐\t优先级\t类型\t滞留周期\t大小/M")
    for i in range(N):
        if flowList[i].dataSize>100:
            m += 1
        else:
            n += 1
        if i < 10:
            printFlow(flowList[i])
    print("大象流个数:{}\t老鼠流个数：{}".format(m,n))
    f = FindFlowMatrix(0,1,r,time,flowList)
    f = SortQueue(f)
    for i in range(len(f)):
        printFlow(f[i])


