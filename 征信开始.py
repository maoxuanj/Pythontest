#*- coding:utf-8 -*-
__author__='MXJ'
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys #需要引入keys包
from selenium.webdriver.support.ui import Select
import randomphone
import random
import string
import win32gui
import win32con
import time
import SendKeys
#这是python程序主入口
if 1==1:
    #随机生成姓名，身份证及手机号码

    #启动firefox
    driver = webdriver.Firefox()



#打开网页 http://www.baidu.com
    driver.get("http://192.168.10.204:8080/view/index.html")
    ele = driver.find_element_by_name("userName")
    ele.send_keys("15728042309")
    ele = driver.find_element_by_name("password")
    ele.send_keys("mao123456")
    driver.find_element_by_id("loginBtn").send_keys(Keys.ENTER)
    sleep(1)
    print "浏览器最大化"
    driver.maximize_window()
    sleep(1)
    #先定位到搜索输入框
    #通过id或name定位即可
    driver.find_element_by_link_text("贷前管理").click()
    sleep(1)
    driver.find_element_by_link_text("资信管理").click()
    sleep(1)
    driver.switch_to_frame('iframe_26')
    ele = driver.find_element_by_id("launchedCredit")
    ele.click()
    sleep(2)
    driver.switch_to.default_content()
    driver.switch_to_frame('iframe_undefined')
    ele = driver.find_element_by_name("customerName")
    shenfen = randomphone.gennerator()
    def random_name(size=1, chars=string.ascii_letters + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))


    def first_name(size=2, ln=None, fn=None):
        _lst = []
        for i in range(size):
            _item = random_name(1, fn)
            if ln:
                while _item in ln:
                    _item = random_name(1, fn)
                _lst.append(_item)
            else: 
                _lst.append(_item)
        return "".join(_lst)


    def last_name(size=1, names=None):
        return random_name(size, names)


    def full_name(lns, fns):
        _last = last_name(1, lns)
        return "{}{}".format(_last, first_name(random.randint(1, 2), _last, fns))


    if __name__ == "__main__":
        last_names = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤',
                      '许',
                      '何', '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', '柏', '水', '窦',
                      '章',
                      '云', '苏', '潘', '葛', '奚', '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤', '花', '方', '俞', '任', '袁',
                      '柳',
                      '酆', '鲍', '史', '唐', '费', '廉', '岑', '薛', '雷', '贺', '倪', '汤', '滕', '殷', '罗', '毕', '郝', '邬', '安',
                      '常',
                      '乐', '于', '时', '傅', '皮', '卞', '齐', '康', '伍', '余', '元', '卜', '顾', '孟', '平', '黄', '和', '穆', '萧',
                      '尹',
                      '姚', '邵', '堪', '汪', '祁', '毛', '禹', '狄', '米', '贝', '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅',
                      '庞',
                      '熊', '纪', '舒', '屈', '项', '祝', '董', '梁']

        first_names = ['的', '一', '是', '了', '我', '不', '人', '在', '他', '有', '这', '个', '上', '们', '来', '到', '时', '大', '地',
                       '为',
                       '子', '中', '你', '说', '生', '国', '年', '着', '就', '那', '和', '要', '她', '出', '也', '得', '里', '后', '自',
                       '以',
                       '会', '家', '可', '下', '而', '过', '天', '去', '能', '对', '小', '多', '然', '于', '心', '学', '么', '之', '都',
                       '好',
                       '看', '起', '发', '当', '没', '成', '只', '如', '事', '把', '还', '用', '第', '样', '道', '想', '作', '种', '开',
                       '美',
                       '总', '从', '无', '情', '己', '面', '最', '女', '但', '现', '前', '些', '所', '同', '日', '手', '又', '行', '意',
                       '动',
                       '方', '期', '它', '头', '经', '长', '儿', '回', '位', '分', '爱', '老', '因', '很', '给', '名', '法', '间', '斯',
                       '知',
                       '世', '什', '两', '次', '使', '身', '者', '被', '高', '已', '亲', '其', '进', '此', '话', '常', '与', '活', '正',
                       '感',
                       '见', '明', '问', '力', '理', '尔', '点', '文', '几', '定', '本', '公', '特', '做', '外', '孩', '相', '西', '果',
                       '走',
                       '将', '月', '十', '实', '向', '声', '车', '全', '信', '重', '三', '机', '工', '物', '气', '每', '并', '别', '真',
                       '打',
                       '太', '新', '比', '才', '便', '夫', '再', '书', '部', '水', '像', '眼', '等', '体', '却', '加', '电', '主', '界',
                       '门',
                       '利', '海', '受', '听', '表', '德', '少', '克', '代', '员', '许', '稜', '先', '口', '由', '死', '安', '写', '性',
                       '马',
                       '光', '白', '或', '住', '难', '望', '教', '命', '花', '结', '乐', '色', '更', '拉', '东', '神', '记', '处', '让',
                       '母',
                       '父', '应', '直', '字', '场', '平', '报', '友', '关', '放', '至', '张', '认', '接', '告', '入', '笑', '内', '英',
                       '军',
                       '候', '民', '岁', '往', '何', '度', '山', '觉', '路', '带', '万', '男', '边', '风', '解', '叫', '任', '金', '快',
                       '原',
                       '吃', '妈', '变', '通', '师', '立', '象', '数', '四', '失', '满', '战', '远', '格', '士', '音', '轻', '目', '条',
                       '呢',
                       '病', '始', '达', '深', '完', '今', '提', '求', '清', '王', '化', '空', '业', '思', '切', '怎', '非', '找', '片',
                       '罗',
                       '钱', '紶', '吗', '语', '元', '喜', '曾', '离', '飞', '科', '言', '干', '流', '欢', '约', '各', '即', '指', '合',
                       '反',
                       '题', '必', '该', '论', '交', '终', '林', '请', '医', '晚', '制', '球', '决', '窢', '传', '画', '保', '读', '运',
                       '及',
                       '则', '房', '早', '院', '量', '苦', '火', '布', '品', '近', '坐', '产', '答', '星', '精', '视', '五', '连', '司',
                       '巴',
                       '奇', '管', '类', '未', '朋', '且', '婚', '台', '夜', '青', '北', '队', '久', '乎', '越', '观', '落', '尽', '形',
                       '影',
                       '红', '爸', '百', '令', '周', '吧', '识', '步', '希', '亚', '术', '留', '市', '半', '热', '送', '兴', '造', '谈',
                       '容',
                       '极', '随', '演', '收', '首', '根', '讲', '整', '式', '取', '照', '办', '强', '石', '古', '华', '諣', '拿', '计',
                       '您',
                       '装', '似', '足', '双', '妻', '尼', '转', '诉', '米', '称', '丽', '客', '南', '领', '节', '衣', '站', '黑', '刻',
                       '统',
                       '断', '福', '城', '故', '历', '惊', '脸', '选', '包', '紧', '争', '另', '建', '维', '绝', '树', '系', '伤', '示',
                       '愿',
                       '持', '千', '史', '谁', '准', '联', '妇', '纪', '基', '买', '志', '静', '阿', '诗', '独', '复', '痛', '消', '社',
                       '算',
                       '义', '竟', '确', '酒', '需', '单', '治', '卡', '幸', '兰', '念', '举', '仅', '钟', '怕', '共', '毛', '句', '息',
                       '功',
                       '官', '待', '究', '跟', '穿', '室', '易', '游', '程', '号', '居', '考', '突', '皮', '哪', '费', '倒', '价', '图',
                       '具',
                       '刚', '脑', '永', '歌', '响', '商', '礼', '细', '专', '黄', '块', '脚', '味', '灵', '改', '据', '般', '破', '引',
                       '食',
                       '仍', '存', '众', '注', '笔', '甚', '某', '沉', '血', '备', '习', '校', '默', '务', '土', '微', '娘', '须', '试',
                       '怀',
                       '料', '调', '广', '蜖', '苏', '显', '赛', '查', '密', '议', '底', '列', '富', '梦', '错', '座', '参', '八', '除',
                       '跑',
                       '亮', '假', '印', '设', '线', '温', '虽', '掉', '京', '初', '养', '香', '停', '际', '致', '阳', '纸', '李', '纳',
                       '验',
                       '助', '激', '够', '严', '证', '帝', '饭', '忘', '趣', '支', '春', '集', '丈', '木', '研', '班', '普', '导', '顿',
                       '睡',
                       '展', '跳', '获', '艺', '六', '波', '察', '群', '皇', '段', '急', '庭', '创', '区', '奥', '器', '谢', '弟', '店',
                       '否',
                       '害', '草', '排', '背', '止', '组', '州', '朝', '封', '睛', '板', '角', '况', '曲', '馆', '育', '忙', '质', '河',
                       '续',
                       '哥', '呼', '若', '推', '境', '遇', '雨', '标', '姐', '充', '围', '案', '伦', '护', '冷', '警', '贝', '著', '雪',
                       '索',
                       '剧', '啊', '船', '险', '烟', '依', '斗', '值', '帮', '汉', '慢', '佛', '肯', '闻', '唱', '沙', '局', '伯', '族',
                       '低',
                       '玩', '资', '屋', '击', '速', '顾', '泪', '洲', '团', '圣', '旁', '堂', '兵', '七', '露', '园', '牛', '哭', '旅',
                       '街',
                       '劳', '型', '烈', '姑', '陈', '莫', '鱼', '异', '抱', '宝', '权', '鲁', '简', '态', '级', '票', '怪', '寻', '杀',
                       '律',
                       '胜', '份', '汽', '右', '洋', '范', '床', '舞', '秘', '午', '登', '楼', '贵', '吸', '责', '例', '追', '较', '职',
                       '属',
                       '渐', '左', '录', '丝', '牙', '党', '继', '托', '赶', '章', '智', '冲', '叶', '胡', '吉', '卖', '坚', '喝', '肉',
                       '遗',
                       '救', '修', '松', '临', '藏', '担', '戏', '善', '卫', '药', '悲', '敢', '靠', '伊', '村', '戴', '词', '森', '耳',
                       '差',
                       '短', '祖', '云', '规', '窗', '散', '迷', '油', '旧', '适', '乡', '架', '恩', '投', '弹', '铁', '博', '雷', '府',
                       '压',
                       '超', '负', '勒', '杂', '醒', '洗', '采', '毫', '嘴', '毕', '九', '冰', '既', '状', '乱', '景', '席', '珍', '童',
                       '顶',
                       '派', '素', '脱', '农', '疑', '练', '野', '按', '犯', '拍', '征', '坏', '骨', '余', '承', '置', '臓', '彩', '灯',
                       '巨',
                       '琴', '免', '环', '姆', '暗', '换', '技', '翻', '束', '增', '忍', '餐', '洛', '塞', '缺', '忆', '判', '欧', '层',
                       '付',
                       '阵', '玛', '批', '岛', '项', '狗', '休', '懂', '武', '革', '良', '恶', '恋', '委', '拥', '娜', '妙', '探', '呀',
                       '营',
                       '退', '摇', '弄', '桌', '熟', '诺', '宣', '银', '势', '奖', '宫', '忽', '套', '康', '供', '优', '课', '鸟', '喊',
                       '降',
                       '夏', '困', '刘', '罪', '亡', '鞋', '健', '模', '败', '伴', '守', '挥', '鲜', '财', '孤', '枪', '禁', '恐', '伙',
                       '杰',
                       '迹', '妹', '藸', '遍', '盖', '副', '坦', '牌', '江', '顺', '秋', '萨', '菜', '划', '授', '归', '浪', '听', '凡',
                       '预',
                       '奶', '雄', '升', '碃', '编', '典', '袋', '莱', '含', '盛', '济', '蒙', '棋', '端', '腿', '招', '释', '介', '烧',
                       '误',
                       '乾', '坤']

        fullname = (full_name(last_names, first_names))
        print fullname
        fullname1 = unicode(fullname)
        ele.send_keys(fullname1)
    driver.find_element_by_id("cardNo").send_keys(shenfen)
    #driver.find_element_by_id("cardNo").send_keys("5646132")  固定输入，验证alert
    Select(driver.find_element_by_id("bankDeraler")).select_by_visible_text(u"工行安徽城建支行")
    Select(driver.find_element_by_id("maritalStatus")).select_by_visible_text("已婚")
    phone = randomphone.createPhone()
    driver.find_element_by_name("relavants[0].mobile").send_keys(phone)
    sleep(3)
    driver.find_element_by_xpath("(//button[@type='button'])[3]").click()

    # SendKeys
    SendKeys.SendKeys("C:\\Users\\mxj\\Desktop\\error\\timg1.jpg")
    sleep(2)
    SendKeys.SendKeys("{ENTER}")
    sleep(2)

    # 验证alert内容是否正确(暂时搞不定）
    #a1=driver.find_element_by_id("toast-container").text
    #print a1
    #"C:\\Users\\mxj\\Desktop\\error\\shensu2016052301[1].jpg" "C:\\Users\\mxj\\Desktop\\error\\7.1.jpg"
    driver.find_element_by_xpath("(//button[@type='button'])[3]").click()

    # SendKeys
    SendKeys.SendKeys("C:\\Users\\mxj\\Desktop\\error\\shensu2016052301[1].jpg")
    sleep(2)
    SendKeys.SendKeys("{ENTER}")

    sleep(2)


    driver.find_element_by_xpath("(//button[@type='button'])[3]").click()
    # SendKeys
    SendKeys.SendKeys("C:\\Users\\mxj\\Desktop\\error\\7.1.png")
    SendKeys.SendKeys("{ENTER}")
    #ele=driver.find_element_by_css_selector("input.hide")
    #ele.send_keys(u"C:\\Users\\mxj\\Desktop\\错误捕捉1\\timg：1.jpg")
    #sleep(3)
    #driver.find_element_by_css_selector("input.hide").send_keys(
    #    u"C:\\Users\\mxj\\Desktop\\错误捕捉1\\3205221987120680271[1].jpg")
    #sleep(2)
    #driver.find_element_by_css_selector("input.hide").send_keys(
    #    u"C:\\Users\\mxj\\Desktop\\错误捕捉1\\151029110134718[1].jpg")
    #sleep(3)
    driver.find_element_by_name("relavants[1].fullName").clear()


    def random_name1(size=1, chars=string.ascii_letters + string.digits):
        return ''.join(random.choice(chars) for _ in range(size))


    def first_name1(size=2, ln=None, fn=None):
        _lst = []
        for i in range(size):
            _item = random_name(1, fn)
            if ln:
                while _item in ln:
                    _item = random_name(1, fn)
                _lst.append(_item)
            else:
                _lst.append(_item)
        return "".join(_lst)


    def last_name1(size=1, names=None):
        return random_name(size, names)


    def full_name1(lns, fns):
        _last = last_name(1, lns)
        return "{}{}".format(_last, first_name(random.randint(1, 2), _last, fns))


    if __name__ == "__main__":
        last_names = ['赵', '钱', '孙', '李', '周', '吴', '郑', '王', '冯', '陈', '褚', '卫', '蒋', '沈', '韩', '杨', '朱', '秦', '尤',
                      '许',
                      '何', '吕', '施', '张', '孔', '曹', '严', '华', '金', '魏', '陶', '姜', '戚', '谢', '邹', '喻', '柏', '水', '窦',
                      '章',
                      '云', '苏', '潘', '葛', '奚', '范', '彭', '郎', '鲁', '韦', '昌', '马', '苗', '凤', '花', '方', '俞', '任', '袁',
                      '柳',
                      '酆', '鲍', '史', '唐', '费', '廉', '岑', '薛', '雷', '贺', '倪', '汤', '滕', '殷', '罗', '毕', '郝', '邬', '安',
                      '常',
                      '乐', '于', '时', '傅', '皮', '卞', '齐', '康', '伍', '余', '元', '卜', '顾', '孟', '平', '黄', '和', '穆', '萧',
                      '尹',
                      '姚', '邵', '堪', '汪', '祁', '毛', '禹', '狄', '米', '贝', '明', '臧', '计', '伏', '成', '戴', '谈', '宋', '茅',
                      '庞',
                      '熊', '纪', '舒', '屈', '项', '祝', '董', '梁']

        first_names = ['的', '一', '是', '了', '我', '不', '人', '在', '他', '有', '这', '个', '上', '们', '来', '到', '时', '大', '地',
                       '为',
                       '子', '中', '你', '说', '生', '国', '年', '着', '就', '那', '和', '要', '她', '出', '也', '得', '里', '后', '自',
                       '以',
                       '会', '家', '可', '下', '而', '过', '天', '去', '能', '对', '小', '多', '然', '于', '心', '学', '么', '之', '都',
                       '好',
                       '看', '起', '发', '当', '没', '成', '只', '如', '事', '把', '还', '用', '第', '样', '道', '想', '作', '种', '开',
                       '美',
                       '总', '从', '无', '情', '己', '面', '最', '女', '但', '现', '前', '些', '所', '同', '日', '手', '又', '行', '意',
                       '动',
                       '方', '期', '它', '头', '经', '长', '儿', '回', '位', '分', '爱', '老', '因', '很', '给', '名', '法', '间', '斯',
                       '知',
                       '世', '什', '两', '次', '使', '身', '者', '被', '高', '已', '亲', '其', '进', '此', '话', '常', '与', '活', '正',
                       '感',
                       '见', '明', '问', '力', '理', '尔', '点', '文', '几', '定', '本', '公', '特', '做', '外', '孩', '相', '西', '果',
                       '走',
                       '将', '月', '十', '实', '向', '声', '车', '全', '信', '重', '三', '机', '工', '物', '气', '每', '并', '别', '真',
                       '打',
                       '太', '新', '比', '才', '便', '夫', '再', '书', '部', '水', '像', '眼', '等', '体', '却', '加', '电', '主', '界',
                       '门',
                       '利', '海', '受', '听', '表', '德', '少', '克', '代', '员', '许', '稜', '先', '口', '由', '死', '安', '写', '性',
                       '马',
                       '光', '白', '或', '住', '难', '望', '教', '命', '花', '结', '乐', '色', '更', '拉', '东', '神', '记', '处', '让',
                       '母',
                       '父', '应', '直', '字', '场', '平', '报', '友', '关', '放', '至', '张', '认', '接', '告', '入', '笑', '内', '英',
                       '军',
                       '候', '民', '岁', '往', '何', '度', '山', '觉', '路', '带', '万', '男', '边', '风', '解', '叫', '任', '金', '快',
                       '原',
                       '吃', '妈', '变', '通', '师', '立', '象', '数', '四', '失', '满', '战', '远', '格', '士', '音', '轻', '目', '条',
                       '呢',
                       '病', '始', '达', '深', '完', '今', '提', '求', '清', '王', '化', '空', '业', '思', '切', '怎', '非', '找', '片',
                       '罗',
                       '钱', '紶', '吗', '语', '元', '喜', '曾', '离', '飞', '科', '言', '干', '流', '欢', '约', '各', '即', '指', '合',
                       '反',
                       '题', '必', '该', '论', '交', '终', '林', '请', '医', '晚', '制', '球', '决', '窢', '传', '画', '保', '读', '运',
                       '及',
                       '则', '房', '早', '院', '量', '苦', '火', '布', '品', '近', '坐', '产', '答', '星', '精', '视', '五', '连', '司',
                       '巴',
                       '奇', '管', '类', '未', '朋', '且', '婚', '台', '夜', '青', '北', '队', '久', '乎', '越', '观', '落', '尽', '形',
                       '影',
                       '红', '爸', '百', '令', '周', '吧', '识', '步', '希', '亚', '术', '留', '市', '半', '热', '送', '兴', '造', '谈',
                       '容',
                       '极', '随', '演', '收', '首', '根', '讲', '整', '式', '取', '照', '办', '强', '石', '古', '华', '諣', '拿', '计',
                       '您',
                       '装', '似', '足', '双', '妻', '尼', '转', '诉', '米', '称', '丽', '客', '南', '领', '节', '衣', '站', '黑', '刻',
                       '统',
                       '断', '福', '城', '故', '历', '惊', '脸', '选', '包', '紧', '争', '另', '建', '维', '绝', '树', '系', '伤', '示',
                       '愿',
                       '持', '千', '史', '谁', '准', '联', '妇', '纪', '基', '买', '志', '静', '阿', '诗', '独', '复', '痛', '消', '社',
                       '算',
                       '义', '竟', '确', '酒', '需', '单', '治', '卡', '幸', '兰', '念', '举', '仅', '钟', '怕', '共', '毛', '句', '息',
                       '功',
                       '官', '待', '究', '跟', '穿', '室', '易', '游', '程', '号', '居', '考', '突', '皮', '哪', '费', '倒', '价', '图',
                       '具',
                       '刚', '脑', '永', '歌', '响', '商', '礼', '细', '专', '黄', '块', '脚', '味', '灵', '改', '据', '般', '破', '引',
                       '食',
                       '仍', '存', '众', '注', '笔', '甚', '某', '沉', '血', '备', '习', '校', '默', '务', '土', '微', '娘', '须', '试',
                       '怀',
                       '料', '调', '广', '蜖', '苏', '显', '赛', '查', '密', '议', '底', '列', '富', '梦', '错', '座', '参', '八', '除',
                       '跑',
                       '亮', '假', '印', '设', '线', '温', '虽', '掉', '京', '初', '养', '香', '停', '际', '致', '阳', '纸', '李', '纳',
                       '验',
                       '助', '激', '够', '严', '证', '帝', '饭', '忘', '趣', '支', '春', '集', '丈', '木', '研', '班', '普', '导', '顿',
                       '睡',
                       '展', '跳', '获', '艺', '六', '波', '察', '群', '皇', '段', '急', '庭', '创', '区', '奥', '器', '谢', '弟', '店',
                       '否',
                       '害', '草', '排', '背', '止', '组', '州', '朝', '封', '睛', '板', '角', '况', '曲', '馆', '育', '忙', '质', '河',
                       '续',
                       '哥', '呼', '若', '推', '境', '遇', '雨', '标', '姐', '充', '围', '案', '伦', '护', '冷', '警', '贝', '著', '雪',
                       '索',
                       '剧', '啊', '船', '险', '烟', '依', '斗', '值', '帮', '汉', '慢', '佛', '肯', '闻', '唱', '沙', '局', '伯', '族',
                       '低',
                       '玩', '资', '屋', '击', '速', '顾', '泪', '洲', '团', '圣', '旁', '堂', '兵', '七', '露', '园', '牛', '哭', '旅',
                       '街',
                       '劳', '型', '烈', '姑', '陈', '莫', '鱼', '异', '抱', '宝', '权', '鲁', '简', '态', '级', '票', '怪', '寻', '杀',
                       '律',
                       '胜', '份', '汽', '右', '洋', '范', '床', '舞', '秘', '午', '登', '楼', '贵', '吸', '责', '例', '追', '较', '职',
                       '属',
                       '渐', '左', '录', '丝', '牙', '党', '继', '托', '赶', '章', '智', '冲', '叶', '胡', '吉', '卖', '坚', '喝', '肉',
                       '遗',
                       '救', '修', '松', '临', '藏', '担', '戏', '善', '卫', '药', '悲', '敢', '靠', '伊', '村', '戴', '词', '森', '耳',
                       '差',
                       '短', '祖', '云', '规', '窗', '散', '迷', '油', '旧', '适', '乡', '架', '恩', '投', '弹', '铁', '博', '雷', '府',
                       '压',
                       '超', '负', '勒', '杂', '醒', '洗', '采', '毫', '嘴', '毕', '九', '冰', '既', '状', '乱', '景', '席', '珍', '童',
                       '顶',
                       '派', '素', '脱', '农', '疑', '练', '野', '按', '犯', '拍', '征', '坏', '骨', '余', '承', '置', '臓', '彩', '灯',
                       '巨',
                       '琴', '免', '环', '姆', '暗', '换', '技', '翻', '束', '增', '忍', '餐', '洛', '塞', '缺', '忆', '判', '欧', '层',
                       '付',
                       '阵', '玛', '批', '岛', '项', '狗', '休', '懂', '武', '革', '良', '恶', '恋', '委', '拥', '娜', '妙', '探', '呀',
                       '营',
                       '退', '摇', '弄', '桌', '熟', '诺', '宣', '银', '势', '奖', '宫', '忽', '套', '康', '供', '优', '课', '鸟', '喊',
                       '降',
                       '夏', '困', '刘', '罪', '亡', '鞋', '健', '模', '败', '伴', '守', '挥', '鲜', '财', '孤', '枪', '禁', '恐', '伙',
                       '杰',
                       '迹', '妹', '藸', '遍', '盖', '副', '坦', '牌', '江', '顺', '秋', '萨', '菜', '划', '授', '归', '浪', '听', '凡',
                       '预',
                       '奶', '雄', '升', '碃', '编', '典', '袋', '莱', '含', '盛', '济', '蒙', '棋', '端', '腿', '招', '释', '介', '烧',
                       '误',
                       '乾', '坤']

        fullname2 = (full_name(last_names, first_names))
    fullname3 = unicode(fullname2)
    driver.find_element_by_name("relavants[1].fullName").send_keys(fullname3)
    Select(driver.find_element_by_id("cardType")).select_by_visible_text("身份证")
    shenfen1 = randomphone.gennerator()
    driver.find_element_by_name("relavants[1].cardId").clear()
    driver.find_element_by_name("relavants[1].cardId").send_keys(shenfen1)
    driver.find_element_by_name("estimateLoanAmount").clear()
    driver.find_element_by_name("estimateLoanAmount").send_keys("100000")
    phone1 = randomphone.createPhone()
    driver.find_element_by_name("relavants[1].mobile").clear()
    driver.find_element_by_name("relavants[1].mobile").send_keys(phone1)
    sleep(3)
    ele = driver.find_element_by_id("save")
    ele.click()
    sleep(1)
    driver.find_element_by_id("sureOption").click()
    sleep(2)

    driver.find_element_by_xpath("(//input[@name='btSelectItem'])[4]").click()
    driver.find_element_by_xpath("(//*[@id='task']/div/div/div[3]/div/button[1])").click()
    # 返回上一个iframe TOP Window
    sleep(5)
    driver.switch_to.default_content()
    #driver.find_element_by_css_selector("span.nav-label").click()
    sleep(5)
    #driver.find_element_by_css_selector("li > a.J_menuItem").click()
    #2018-1-24以上内容成功
    """driver.find_element_by_css_selector("span.J_tabExit").click()
    sleep(2)
    driver.find_element_by_id("exitSure").click()
    sleep(2)
    driver.find_element_by_name("userName").clear()
    driver.find_element_by_name("userName").send_keys("15129209059")
    sleep(2)
    ele = driver.find_element_by_name("password")
    ele.send_keys("mao123456")
    driver.find_element_by_id("loginBtn").send_keys(Keys.ENTER)
    sleep(1)
    # 征信录入
    driver.find_element_by_link_text("我的任务").click()
    sleep(0.5)
    driver.find_element_by_css_selector("li > a.J_menuItem").click()
    driver.switch_to_frame('iframe_21')

    s1 = driver.find_element_by_id("ftCode")
    Select(s1).select_by_value("CREDIT_FLOW")
    # ele=driver.find_element_by_id("ftCode")
    # ele.find_element_by_link_text(u"征信流程").click()
    driver.find_element_by_css_selector("option[value=\"CREDIT_FLOW\"]").click()
    Select(driver.find_element_by_id("flowNode")).select_by_visible_text("征信录入")
    driver.find_element_by_id("btn-search").click()
    sleep(2)
    driver.find_element_by_link_text("征信录入").click()
    sleep(2)
    driver.switch_to.default_content()
    driver.switch_to_frame('iframe_undefined')
    sleep(2)
    driver.find_element_by_name("relavants[0].checkDate").click()
    sleep(2)
    ele = driver.find_element_by_xpath("html/body/div[7]/div[3]/table/tfoot/tr/th")
    ele.click()
    Select(driver.find_element_by_name("relavants[0].checkResult")).select_by_value("1")
    driver.find_element_by_xpath("(//input[@name='relavants[0].loanRepayment'])[2]").click()
    sleep(1)
    driver.find_element_by_name("relavants[1].checkDate").send_keys("2017-7-26")
    sleep(2)
    Select(driver.find_element_by_name("relavants[1].checkResult")).select_by_value("1")
    driver.find_element_by_xpath("(//input[@name='relavants[1].loanRepayment'])[2]").click()
    driver.find_element_by_name("relavants[1].checkDate").click()
    sleep(2)
    ele = driver.find_element_by_xpath("html/body/div[8]/div[3]/table/tfoot/tr/th")
    ele.click()
    driver.find_element_by_id("save").click()
    sleep(2)
    driver.find_element_by_id("sureOption").click()
    sleep(15)



    driver.switch_to.default_content()
    sleep(1)
    driver.find_element_by_css_selector("span.J_tabExit").click()
    sleep(2)
    driver.find_element_by_id("exitSure").click()
    sleep(2)
    driver.find_element_by_name("userName").clear()
    driver.find_element_by_name("userName").send_keys("15728042309")
    sleep(2)
    ele = driver.find_element_by_name("password")
    ele.send_keys("mao123456")
    driver.find_element_by_id("loginBtn").send_keys(Keys.ENTER)
    sleep(1)"""
    # 征信接受
    driver.find_element_by_link_text("我的任务").click()
    sleep(1)
    driver.find_element_by_xpath("//a[contains(text(),'我的任务')]").click()
    #driver.switch_to.default_content()
    driver.switch_to_frame('iframe_21')
    sleep(3)
    s1 = driver.find_element_by_id("ftCode")
    Select(s1).select_by_value("CREDIT_FLOW")
    driver.find_element_by_css_selector("option[value=\"CREDIT_FLOW\"]").click()
    Select(driver.find_element_by_id("flowNode")).select_by_visible_text("征信接受")
    driver.find_element_by_id("btn-search").click()
    sleep(2)
    driver.find_element_by_link_text("征信接受").click()
    sleep(1)
    driver.switch_to.default_content()
    driver.switch_to_frame('iframe_undefined')
    sleep(2)
    driver.find_element_by_id("save").click()
    sleep(2)
    driver.find_element_by_id("sureOption").click()
    sleep(2)

