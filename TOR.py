import copy

from simulation.OCS import *
from simulation.EPS import *
from simulation.QoSBaseFlow import *

'''
对数据流队列分类
HBanAndHLat 高带宽高时延
LBanAndLLat 低带宽低时延
HBanAndLLat 高带宽低时延
LBanAndHLat 低带宽高时延
'''
def FlowClassify(currentFlowList):
    HBanAndHLat, LBanAndLLat, HBanAndLLat, LBanAndHLat = {}, {}, {}, {}
    a, b, c , d = 0, 0, 0, 0
    for i in range(len(currentFlowList)):
        if currentFlowList[i].type == 1:
            if currentFlowList[i].dataSize <= 100:
                LBanAndHLat[a] = currentFlowList[i]
                a += 1
            else:
                HBanAndHLat[b] = currentFlowList[i]
                b += 1
        else:
            if currentFlowList[i].dataSize <= 100:
                LBanAndLLat[c] = currentFlowList[i]
                c += 1
            else:
                HBanAndLLat[d] = currentFlowList[i]
                d += 1
    # for i in range(len(LBanAndHLat)):
    #     printFlow(LBanAndHLat[i])
    return HBanAndHLat, LBanAndLLat, HBanAndLLat, LBanAndHLat

'''
对单个的数据流进行分类
高带宽高时延 1
低带宽低时延 4
高带宽低时延 2
低带宽高时延 3
'''
def Classify(flow):
    if flow.type == 1:
        if flow.dataSize > 100:
            return 1
        else:
            return 3
    else:
        if flow.dataSize > 100:
            return 2
        else:
            return 4

# 数据流转发
def FlowForward(flowList, r):
    flowList = SortQueue(flowList)
    currentFlowList = {}
    index = 0
    for i in range(r - 1):
        # for a in range(len(ocs1)):
        #     print(ocs1[a])
        #     print(ocs2[a])
        for time in range(r - 1):
            ocs1, ocs2 = FindConnMatrix(time, r)
            for j in range(r):
                # currentFlowList1 = SortQueue(FindFlowMatrix(ocs1[j][0], ocs1[j][1], r, i, flowList))
                # currentFlowList2 = SortQueue(FindFlowMatrix(ocs2[j][0], ocs2[j][1], r, i, flowList))
                # for k in range(len(currentFlowList1)):
                #     printFlow(currentFlowList1[k])
                # printFlow(currentFlowList2[0])
                for k in range(len(flowList)):
                    if flowList[k].timeStamp == i and flowList[k].src == ocs1[j][0] and flowList[k].dst == ocs1[j][1]:
                        currentFlowList[index] = flowList[k]
                        index += 1
                        # printFlow(flowList[k])
                    # if flowList[k].timeStamp == i and flowList[k].src == ocs2[j][1] and flowList[k].dst == ocs2[j][0]:
                        # printFlow(flowList[k])
                        # l += 1
        # HBanAndHLat1, LBanAndLLat1, HBanAndLLat1, LBanAndHLat1 = FlowClassify(currentFlowList1)
        # HBanAndHLat2, LBanAndLLat2, HBanAndLLat2, LBanAndHLat2 = FlowClassify(currentFlowList2)
    return currentFlowList

# 更新流量矩阵
def UpdateFlowMatrix():
    return True

# 最基本的光电混合数据中心数据流转发
def baseFlowForward(flowList1, r, ocsAblity, epsAblity):
    flowList_c = flowList1[:]
    f = set()
    for i in range(len(flowList_c)):
        f.add(flowList_c[i])
    num = 0
    for k in range(len(flowList_c)):
        if flowList_c[k].src == flowList_c[k].dst:
            num += 1
    print(num)
    for i in range(r - 1):
        ocsPort0, ocsPort1, ocsPort2, ocsPort3, ocsPort4 = ocsAblity, ocsAblity, ocsAblity, ocsAblity, ocsAblity
        ocsPort00, ocsPort11, ocsPort22, ocsPort33, ocsPort44 = ocsAblity, ocsAblity, ocsAblity, ocsAblity, ocsAblity
        dealFlowList = {}
        index = 0
        for k in f:
            if k.timeStamp == i:
                if k.src != k.dst:
                    dealFlowList[index] = k
                    index += 1
        dealFlowList = FlowForward(SortQueue(dealFlowList), r)
        ocs1, ocs2 = FindConnMatrix(i, r)
        for k in range(len(dealFlowList)):
            if dealFlowList[k].src == ocs1[0][0] and dealFlowList[k].dst == ocs1[0][1]:
                if ocsPort0 - dealFlowList[k].dataSize >= 0:
                    ocsPort0 -= dealFlowList[k].dataSize
                    f.remove(dealFlowList[k])
                    dealFlowList[k].src = dealFlowList[k].dst
                    f.add(dealFlowList[k])
                else:
                    dealFlowList[k].timeStamp = i + 1
                    dealFlowList[k].priority -= 1
                    dealFlowList[k].delay += 1
            elif dealFlowList[k].src == ocs1[1][0] and dealFlowList[k].dst == ocs1[1][1]:
                if ocsPort1 - dealFlowList[k].dataSize >= 0:
                    ocsPort1 -= dealFlowList[k].dataSize
                    f.remove(dealFlowList[k])
                    dealFlowList[k].src = dealFlowList[k].dst
                    f.add(dealFlowList[k])
                else:
                    dealFlowList[k].timeStamp = i + 1
                    dealFlowList[k].priority -= 1
                    dealFlowList[k].delay += 1
            elif dealFlowList[k].src == ocs1[2][0] and dealFlowList[k].dst == ocs1[2][1]:
                if ocsPort2 - dealFlowList[k].dataSize >= 0:
                    ocsPort2 -= dealFlowList[k].dataSize
                    f.remove(dealFlowList[k])
                    dealFlowList[k].src = dealFlowList[k].dst
                    f.add(dealFlowList[k])
                else:
                    dealFlowList[k].timeStamp = i + 1
                    dealFlowList[k].priority -= 1
                    dealFlowList[k].delay += 1
            elif dealFlowList[k].src == ocs1[3][0] and dealFlowList[k].dst == ocs1[3][1]:
                if ocsPort3 - dealFlowList[k].dataSize >= 0:
                    ocsPort3 -= dealFlowList[k].dataSize
                    f.remove(dealFlowList[k])
                    dealFlowList[k].src = dealFlowList[k].dst
                    f.add(dealFlowList[k])
                else:
                    dealFlowList[k].timeStamp = i + 1
                    dealFlowList[k].priority -= 1
                    dealFlowList[k].delay += 1
            elif dealFlowList[k].src == ocs1[4][0] and dealFlowList[k].dst == ocs1[4][1]:
                if ocsPort4 - dealFlowList[k].dataSize >= 0:
                    ocsPort4 -= dealFlowList[k].dataSize
                    f.remove(dealFlowList[k])
                    dealFlowList[k].src = dealFlowList[k].dst
                    f.add(dealFlowList[k])
                else:
                    dealFlowList[k].timeStamp = i + 1
                    dealFlowList[k].priority -= 1
                    dealFlowList[k].delay += 1
            elif dealFlowList[k].src == ocs2[0][0] and dealFlowList[k].dst == ocs2[0][1]:
                if ocsPort00 - dealFlowList[k].dataSize >= 0:
                    ocsPort00 -= dealFlowList[k].dataSize
                    f.remove(dealFlowList[k])
                    dealFlowList[k].src = dealFlowList[k].dst
                    f.add(dealFlowList[k])
                else:
                    dealFlowList[k].timeStamp = i + 1
                    dealFlowList[k].priority -= 1
                    dealFlowList[k].delay += 1
            elif dealFlowList[k].src == ocs2[1][0] and dealFlowList[k].dst == ocs2[1][1]:
                if ocsPort11 - dealFlowList[k].dataSize >= 0:
                    ocsPort11 -= dealFlowList[k].dataSize
                    f.remove(dealFlowList[k])
                    dealFlowList[k].src = dealFlowList[k].dst
                    f.add(dealFlowList[k])
                else:
                    dealFlowList[k].timeStamp = i + 1
                    dealFlowList[k].priority -= 1
                    dealFlowList[k].delay += 1
            elif dealFlowList[k].src == ocs2[2][0] and dealFlowList[k].dst == ocs2[2][1]:
                if ocsPort22 - dealFlowList[k].dataSize >= 0:
                    ocsPort22 -= dealFlowList[k].dataSize
                    f.remove(dealFlowList[k])
                    dealFlowList[k].src = dealFlowList[k].dst
                    f.add(dealFlowList[k])
                else:
                    dealFlowList[k].timeStamp = i + 1
                    dealFlowList[k].priority -= 1
                    dealFlowList[k].delay += 1
            elif dealFlowList[k].src == ocs2[3][0] and dealFlowList[k].dst == ocs2[3][1]:
                if ocsPort33 - dealFlowList[k].dataSize >= 0:
                    ocsPort33 -= dealFlowList[k].dataSize
                    f.remove(dealFlowList[k])
                    dealFlowList[k].src = dealFlowList[k].dst
                    f.add(dealFlowList[k])
                else:
                    dealFlowList[k].timeStamp = i + 1
                    dealFlowList[k].priority -= 1
                    dealFlowList[k].delay += 1
            elif dealFlowList[k].src == ocs2[4][0] and dealFlowList[k].dst == ocs2[4][1]:
                if ocsPort44 - dealFlowList[k].dataSize >= 0:
                    ocsPort44 -= dealFlowList[k].dataSize
                    f.remove(dealFlowList[k])
                    dealFlowList[k].src = dealFlowList[k].dst
                    f.add(dealFlowList[k])
                else:
                    dealFlowList[k].timeStamp = i + 1
                    dealFlowList[k].priority -= 1
                    dealFlowList[k].delay += 1
            else:
                if epsAblity - dealFlowList[k].dataSize >= 0:
                    epsAblity -= dealFlowList[k].dataSize
                    f.remove(dealFlowList[k])
                    dealFlowList[k].src = dealFlowList[k].dst
                    f.add(dealFlowList[k])
                else:
                    dealFlowList[k].timeStamp = i + 1
                    dealFlowList[k].priority -= 1
                    dealFlowList[k].delay += 1
        print(epsAblity, ocsPort0, ocsPort1, ocsPort2, ocsPort3, ocsPort4)
        print(epsAblity, ocsPort00, ocsPort11, ocsPort22, ocsPort33, ocsPort4)
    flowList_copy = {}
    index = 0
    for k in f:
        flowList_copy[index] = k
        index += 1
    return flowList_copy

# 第一个方案
def firstPlan(flowList, r, ocsAblity, epsAblity):
    f = set()
    for i in range(len(flowList)):
        f.add(flowList[i])
    num = 0
    for k in range(len(flowList)):
        if flowList[k].src == flowList[k].dst:
            num += 1
    print(num)
    for i in range(r - 1):
        ocsPort0, ocsPort1, ocsPort2, ocsPort3, ocsPort4 = ocsAblity, ocsAblity, ocsAblity, ocsAblity, ocsAblity
        ocsPort00, ocsPort11, ocsPort22, ocsPort33, ocsPort44 = ocsAblity, ocsAblity, ocsAblity, ocsAblity, ocsAblity
        dealFlowList = {}
        index = 0
        for k in f:
            if k.timeStamp == i:
                if k.src != k.dst:
                    dealFlowList[index] = k
                    index += 1
        dealFlowList = FlowForward(SortQueue(dealFlowList), r)
        ocs1, ocs2 = FindConnMatrix(i, r)
        for k in range(len(dealFlowList)):
            if dealFlowList[k].type == 0:
                if dealFlowList[k].src == ocs1[0][0] and dealFlowList[k].dst == ocs1[0][1]:
                    if ocsPort0 - dealFlowList[k].dataSize >= 0:
                        ocsPort0 -= dealFlowList[k].dataSize
                        f.remove(dealFlowList[k])
                        dealFlowList[k].src = dealFlowList[k].dst
                        f.add(dealFlowList[k])
                    else:
                        dealFlowList[k].timeStamp = i + 1
                        dealFlowList[k].priority -= 1
                        dealFlowList[k].delay += 1
                elif dealFlowList[k].src == ocs1[1][0] and dealFlowList[k].dst == ocs1[1][1]:
                    if ocsPort1 - dealFlowList[k].dataSize >= 0:
                        ocsPort1 -= dealFlowList[k].dataSize
                        f.remove(dealFlowList[k])
                        dealFlowList[k].src = dealFlowList[k].dst
                        f.add(dealFlowList[k])
                    else:
                        dealFlowList[k].timeStamp = i + 1
                        dealFlowList[k].priority -= 1
                        dealFlowList[k].delay += 1
                elif dealFlowList[k].src == ocs1[2][0] and dealFlowList[k].dst == ocs1[2][1]:
                    if ocsPort2 - dealFlowList[k].dataSize >= 0:
                        ocsPort2 -= dealFlowList[k].dataSize
                        f.remove(dealFlowList[k])
                        dealFlowList[k].src = dealFlowList[k].dst
                        f.add(dealFlowList[k])
                    else:
                        dealFlowList[k].timeStamp = i + 1
                        dealFlowList[k].priority -= 1
                        dealFlowList[k].delay += 1
                elif dealFlowList[k].src == ocs1[3][0] and dealFlowList[k].dst == ocs1[3][1]:
                    if ocsPort3 - dealFlowList[k].dataSize >= 0:
                        ocsPort3 -= dealFlowList[k].dataSize
                        f.remove(dealFlowList[k])
                        dealFlowList[k].src = dealFlowList[k].dst
                        f.add(dealFlowList[k])
                    else:
                        dealFlowList[k].timeStamp = i + 1
                        dealFlowList[k].priority -= 1
                        dealFlowList[k].delay += 1
                elif dealFlowList[k].src == ocs1[4][0] and dealFlowList[k].dst == ocs1[4][1]:
                    if ocsPort4 - dealFlowList[k].dataSize >= 0:
                        ocsPort4 -= dealFlowList[k].dataSize
                        f.remove(dealFlowList[k])
                        dealFlowList[k].src = dealFlowList[k].dst
                        f.add(dealFlowList[k])
                    else:
                        dealFlowList[k].timeStamp = i + 1
                        dealFlowList[k].priority -= 1
                        dealFlowList[k].delay += 1
                elif dealFlowList[k].src == ocs2[0][0] and dealFlowList[k].dst == ocs2[0][1]:
                    if ocsPort00 - dealFlowList[k].dataSize >= 0:
                        ocsPort00 -= dealFlowList[k].dataSize
                        f.remove(dealFlowList[k])
                        dealFlowList[k].src = dealFlowList[k].dst
                        f.add(dealFlowList[k])
                    else:
                        dealFlowList[k].timeStamp = i + 1
                        dealFlowList[k].priority -= 1
                        dealFlowList[k].delay += 1
                elif dealFlowList[k].src == ocs2[1][0] and dealFlowList[k].dst == ocs2[1][1]:
                    if ocsPort11 - dealFlowList[k].dataSize >= 0:
                        ocsPort11 -= dealFlowList[k].dataSize
                        f.remove(dealFlowList[k])
                        dealFlowList[k].src = dealFlowList[k].dst
                        f.add(dealFlowList[k])
                    else:
                        dealFlowList[k].timeStamp = i + 1
                        dealFlowList[k].priority -= 1
                        dealFlowList[k].delay += 1
                elif dealFlowList[k].src == ocs2[2][0] and dealFlowList[k].dst == ocs2[2][1]:
                    if ocsPort22 - dealFlowList[k].dataSize >= 0:
                        ocsPort22 -= dealFlowList[k].dataSize
                        f.remove(dealFlowList[k])
                        dealFlowList[k].src = dealFlowList[k].dst
                        f.add(dealFlowList[k])
                    else:
                        dealFlowList[k].timeStamp = i + 1
                        dealFlowList[k].priority -= 1
                        dealFlowList[k].delay += 1
                elif dealFlowList[k].src == ocs2[3][0] and dealFlowList[k].dst == ocs2[3][1]:
                    if ocsPort33 - dealFlowList[k].dataSize >= 0:
                        ocsPort33 -= dealFlowList[k].dataSize
                        f.remove(dealFlowList[k])
                        dealFlowList[k].src = dealFlowList[k].dst
                        f.add(dealFlowList[k])
                    else:
                        dealFlowList[k].timeStamp = i + 1
                        dealFlowList[k].priority -= 1
                        dealFlowList[k].delay += 1
                elif dealFlowList[k].src == ocs2[4][0] and dealFlowList[k].dst == ocs2[4][1]:
                    if ocsPort44 - dealFlowList[k].dataSize >= 0:
                        ocsPort44 -= dealFlowList[k].dataSize
                        f.remove(dealFlowList[k])
                        dealFlowList[k].src = dealFlowList[k].dst
                        f.add(dealFlowList[k])
                    else:
                        dealFlowList[k].timeStamp = i + 1
                        dealFlowList[k].priority -= 1
                        dealFlowList[k].delay += 1
                else:
                    if epsAblity - dealFlowList[k].dataSize >= 0:
                        epsAblity -= dealFlowList[k].dataSize
                        f.remove(dealFlowList[k])
                        dealFlowList[k].src = dealFlowList[k].dst
                        f.add(dealFlowList[k])
                    else:
                        dealFlowList[k].timeStamp = i + 1
                        dealFlowList[k].priority -= 1
                        dealFlowList[k].delay += 1
            else:
                if dealFlowList[k].dataSize > 100:
                    if dealFlowList[k].src == ocs1[0][0] and dealFlowList[k].dst == ocs1[0][1]:
                        if ocsPort0 - dealFlowList[k].dataSize >= 0:
                            ocsPort0 -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                    elif dealFlowList[k].src == ocs1[1][0] and dealFlowList[k].dst == ocs1[1][1]:
                        if ocsPort1 - dealFlowList[k].dataSize >= 0:
                            ocsPort1 -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                    elif dealFlowList[k].src == ocs1[2][0] and dealFlowList[k].dst == ocs1[2][1]:
                        if ocsPort2 - dealFlowList[k].dataSize >= 0:
                            ocsPort2 -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                    elif dealFlowList[k].src == ocs1[3][0] and dealFlowList[k].dst == ocs1[3][1]:
                        if ocsPort3 - dealFlowList[k].dataSize >= 0:
                            ocsPort3 -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                    elif dealFlowList[k].src == ocs1[4][0] and dealFlowList[k].dst == ocs1[4][1]:
                        if ocsPort4 - dealFlowList[k].dataSize >= 0:
                            ocsPort4 -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                    elif dealFlowList[k].src == ocs2[0][0] and dealFlowList[k].dst == ocs2[0][1]:
                        if ocsPort00 - dealFlowList[k].dataSize >= 0:
                            ocsPort00 -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                    elif dealFlowList[k].src == ocs2[1][0] and dealFlowList[k].dst == ocs2[1][1]:
                        if ocsPort11 - dealFlowList[k].dataSize >= 0:
                            ocsPort11 -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                    elif dealFlowList[k].src == ocs2[2][0] and dealFlowList[k].dst == ocs2[2][1]:
                        if ocsPort22 - dealFlowList[k].dataSize >= 0:
                            ocsPort22 -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                    elif dealFlowList[k].src == ocs2[3][0] and dealFlowList[k].dst == ocs2[3][1]:
                        if ocsPort33 - dealFlowList[k].dataSize >= 0:
                            ocsPort33 -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                    elif dealFlowList[k].src == ocs2[4][0] and dealFlowList[k].dst == ocs2[4][1]:
                        if ocsPort44 - dealFlowList[k].dataSize >= 0:
                            ocsPort44 -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                    else:
                        dealFlowList[k].timeStamp = i + 1
                        dealFlowList[k].priority -= 1
                        dealFlowList[k].delay += 1
                else:
                    if dealFlowList[k].src == ocs1[0][0] and dealFlowList[k].dst == ocs1[0][1]:
                        if ocsPort0 - dealFlowList[k].dataSize >= 0:
                            ocsPort0 -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                    elif dealFlowList[k].src == ocs1[1][0] and dealFlowList[k].dst == ocs1[1][1]:
                        if ocsPort1 - dealFlowList[k].dataSize >= 0:
                            ocsPort1 -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                    elif dealFlowList[k].src == ocs1[2][0] and dealFlowList[k].dst == ocs1[2][1]:
                        if ocsPort2 - dealFlowList[k].dataSize >= 0:
                            ocsPort2 -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                    elif dealFlowList[k].src == ocs1[3][0] and dealFlowList[k].dst == ocs1[3][1]:
                        if ocsPort3 - dealFlowList[k].dataSize >= 0:
                            ocsPort3 -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                    elif dealFlowList[k].src == ocs1[4][0] and dealFlowList[k].dst == ocs1[4][1]:
                        if ocsPort4 - dealFlowList[k].dataSize >= 0:
                            ocsPort4 -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                    elif dealFlowList[k].src == ocs2[0][0] and dealFlowList[k].dst == ocs2[0][1]:
                        if ocsPort00 - dealFlowList[k].dataSize >= 0:
                            ocsPort00 -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                    elif dealFlowList[k].src == ocs2[1][0] and dealFlowList[k].dst == ocs2[1][1]:
                        if ocsPort11 - dealFlowList[k].dataSize >= 0:
                            ocsPort11 -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                    elif dealFlowList[k].src == ocs2[2][0] and dealFlowList[k].dst == ocs2[2][1]:
                        if ocsPort22 - dealFlowList[k].dataSize >= 0:
                            ocsPort22 -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                    elif dealFlowList[k].src == ocs2[3][0] and dealFlowList[k].dst == ocs2[3][1]:
                        if ocsPort33 - dealFlowList[k].dataSize >= 0:
                            ocsPort33 -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                    elif dealFlowList[k].src == ocs2[4][0] and dealFlowList[k].dst == ocs2[4][1]:
                        if ocsPort44 - dealFlowList[k].dataSize >= 0:
                            ocsPort44 -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                    else:
                        if epsAblity - dealFlowList[k].dataSize >= 0:
                            epsAblity -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
        print(epsAblity, ocsPort0, ocsPort1, ocsPort2, ocsPort3, ocsPort4)
        print(epsAblity, ocsPort00, ocsPort11, ocsPort22, ocsPort33, ocsPort4)
    flowList_copy = {}
    index = 0
    for k in f:
        flowList_copy[index] = k
        index += 1
    return flowList_copy


# 仿真参数：数据流个数N = 10000 TOR个数 r = 5 EPS = 4 OCS = 2
# 千兆电，万兆光
if __name__ == '__main__':
    N = 100000
    r = 5
    cycle = 10
    eps = 10000
    ocs = 10000
    ocsAblity = ocs * cycle
    epsAblity = eps * cycle * 20
    List = CreateFlowList(N, r)
    flowList = []
    for k in range(len(List)):
        flowList.append(List[k])
    # FlowForward(flowList, r)
    List1 = copy.deepcopy(flowList)
    num = 0
    total = 0
    num1 = 0
    total1 = 0
    base = baseFlowForward(flowList, r, ocsAblity, epsAblity)
    for k in range(len(base)):
        if base[k].src == base[k].dst:
            num += 1
    for k in range(len(base)):
        if base[k].timeStamp == 4:
            # if base[k].type == 0:
            #     num += 1
            if base[k].delayTolerance < base[k].delay * cycle:
                if base[k].delayTolerance < base[k].delay * cycle:
                    total += base[k].dataSize * base[k].delay * cycle
    print(num)
    print(total)

    plan1 = firstPlan(List1, r, ocsAblity, epsAblity)
    for k in range(len(plan1)):
        if plan1[k].src == plan1[k].dst:
            num1 += 1
    for k in range(len(plan1)):
        if plan1[k].timeStamp == 4:
            # if plan1[k].type == 0:
            #     num1 += 1
            if plan1[k].delayTolerance < plan1[k].delay * cycle:
                if plan1[k].delayTolerance < plan1[k].delay * cycle:
                    total1 += plan1[k].dataSize * plan1[k].delay * cycle
    print(num1)
    print(total1)
    print(num1 - num)
    print(total - total1)