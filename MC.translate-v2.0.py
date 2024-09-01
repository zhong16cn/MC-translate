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
    dataa = html.unescape(parse.unquote(str(dataa.text)))
    expr = r'class="result-container">(.*?)<'
    dataa = re.findall(expr, dataa)

    return dataa[0]


#搜狗翻译模块
def sogou(text):  
#    text = parse.quote(text)
    data = {'from':'en','to':'zh-CHS','query':text}
    url = 'https://fanyi.sogou.com/api/transpc/text/transword'
    
    dataa = requests.post(url=url,data=data,headers=ua,timeout=6)
    dataa = html.unescape(parse.unquote(str(dataa.text)))
    expr = r'{"from":"en","trans_text":"(.*?)","to":"zh-CHS"}'
    dataa = re.findall(expr, dataa)
    
    return dataa[0]


#停止等待模块
def tzdd(zddd):
    ddsj = random.randint(1,zddd)
    for tzsj in range(ddsj): 
        print('随机等待%s秒,剩余等待%s秒' % (ddsj,ddsj-tzsj),end='\r')
        time.sleep(1)


#空值清除模块
def kzqc(n):
    return n != ''


#脚本标题打印
print('\033[0;32mMC插件汉化与注释翻译脚本V2.0\033[0m')
print('''
\033[0;32m最新发布地址:https://github.com/zhong16cn/MC-translate 
此脚本由zhong16cn@outlook.com制作,如有侵权请告知立即删除
此脚本仅供学习使用,完全免费请勿倒卖,请勿用于商业用途
使用此脚本产生的一切后果由你自己承担\033[0m''')


#特定字符选择
tdzf = ''

print('''
本脚本支持单行和换行翻译(换行翻译可能有问题)如:
+-----------------------------------------------------+  +------------------------------------+
|插件汉化:                                            |  |注释翻译:                           |
|name.hover.ign=&eIGN: &f{0}                          |  |# Sets whether a command is enabled.|
|color="dark_green"                                   |  |    enabled=true                    |
|text="registration successful!"                      |  |                                    |
+-----------------------------------------------------+  +------------------------------------+
|move_success: $4La parcela fue movida correctamente. |  |换行翻译:                           |
|copy_success: $4La parcela fue copiada correctamente.|  |ceshi=home\\或\\n                     |
+-----------------------------------------------------+  +------------------------------------+
\033[0;33m脚本原理是将第一个匹配到的特定字符如(#,:,text=)等后的内容拿去翻译,换行是末尾有换行符的如(\\,\\n)后面的内容在下一行的\033[0m''')

while tdzf == '':
    print('\033[0;33m特定字符不能为空\033[0m')
    tdzf = str(input('请输入要翻译文本中的字符:'))
else:
    zfcd = len(tdzf)
    print('特定字符为:'+tdzf)
    print('特定字符长度为:'+str(zfcd))


#正则表达选择
zzbd = ''

print('''
对于不需要翻译内容的保留是用python3中的re.split()函数进行字符串分割处理的如:
+------------------------------------------------------------------------------------------------+
|常用表达:                                                                                       |
|name.hover.ign=&eIGN: &f{0},只要保留{0}的话,用括号中的正则表达式:(\\{.*?\\})                      |
|command-balance="&6current balance: &a{balance} &6{label}",只翻译单词用:(\\&.|\\{.*?\\}|\\")        |
+------------------------------------------------------------------------------------------------+
|简单讲解:                                                                                       |
|.号表示任意一个字符,.*号表示匹配任意次数,?号表示非贪婪匹配,没?号表示贪婪匹配                    |
|如:{0}aaa{0},非贪婪匹配表示两个{0},贪婪匹配表示{0}aaa{0},贪婪匹配会最大限度匹配                 |
|[]号表示匹配[]中的字符,[^]号表示匹配除了[]中字符之外的字符,|号表示组合使用同时使用多个表达式    |
|\\号表示转译将表达式符号转成普通字符,转译字符:https://www.cnblogs.com/dyfblog/p/6088582.html     |
+------------------------------------------------------------------------------------------------+
\033[0;33m正则表达式讲解:https://tool.oschina.net/uploads/apidocs/jquery/regexp.html\033[0m''')

print('\033[0;33m直接回车即表示所有内容都翻译\033[0m')
zzbd = str(input('请输入表示不用翻译内容的正则表达式:'))
print('表示不用翻译内容的正则表达式为:'+zzbd)


#翻译文件选择
wjdz = ''

print('''
输入要翻译的文件地址如:
D:\\Desktop\\nucleus\\commands.conf
\033[0;33m地址头尾“”号会自动删,请确保文件是UTF-8编码的\033[0m''')

while wjdz == '':
    print('\033[0;33m文件地址不能为空\033[0m')
    wjdz = str(input('请输入要翻译文件的地址:')).strip('"')
else:
    print('文件地址为:'+wjdz)


#翻译方式选择
fyfs = ''

print('''
可选择的翻译方式:
联机翻译(1):全自动,翻译效果好,速度慢有随机等待时间,容易被封
(应服务器对URL的最大限制,单行的内容最好别超2000个字符(1000个汉字),翻译内容少时推荐)
脱机翻译(2):将要翻译的内容打包成一个txt文件给你,自行翻译后将翻译后的txt文件地址填入
(可以随意选择翻译结果的的来源,有上百行要翻译的建议选这翻译快,翻译模块无法使用时推荐)
\033[0;33m使用联机翻译输入:1,脱机翻译输入:2\033[0m''')

while fyfs != '1' and fyfs != '2':
    print('\033[0;33m请勿输入(1,2)之外的字符\033[0m')
    fyfs = str(input('请输入使用的翻译方式:'))
else:
    if fyfs == '1':
        print('翻译方式为:联机翻译')
    else:
        print('翻译方式为:脱机翻译')


#翻译信息配置
if fyfs == '1':
    #翻译模块选择
    fymk = ''

    print('''
可选择的翻译模块:
谷歌(1):翻译效果好,多语言翻译,无需配cookie(推荐)
(谷歌翻译请确保可以打开以下网址:https://translate.google.com/m)
搜狗(2):插件提示汉化容易出现翻译效果不准确,只支持英文翻译成中文,需要配cookie
(搜狗翻译请确保可以打开以下网址:https://fanyi.sogou.com/api/transpc/text/transword)
\033[0;33m使用谷歌模块输入:1,使用搜狗模块输入:2\033[0m''')

    while fymk != '1' and fymk !='2':
        print('\033[0;33m请勿输入(1,2)之外的字符\033[0m')
        fymk = str(input('请输入使用的翻译模块:'))
    else:
        if fymk == '1':
            print('翻译模块为:谷歌翻译')
        else:
            print('翻译模块为:搜狗翻译')
       
    
    #cookie的选择
    ua = {'Cookie':'','User-Agent':''}

    print('''
使用谷歌翻译:Cookie,User-Agent可以不用配直接回车即用默认的
使用搜狗翻译:Cookie,User-Agent必须配不然用不了
\033[0;33mCookie建议浏览器开无痕模式获取,保证一定时间内是可用的\033[0m''')

    ua['Cookie'] = str(input('请输入Cookie:'))
    ua['User-Agent'] = str(input('请输入User-Agent:'))
    if ua['Cookie'] == '':
        ua['Cookie'] = 'AEC=Ad49MVF9tIpD0Mr4KRtukWsfEBey8bjWFwFCnK4kXqiRroEfmWIUPmhvz98; NID=511=mgemvBCqelXTDbAr5vjRlV6jzEWxcT0c7eRJa_DlKhLgq13WEcEltWmf7J3lm690Bzpo-T0MLFcepsQH1wjE4_IkwfalbwCiMnSsEWU2AWDiMQpnH8mLaiOJAUg9Bgn9mpyBiM-HFaJzzYhiEP7nansYB0n9ee1hIjdmH7tDgjs'
        print('Cookie为:'+ua['Cookie'])
    else:
        print('Cookie为:'+ua['Cookie'])

    if ua['User-Agent'] == '':
        ua['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
        print('User-Agent为:'+ua['User-Agent'])
    else:
        print('User-Agent为:'+ua['User-Agent'])

    
    #翻译语言选择
    sourcea = ''
    Targeta = ''

    print('''
谷歌翻译:要翻译的语言默认为自动判断,翻译成的语言默认为中文,直接回车即用默认的
搜狗翻译:只支持英文转中文,直接回车就好
\033[0;33m谷歌翻译语言标识:https://cloud.google.com/translate/docs/languages\033[0m''')

    sourcea = str(input('请输入需要被翻译的语言的标识:'))
    Targeta = str(input('请输入想要翻译成的语言的标识:'))
    if sourcea == '':
        sourcea = 'auto'
        print('要翻译的语言为:'+sourcea)
    else:
        print('要翻译的语言为:'+sourcea)

    if Targeta == '':
        Targeta = 'zh-CN'
        print('翻译成的语言为:'+Targeta)
    else:
        print('翻译成的语言为:'+Targeta)


    #重试次数选择
    zdcs = ' '

    print('''
翻译过程因网络波动有时会翻译失败,不要设置太大,重试三五次还不行基本就是用不了
\033[0;33m默认最多重试3次,直接回车即用默认的\033[0m''')

    while not(zdcs.isdigit() or zdcs == ''):
        print('\033[0;33m请勿输入数字之外的字符\033[0m')
        zdcs = str(input('请输入最大重试次数:'))
    else:
        if zdcs == '':
            zdcs = '3'
            print('最大重试次数为:%s次' % zdcs)
            zdcs = int(zdcs)
        else:
            print('最大重试次数为:%s次' % zdcs)
            zdcs = int(zdcs)
    
    
    #等待时间选择
    zdms = ' '

    print('''
翻译失败重试翻译过程发送数据包太频繁的话容易被封ip,导致联机翻译无法使用
\033[0;33m等待时间为随机1到最大等待秒数,默认最大等待3秒,直接回车即用默认的\033[0m''')

    while not(zdms.isdigit() or zdms == '') or zdms == '0':
        print('\033[0;33m请勿输入大于零的整数之外的字符\033[0m')
        zdms = str(input('请输入最大等待秒数:'))
    else:
        if zdms == '':
            zdms = '3'
            print('最大等待时间为:%s秒' % zdms)
            zdms = int(zdms)
        else:
            print('最大等待时间为:%s秒' % zdms)
            zdms = int(zdms)
else:
    pass


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

    #翻译类型判断
    if tdzf[:1] == '#' or tdzf[:2] == '/*' or tdzf[:2] == '//':
        #注释翻译提取
        for tqsy in range(len(wjdq)):
            tqwz = wjdq[tqsy].find(tdzf)
            if tqwz == -1:
                continue
            else:  
                nrtq.append(wjdq[tqsy][tqwz+zfcd:])               
    else:
        #插件汉化提取
        for tqsy in range(len(wjdq)):
            tqwz = wjdq[tqsy].find(tdzf)
            if tqwz == -1:
                continue
            else:  
                nrtq.append(wjdq[tqsy][tqwz+zfcd:])
                while wjdq[tqsy].strip(' ')[-1:] == '\\' or wjdq[tqsy].strip(' ')[-2:] == '\\n':
                        tqsy = tqsy + 1
                        tqwz = wjdq[tqsy].find(tdzf)
                        if tqwz == -1:
                                    nrtq.append(wjdq[tqsy])
                        else:  
                            nrtq.append(wjdq[tqsy][tqwz+zfcd:])                            
                else:
                    continue
    
    #内容提取清洗
    nrtq = list(set(nrtq))
    for qcsy in range(len(nrtq)):
        nrtq[qcsy] = nrtq[qcsy].strip('\\ \n')
    nrtq = list(filter(kzqc,nrtq))
    
except:
    print('\033[0;31m翻译内容提取失败,请确认翻译符号及重试\033[0m')
    input('按任意键退出')
    sys.exit(0)


#翻译内容提取成功提示
print('\033[0;32m翻译内容提取成功\033[0m')


#翻译内容过滤
try:
    nrgl = []

    #判断是否过滤
    if zzbd == '':
        nrgl = nrtq
    else:
        for glnr in nrtq:
            nrgl = nrgl + re.split(zzbd,glnr)
    
    #内容过滤清洗
    nrgl = list(set(nrgl))
    for qcsy in range(len(nrgl)):
        nrgl[qcsy] = nrgl[qcsy].strip('\\ \n')
    nrgl = list(filter(kzqc,nrgl))

except:
    print('\033[0;31m翻译内容过滤失败,请确认正则表达式及重试\033[0m')
    input('按任意键退出')
    sys.exit(0)


#翻译内容过滤成功提示
print('\033[0;32m翻译内容过滤成功\033[0m')


#翻译内容翻译
try:
    fyjg = []

    #翻译方式判断
    if fyfs == '1':
        fyts = len(nrgl)
        #翻译模块判断
        if fymk == '1':
            #google翻译模块
            for fynr in nrgl:
                    cscs = zdcs
                    while cscs > -1:
                        try:
                            fyjg.append(google(text=fynr, Target=Targeta, source=sourcea))
                            cscs = -1
                        except:
                            cscs = cscs -1
                            if cscs > -1:
                                print('\033[0;31m当前条目翻译失败:第%s次重试,最多%s次\033[0m' % (zdcs-cscs,zdcs))
                                tzdd(zddd=zdms)
                            else:
                                raise
                    else:
                        print('共需翻译%s条,已经翻译%s条' % (fyts,len(fyjg)))             
        else:
            #sogou翻译模块
            for fynr in nrgl:
                    cscs = zdcs
                    while cscs > -1:
                        try:
                            fyjg.append(sogou(text=fynr))
                            cscs = -1
                        except:
                            cscs = cscs -1
                            if cscs > -1:
                                print('\033[0;31m当前条目翻译失败:第%s次重试,最多%s次\033[0m' % (zdcs-cscs,zdcs))
                                tzdd(zddd=zdms)
                            else:
                                raise
                    else:
                        print('共需翻译%s条,已经翻译%s条' % (fyts,len(fyjg)))         
    else:
        #脱机翻译模式
        xrsy = wjdz.rfind('\\')
        xrdz = wjdz[:xrsy+1] + '[自行翻译]' + wjdz[xrsy+1:]
        with open(xrdz,mode='a',encoding='utf-8') as tqjg:
            for tqxr in nrgl:
                tqjg.write(tqxr+'\n')
        
        print('自行翻译的文件在要翻译文件的目录下')
        print('源文件名前有[自行翻译]就是即:'+xrdz)
        print('输入翻译后的文件地址(地址头尾“”号会自动删,确保文件是UTF-8编码的)')
        print('\033[0;33m自行翻译文件以追加的方式写入,且同一个源文件每次生成的自行翻译文件内容的顺序都不同\033[0m')
        print('\033[0;33m请确保自行翻译文件与翻译好的文件逐行对应,即两个文件的每行是对照的,行数也要相同\033[0m')        

        #自行翻译读取
        zxfy = ''
        while zxfy == '':
            print('\033[0;33m文件地址不能为空\033[0m')
            zxfy = str(input('请输入翻译后文件的地址:')).strip('"')
        else:
            print('文件地址为:'+zxfy)

        with open(file=zxfy,mode='r',encoding='utf-8-sig') as fyjg:
            fyjg = str(fyjg.read())
        fyjg = fyjg.splitlines()

except:
    print('\033[0;31m翻译内容翻译失败,请确认填写的内容,文件读写权限及网络\033[0m')
    input('按任意键退出')
    sys.exit(0)


#翻译内容翻译成功提示
print('\033[0;32m翻译内容翻译成功\033[0m')


#翻译行数检查
if len(nrgl) != len(fyjg):
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

    #创建替换字典
    zfzd = str.maketrans(r'＃，。！？；：（）《》【】“”\‘\’、',r'#,.!?;:()<>[]""\'\',')
    fyjg = '<!#@$%&^*>'.join(fyjg)
    fyjg = fyjg.translate(zfzd)
    fyjg = fyjg.split('<!#@$%&^*>')

    thzd = dict(zip(nrgl,fyjg))
    thzd['\\'] = '\\'
    thzd[' '] = ' '
    thzd[''] = ''

    #翻译类型判断
    if tdzf[:1] == '#' or tdzf[:2] == '/*' or tdzf[:2] == '//':
        #注释翻译替换
        if zzbd == '':
            thsy = 0
            while thsy < len(wjdq):
                thwz = wjdq[thsy].find(tdzf)
                if thwz == -1:
                    zzjg.append(wjdq[thsy])
                else:
                    thwz = thwz + zfcd
                    ktzf = wjdq[thsy][:thwz]
                    thjg = wjdq[thsy][thwz:]        
                    thnr = thjg.strip('\\ \n')
                    thjg = thjg.replace(thnr,thzd[thnr],1)
                    zzjg.append(ktzf+thjg)
                thsy = thsy + 1
            else:
                pass
        else:
            thsy = 0
            while thsy < len(wjdq):
                thwz = wjdq[thsy].find(tdzf)
                if thwz == -1:
                    zzjg.append(wjdq[thsy])
                else:
                    thwz = thwz + zfcd
                    ktzf = wjdq[thsy][:thwz]
                    thjg = wjdq[thsy][thwz:]     
                    thnr = re.split(zzbd,thjg)
                    for thfg in thnr:
                        thfg = thfg.strip('\\ \n')
                        thjg = thjg.replace(thfg,thzd[thfg],1)
                    zzjg.append(ktzf+thjg)
                thsy = thsy + 1       
            else:
                pass                 
    else:
        #插件汉化替换
        if zzbd == '':
            thsy = 0
            while thsy < len(wjdq):
                thwz = wjdq[thsy].find(tdzf)
                if thwz == -1:
                    zzjg.append(wjdq[thsy])
                else:
                    thwz = thwz + zfcd
                    ktzf = wjdq[thsy][:thwz]
                    thjg = wjdq[thsy][thwz:]        
                    thnr = thjg.strip('\\ \n')
                    thjg = thjg.replace(thnr,thzd[thnr],1)
                    zzjg.append(ktzf+thjg)

                    while wjdq[thsy].strip(' ')[-1:] == '\\' or wjdq[thsy].strip(' ')[-2:] == '\\n':
                        thsy = thsy + 1
                        thjg = wjdq[thsy]        
                        thnr = thjg.strip('\\ \n')
                        thjg = thjg.replace(thnr,thzd[thnr],1)
                        zzjg.append(thjg)
                    else:
                        pass
                thsy = thsy + 1
            else:
                pass
        else:
            thsy = 0
            while thsy < len(wjdq):
                thwz = wjdq[thsy].find(tdzf)
                if thwz == -1:
                    zzjg.append(wjdq[thsy])
                else:
                    thwz = thwz + zfcd
                    ktzf = wjdq[thsy][:thwz]
                    thjg = wjdq[thsy][thwz:]     
                    thnr = re.split(zzbd,thjg)
                    for thfg in thnr:
                        thfg = thfg.strip('\\ \n')
                        thjg = thjg.replace(thfg,thzd[thfg],1)
                    zzjg.append(ktzf+thjg)

                    while wjdq[thsy].strip(' ')[-1:] == '\\' or wjdq[thsy].strip(' ')[-2:] == '\\n':
                        thsy = thsy + 1
                        thjg = wjdq[thsy]     
                        thnr = re.split(zzbd,thjg)
                        for thfg in thnr:
                            thfg = thfg.strip('\\ \n')
                            thjg = thjg.replace(thfg,thzd[thfg],1)
                        zzjg.append(thjg)
                    else:
                        pass
                thsy = thsy + 1
            else:
                pass

except:
    print('\033[0;31m翻译内容替换失败,请确认填写的内容及内存\033[0m')
    input('按任意键退出')
    sys.exit(0)


#翻译内容替换成功提示
print('\033[0;32m翻译内容替换成功\033[0m')


#翻译文件写入
try:
    xrsy = wjdz.rfind('\\')
    xrdz = wjdz[:xrsy+1] + '[翻译]' + wjdz[xrsy+1:]
    with open(xrdz,mode='a',encoding='utf-8') as xrjg:
        for fyxr in zzjg:
            xrjg.write(fyxr+'\n')
       
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

    