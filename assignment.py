#assignment
import monkdata as m
import dtree as dtree
import random
import drawtree_qt5 as drawtree

entropy1 = dtree.entropy(m.monk1)
entropy2 = dtree.entropy(m.monk2)
entropy3 = dtree.entropy(m.monk3)
print(entropy1,entropy2,entropy3)
monk1gain = list()
monk2gain = list()
monk3gain = list()
for i in range(0,6):
    monk1gain.append(dtree.averageGain(m.monk1,m.attributes[i]))
    monk2gain.append(dtree.averageGain(m.monk2,m.attributes[i]))
    monk3gain.append(dtree.averageGain(m.monk3,m.attributes[i]))
print(monk1gain)
print(monk2gain)
print(monk3gain)
t1 = dtree.buildTree(m.monk1, m.attributes)
print(1-dtree.check(t1, m.monk1),1-dtree.check(t1, m.monk1test))
t2 = dtree.buildTree(m.monk2, m.attributes)
print(1-dtree.check(t2, m.monk2),1-dtree.check(t2, m.monk2test))
t3 = dtree.buildTree(m.monk3, m.attributes)
print(1-dtree.check(t3, m.monk3),1-dtree.check(t3, m.monk3test))
#drawtree.drawTree(t3)

subset1 = dtree.select(m.monk1, m.attributes[4], 1)
subset2 = dtree.select(m.monk1, m.attributes[4], 2)
subset3 = dtree.select(m.monk1, m.attributes[4], 3)
subset4 = dtree.select(m.monk1, m.attributes[4], 4)
subset1gain = list()
subset2gain = list()
subset3gain = list()
subset4gain = list()
for i in range(0,6):
    subset1gain.append(dtree.averageGain(subset1,m.attributes[i]))
    subset2gain.append(dtree.averageGain(subset2,m.attributes[i]))
    subset3gain.append(dtree.averageGain(subset3,m.attributes[i]))
    subset4gain.append(dtree.averageGain(subset4,m.attributes[i]))
print(subset1gain)
print(subset2gain)
print(subset3gain)
print(subset4gain)


m1par = list()
for p in (0.3, 0.4, 0.5, 0.6, 0.7, 0.8):
    m1pur0 = list()
    m1pur1 = list()
    for j in range(0,100):
        def partition(data, fraction):
            ldata = list(data)
            random.shuffle(ldata)
            breakPoint = int(len(ldata) * fraction)
            return ldata[:breakPoint], ldata[breakPoint:]

        monk1train, monk1val = partition(m.monk1, p)

        t10 = dtree.buildTree(monk1train, m.attributes)
        t11 = dtree.buildTree(monk1train, m.attributes)
        cor10 = dtree.check(t11, monk1val)
        cor11 = dtree.check(t11, monk1val)
        x = 0
        m1pur0.append(cor11)

        while cor10 <= cor11:
            t10 = t11
            cor10 = cor11
            lt11 = list(dtree.allPruned(t10))
            for i in lt11:
                if dtree.check(i, monk1val) > x:
                    x = dtree.check(i, monk1val)
                    t11 = i
            cor11 = x
            x = 0  
                
        testerr1 = 1 - dtree.check(t10, m.monk1test)
        m1pur1.append(testerr1)
    #    drawtree.drawTree(t10)
    sum1 = 0
    for i in m1pur1:
        sum1 += i
    m1par.append(sum1/100)
print(m1par)

m3par = list()
for p in (0.3, 0.4, 0.5, 0.6, 0.7, 0.8):
    m3pur0 = list()
    m3pur1 = list()
    for j in range(0,100):
        monk3train, monk3val = partition(m.monk3, p)

        t30 = dtree.buildTree(monk3train, m.attributes)
        t31 = dtree.buildTree(monk3train, m.attributes)
        cor30 = dtree.check(t31, monk3val)
        cor31 = dtree.check(t31, monk3val)
        x = 0
        m3pur0.append(cor31)

        while cor30 <= cor31:
            t30 = t31
            cor30 = cor31
            lt13 = list(dtree.allPruned(t30))
            for i in lt13:
                if dtree.check(i, monk3val) > x:
                    x = dtree.check(i, monk3val)
                    t31 = i
            cor31 = x
            x = 0  
        
        testerr3 = 1- dtree.check(t30, m.monk3test)        
        m3pur1.append(testerr3)
    #    drawtree.drawTree(t10)
    sum3 = 0
    for i in m3pur1:
        sum3 += i
    m3par.append(sum3/100)
print(m3par)

def partition(data, fraction):
            ldata = list(data)
            random.shuffle(ldata)
            breakPoint = int(len(ldata) * fraction)
            return ldata[:breakPoint], ldata[breakPoint:]

monk1train, monk1val = partition(m.monk1, 0.6)

t10 = dtree.buildTree(monk1train, m.attributes)
t11 = dtree.buildTree(monk1train, m.attributes)
cor10 = dtree.check(t11, monk1val)
cor11 = dtree.check(t11, monk1val)
x=0

while cor10 <= cor11:
            t10 = t11
            cor10 = cor11
            lt11 = list(dtree.allPruned(t10))
            for i in lt11:
                if dtree.check(i, monk1val) > x:
                    x = dtree.check(i, monk1val)
                    t11 = i
            cor11 = x
            x = 0  
drawtree.drawTree(t10)