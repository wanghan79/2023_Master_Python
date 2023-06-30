# 函数功能：产生任意数据类型的随机数 （随机数生成函数）
# 作业1 
import random
import string
listAll = []
def createRandomList(dataDict):
    list = []
    for i in range(0, len(Dict.keys())):
        for j in range(0, dataDict['randomRange'+str(i+1)]['count']):
            try:
                if dataDict['randomRange'+str(i+1)]['datatype'] is int:
                    list.append(random.randint(dataDict['randomRange'+str(i+1)]['start'],
                                               dataDict['randomRange'+str(i+1)]['stop']))
                if dataDict['randomRange'+str(i+1)]['datatype'] is str:
                    list.append(chr(random.randint(ord(dataDict['randomRange' + str(i + 1)]['start']),
                                               ord(dataDict['randomRange' + str(i + 1)]['stop']))))
            except:
                print('TODO')
        listAll.append(list)
        list = []


# x = random.randint(int, 1, 10)
# print(x)
Dict = {
        'randomRange1': {
            'start': 0,
            'stop': 1,
            'count': 10,
            'datatype':int
        },
        'randomRange2':{
            'start': 'a',
            'stop': 'c',
            'count': 5,
            'datatype':str
        }
    }

# print(chr(ord('a') + 1))
createRandomList(Dict)
print(listAll)