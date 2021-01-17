
# 定义电交换机参数
class EPSInit:
    def __init__(self,bandwidth,forwardingRate):
        self.bandwidth = bandwidth
        self.forwardingRate = forwardingRate

# 使用电交换机处理数据流队列
def EPS(flowList,EPSInit):
    rate = EPSInit.forwardingRate
    forwardTime = 0
    for i in range(len(flowList)):
        forwardTime += flowList[i].dataSize / rate
        flowList[i].src = flowList[i].dst
    return flowList