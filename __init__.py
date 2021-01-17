from simulation.QoSBaseFlow import CreateFlowList, printFlow, SortQueue
from simulation.TOR import FlowForward, FindConnMatrix, Classify, baseFlowForward

if __name__ == '__main__':
    print("光电混合数据中心仿真系统开始运行…………")
    N = 10000
    r = 5
    cycle = 5
    eps = 10000
    ocs = 10000
    ocsAblity = ocs * cycle
    epsAblity = eps * cycle * 15
    num3 = 0
    num4 = 0
    flowList = CreateFlowList(N, r)
    flowList1 = {}
    for k in range(len(flowList)):
        flowList1[k] = flowList[k]
    for k in range(len(flowList)):
        if flowList[k].src == flowList[k].dst:
            num3 += 1
    print(num3)
    f = set()
    for i in range(len(flowList)):
        f.add(flowList[i])
    # for k in f:
    #     printFlow(k)
    # print(type(f))
    # for k in f.copy():
    #     # m = set()
    #     if k.timeStamp == 1:
    #         # m.add(k)
    #         f.remove(k)
    # for k in f:
    #     printFlow(k)
    middleFlowList = {}
    num = 0
    # FlowForward(flowList, r)
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
        # print(len(dealFlowList))
        ocs,ocs1 = FindConnMatrix(i, r)
        for k in range(len(dealFlowList)):
            if dealFlowList[k].type == 0:
                if dealFlowList[k].dataSize > 100:
                    if dealFlowList[k].src == ocs[0][0] and dealFlowList[k].dst == ocs[0][1]:
                        if ocsPort0 - dealFlowList[k].dataSize >= 0:
                            ocsPort0 -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                    elif dealFlowList[k].src == ocs[1][0] and dealFlowList[k].dst == ocs[1][1]:
                        if ocsPort1 - dealFlowList[k].dataSize >= 0:
                            ocsPort1 -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                    elif dealFlowList[k].src == ocs[2][0] and dealFlowList[k].dst == ocs[2][1]:
                        if ocsPort2 - dealFlowList[k].dataSize >= 0:
                            ocsPort2 -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                    elif dealFlowList[k].src == ocs[3][0] and dealFlowList[k].dst == ocs[3][1]:
                        if ocsPort3 - dealFlowList[k].dataSize >= 0:
                            ocsPort3 -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                    elif dealFlowList[k].src == ocs[4][0] and dealFlowList[k].dst == ocs[4][1]:
                        if ocsPort4 - dealFlowList[k].dataSize >= 0:
                            ocsPort4 -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                    elif dealFlowList[k].src == ocs1[0][0] and dealFlowList[k].dst == ocs1[0][1]:
                        if ocsPort00 - dealFlowList[k].dataSize >= 0:
                            ocsPort00 -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                    elif dealFlowList[k].src == ocs1[1][0] and dealFlowList[k].dst == ocs1[1][1]:
                        if ocsPort11 - dealFlowList[k].dataSize >= 0:
                            ocsPort11 -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                    elif dealFlowList[k].src == ocs1[2][0] and dealFlowList[k].dst == ocs1[2][1]:
                        if ocsPort22 - dealFlowList[k].dataSize >= 0:
                            ocsPort22 -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                    elif dealFlowList[k].src == ocs1[3][0] and dealFlowList[k].dst == ocs1[3][1]:
                        if ocsPort33 - dealFlowList[k].dataSize >= 0:
                            ocsPort33 -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                    elif dealFlowList[k].src == ocs1[4][0] and dealFlowList[k].dst == ocs1[4][1]:
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
                            epsAblity  -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                else:
                    if dealFlowList[k].src == ocs[0][0] and dealFlowList[k].dst == ocs[0][1]:
                        if ocsPort0 - dealFlowList[k].dataSize >= 0:
                            ocsPort0 -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                    elif dealFlowList[k].src == ocs[1][0] and dealFlowList[k].dst == ocs[1][1]:
                        if ocsPort1 - dealFlowList[k].dataSize >= 0:
                            ocsPort1 -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                    elif dealFlowList[k].src == ocs[2][0] and dealFlowList[k].dst == ocs[2][1]:
                        if ocsPort2 - dealFlowList[k].dataSize >= 0:
                            ocsPort2 -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                    elif dealFlowList[k].src == ocs[3][0] and dealFlowList[k].dst == ocs[3][1]:
                        if ocsPort3 - dealFlowList[k].dataSize >= 0:
                            ocsPort3 -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                    elif dealFlowList[k].src == ocs[4][0] and dealFlowList[k].dst == ocs[4][1]:
                        if ocsPort4 - dealFlowList[k].dataSize >= 0:
                            ocsPort4 -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                    elif dealFlowList[k].src == ocs1[0][0] and dealFlowList[k].dst == ocs1[0][1]:
                        if ocsPort00 - dealFlowList[k].dataSize >= 0:
                            ocsPort00 -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                    elif dealFlowList[k].src == ocs1[1][0] and dealFlowList[k].dst == ocs1[1][1]:
                        if ocsPort11 - dealFlowList[k].dataSize >= 0:
                            ocsPort11 -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                    elif dealFlowList[k].src == ocs1[2][0] and dealFlowList[k].dst == ocs1[2][1]:
                        if ocsPort22 - dealFlowList[k].dataSize >= 0:
                            ocsPort22 -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                    elif dealFlowList[k].src == ocs1[3][0] and dealFlowList[k].dst == ocs1[3][1]:
                        if ocsPort33 - dealFlowList[k].dataSize >= 0:
                            ocsPort33 -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                    elif dealFlowList[k].src == ocs1[4][0] and dealFlowList[k].dst == ocs1[4][1]:
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
                    if dealFlowList[k].src == ocs[0][0] and dealFlowList[k].dst == ocs[0][1]:
                        if ocsPort0 - dealFlowList[k].dataSize >= 0:
                            ocsPort0 -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                    elif dealFlowList[k].src == ocs[1][0] and dealFlowList[k].dst == ocs[1][1]:
                        if ocsPort1 - dealFlowList[k].dataSize >= 0:
                            ocsPort1 -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                    elif dealFlowList[k].src == ocs[2][0] and dealFlowList[k].dst == ocs[2][1]:
                        if ocsPort2 - dealFlowList[k].dataSize >= 0:
                            ocsPort2 -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                    elif dealFlowList[k].src == ocs[3][0] and dealFlowList[k].dst == ocs[3][1]:
                        if ocsPort3 - dealFlowList[k].dataSize >= 0:
                            ocsPort3 -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                    elif dealFlowList[k].src == ocs[4][0] and dealFlowList[k].dst == ocs[4][1]:
                        if ocsPort4 - dealFlowList[k].dataSize >= 0:
                            ocsPort4 -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                    elif dealFlowList[k].src == ocs1[0][0] and dealFlowList[k].dst == ocs1[0][1]:
                        if ocsPort00 - dealFlowList[k].dataSize >= 0:
                            ocsPort00 -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                    elif dealFlowList[k].src == ocs1[1][0] and dealFlowList[k].dst == ocs1[1][1]:
                        if ocsPort11 - dealFlowList[k].dataSize >= 0:
                            ocsPort11 -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                    elif dealFlowList[k].src == ocs1[2][0] and dealFlowList[k].dst == ocs1[2][1]:
                        if ocsPort22 - dealFlowList[k].dataSize >= 0:
                            ocsPort22 -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                    elif dealFlowList[k].src == ocs1[3][0] and dealFlowList[k].dst == ocs1[3][1]:
                        if ocsPort33 - dealFlowList[k].dataSize >= 0:
                            ocsPort33 -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                    elif dealFlowList[k].src == ocs1[4][0] and dealFlowList[k].dst == ocs1[4][1]:
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
                    if dealFlowList[k].src == ocs[0][0] and dealFlowList[k].dst == ocs[0][1]:
                        if ocsPort0 - dealFlowList[k].dataSize >= 0:
                            ocsPort0 -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                    elif dealFlowList[k].src == ocs[1][0] and dealFlowList[k].dst == ocs[1][1]:
                        if ocsPort1 - dealFlowList[k].dataSize >= 0:
                            ocsPort1 -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                    elif dealFlowList[k].src == ocs[2][0] and dealFlowList[k].dst == ocs[2][1]:
                        if ocsPort2 - dealFlowList[k].dataSize >= 0:
                            ocsPort2 -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                    elif dealFlowList[k].src == ocs[3][0] and dealFlowList[k].dst == ocs[3][1]:
                        if ocsPort3 - dealFlowList[k].dataSize >= 0:
                            ocsPort3 -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                    elif dealFlowList[k].src == ocs[4][0] and dealFlowList[k].dst == ocs[4][1]:
                        if ocsPort4 - dealFlowList[k].dataSize >= 0:
                            ocsPort4 -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                    elif dealFlowList[k].src == ocs1[0][0] and dealFlowList[k].dst == ocs1[0][1]:
                        if ocsPort00 - dealFlowList[k].dataSize >= 0:
                            ocsPort00 -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                    elif dealFlowList[k].src == ocs1[1][0] and dealFlowList[k].dst == ocs1[1][1]:
                        if ocsPort11 - dealFlowList[k].dataSize >= 0:
                            ocsPort11 -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                    elif dealFlowList[k].src == ocs1[2][0] and dealFlowList[k].dst == ocs1[2][1]:
                        if ocsPort22 - dealFlowList[k].dataSize >= 0:
                            ocsPort22 -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                    elif dealFlowList[k].src == ocs1[3][0] and dealFlowList[k].dst == ocs1[3][1]:
                        if ocsPort33 - dealFlowList[k].dataSize >= 0:
                            ocsPort33 -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1
                    elif dealFlowList[k].src == ocs1[4][0] and dealFlowList[k].dst == ocs1[4][1]:
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
                            epsAblity  -= dealFlowList[k].dataSize
                            f.remove(dealFlowList[k])
                            dealFlowList[k].src = dealFlowList[k].dst
                            f.add(dealFlowList[k])
                        else:
                            dealFlowList[k].timeStamp = i + 1
                            dealFlowList[k].priority -= 1
                            dealFlowList[k].delay += 1

        print(epsAblity,ocsPort2,ocsPort3,ocsPort1,ocsPort0,ocsPort4)
    # for k in range(len(middleFlowList)):
    #     printFlow(middleFlowList[k])
    # for k in f:
    #     printFlow(k)
    nummmm = {}
    numm = 0
    for k in f:
        nummmm[numm] = k
        numm += 1
    # nummmm = FlowForward(SortQueue(nummmm), r + 1)
    num5 = 0
    total = 0
    for i in range(len(nummmm)):
        # printFlow(nummmm[i])
        if nummmm[i].src == nummmm[i].dst:
            num4 += 1
        if nummmm[i].timeStamp == 4:
            if nummmm[i].delayTolerance < nummmm[i].delay * cycle:
                total += nummmm[i].dataSize
            num5 += 1
        # printFlow
    print(num4)
    print(num5)
    print(total)
    print(len(nummmm))

    flowList11 = CreateFlowList(N, r)
    total1 = 0
    ff = {}
    ff =  baseFlowForward(flowList11, r, ocsAblity, epsAblity)
    for k in range(len(ff)):
        if ff[k].timeStamp == 4:
            if ff[k].delayTolerance < ff[k].delay * cycle:
                total1 += ff[k].dataSize
    print(total1)
