import datetime, time
import urllib.request
import operator

f = urllib.request.urlopen('http://www.yonhapnews.co.kr/bulletin/2016/08/15/0200000000AKR20160815027000001.HTML')
data = f.read().decode('utf-8')

begin = data.find("존경하는 국민 여러분")
end = data.find("나아갑시다! 감사합니다.")

data = data.replace(',','')
data = data.replace('/','')
data = data.replace('<','')
data = data.replace('>','')
data = data.replace('p','')
data = data.replace('-->','')
data = data.replace('!--','')
data = data.replace('scrolling="no"','')
data = data.replace('div','')
data = data.replace('iframe','')
data = data.replace('frameborder="0"','')
data = data.replace('iframe','')
data = data.replace('div','')
data = data.replace('var','')
data = data.replace('span','')

end += len("나아갑시다! 감사합니다.")
print("begin: ", begin)
print("end : ", end)
print("length : ", end-begin)

speech = data[begin:end]
speech = speech.split()

anal={}
for word in speech:
    anal[word] = anal.get(word, 0) + 1

newlist = {}
newlist = sorted(anal.items(), key = operator.itemgetter(1), reverse=True)

i = 0
for i in range(len(newlist)):
    #if newlist[i].value > 5:
        print(newlist[i])
