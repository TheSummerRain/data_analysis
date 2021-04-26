# -*- coding:utf-8 -*-
import jieba
import jieba.analyse
import numpy as np


class SimHash(object):
    def simHash(self, content):
        seg = jieba.cut(content)
        jieba.analyse.set_stop_words('stopword.txt')
        # jieba基于TF-IDF提取关键词
        keyWords = jieba.analyse.extract_tags("|".join(seg), topK=10, withWeight=True)

        keyList = []
        for feature, weight in keyWords:
            print('weight: {}'.format(weight))
            # weight = math.ceil(weight)
            weight = int(weight)
            binstr = self.string_hash(feature)
            temp = []
            for c in binstr:
                if (c == '1'):
                    temp.append(weight)
                else:
                    temp.append(-weight)
            keyList.append(temp)
        listSum = np.sum(np.array(keyList), axis=0)
        if (keyList == []):
            return '00'
        simhash = ''
        for i in listSum:
            if (i > 0):
                simhash = simhash + '1'
            else:
                simhash = simhash + '0'

        return simhash

    def string_hash(self, source):
        if source == "":
            return 0
        else:
            x = ord(source[0]) << 7
            m = 1000003
            mask = 2 ** 128 - 1
            for c in source:
                x = ((x * m) ^ ord(c)) & mask
            x ^= len(source)
            if x == -1:
                x = -2
            x = bin(x).replace('0b', '').zfill(64)[-64:]
            # print('strint_hash: %s, %s'%(source, x))

            return str(x)

    def getDistance(self, hashstr1, hashstr2):
        '''
            计算两个simhash的汉明距离
        '''
        length = 0
        for index, char in enumerate(hashstr1):
            if char == hashstr2[index]:
                continue
            else:
                length += 1

        return length




if __name__ == '__main__':
    s1 = """
    引子：
    公元2000年，三月二十号，一个球状不明物体突然出现在各国卫星云图上。
    信号强烈，绝对不是一般物体！
    而在此前，几个科技强国的地外监测站并未监测到任何异状。
    各国高层得到消息全都紧张起来。
    最终，该物体掉落在秦国海域，秦国科研人员迅速前往打捞。
    世界各国的天文、地质学家都密切关注此次打捞行为。
    可是历经数月，打捞人员却一无所获。
    各国科学家以为秦国隐瞒消息，不肯公诸于众人，纷纷表示抗议。
    大秦帝国只是发表了一个声明后，再不理会。
    ……
    不明物体入海的同一时间，秦国沿海城市，云海市。
    六中，高二八班。
    “1830年6月，随着矛盾激化，XXX等国对我大秦帝国正式宣战！XXX战争爆发，联军由西南
    陆路、西北高原以及东部海路两个方向妄图入侵我国。嬴元嘉陛下一声令下，全国动员，五千万
    大秦将士奔赴战场。同年11月，我大秦海军在白蒙元帅的带领下，一举歼灭联军精锐太平洋舰
    队，此战也标志着……第二年的2月，联军西南陆军总指挥向我国请降……我大秦帝国从此成为世
    界最强国。”
    　　历史老师韩天华正在滔滔不绝的讲述着大秦帝国的近代史。
    　　从教室的后面传出一串不怎么和谐的声音。
    　　“呼~~~~~~~ZZzz...”
    　　春困、夏倦、秋乏、冬眠，四季如梦。
    　　恰逢春困！
    """

    s2 = """
    　一辆科尼赛克跑车，驶入南江市临雪集团的地下停车场。
    　　道九言停好车后，坐在驾驶位上，迟迟没有下车。
    　　“十五年过去了，马上就要见到大姐了，就是不知道她还记不记得我？”
    　　他的心情无比激动，又有着许多忐忑。
    　　道九言是个孤儿，从小被一个老道士收养，在道九言被收养之前，老道士还收养了九个女
    孩。
    　　他们从小一起长大，虽然没有血缘，关系却胜过亲姐弟。
    　　可就在道九言七岁那年，意外发生。
    　　有一天，他被前来道观烧香的人贩子，用几块奶糖给拐走，卖到了国外。
    　　对于那段记忆，道九言是记忆犹深。
    　　他被人贩子拐卖到国外的第三天，趁人贩子不注意从二楼跳了下来。
    　　然而，他不仅没有逃掉，还摔断了左手臂。
    　　森森白骨刺破皮肉，血流不止。
    　　人贩子将他抓回后，直接扔进一个冰冷的小黑屋内，任其自生自灭。
    　　道九言感觉到自己生命就要走到尽头时，用那满是鲜血的右手，取下脖子上佩戴的玉坠。
    　　这个玉坠看上去十分普通，可却是道九言父母留给他的唯一信物，从小就佩戴在身上。
    　　虽然他不知道自己的父母是谁，可他还是希望有一天，可以凭借着这块玉佩找到自己的亲生
    父母。
    　　或许是人贩子看这个玉坠普通，不值钱，所以才没有收走。
    　　可就在道九言取下玉佩那瞬间，诡异的一幕发生了。
    　　那块玉佩居然如同是海绵一样，在吸收着道九言流出来的鲜血。
    　　这一幕，道九言看不到，可他却能感受到体内的鲜血在快速地流失。
    　　本就奄奄一息的他，直接昏死过去。
    """

    simhash = SimHash()
    s1 = simhash.simHash('或许是人贩子看这个玉坠普通，不值钱，所以才没有收走。可就在道九言取下玉佩那瞬间，诡异的一幕发生了。')
    print("==================")
    s2 = simhash.simHash('或许是人贩子看这个玉坠普通，不值钱，所以才没有收走。可就在道九言取下玉佩那瞬间，诡异的一幕发生了。')

    dis = simhash.getDistance(s1, s2)

    print('dis: {}'.format(dis))
