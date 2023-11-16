import re
import sys
import html
import time
import random
import requests
from urllib import parse


#谷歌翻译模块
def google(text, Target='zh-CN', source='auto'):
    text = parse.quote(text)
    url = 'https://translate.google.com/m?sl=%s&tl=%s&hl=%s&q=%s' % (source,Target,'zh-CN',text)
    
    dataa = requests.get(url=url,headers=ua,timeout=6)
    dataa = str(dataa.text)
    expr = r'class="result-container">(.*?)<'
    dataa = re.findall(expr, dataa)

    return html.unescape(dataa[0])


#搜狗翻译模块
def sogou(text):  
    text = parse.quote(text)
    data = {'from':'en','to':'zh-CHS','query':text}
    url = 'https://fanyi.sogou.com/api/transpc/text/transword'
    
    dataa = requests.post(url=url,data=data,headers=ua,timeout=6)
    dataa = str(dataa.text)
    expr = r'{"from":"en","trans_text":"(.*?)","to":"zh-CHS"}'
    dataa = re.findall(expr, dataa)
    
    return html.unescape(dataa[0])


#停止等待模块
def tzdd():
    ddsj = random.randint(3,12)
    for tzsj in range(ddsj): 
        print('随机等待%s秒,剩余等待%s秒' % (ddsj,ddsj-tzsj),end='\r')
        time.sleep(1)


#英文判断模块
def ywpd(txt):
    global zzbd
    if len(re.findall(r'[A-Za-z0-9 ]',txt))+1 / (len(txt)+1) > 0.6:
        #zzbd = r'{.*?}|[^A-Za-z ]'
        zzbd = r'{.*?}'
    else:
        #zzbd = r'{.*?}|[0-9$&-(){}\]'
        zzbd = r'{.*?}'


#空值清除模块
def kzqc(n):
    return n != ''


#脚本标题打印
print('\033[0;32msponge插件汉化与配置翻译脚本V1.0\033[0m')
print('''
\033[0;32m此脚本由zhong16cn@outlook.com制作,如有侵权请告知立即删除
此脚本仅供学习使用,完全免费请勿倒卖,请勿用于商业用途
使用此脚本产生的一切后果由你自己承担\033[0m''')


#翻译符号选择
print('''
本脚本支持单行和换行翻译(换行翻译可能有问题)如:
+-----------------------------------------------------+  +------------------------------------+
|插件汉化:                                            |  |配置翻译:                           |
|name.hover.ign=&eIGN: &f{0}                          |  |# Sets whether a command is enabled.|
|name.hover.command=&eClick to suggest: &f&o{0}       |  |    enabled=true                    |
|-----------------------------------------------------|  +------------------------------------+
|move_success: $4La parcela fue movida correctamente. |  |换行翻译:                           |
|copy_success: $4La parcela fue copiada correctamente.|  |ceshi=home\\或\\n                     |
+-----------------------------------------------------+  +------------------------------------+
\033[0;33m脚本原理是将特定符号如(#,=,:)后的内容拿去翻译,换行是末尾有换行的如(\\,\\n)后面的内容在下一行的\033[0m''')

tdfh = ''
while tdfh == '':
    print('特定符号不能为空')
    tdfh = str(input('请输入要翻译文本中的符号:'))
else:
    print('特定符号为:'+tdfh)


#翻译模块选择
print('''
可选择的翻译模块:
谷歌(1):翻译效果好,多语言翻译,无需配cookie(推荐)
(谷歌翻译请确保可以打开以下网址:https://translate.google.com/m)
搜狗(2):插件提示汉化容易出问题,只支持英文翻译成中文,需要配cookie
(搜狗翻译请确保可以打开以下网址:https://fanyi.sogou.com/api/transpc/text/transword)
\033[0;33m使用谷歌模块输入:1,使用搜狗模块输入:2\033[0m''')

fymk = ''
while fymk != '1' and fymk !='2':
    print('请勿输入(1,2)之外的字符')
    fymk = str(input('请输入使用的翻译模块:'))
else:
    if fymk == '1':
        print('翻译模块为:'+'谷歌翻译')
    else:
        print('翻译模块为:'+'搜狗翻译')


#cookie的选择
print('''
使用谷歌翻译:Cookie,User-Agent可以不用配直接回车即用默认的
使用搜狗翻译:Cookie,User-Agent必须配不然用不了
\033[0;33mCookie建议浏览器开无痕模式获取,保证一定时间内是可用的\033[0m''')

ua = {'Cookie':'','User-Agent':''}

ua['Cookie'] = str(input('请输入Cookie:'))
ua['User-Agent'] = str(input('请输入User-Agent:'))
if ua['Cookie'] == '':
    ua['Cookie'] = 'AEC=Ad49MVF9tIpD0Mr4KRtukWsfEBey8bjWFwFCnK4kXqiRroEfmWIUPmhvz98; NID=511=mgemvBCqelXTDbAr5vjRlV6jzEWxcT0c7eRJa_DlKhLgq13WEcEltWmf7J3lm690Bzpo-T0MLFcepsQH1wjE4_IkwfalbwCiMnSsEWU2AWDiMQpnH8mLaiOJAUg9Bgn9mpyBiM-HFaJzzYhiEP7nansYB0n9ee1hIjdmH7tDgjs'
else:
    pass

if ua['User-Agent'] == '':
    ua['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
else:
    pass

print('Cookie为:'+ua['Cookie'])
print('User-Agent为:'+ua['User-Agent'])


#翻译语言选择
print('''
谷歌翻译:要翻译的语言默认为自动判断,翻译成的语言默认为中文,直接回车即用默认的
搜狗翻译:只支持英文转中文,直接回车就好
\033[0;33m谷歌翻译语言标识:https://cloud.google.com/translate/docs/languages\033[0m''')

sourcea = str(input('请输入要翻译的语言:'))
Targeta = str(input('请输入翻译成的语言:'))
if sourcea == '':
    sourcea = 'auto'
else:
    pass

if Targeta == '':
    Targeta = 'zh-CN'
else:
    pass

print('要翻译的语言为:'+sourcea)
print('翻译成的语言为:'+Targeta)


#翻译方式选择
print('''
可选择的翻译方式:
联机翻译(1):全自动,翻译效果好,速度慢有随机等待时间,容易被封
(应服务器对URL的最大限制,单行的内容最好别超2000个字符(1000个汉字),翻译内容少时推荐)
脱机翻译(2):将要翻译的内容打包成一个txt文件给你,自行翻译后将翻译后的txt文件地址填入
(可以随意选择翻译结果的的来源,有上百行要翻译的建议选这翻译快,翻译模块无法使用时推荐)
\033[0;33m使用联机翻译输入:1,脱机翻译输入:2\033[0m''')

fyfs = ''
while fyfs != '1' and fyfs != '2':
    print('请勿输入(1,2)之外的字符')
    fyfs = str(input('请输入使用的翻译方式:'))
else:
    if fyfs == '1':
        print('翻译方式为:'+'联机翻译')
    else:
        print('翻译方式为:'+'脱机翻译')


#翻译文件选择
print('''
输入要翻译的文件地址如:
D:\Desktop\\nucleus\commands.conf
\033[0;33m地址头尾“”号会自动删,请确保文件是UTF-8编码的\033[0m''')

wjdz = ''
while wjdz == '':
    print('文件地址不能为空')
    wjdz = str(input('请输入要翻译文件的地址:')).strip('"')
else:
    print('文件地址为:'+wjdz)


#翻译信息输入成功提示
print('\033[0;32m翻译信息输入成功\033[0m')


#翻译文件读取
try:
    wjdq = []

    with open(file=wjdz,mode='r',encoding='utf-8-sig') as wjdq:
        wjdq = str(wjdq.read())
    wjdq = wjdq.splitlines()

except:
    print('\033[0;31m翻译文件读取失败,请确认文件格式及权限(确保文件是UTF-8编码的)\033[0m')
    input('按任意键退出')
    sys.exit(0)


#翻译文件读取成功提示
print('\033[0;32m翻译文件读取成功\033[0m')


#翻译内容提取
try:
    nrtq = []

    for tqsy in range(len(wjdq)):
        tqwz = wjdq[tqsy].find(tdfh)
        if tqwz == -1:
            continue
        else:
            ywpd(txt=wjdq[tqsy][tqwz+1:])
            nrtq = nrtq + re.split(zzbd,wjdq[tqsy][tqwz+1:])
            while wjdq[tqsy].strip(' ')[-1:] == '\\' or wjdq[tqsy].strip(' ')[-2:] == '\\n':
                tqsy = tqsy + 1
                ywpd(txt=wjdq[tqsy])
                nrtq = nrtq + re.split(zzbd,wjdq[tqsy])
            else:
                pass
            
    nrtq = list(filter(kzqc,nrtq))

    for qcsy in range(len(nrtq)):
        nrtq[qcsy] = nrtq[qcsy].strip('\ \n')
        
    nrtq = list(set(nrtq))

except:
    print('\033[0;31m翻译内容提取失败,请确认翻译符号及重试\033[0m')
    input('按任意键退出')
    sys.exit(0)


#翻译内容提取成功提示
print('\033[0;32m翻译内容提取成功\033[0m')


#翻译内容翻译
try:
    fyjg = []

    if fyfs == '1':
        fyts = len(nrtq)
        if fymk == '1':
            for fycs in nrtq:
                try:
                    fyjg.append(google(text=fycs, Target=Targeta, source=sourcea))
                    tzdd()
                except:
                    print('\033[0;31m当前条目翻译失败:第一次重试,最多三次\033[0m')
                    try:
                        fyjg.append(google(text=fycs, Target=Targeta, source=sourcea))
                        tzdd()
                    except:
                        print('\033[0;31m当前条目翻译失败:第二次重试,最多三次\033[0m')
                        try:
                            fyjg.append(google(text=fycs, Target=Targeta, source=sourcea))
                            tzdd()
                        except:
                            print('\033[0;31m当前条目翻译失败:第三次重试,最多三次\033[0m')
                            try:
                                fyjg.append(google(text=fycs, Target=Targeta, source=sourcea))
                                tzdd()
                            except:
                                sys.exit(0)                
                print('共需翻译%s条,已经翻译%s条' % (fyts,len(fyjg)))
        else:
            for fycs in nrtq:
                try:
                    fyjg.append(sogou(text=fycs))
                    tzdd()
                except:
                    print('\033[0;31m当前条目翻译失败:第一次重试,最多三次\033[0m')
                    try:
                        fyjg.append(sogou(text=fycs))
                        tzdd()
                    except:
                        print('\033[0;31m当前条目翻译失败:第二次重试,最多三次\033[0m')
                        try:
                            fyjg.append(sogou(text=fycs))
                            tzdd()
                        except:
                            print('\033[0;31m当前条目翻译失败:第三次重试,最多三次\033[0m')
                            try:
                                fyjg.append(sogou(text=fycs))
                                tzdd()
                            except:
                                sys.exit(0)
                print('共需翻译%s条,已经翻译%s条' % (fyts,len(fyjg)))
    else:
        xrsy = wjdz.rfind('\\')
        xrdz = wjdz[:xrsy+1]+'[自行翻译]'+wjdz[xrsy+1:]
        with open(xrdz,mode='a',encoding='utf-8') as tqjg:
            for tqxr in nrtq:
                tqjg.write(tqxr + '\n')
        
        print('自行翻译的文件在要翻译文件的目录下')
        print('源文件名前有[自行翻译]就是即:'+xrdz)

        print('\033[0;33m请确保自行翻译文件与你翻译好的文件逐行对应,即两个文件的每行是对照的,行数也要相同\033[0m')        
        print('输入翻译后的文件地址(地址头尾“”号会自动删,确保文件是UTF-8编码的)')

        zyfy = ''
        while zyfy == '':
            print('文件地址不能为空')
            zyfy = str(input('请输入翻译后文件的地址:')).strip('"')
        else:
            print('文件地址为:'+zyfy)

        with open(file=zyfy,mode='r',encoding='utf-8-sig') as fyjg:
            fyjg = str(fyjg.read())
        fyjg = fyjg.splitlines()

except:
    print('\033[0;31m翻译内容翻译失败,请确认填写的内容及网络\033[0m')
    input('按任意键退出')
    sys.exit(0)

#翻译内容翻译成功提示
print('\033[0;32m翻译内容翻译成功\033[0m')


#翻译行数检查
if len(nrtq) != len(fyjg):
    print('\033[0;31m翻译文件与翻译好的文件行数不同\033[0m')
    input('按任意键退出')
    sys.exit(0)
else:
    pass


#翻译行数检查成功提示
print('\033[0;32m翻译行数检查成功\033[0m')


#翻译内容替换
try:
    zzjg = []

    zfzd = str.maketrans(r'＆＃，。！？；：（）《》【】“”\‘\’、',r'&#,.!?;:()<>[]""\'\',')
    fyjg = '<!#@$%&^*>'.join(fyjg)
    fyjg = fyjg.translate(zfzd)
    fyjg = fyjg.split('<!#@$%&^*>')

    thzd = dict(zip(nrtq,fyjg))
    thzd['\\'] = '\\'
    thzd[' '] = ' '
    thzd[''] = ''

    thsy = 0
    while thsy < len(wjdq):
        thwz = wjdq[thsy].find(tdfh)
        if thwz == -1:
            zzjg.append(wjdq[thsy])
        else:
            fyth = wjdq[thsy][thwz+1:]
            ywpd(txt=fyth)
            thnr = re.split(zzbd,fyth)
            thnr = list(set(filter(kzqc,thnr)))

            for thcx in thnr:
                thcx = thcx.strip('\ \n')
                fyth = fyth.replace(thcx,thzd[thcx])

            zzjg.append(wjdq[thsy][:thwz+1]+fyth)

            while wjdq[thsy].strip(' ')[-1:] == '\\' or wjdq[thsy].strip(' ')[-2:] == '\\n':
                thsy = thsy + 1
                
                fyth = wjdq[thsy]
                ywpd(txt=fyth)
                thnr = re.split(zzbd,fyth)
                thnr = list(set(filter(kzqc,thnr)))

                for thcx in thnr:
                    thcx = thcx.strip('\ \n')
                    fyth = fyth.replace(thcx,thzd[thcx])

                zzjg.append(fyth)
            else:
                pass

        thsy = thsy + 1

except:
    print('\033[0;31m翻译内容替换失败,请确认填写的内容及内存\033[0m')
    input('按任意键退出')
    sys.exit(0)


#翻译内容替换成功提示
print('\033[0;32m翻译内容替换成功\033[0m')


#翻译文件写入
try:
    xrsy = wjdz.rfind('\\')
    xrdz = wjdz[:xrsy+1]+'[翻译]'+wjdz[xrsy+1:]
    with open(xrdz,mode='a',encoding='utf-8') as xrjg:
        for fyxr in zzjg:
            xrjg.write(fyxr + '\n')
       
except:
    print('\033[0;31m翻译文件写入失败,请确认内存及权限\033[0m')
    input('按任意键退出')
    sys.exit(0)


#翻译文件写入成功提示
print('\033[0;32m翻译文件写入成功\033[0m')
print('''
翻译后文件在要翻译文件的目录下
源文件名前有[翻译]就是即:'''+xrdz)

#翻译脚本退出
input('按任意键退出')
        






