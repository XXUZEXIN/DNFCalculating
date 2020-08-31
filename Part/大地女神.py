from math import *
from PublicReference.base import *


# 武器巨剑
class 大地女神主动技能(主动技能):
    def 等效CD(self, 武器类型):
        if 武器类型 == '巨剑':
            return round(self.CD / self.恢复 * 1, 1)

# 骑士信念
class 大地女神技能0(被动技能):
    名称 = '骑士信念'
    所在等级 = 15
    等级上限 = 20
    基础等级 = 10

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.10 + 0.02 * self.等级, 5)

    def 物理攻击力倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.10 + 0.02 * self.等级, 5)

# 一觉被动 由于一觉二觉主动不受剑盾猛攻连锁BUFF加成，所以这里有个额外的加成，这个一绝被动加成吃两次
# 例如：一绝被动=1.42，二觉受到的加成为1.42*1.42
class 大地女神技能1(被动技能):
    名称 = '自然恩泽'
    所在等级 = 48
    等级上限 = 40
    基础等级 = 20

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.00+0.02 * self.等级, 5)

# 二觉被动
class 大地女神技能2(被动技能):
    名称 = '信仰鼓舞'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 11

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

# 卓越之力
class 大地女神技能3(被动技能):
    名称 = '卓越之力'
    所在等级 = 95
    等级上限 = 40
    基础等级 = 4

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.18 + 0.02 * self.等级, 5)

# 超卓之心
class 大地女神技能4(被动技能):
    名称 = '超卓之心'
    所在等级 = 95
    等级上限 = 11
    基础等级 = 1

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.045 + 0.005 * self.等级, 5)

# 觉醒之抉择
class 大地女神技能5(被动技能):
    名称 = '觉醒之抉择'
    所在等级 = 100
    等级上限 = 40
    基础等级 = 2
    关联技能 = ['无']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.10 + 0.05 * self.等级, 5)

# 剑盾猛攻 一级默认13%，但测试实际为12.5%，游戏内显示每2级提高1%，但测试伤害实际为每级0.5%
# 剑盾猛攻本身不受剑盾猛攻连锁BUFF加成，一二觉也不受加成，剑盾强袭加成=（剑盾猛攻加成+5%）*连锁层数
class 大地女神技能6(大地女神主动技能):
    名称 = '剑盾猛攻'
    所在等级 = 30
    等级上限 = 16
    基础等级 = 6
    基础 = 906.4
    成长 = 273.6
    CD = 0.5
    关联技能 = ['所有']

    def 加成倍率(self, 武器类型):
        if self.等级 == 0:
            return 1.0
        else:
            return round(1.72 + 0.03 * self.等级, 5)

# 盾挑    技能太多了，这个就不写上去了，Z，吃基础精通
# class 大地女神技能7(大地女神主动技能):
#    名称 = '盾挑'
#    所在等级 = 1
#    等级上限 = 20
#    基础等级 = 10
#    基础 = 89
#    成长 = 11
#    CD = 2
#    TP成长 = 0.08
#    TP上限 = 5

# 强踢
class 大地女神技能7(大地女神主动技能):
    名称 = '强踢'
    所在等级 = 1
    等级上限 = 60
    基础等级 = 50
    基础 = 684.7
    成长 = 77.3
    CD = 5

# 盾击
class 大地女神技能8(大地女神主动技能):
    名称 = '盾击'
    所在等级 = 5
    等级上限 = 60
    基础等级 = 50
    基础 = 293.9
    成长 = 33.1
    CD = 3

# 致命突刺
class 大地女神技能9(大地女神主动技能):
    名称 = '致命突刺'
    所在等级 = 10
    等级上限 = 60
    基础等级 = 48
    基础 = 163.1
    成长 = 22.9
    CD = 3

# 愤怒冲撞
class 大地女神技能10(大地女神主动技能):
    名称 = '愤怒冲撞'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 1895.9
    成长 = 214.1
    CD = 9

# 破武之轮
class 大地女神技能11(大地女神主动技能):
    名称 = '破武之轮'
    所在等级 = 15
    等级上限 = 60
    基础等级 = 46
    基础 = 1071.6
    成长 = 160.4
    CD = 6

# 守护神鹿
class 大地女神技能12(大地女神主动技能):
    名称 = '守护神鹿'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    基础 = 1466.4
    成长 = 165.6
    CD = 6

# 审判之盾
class 大地女神技能13(大地女神主动技能):
    名称 = '审判之盾'
    所在等级 = 20
    等级上限 = 60
    基础等级 = 43
    基础 = 1910
    成长 = 216
    CD = 7

# 破甲冲击
class 大地女神技能14(大地女神主动技能):
    名称 = '破甲冲击'
    所在等级 = 25
    等级上限 = 60
    基础等级 = 41
    基础 = 1621.8
    成长 = 183.2
    CD = 7
    TP成长 = 0.10
    TP上限 = 5

# 精灵之跃 蓄力提高15%伤害，默认一瞬间释放也提高3%，冲击波不受加成，一级刮痧技能就不写那么多了
class 大地女神技能15(大地女神主动技能):
    名称 = '精灵之跃'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 2675.8
    成长 = 302.2
    CD = 7.5
    TP成长 = 0.10
    TP上限 = 5

# 神木刺击
class 大地女神技能16(大地女神主动技能):
    名称 = '神木刺击'
    所在等级 = 30
    等级上限 = 60
    基础等级 = 38
    基础 = 2420.6
    成长 = 273.4
    CD = 10
    TP成长 = 0.10
    TP上限 = 5

# 铁壁推进 持盾推进8秒，18hit，但一般学1级用来刮痧，这里就做1hit使用
class 大地女神技能17(大地女神主动技能):
    名称 = '铁壁推进'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 367.4
    成长 = 41.6
    CD = 20
    TP成长 = 0.10
    TP上限 = 5

# 自然束缚
class 大地女神技能18(大地女神主动技能):
    名称 = '自然束缚'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 4000.3
    成长 = 451.7
    CD = 15
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

# 一刀两断
class 大地女神技能19(大地女神主动技能):
    名称 = '一刀两断'
    所在等级 = 35
    等级上限 = 60
    基础等级 = 36
    基础 = 3502.4
    成长 = 395.6
    CD = 15
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 1.265

# 飓风旋枪 刺击2HIT，旋风10hit
class 大地女神技能20(大地女神主动技能):
    名称 = '飓风旋枪'
    所在等级 = 40
    等级上限 = 60
    基础等级 = 33
    基础 = 7114.3
    成长 = 803.7
    CD = 25
    演出时间 = 2
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 1.1714
        self.CD *= 0.90

# 天陨断空斩
class 大地女神技能21(大地女神主动技能):
    名称 = '天陨断空斩'
    所在等级 = 45
    等级上限 = 60
    基础等级 = 31
    基础 = 10129.2
    成长 = 1143.8
    CD = 45
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 1.2053

# 一觉 1+4+1 hit
class 大地女神技能22(大地女神主动技能):
    名称 = '天马流星落'
    所在等级 = 50
    等级上限 = 40
    基础等级 = 12
    基础 = 32891.3
    成长 = 9930.6
    CD = 159.5

# 生命审判
class 大地女神技能23(大地女神主动技能):
    名称 = '生命审判'
    所在等级 = 60
    等级上限 = 40
    基础等级 = 23
    基础 = 9299.1
    成长 = 1049.9
    CD = 30
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 1.08

# 壁垒突袭
class 大地女神技能24(大地女神主动技能):
    名称 = '壁垒突袭'
    所在等级 = 70
    等级上限 = 40
    基础等级 = 18
    基础 = 16225.2
    成长 = 1831.8
    CD = 50
    TP成长 = 0.10
    TP上限 = 5
    是否有护石 = 1

    def 装备护石(self):
        self.倍率 *= 1.221

# 剑盾强袭
class 大地女神技能25(大地女神主动技能):
    名称 = '剑盾强袭'
    所在等级 = 75
    等级上限 = 40
    基础等级 = 16
    基础 = 22287.6
    成长 = 2516.4
    CD = 40

# 自然之怒  1+6+1 hit
class 大地女神技能26(大地女神主动技能):
    名称 = '自然之怒'
    所在等级 = 80
    等级上限 = 40
    基础等级 = 13
    基础 = 26353
    成长 = 2976
    CD = 45

# 二觉    3+1+5 hit
class 大地女神技能27(大地女神主动技能):
    名称 = '暮光之灵黄昏独角兽'
    所在等级 = 85
    等级上限 = 40
    基础等级 = 5
    基础 = 76675
    成长 = 23148.2
    CD = 198

大地女神技能列表 = []
i = 0
while i >= 0:
    try:
        exec('大地女神技能列表.append(大地女神技能' + str(i) + '())')
        i += 1
    except:
        i = -1

大地女神技能序号 = dict()
for i in range(len(大地女神技能列表)):
    大地女神技能序号[大地女神技能列表[i].名称] = i

大地女神一觉序号 = 0
大地女神二觉序号 = 0
大地女神三觉序号 = 0
for i in 大地女神技能列表:
    if i.所在等级 == 50:
        大地女神一觉序号 = 大地女神技能序号[i.名称]
    if i.所在等级 == 85:
        大地女神二觉序号 = 大地女神技能序号[i.名称]
    if i.所在等级 == 100:
        大地女神三觉序号 = 大地女神技能序号[i.名称]

大地女神护石选项 = ['无']
for i in 大地女神技能列表:
    if i.是否有伤害 == 1 and i.是否有护石 == 1:
        大地女神护石选项.append(i.名称)

大地女神符文选项 = ['无']
for i in 大地女神技能列表:
    if i.所在等级 >= 20 and i.所在等级 <= 80 and i.所在等级 != 50 and i.是否有伤害 == 1:
        大地女神符文选项.append(i.名称)

class 大地女神角色属性(角色属性):
    实际名称 = '大地女神'
    角色 = '守护者'
    职业 = '精灵骑士'

    武器选项 = ['巨剑']

    伤害类型选择 = ['物理百分比']

    伤害类型 = '物理百分比'
    防具类型 = '板甲'
    防具精通属性 = ['力量']

    主BUFF = 2.03

    def __init__(self):
        基础属性输入(self)
        self.技能栏 = deepcopy(大地女神技能列表)
        self.技能序号 = deepcopy(大地女神技能序号)

    def 被动倍率计算(self):
        super().被动倍率计算()
        self.技能栏[self.技能序号['天马流星落']].被动倍率 /= self.技能栏[self.技能序号['剑盾猛攻']].加成倍率(self.武器类型)
        self.技能栏[self.技能序号['暮光之灵黄昏独角兽']].被动倍率 /= self.技能栏[self.技能序号['剑盾猛攻']].加成倍率(self.武器类型)
        self.技能栏[self.技能序号['天马流星落']].被动倍率 *= self.技能栏[self.技能序号['自然恩泽']].加成倍率(self.武器类型)
        self.技能栏[self.技能序号['暮光之灵黄昏独角兽']].被动倍率 *= self.技能栏[self.技能序号['自然恩泽']].加成倍率(self.武器类型)
        self.技能栏[self.技能序号['剑盾强袭']].被动倍率 /= self.技能栏[self.技能序号['剑盾猛攻']].加成倍率(self.武器类型)
        self.技能栏[self.技能序号['剑盾强袭']].被动倍率 *= 0.30 + self.技能栏[self.技能序号['剑盾猛攻']].加成倍率(self.武器类型)
        self.技能栏[self.技能序号['剑盾猛攻']].被动倍率 /= self.技能栏[self.技能序号['剑盾猛攻']].加成倍率(self.武器类型)

class 大地女神(角色窗口):
    def 窗口属性输入(self):
        self.初始属性 = 大地女神角色属性()
        self.角色属性A = 大地女神角色属性()
        self.角色属性B = 大地女神角色属性()
        self.一觉序号 = 大地女神一觉序号
        self.二觉序号 = 大地女神二觉序号
        self.三觉序号 = 大地女神三觉序号
        self.护石选项 = deepcopy(大地女神护石选项)
        self.符文选项 = deepcopy(大地女神符文选项)