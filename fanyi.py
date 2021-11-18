from urllib import parse
import requests
import json
import execjs
import pyperclip

headers = {
    'Host': 'fanyi.baidu.com',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/',
    'Cookie': 'BAIDUID=79F4098A668D4D7D100960CA687FD28F:FG=1; BDUSS=JsN2tkWW1BSDV6NVc0WGJZMVZuTkRTUkFQYXcyT2V4eVI3TTdxODlyaU5GMjFkSVFBQUFBJCQAAAAAAAAAAAEAAADB5LJ7MTIxN7rAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAI2KRV2NikVdfm; BIDUPSID=79F4098A668D4D7D100960CA687FD28F; PSTM=1565070241; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; APPGUIDE_8_2_2=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; H_WISE_SIDS=139891_128063_141000_100805_141254_135846_140631_140202_139296_136863_138585_141650_140113_140324_140579_133847_140065_134047_141808_131423_141674_107314_140257_139885_140996_140798_140967_136537_110085_141860_140853_138878_137979_141200_140174_131246_141261_138165_138883_140259_141942_127969_140593_140236_138426_138941_141190_141924; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; delPer=0; PSINO=6; H_PS_PSSID=1446_21106_30794_28704; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1581779606,1582011836,1582088164,1582106615; __yjsv5_shitong=1.0_7_0bf690d52ec53291622b903f6a47f18166d9_300_1582107165664_222.247.136.147_cf2cf644; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1582107168; yjs_js_security_passport=ae8d814647837832914c67d862c00b19f36b4a9e_1582107166_js',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36',
    'X-requested-with': 'XMLHttpRequest',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'
}

class Spider():

    def __get_json(self, url, data):

        req = requests.post(url, data=data, headers=headers, proxies={'https': None})
        return req.json()

    def __get_lan(self, query):

        dic = {'query' : query}

        url = 'https://fanyi.baidu.com/langdetect'
        data = bytes(parse.urlencode(dic), encoding='utf8')

        rst = self.__get_json(url, data)
        lan = rst['lan']
        return lan

    def tslt(self, query, to):

        with open('E:/workSpace/python/test2/index_df4b4e4.js') as f:
            js = f.read()
        sign = execjs.compile(js).call('e', query)

        fr = self.__get_lan(query)

        if fr != 'zh':
            to = 'zh'

        dic = {}
        dic['from'] = fr
        dic['to'] = to
        dic['query'] = query
        dic['transtype'] = 'realtime'
        dic['simple_means_flag'] = 3
        dic['sign'] = sign
        dic['token'] = 'c404c88cf65f681e1a77d92b94107564'
        dic['domain'] = 'common'

        url = 'https://fanyi.baidu.com/v2transapi?from=' + fr + '&to=' + to
        data = bytes(parse.urlencode(dic), encoding='utf8')

        if (fr == to):
            return query
        else:
            rst = self.__get_json(url, data)
            fanyi = rst['trans_result']['data'][0]['dst']
            return fanyi

langlistzh = {'zh': '中文', 'jp': '日语', 'jpka': '日语假名', 'th': '泰语', 'fra': '法语', 'en': '英语', 'spa': '西班牙语', 'kor': '韩语', 'tr': '土耳其语', 'vie': '越南语', 'ms': '马来语', 'de': '德语', 'ru': '俄语', 'ir': '伊朗语', 'ara': '阿拉伯语', 'est': '爱沙尼亚语', 'be': '白俄罗斯语', 'bul': '保加利亚语', 'hi': '印地语', 'is': '冰岛语', 'pl': '波兰语', 'fa': '波斯语', 'dan': '丹麦语', 'tl': '菲律宾语', 'fin': '芬兰语', 'nl': '荷兰语', 'ca': '加泰罗尼亚语', 'cs': '捷克语', 'hr': '克罗地亚语', 'lv': '拉脱维亚语', 'lt': '立陶宛语', 'rom': '罗马尼亚语', 'af': '南非语', 'no': '挪威语', 'pt_BR': '巴西语', 'pt': '葡萄牙语', 'swe': '瑞典语', 'sr': '塞尔维亚语', 'eo': '世界语', 'sk': '斯洛伐克语', 'slo': '斯洛文尼亚语', 'sw': '斯瓦希里语', 'uk': '乌克兰语', 'iw': '希伯来语', 'el': '希腊语', 'hu': '匈牙利语', 'hy': '亚美尼亚语', 'it': '意大利语', 'id': '印尼语', 'sq': '阿尔巴尼亚语', 'am': '阿姆哈拉语', 'as': '阿萨姆语', 'az': '阿塞拜疆语', 'eu': '巴斯克语', 'bn': '孟加拉语', 'bs': '波斯尼亚语', 'gl': '加利西亚语', 'ka': '格鲁吉亚语', 'gu': '古吉拉特语', 'ha': '豪萨语', 'ig': '伊博语', 'iu': '因纽特语', 'ga': '爱尔兰语', 'zu': '祖鲁语', 'kn': '卡纳达语', 'kk': '哈萨克语', 'ky': '吉尔吉斯语', 'lb': '卢森堡语', 'mk': '马其顿语', 'mt': '马耳他语', 'mi': '毛利语', 'mr': '马拉提语', 'ne': '尼泊尔语', 'or': '奥利亚语', 'pa': '旁遮普语', 'qu': '凯楚亚语', 'tn': '塞茨瓦纳语', 'si': '僧加罗语', 'ta': '泰米尔语', 'tt': '塔塔尔语', 'te': '泰卢固语', 'ur': '乌尔都语', 'uz': '乌兹别克语', 'cy': '威尔士语', 'yo': '约鲁巴语', 'yue': '粤语', 'wyw': '文言文', 'cht': '中文繁体'}
langlisten = {1: 'zh', 2: 'jp', 3: 'jpka', 4: 'th', 5: 'fra', 6: 'en', 7: 'spa', 8: 'kor', 9: 'tr', 10: 'vie', 11: 'ms', 12: 'de', 13: 'ru', 14: 'ir', 15: 'ara', 16: 'est', 17: 'be', 18: 'bul', 19: 'hi', 20: 'is', 21: 'pl', 22: 'fa', 23: 'dan', 24: 'tl', 25: 'fin', 26: 'nl', 27: 'ca', 28: 'cs', 29: 'hr', 30: 'lv', 31: 'lt', 32: 'rom', 33: 'af', 34: 'no', 35: 'pt_BR', 36: 'pt', 37: 'swe', 38: 'sr', 39: 'eo', 40: 'sk', 41: 'slo', 42: 'sw', 43: 'uk', 44: 'iw', 45: 'el', 46: 'hu', 47: 'hy', 48: 'it', 49: 'id', 50: 'sq', 51: 'am', 52: 'as', 53: 'az', 54: 'eu', 55: 'bn', 56: 'bs', 57: 'gl', 58: 'ka', 59: 'gu', 60: 'ha', 61: 'ig', 62: 'iu', 63: 'ga', 64: 'zu', 65: 'kn', 66: 'kk', 67: 'ky', 68: 'lb', 69: 'mk', 70: 'mt', 71: 'mi', 72: 'mr', 73: 'ne', 74: 'or', 75: 'pa', 76: 'qu', 77: 'tn', 78: 'si', 79: 'ta', 80: 'tt', 81: 'te', 82: 'ur', 83: 'uz', 84: 'cy', 85: 'yo', 86: 'yue', 87: 'wyw', 88: 'cht'}
s = Spider()
f = 1
isCopy = False
to = 'en'

print("需要指定语种输入1，不输入退出")
print("翻译结果直接复制输入2（不需要复制即可粘贴），再次输入可恢复")
print("默认输入语种自动检测")
while f:
    i = 0
    fy = 1
    query = input('输入您需要翻译的内容：')

    if query == '1':
        for lan in langlistzh:
            i += 1
            l = str(14 - len(langlistzh[lan]))
            fmt = '%02d:%-' + l + 's'
            print(fmt % (i, langlistzh[lan]), end='')
            if i % 10 == 0:
                print()
        while fy:
            to = int(input("\n输入语种序号（from to）："))
            if to > 89:
                print('输入有误，请重新输入')
            else:
                to = langlisten[to]
                break
        query = input('输入您需要翻译的内容：')
    elif query == '2':
        isCopy = not isCopy
        print('将' + ('会' if isCopy else '不会') + '复制到剪贴板')

    if not query:
        f = 0
    elif query != '1' and query != '2':
        x = s.tslt(query, to=to)
        # y = s.tslt(x, to='zh')
        if isCopy:
            pyperclip.copy(x)
        print(x)
        # print(x+ '   ----->   ' + y)
