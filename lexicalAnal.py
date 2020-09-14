# -*- coding: utf-8 -*-

import string
#from gtts import gTTS

symbolTags = {\
0:set(),\
1:{'[',']','&','%','#',',','{','}'}, \
2:{'mu','Mu','nu','Nu','xi','Xi','pm','in','Re','ll','gg','pi','Pi', 'to'}, \
3:{'eta','Eta','phi','Phi','chi','Chi','psi','Psi','tau','Tau','rho','Rho','neg','geq','div','sim','cap','cup','vee','ell','bot','neq','not','mod',\
'leq','geq'}, \
4:{'beta','Beta','zeta','Zeta','iota','Iota','circ','serd','hbar','circ','perp','cdot','dots','Join','nleq','ngeq'},\
5:{'left{', 'left[', 'left|', 'alpha','Alpha','gamma','Gamma','kappa','Kappa','sigma','Sigma','omega','Omega','theta','Theta','angle',\
'infty','since','times','equiv','wedge','aleph','oplus','cdots','ddots','vdots','nabla','left('}, \
6:{'right}', 'right]', 'right|', 'lambda','Lambda','approx','propto','subset','supset','forall','square','otimes','right)'}, \
7:{'epsilon','Epsilon','upsilon','Upsilon','omicron','Omicron','nearrow','forsome','partial'}, \
8:{'subseteq','supseteq','emptyset','parallel'}, \
9:{'therefore','leftarrow','downarrow','textdollar','backslash'}, \
10:{'rightarrow'}, \
11:set(), \
12:set(), \
13:set(), \
14:{'leftrightarrow'} \
}

functionTags = {\
0:set(),\
1:set(),\
2:{'ln','lg','Pr'},\
3:{'exp','log','sin','cos','tan','csc','sec','cot','arg','max','min','sup','gcd','dim','ker','det','deg','hom'},\
4:{'sinh','cosh','tanh','coth'},\
5:set(),\
6:{'arcsin','arccos','arctan'} \
}

arrayTags = {\
0:set(), 1:set(), 2:set(), 3:set(), 4:set(),\
5:{'array'},\
6:set(),\
7:{'bmatrix','pmatrix','vmatrix'},\
8:set(), 9:set(), 10:set(), 11:set(), 12:set(), 13:set(), 14:set() \
}

accentTags = {\
0:set(), 1:set(), \
2:{'bf','rm'},\
3:{'hat','dot','vec','bar','cal'}, \
4:{'ddot'}, \
5:[],\
6:{'mathbf', 'mathrm','cancel'},\
7:{'mathcal'},\
8:{'overline'}, 9:set(), 10:set(), 11:set(), 12:set(), 13:{'overleftarrow'}, 14:{'overrightarrow'}, \
18:{'overleftrightarrow'} \
}

tags = {\
0:set(),\
1:{'{','}','&','%','#', '\\',','}, \
2:{'mu','Mu','nu','Nu','xi','Xi','pm','in','Re','ll','gg','pi','Pi',\
'ln','lg','Pr', 'to','bf','rm'}, \
3:{'hat', 'dot', 'vec', 'eta','Eta','phi','Phi','chi','Chi','psi','Psi','tau','Tau','rho','Rho','neg','geq','div','sim','cap','cup','vee','ell','bot','neq','not','mod',\
'leq','geq',\
'exp','log','sin','cos','tan','csc','sec','cot','arg','max','min','sup','gcd','dim','ker','det','deg','hom',\
'sum','int','lim', 'end','cal'}, \
4:{'ddot', 'beta','Beta','zeta','Zeta','iota','Iota','circ','serd','hbar','circ','perp','cdot','dots','Join','nleq','ngeq',\
'sinh','cosh','tanh','coth', 'frac','sqrt', 'prod', 'iint', 'oint'},\
5:{'left{', 'left[', 'left|','alpha','Alpha','gamma','Gamma','kappa','Kappa','sigma','Sigma','omega','Omega','theta','Theta','angle',\
'infty','since','times','equiv','wedge','aleph','oplus','cdots','ddots','vdots','nabla','left(',\
'binom', 'iiint', 'begin'}, \
6:{'mathbf', 'mathrm', 'cancel', 'right}', 'right]', 'right|', 'lambda','Lambda','approx','propto','subset','supset','forall','square','otimes','right)',\
'arcsin','arccos','arctan', 'iiiint'}, \
7:{'mathcal', 'epsilon','Epsilon','upsilon','Upsilon','omicron','Omicron','nearrow','forsome','partial'}, \
8:{'subseteq','supseteq','emptyset','parallel', 'idotsint','overline'}, \
9:{'therefore','leftarrow','downarrow','textdollar','backslash'}, \
10:{'rightarrow'}, \
11:set(), \
12:set(), \
13:{'overleftarrow'}, \
14:{'leftrightarrow','overrightarrow'}, \
18:{'overleftrightarrow'} \
}

mapEngThai_gTTS = {\
' ':'',\
'1':'หนึ่ง', '2':'สอง', '3':'สาม', '4':'สี่', '5':'ห้า', '6':'หก', '7':'เจ็ด', '8':'แปด', '9':'เก้า', '0':'ศูนย์', '1000000':'ล้าน',\
'100000':'แสน', '10000':'หมื่น', '1000':'พัน', '100':'ร้อย', '10':'สิบ', 'ed':'เอ็ด', 'yi':'ยี่',\
'a':'เอ', 'A':'เอพิมพ์ใหญ่', 'b':'บี', 'B':'บีพิมพ์ใหญ่', 'c':'ซี', 'C':'ซีพิมพ์ใหญ่', 'd':'ดี', 'D':'ดีพิมพ์ใหญ่', 'e':'อี', 'E':'อีพิมพ์ใหญ่', 'f':'เอฟ',\
 'F':'เอฟพิมพ์ใหญ่', 'g':'จี', 'G':'จีพิมพ์ใหญ่', 'h':'เฮช', 'H':'เฮชพิมพ์ใหญ่', 'i':'ไอ', 'I':'ไอพิมพ์ใหญ่', 'j':'เจ', 'J':'เจพิมพ์ใหญ่', \
 'k':'เค', 'K':'เคพิมพ์ใหญ่', 'l':'แอล', 'L':'แอลพิมพ์ใหญ่', 'm':'เอ็ม', 'M':'เอ็มพิมพ์ใหญ่', 'n':'เอ็น', 'N':'เอ็นพิมพ์ใหญ่', 'o':'โอ', 'O':'โอพิมพ์ใหญ่',\
 'p':'พี', 'P':'พีพิมพ์ใหญ่', 'q':'คิว', 'Q':'คิวพิมพ์ใหญ่', 'r':'อาร์', 'R':'อาร์พิมพ์ใหญ่', 's':'เอส', 'S':'เอสพิมพ์ใหญ่', 't':'ที', 'T':'ทีพิมพ์ใหญ่',\
 'u':'ยู', 'U':'ยูพิมพ์ใหญ่', 'v':'วี', 'V':'วีพิมพ์ใหญ่', 'w':'ดับเบิ้ลยู', 'W':'ดับเบิ้ลยูพิมพ์ใหญ่', 'x':'เอ็กซ์', 'X':'เอ็กซ์พิมพ์ใหญ่', 'y':'วาย', 'Y':'วายพิมพ์ใหญ่',\
 'z':'แซด', 'Z':'แซดพิมพ์ใหญ่',\
 '+':'บวก', '-':'ลบ', '*':'สตาร์', '/':'หาร', '^':'ยกกำลัง', '=':'เท่ากับ', '>':'มากกว่า', '<':'น้อยกว่า', ',':'คอมม่า', ':':'โคล่อน', ';':'เซมิโคล่อน',\
 '?':'เครื่องหมายคำถาม', '!':'แฟคทอเรียล', '\'':'ไพรม์', '.':'จุด', '(':'วงเล็บเปิด', ')':'วงเล็บปิด', '[':'วงเล็บก้ามปูเปิด', ']':'วงเล็บก้ามปูปิด',\
 '{':'วงเล็บปีกกาเปิด', '}':'วงเล็บปีกกาปิด','left|':'เริ่มแอ๊บโซลูท', 'right|':'จบแอ๊บโซลูท',\
 '|':'ขีดตรง', '_':'ห้อย', '\\\\':'ขึ้นบรรทัดใหม่', \
'left{':'วงเล็บปีกกาเปิด', 'right}':'วงเล็บปีกกาปิด', '&':'เครื่องหมายแอนด์', '%':'เปอร์เซ็นต์','#':'ชาร์ป',\
'left[':'วงเล็บก้ามปูเปิด', 'right]':'วงเล็บก้ามปูปิด', \
'mu':'มิว', 'Mu':'มิวพิมพ์ใหญ่', 'nu':'นิว', 'Nu':'นิวพิมพ์ใหญ่', 'xi':'ซี', 'Xi':'ซีพิมพ์ใหญ่', 'pm':'บวกลบ', 'in':'เป็นสมาชิกของเซต', 'Re':'อาร์พิมพ์ใหญ่สคริปต์', 'll':'น้อยกว่ามากมาก', 'gg':'มากกว่ามากมาก',\
'pi':'พาย', 'Pi':'พายพิมพ์ใหญ่',\
'eta':'อีต้า', 'Eta':'อีต้าพิมพ์ใหญ่', 'phi':'ฟี', 'Phi':'ฟีพิมพ์ใหญ่', 'chi':'ไค', 'Chi':'ไคพิมพ์ใหญ่', 'psi':'ไซ', 'Psi':'ไซพิมพ์ใหญ่', 'tau':'ทาล', 'Tau':'ทาลพิมพ์ใหญ่','rho':'โร',\
 'Rho':'โรพิมพ์ใหญ่', 'neg':'นิเสธ', 'geq':'มากกว่าหรือเท่ากับ', 'div':'หาร', 'sim':'คล้าย', 'cap':'อินเตอร์เซคชัน', 'cup':'ยูเนียน', 'vee':'หรือ', 'ell':'แอลสคริปต์', 'bot':'ตั้งฉาก', 'neq':'ไม่เท่ากับ',\
  'not':'ไม่', 'mod':'ม็อดดูโล', 'leq':'น้อยกว่าหรือเท่ากับ', 'geq':'มากกว่าหรือเท่ากับ', 'beta':'เบต้า', 'Beta':'เบต้าพิมพ์ใหญ่', 'zeta':'ซีต้า', 'Zeta':'ซีต้าพิมพ์ใหญ่', 'iota':'ไอโอต้า', 'Iota':'ไอโอต้า', 'circ':'วงกลม',\
   'perp':'ตั้งฉาก','cdot':'ดอท',\
  'dots':'จุดจุดจุด','Join':'จอย', 'nleq':'ไม่น้อยกว่าและเท่ากับ','ngeq':'ไม่มากกว่าหรือเท่ากับ', 'sqrt':'รากที่', 'root':'ตัวราก', \
  'alpha':'แอลฟา','Alpha':'แอลฟาพิมพ์ใหญ่','gamma':'แกมม่า','Gamma':'แกมม่่าพิมพ์ใหญ่','kappa':'คัป ป้า', 'Kappa':'คัปปาพิมพ์ใหญ่', 'sigma':'ซิกม่า', 'Sigma':'ซิกม่าพิมพ์ใหญ่', 'omega':'โอเมก้า', 'Omega':'โอเมก้าพิมพ์ใหญ่',\
   'theta':'ทีต้า', 'Theta':'ทีต้าพิมพ์ใหญ่', 'angle':'มุม', 'infty':'อินฟินีตี้', 'since':'เนื่องจาก', 'times':'คูณ', 'equiv':'สมมูลกับ', 'wedge':'และ', 'aleph':'เอวพ์', 'oplus':'เครื่องหมายบวกในวงกลม', 'cdots':'จุดจุดจุด',\
   'ddots':'จุดจุดจุดในแนวทแยงมุม', 'vdots':'จุดจุดจุดในแนวตั้ง', 'nabla':'นาบลา', 'left(':'วงเล็บเปิด',\
   'lambda':'แลมด้า', 'Lambda':'แลมด้าพิมพ์ใหญ่', 'approx':'ประมาณ', 'propto':'แปรผันตาม', 'subset':'เป็นสับเซตของ', 'supset':'เป็นซุปเปอร์เซตของ', 'forall':'ฟอร์ออล', 'square':'สี่เหลี่ยมจัตุรัส', 'otimes':'เครื่องหมายคูณในวงกลม',\
   'right)':'วงเล็บเปิด', 'epsilon':'เอปไซลอน', 'Epsilon':'เอปไซลอนพิมพ์ใหญ่', 'upsilon':'อัปไซลอน', 'Upsilon':'อัปไซลอนพิมพ์ใหญ่', 'omicron':'โอมิครอน', 'Omicron':'โอมิครอนพิมพ์ใหญ่', 'nearrow':'ลูกศรชี้ขวาบน', 'forsome':'ฟอร์ซัม',\
   'partial':'ดิฟเฟอรันเชียลย่อย',\
   'subseteq':'เป็นสับเซตหรือเท่ากับ', 'supseteq':'เป็นซุปเปอร์เซตหรือเท่ากับ', 'emptyset':'เซตว่าง', 'parallel':'ขนานกับ',\
   'therefore':'เพราะฉะนั้น', 'leftarrow':'ลูกศรชี้ซ้าย', 'downarrow':'ลูกศรชี้ล่าง','textdollar':'เครื่องหมายดอลล่า', 'backslash':'แบคสแลช',\
   'rightarrow':'ลูกศรชี้ขวา',\
   'leftrightarrow':'ลูกศรชี้สองทาง',\
   'ln':'ลอน', 'lg':'ล็อก', 'Pr':'ความน่าจะเป็น',\
   'exp':'เอ็กซ์โปเนนเชียล', 'log':'ล็อก', 'sin':'ไซน์', 'cos':'โคไซน์', 'tan':'แทนเจนต์', 'csc':'โคเซ็ก', 'sec':'เซ็ก', 'cot':'ค็อท',\
   'arg':'อาร์กิวเมนต์', 'max':'แม็กซิ มั่ม', 'min':'มินนิ มั่น', 'sup':'ซุพรีมั่ม', 'gcd':'ตัวหารร่วมมาก', 'dim':'ไดเมนชั่น', 'ker':'เคอร์เนล', 'det':'ดีเทอร์มิแนนต์', 'deg':'ดีกรี', 'hom':'โฮม ฟังเตอร์',\
   'sinh':'ไซน์ ไฮ เพอร์โบลิก','cosh':'โคไซน์ ไฮ เพอร์โบลิก','tanh':'แทนเจนต์ ไฮ เพอร์โบลิก','coth':'คอท ไฮ เพอร์โบลิก',\
   'of':'ของ', 'base':'ฐาน', 'endbase':'จบตัวฐาน', 'frac_start':'เศษ', 'frac_over':'ส่วน', 'frac_end':'เศษส่วน',\
   'arcsin':'อาคไซน์', 'arccos':'อาคโคไซน์', 'arctan':'อาคแทน',\
   'degree':'องศา',\
   'power':'ยกกำลัง', 'subscript':'ตัวห้อย', 'end':'จบ', 'all':'ทั้งหมด', 'parenthesisExp':'นิพจน์วงเล็บ', 'number':'จำนวน', 'level':'ชั้น', 'at':'ที่',\
   'open':'เปิด', 'openRadical':'เปิดราก', 'closeRadical':'ปิดราก',\
   'binom':'ทวินาม', 'choose':'เลือก',\
   'bigcup':'ยูเนียน', 'bigcap':'อินเตอร์เซคชัน', \
   'sum':'ซัมเม ชั่น', 'prod':'โปรดัก', 'from':'ตั้งแต่', 'toSum':'ถึง', 'where':'เมื่อ',\
    'int':'อินทิเกรต', 'referenceToVar':'เทียบกับตัวแปร',\
    'on':'บน', 'iint':'อินทิเกรตสองชั้น', 'iiint':'อินทิเกรตสามชั้น', 'iiiint':'อินทิเกรตสี่ชั้น', 'idotsint':'อินทิเกรตหลายชั้น', 'oint':'อินทิเกรตวงปิด',\
    'lim':'ลิมิต', 'to':'มีค่าย่างเข้า', \
    'accent':'กำกับด้วยเครื่องหมาย', 'hat':'หมวก', 'dot':'จุด', 'ddot':'จุดจุด', 'vec':'เวกเตอร์',\
    'bar':'บาร์', 'overleftarrow':'ลูกศรชี้ซ้าย', 'overrightarrow':'ลูกศรชี้ขวา', 'overleftrightarrow':'ลูกศรสองทาง', 'overline':'บาร์',\
    'segment':'ส่วนของเส้นตรง', 'ray':'รังสี', 'line':'เส้นตรง',\
    'cancel':'กำกับด้วยเครื่องหมายขีดฆ่า', 'mathbf':'ตัวหนา', 'mathrm':'ตัวปกติ', 'mathcal':'ตัวสคริปต์', \
    'bf':'ตัวหนา', 'cal':'ตัวสคริปต์',\
    'begin':'เริ่มต้น', 'end':'จบ', 'array':'ตาราง', 'bmatrix':'เมทริกซ์', 'pmatrix':'เมทริกซ์', 'vmatrix':'ดีเทอร์มิแนนต์', \
    'array':'ตาราง', 'nextRow':'ขึ้นแถวใหม่', 'start':'เริ่ม', 'nextElement':'ตัวถัดไป', 'blank':'ช่องว่าง', \
    'cases':'กรณี', 'where':'เมื่อ', 'for':'สำหรับ', 'power_superbrief':'กำลัง' \
    }

sound = dict()
sound[' '] = (' ', ' ')

for eng, thai in mapEngThai_gTTS.items():
    if eng != ' ':
        if 'A' <= eng <= 'Z':
            sound[eng] = (eng + '_upper', thai)
        elif eng == '%':
            sound[eng] = ('percent', thai)
        else:
            sound[eng] = (eng, thai)

def generatePrefixs(s):
    prefixs = []
    prefixLength = 14
    if len(s) < 14: prefixLength = len(s)
    for i in range(1,prefixLength+1):
        prefixs.append(s[:i])
    return prefixs

def readNumber(number):
    if number == '0':   return [sound['0']]
    tokens = []
    digit = len(number)
    g = digit
    idx = len(number)
    while(g > 0):
        d = g
        millionFlag = False
        if g > 7:
            d = d%7 + 1; millionFlag = True

        if d == 7:
            if(int(number[idx-g]) != 0):
                tokens.append(sound[number[idx-g]])
                tokens.append(sound['1000000'])
            g -= 1; d -= 1

        if d == 6:
            if(int(number[idx-g]) != 0):
                tokens.append(sound[number[idx-g]])
                tokens.append(sound['100000'])
            g -= 1; d -= 1

        if d == 5:
            if(int(number[idx-g]) != 0):
                tokens.append(sound[number[idx-g]])
                tokens.append(sound['10000'])
            g -= 1; d -= 1

        if d == 4:
            if(int(number[idx-g]) != 0):
                tokens.append(sound[number[idx-g]])
                tokens.append(sound['1000'])
            g -= 1; d -= 1

        if d == 3:
            if(int(number[idx-g]) != 0):
                tokens.append(sound[number[idx-g]])
                tokens.append(sound['100'])
            g -= 1; d -= 1

        if d == 2:
            if(int(number[idx-g]) != 0):
                if(int(number[idx-g]) == 2):
                    tokens.append(sound['yi'])
                elif(int(number[idx-g]) != 1):
                    tokens.append(sound[number[idx-g]])
                tokens.append(sound['10'])
            g -= 1; d -= 1

        if d == 1:
            if(int(number[idx-g]) == 1 and digit != 1):
                tokens.append(sound['ed'])
            elif(int(number[idx-g]) != 0):
                tokens.append(sound[number[idx-g]])
            g -= 1; d -= 1

        if millionFlag:
            tokens.append(sound['1000000'])

    return tokens

def isSymbol(c):
    return (c in string.ascii_letters + '+-*/>=<.,:;?!\'|()[]' + ' ')

def countExceptSpace(s):
    count = 0
    for c in s:
        if c != ' ':
            count += 1
    return count

def extractStackingExp(latex, idx):
    #parsing by stack
    parsingStack = [0]
    stackingExp = ''
    while(idx < len(latex) and len(parsingStack) > 0):
        if latex[idx] == '{':   parsingStack.append(0)
        elif latex[idx] == '}':   parsingStack.pop()
        stackingExp += latex[idx]
        idx += 1

    return stackingExp[:-1], idx

def extractParenthesisExp(latex, idx, delim):
    #parsing by stack
    # demim[0] --> ( and delim[1] --> )
    level = 0
    parsingStack = [level]
    stackingExp = ''
    while(idx < len(latex) and len(parsingStack) > 0):
        if latex[idx] == delim[0]:
            level += 1
            parsingStack.append(level)
        elif latex[idx] == delim[1]:
            parsingStack.pop()
        stackingExp += latex[idx]
        idx += 1

    return stackingExp[:-1], idx, level

def readArray(array, verbosity):
    tokens = []
    rowCount = 1
    #tokens.append(sound['rowNumber'])
    #tokens.append(sound[str(rowCount)])
    #tokens.append(sound['start'])
    i = 0

    while i < len(array):
        if i+1 < len(array) and array[i] == '\\' and array[i+1] == '\\':
            if tokens[-1] == sound['nextElement']:
                tokens = tokens[:-1]

            tokens.append(sound['\\\\'])
            rowCount += 1
            #tokens.append(sound['nextRow'])
            #tokens.append(sound[str(rowCount)])
            i += 2

        elif i < len(array) and array[i] == '&':
            #tokens.append(sound['nextElement'])
            i += 1

        else:
            exp = ''
            while i+1 < len(array) and array[i] != '&' and array[i:i+2] != '\\\\':
                exp += array[i]; i += 1
            #print(exp)
            if exp == '' or exp.isspace():
                tokens.append(sound['blank'])
                tokens.append(sound['nextElement'])
                tokens.append(sound[' '])
            else:
                expTokens = lexAnal(exp, verbosity)
                if verbosity == 'verbose':
                    if len(tokens) > 0  and tokens[-1] != sound['\\\\'] :
                        tokens.append(sound['nextElement'])
                    tokens.extend(expTokens)
                    tokens.append(sound['nextElement'])
                    tokens.append(sound[' '])

                elif verbosity == 'brief':
                    if len(expTokens) > 4 and len(tokens) > 0  and tokens[-1] != sound['\\\\'] :
                        tokens.append(sound['nextElement'])
                    tokens.extend(expTokens)
                    if len(expTokens) > 4:
                        tokens.append(sound['nextElement'])
                    tokens.append(sound[' '])
                elif verbosity == 'superbrief':
                    tokens.extend(expTokens)
                    tokens.append(sound[' '])
    #print(tokens)
    tokens = tokens[:-1]
    if tokens[-1] == sound['nextElement']:
        tokens = tokens[:-1]

    return tokens

def readCases(array, verbosity):
    tokens = []
    rowCount = 1
    #tokens.append(sound['cases'])
    #tokens.append(sound['at'])
    #tokens.append(sound[str(rowCount)])
    #tokens.append(sound['start'])
    i = 0

    while i < len(array):
        expTokens = []
        if i+1 < len(array) and array[i] == '\\' and array[i+1] == '\\':
            tokens.append(sound['nextRow'])
            rowCount += 1
            i += 2

        elif i < len(array) and array[i] == '&':
            tokens.append(sound['where'])
            i += 1

        else:
            exp = ''
            while i+1 < len(array) and array[i] != '&' and array[i:i+2] != '\\\\':
                exp += array[i]; i += 1
            #print(exp)
            if exp == '' or exp.isspace():
                tokens.append(sound['blank'])
                #tokens.append(sound['nextElement'])
            else:
                expTokens = lexAnal(exp, verbosity)
                tokens.extend(expTokens)
                #if len(expTokens) > 7:
                #    tokens.append(sound['nextElement'])
    #print(tokens)
    return tokens[:-1]

def cleanTokens(tokens):
    # when have accents '$'
    return list(filter(lambda x: x != '$' and x != '', tokens))

def extractThai(tokens):
    return [t[1] for t in tokens if t[0] != '$']

def extractSounds(tokens):
    return [t[0] for t in tokens if t[0] != '$']


def lexAnal(latex, verbosity):
    tokens = []
    idx = 0
    decimalFlag = False
    while(idx < len(latex)):
        if decimalFlag and latex[idx] == '.':
            tokens.append(sound['.'])
            idx += 1
            while(idx < len(latex) and '0' <= latex[idx] <= '9'):
                tokens.append(sound[latex[idx]])
                idx += 1
            decimalFlag = False
            continue

        if latex[idx].isnumeric():
            decimalFlag = True
            number = ''
            while(idx < len(latex) and '0' <= latex[idx] <= '9'):
                number += latex[idx]
                idx += 1
            tokens.extend(readNumber(number))
            continue

        if isSymbol(latex[idx]):
            if verbosity == 'superbrief' and latex[idx] == '^':
                tokens.append(sound['power_superbrief'])
            else:
                tokens.append(sound[latex[idx]])
            idx += 1
            continue

        ''' tag ---------------------------------------- '''
        if latex[idx] == '\\':
            idx += 1
            tag = ''

            prefixs = generatePrefixs(latex[idx:])
            foundTag = False
            for p in prefixs:
                if p in tags[len(p)]:
                    tag = p
                    foundTag = True

            if not foundTag:
                raise Exception()

            idx += len(tag)

            if tag == 'begin':
                tokens.append(sound['begin'])
                if latex[idx] == '{':
                    idx += 1
                    pattern = ''
                    while latex[idx] != '}':
                        pattern += latex[idx]; idx += 1

                    if pattern in arrayTags[len(pattern)]:
                        #print(pattern)
                        tokens.append(sound[pattern])
                        if pattern == 'bmatrix':
                            tokens.append(sound['['])
                        elif pattern == 'pmatrix':
                            tokens.append(sound['('])
                        elif pattern == 'vmatrix':  # absolute of a matrix
                            tokens.append(sound['of'])
                            tokens.append(sound['bmatrix'])

                        idx += 1

                        arrayPart = ''
                        while(idx + 3 < len(latex) and latex[idx:idx+4] != '\\end'):
                            arrayPart += latex[idx]; idx += 1
                        #print('array:',arrayPart)
                        tokens.extend(readArray(arrayPart+'\\\\', verbosity))

                        if latex[idx:idx+4] == '\\end':

                            if pattern == 'bmatrix':
                                tokens.append(sound['end'])
                                tokens.append(sound[pattern])
                                tokens.append(sound[']'])
                            elif pattern == 'pmatrix':
                                tokens.append(sound['end'])
                                tokens.append(sound[pattern])
                                tokens.append(sound[')'])
                            elif pattern == 'vmatrix':  # absolute of a matrix
                                tokens.append(sound['end'])
                                tokens.append(sound['bmatrix'])

                            while latex[idx] != '}':
                                idx += 1
                            idx += 1

                    elif pattern == 'cases':
                        #print(pattern)
                        tokens.append(sound['cases'])

                        idx += 1

                        casesPart = ''
                        while(idx + 3 < len(latex) and latex[idx:idx+4] != '\\end'):
                            casesPart += latex[idx]; idx += 1
                        tokens.extend(readCases(casesPart+'\\\\', verbosity))

                        if latex[idx:idx+4] == '\\end':
                            tokens.append(sound['end'])
                            tokens.append(sound['cases'])

                            while latex[idx] != '}':
                                idx += 1
                            idx += 1
                    else:
                        raise Exception()

                #print('eiei',latex[idx])
                continue

            if tag in symbolTags[len(tag)]:
                #print('*',tag)
                if tag == ',':
                    tokens.append(sound['referenceToVar'])
                else:
                    tokens.append(sound[tag])
                continue
                #print('*',tag)

            elif tag in functionTags[len(tag)]:
                tokens.append(sound[tag])
                if idx >= len(latex):   continue

                # handling subscript and superscript
                if latex[idx] == '_':
                    if tag == 'log':
                        tokens.append(sound['base'])
                    else:
                        tokens.append(sound['_'])
                    idx += 1
                    if latex[idx] == '{':
                        idx += 1

                        #parsing by stack
                        subscript, idx = extractStackingExp(latex,idx)
                        subscriptTokens = lexAnal(subscript,verbosity)
                        tokens.extend(subscriptTokens)

                        # ------ verbosity -------
                        if verbosity == 'verbose':
                            tokens.append(sound['end'])
                            if tag == 'log':
                                tokens.append(sound['base'])
                            else:
                                tokens.append(sound['subscript'])

                        elif verbosity == 'brief':
                            if len(subscript) > 4:
                                tokens.append(sound['end'])
                                if tag == 'log':
                                    tokens.append(sound['base'])
                                else:
                                    tokens.append(sound['subscript'])

                    else:
                        subscript = ''
                        if latex[idx] == '\\':
                            subscript = latex[idx]
                            idx += 1

                        while(latex[idx] != ' ' and latex[idx] != '\\' and latex[idx] != '{'):
                            subscript += latex[idx]; idx += 1

                        tokens.extend(lexAnal(subscript,verbosity))

                elif latex[idx] == '^':
                    if verbosity == 'verbose':
                        tokens.append(sound['start'])
                        tokens.append(sound['power'])
                    elif verbosity == 'brief':
                        tokens.append(sound['power'])
                    elif verbosity == 'superbrief':
                        tokens.append(sound['power_superbrief'])

                    idx += 1
                    if latex[idx] == '{':
                        idx += 1

                        #parsing by stack
                        superscript, idx = extractStackingExp(latex,idx)

                        tokens.extend(lexAnal(superscript,verbosity))

                        # ------ verbosity ------
                        if verbosity == 'verbose':
                            tokens.append(sound['end'])
                            tokens.append(sound['power'])

                        elif verbosity == 'brief':
                            if len(superscript) > 4:
                                tokens.append(sound['end'])
                                tokens.append(sound['power'])

                    else:
                        superscript = ''
                        if latex[idx] == '\\':
                            superscript = latex[idx]
                            idx += 1

                        while(latex[idx] != ' ' and latex[idx] != '\\' and latex[idx] != '{'):
                            superscript += latex[idx]; idx += 1

                        tokens.extend(lexAnal(superscript, verbosity))

                # handling argument
                if latex[idx] == '{':
                    tokens.append(sound['of'])
                    argument = ''
                    idx += 1

                    argument, idx = extractStackingExp(latex,idx)

                    argumentTokens = lexAnal(argument, verbosity)
                    tokens.extend(argumentTokens)

                    # ------ verbosity ------
                    if verbosity == 'verbose':
                        tokens.append(sound['end'])
                        tokens.append(sound[tag])
                        tokens.append(sound[' '])
                        tokens.append(sound[' '])

                    elif verbosity == 'brief':
                        tokens.append(sound['end'])
                        tokens.append(sound[tag])
                        tokens.append(sound[' '])
                        tokens.append(sound[' '])

                    elif verbosity == 'superbrief':
                        tokens.append(sound[' '])
                        tokens.append(sound[' '])

                    idx += 1

                continue

            elif tag in accentTags[len(tag)]:
                accents = []
                accents.append(sound[tag])
                #idx += 1
                if latex[idx] == '{':
                    idx += 1
                    argument, idx = extractStackingExp(latex, idx)
                    if argument[0] != '\\':
                        argumentTokens = lexAnal(argument, verbosity)
                        if countExceptSpace(argumentTokens) > 1:
                            accents.extend(['$']+[' '.join(argumentTokens+[sound['all']])]+[''])
                        else:
                            accents.extend(['$']+[' '.join(argumentTokens)]+[''])

                    else:
                        accents.extend(['$']+[' '.join(lexAnal(argument, verbosity))])
                else:
                    argument = ''
                    while(latex[idx] == ' '):
                        idx += 1
                    argument = latex[idx]
                    idx += 1
                    accents.append('$')
                    accents.append(argument)

                # bring argument to the front
                if '$' in accents:
                    argIndex = accents.index('$')
                    accents = [accents[argIndex+1]] + accents[:argIndex] + accents[argIndex+2:]
                #print(accents)
                tokens.extend(accents)
                continue

            elif tag == 'frac':
                #tokens.append(sound['frac_start'])
                numeratorTokens = []
                denominatorTokens = []
                if latex[idx] == '{':
                    idx += 1
                    numerator, idx = extractStackingExp(latex, idx)
                    #print(numerator)
                    numeratorTokens = lexAnal(numerator, verbosity)

                    # ------ verbosity -------
                    if verbosity == 'verbose':
                        tokens.append(sound['start'])
                        tokens.append(sound['frac_start'])
                        tokens.append(sound[' '])

                    elif verbosity == 'brief':
                        if len(numeratorTokens) >= 3 and len(numerator) > 4:
                            tokens.append(sound['start'])
                            tokens.append(sound['frac_start'])
                            tokens.append(sound[' '])
                        else:
                            tokens.append(sound['frac_start'])

                    elif verbosity == 'superbrief':
                        tokens.append(sound['frac_start'])

                    tokens.extend(numeratorTokens)
                    #tokens.append(sound[' '])
                    #tokens.append(sound[' '])
                    if verbosity == 'verbose':
                        tokens.append(sound['end'])
                        tokens.append(sound['frac_start'])
                        tokens.append(sound[' '])

                    elif verbosity == 'brief':
                        if len(numeratorTokens) >= 3 and len(numerator) > 4:
                            #tokens.append(sound['all'])
                            tokens.append(sound['end'])
                            tokens.append(sound['frac_start'])
                            tokens.append(sound[' '])

                    #elif verbosity == 'superbrief':

                    # search for '{' during blank spaces
                    while latex[idx] == ' ':    idx += 1

                    if latex[idx] == '{':
                        tokens.append(sound['frac_over'])

                        idx += 1
                        denominator, idx = extractStackingExp(latex, idx)
                        denominatorTokens = lexAnal(denominator, verbosity)

                        if verbosity == 'verbose':
                            tokens.append(sound[' '])
                            tokens.append(sound['start'])
                            tokens.append(sound['frac_over'])
                            tokens.append(sound[' '])

                        elif verbosity == 'brief':
                            if len(denominatorTokens) >= 3 and len(denominator) > 4:
                                tokens.append(sound[' '])
                                tokens.append(sound['start'])
                                tokens.append(sound['frac_over'])
                                tokens.append(sound[' '])
                        #elif verbosity == 'superbrief':

                        tokens.extend(denominatorTokens)

                        if verbosity == 'verbose':
                            tokens.append(sound['end'])
                            tokens.append(sound['frac_end'])
                        elif verbosity == 'brief':
                            if len(denominatorTokens) >= 3 and len(denominator) > 4:
                                tokens.append(sound['end'])
                                tokens.append(sound['frac_end'])
                                #tokens.append(sound[' '])
                                #tokens.append(sound[' '])

                        tokens.append(sound[' '])
                        tokens.append(sound[' '])

                    else:
                        raise Exception()

                continue

            elif tag == 'sqrt':

                order = '2'
                orderTokens = [sound['2']]

                while latex[idx] == ' ':    idx += 1

                if latex[idx] == '[':
                    idx += 1
                    order, idx, _ = extractParenthesisExp(latex, idx, '[]')
                    orderTokens = lexAnal(order, verbosity)
                    #tokens.extend(lexAnal(order, verbosity))

                while latex[idx] == ' ':    idx += 1

                if latex[idx] == '{':
                    idx += 1
                    argument, idx = extractStackingExp(latex, idx)
                    argumentTokens = lexAnal(argument, verbosity)

                else:
                    raise Exception()
                    '''
                    argument = latex[idx]
                    idx += 1
                    argumentTokens = lexAnal(argument, verbosity)
                    '''

                # reading sqrt with arguments
                if verbosity == 'verbose':
                    tokens.append(sound['open'])
                elif verbosity == 'brief':
                    if len(argumentTokens) >= 3:
                        tokens.append(sound['open'])

                tokens.append(sound['sqrt'])
                tokens.extend(orderTokens)

                tokens.append(sound['of'])

                tokens.extend(argumentTokens)

                if verbosity == 'verbose':
                    tokens.append(sound['closeRadical'])
                elif verbosity == 'brief':
                    if len(argumentTokens) >= 3:
                        tokens.append(sound['closeRadical'])

                # gap
                tokens.append(sound[' '])
                tokens.append(sound[' '])

                continue

            elif tag == 'binom':
                tokens.append(sound['binom'])

                if latex[idx] == ' ':   idx += 1

                if latex[idx] == '{':
                    idx += 1
                    upper, idx = extractStackingExp(latex, idx)
                    tokens.extend(lexAnal(upper, verbosity))
                    tokens.append(sound['choose'])

                    if latex[idx] == '{':
                        idx += 1
                        lower, idx = extractStackingExp(latex, idx)
                        tokens.extend(lexAnal(lower, verbosity))
                        tokens.append(sound['end'])
                        tokens.append(sound['binom'])
                    else:
                        raise Exception()
                else:
                    raise Exception()

                continue

            elif tag == 'lim':
                tokens.append(sound['lim'])
                tokens.append(sound['where'])
                if latex[idx] == '_':
                    idx += 1
                    if latex[idx] == '{':
                        idx += 1
                        lower, idx = extractStackingExp(latex, idx)
                    else:
                        lower = latex[idx]; idx += 1
                    tokens.extend(lexAnal(lower, verbosity))
                    tokens.append(sound['of'])
                    if latex[idx] == '{':
                        idx += 1
                        argument, idx = extractStackingExp(latex, idx)
                        tokens.extend(lexAnal(argument, verbosity))
                continue

            elif tag in ['sum','prod','int','bigcup','bigcap']:
                isHasBothLowerUpper = False
                tokens.append(sound[tag])

                if latex[idx] == '_':
                    idx += 1
                    if latex[idx] == '{':
                        idx += 1
                        lower, idx = extractStackingExp(latex, idx)
                    else:
                        lower = latex[idx]; idx += 1

                    if latex[idx] == '^':
                        idx += 1
                        isHasBothLowerUpper = True
                        if latex[idx] == '{':
                            idx += 1
                            upper, idx = extractStackingExp(latex, idx)
                        else:
                            upper = latex[idx]; idx += 1

                    if isHasBothLowerUpper:
                        tokens.append(sound['from'])
                        tokens.extend(lexAnal(lower, verbosity))
                        tokens.append(sound['toSum'])
                        tokens.extend(lexAnal(upper, verbosity))
                    else:
                        tokens.append(sound['for'])
                        tokens.extend(lexAnal(lower, verbosity))

                    tokens.append(sound[' '])
                    tokens.append(sound[' '])

                tokens.append(sound['of'])
                continue

            elif tag in ['iint', 'iiint', 'iiiint', 'oint']:
                tokens.append(sound[tag])
                if latex[idx] == '_':
                    idx += 1
                    if latex[idx] == '{':
                        idx += 1
                        lower, idx = extractStackingExp(latex, idx)
                    else:
                        lower = latex[idx]; idx += 1

                    tokens.append(sound['on'])
                    tokens.extend(lexAnal(lower, verbosity))
                tokens.append(sound['of'])
                continue

        if latex[idx] == '^':
            idx += 1
            if latex[idx] == '{':
                idx += 1
                superscript, idx = extractStackingExp(latex, idx)
                if superscript == '\\circ':
                    tokens.append(sound['degree'])
                    continue

                superscriptTokens = lexAnal(superscript, verbosity)

                if verbosity == 'verbose':
                    tokens.append(sound['start'])
                    tokens.append(sound['power'])
                    tokens.extend(superscriptTokens)
                    tokens.append(sound['end'])
                    tokens.append(sound['power'])

                elif verbosity == 'brief':
                    if len(superscriptTokens) >= 3:
                        tokens.append(sound['start'])
                        tokens.append(sound['power'])
                        tokens.extend(superscriptTokens)
                        tokens.append(sound['end'])
                        tokens.append(sound['power'])
                    else:
                        tokens.append(sound['power'])
                        tokens.extend(superscriptTokens)

                elif verbosity == 'superbrief':
                    tokens.append(sound['power_superbrief'])
                    tokens.extend(superscriptTokens)

                tokens.append(sound[' '])
                tokens.append(sound[' '])

            elif latex[idx:idx+5] == '\\circ':
                tokens.append(sound['degree'])
                idx += 5
            else:
                if verbosity == 'verbose':
                    tokens.append(sound['start'])
                    tokens.append(sound['power'])
                    tokens.append(sound[latex[idx]])
                    tokens.append(sound['end'])
                    tokens.append(sound['power'])
                    idx += 1
                elif verbosity == 'brief':
                    tokens.append(sound['power'])
                    tokens.append(sound[latex[idx]])
                elif verbosity == 'superbrief':
                    tokens.append(sound['power_superbrief'])
                    tokens.append(sound[latex[idx]])

                idx += 1
                tokens.append(sound[' '])
                tokens.append(sound[' '])

            continue

        if latex[idx] == '_':
            idx += 1
            if latex[idx] == '{':
                idx += 1
                subscript, idx = extractStackingExp(latex, idx)
                subscriptTokens = lexAnal(subscript, verbosity)

                if verbosity == 'verbose':
                    tokens.append(sound['start'])
                    tokens.append(sound['subscript'])
                    tokens.extend(subscriptTokens)
                    tokens.append(sound['end'])
                    tokens.append(sound['subscript'])

                elif verbosity == 'brief':
                    if len(subscriptTokens) >= 3:
                        tokens.append(sound['start'])
                        tokens.append(sound['subscript'])
                        tokens.extend(subscriptTokens)
                        tokens.append(sound['end'])
                        tokens.append(sound['subscript'])
                    else:
                        tokens.append(sound['_'])
                        tokens.extend(subscriptTokens)

                elif verbosity == 'superbrief':
                    #tokens.append(sound['_'])
                    tokens.extend(subscriptTokens)

                tokens.append(sound[' '])
                tokens.append(sound[' '])

            continue

    return tokens
