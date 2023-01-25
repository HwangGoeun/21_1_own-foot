from tkinter import *
import webbrowser


def callback(url):
    webbrowser.open_new(url)


window = Tk()
window.title("Own Foot")
window.geometry("600x400")

brandframe = Frame(window)
bollframe = Frame(window)
archieframe = Frame(window)

text = ["발 볼은 넓은 편인가요?", "발 아치는 어떤 모양인가요?", "선호하는 브랜드는?"]
ball = 0
archii = 0


def ball1():
    global ball
    ball = 1


def ball2():
    global ball
    ball = 2


def ball3():
    global ball
    ball = 3


def archii1():
    global archii
    archii = 1


def archii2():
    global archii
    archii = 2


def archii3():
    global archii
    archii = 3


def boll():
    global i, ball

    label = Label(window)
    label['text'] = text[i]
    label.pack()

    LBt = Button(bollframe, text="넓음", command=ball1)
    MBt = Button(bollframe, text="보통", command=ball2)
    SBt = Button(bollframe, text="좁음", command=ball3)
    LBt.pack(side=LEFT)
    MBt.pack(side=LEFT)
    SBt.pack(side=LEFT)

    bollframe.pack()


def archie():
    global i, archii

    label = Label(window)
    label['text'] = text[i]
    label.pack()

    hBt = Button(archieframe, text="높음", command=archii1)
    mBt = Button(archieframe, text="보통", command=archii2)
    lBt = Button(archieframe, text="낮음(평발)", command=archii3)
    hBt.pack(side=LEFT)
    mBt.pack(side=LEFT)
    lBt.pack(side=LEFT)

    archieframe.pack()


e1 = Entry(window)
shoe = "당신의 신발은?!"
e1.delete(0, END)
e1.insert(0, str(shoe))
link1 = Label(window, text="신발 구매하러 가기", fg="blue", cursor="hand2")


def adidas():
    global ball, archii
    if (ball == 1):
        if (archii == 1):
            shoe = "아디다스 슈퍼스타, 정사이즈"
            link1.bind("<Button-1>", lambda e: callback("https://search.shopping.naver.com/catalog/23454748293?query=%EC%95%84%EB%94%94%EB%8B%A4%EC%8A%A4%20%EC%8A%88%ED%8D%BC%EC%8A%A4%ED%83%80&NaPm=ct%3Dkqn3ns20%7Cci%3Dc80c7212bec693379fbb9497552cf26576d9767d%7Ctr%3Dslsl%7Csn%3D95694%7Chk%3Dbace937245956301ead5cd983d012fd6c9ca2ef4"))
            e1.delete(0, END)
            e1.insert(0, str(shoe))
        elif (archii == 2):
            shoe = "아디다스 튜블라 둠 PK, 정사이즈"
            link1.bind("<Button-1>", lambda e: callback("https://search.shopping.naver.com/catalog/12738744378?cat_id=50003854&frm=NVSCPRO&query=%EC%95%84%EB%94%94%EB%8B%A4%EC%8A%A4+%ED%8A%9C%EB%B8%94%EB%9D%BC+%EB%91%A0&NaPm=ct%3Dkqn40bg0%7Cci%3Dd57d4cb688ec65c7d29527aa4cb66217e674b9fa%7Ctr%3Dsls%7Csn%3D95694%7Chk%3D5b95deeed03e05a40f1f02fe10195eafa0bc5b2c"))
            e1.delete(0, END)
            e1.insert(0, str(shoe))
        else:
            shoe = "아디다스 스탠스미스, 한 치수 작게"
            link1.bind("<Button-1>", lambda e: callback("https://search.shopping.naver.com/catalog/23001492177?cat_id=50000788&frm=NVSCVUI&query=%EC%95%84%EB%94%94%EB%8B%A4%EC%8A%A4+%EC%8A%A4%ED%83%A0%EC%8A%A4%EB%AF%B8%EC%8A%A4&NaPm=ct%3Dkqn42pv4%7Cci%3D36c06daaa97d99448ddec287e3f82e9e13da730d%7Ctr%3Dsls%7Csn%3D95694%7Chk%3D059aef0ce26ae880055ac4689e1dcd380c4d893f"))
            e1.delete(0, END)
            e1.insert(0, str(shoe))
    elif (ball == 2):
        if (archii == 1):
            shoe = "아디다스 슈퍼스타, 반사이즈 다운"
            link1.bind("<Button-1>", lambda e: callback("https://search.shopping.naver.com/catalog/23454748293?query=%EC%95%84%EB%94%94%EB%8B%A4%EC%8A%A4%20%EC%8A%88%ED%8D%BC%EC%8A%A4%ED%83%80&NaPm=ct%3Dkqn3ns20%7Cci%3Dc80c7212bec693379fbb9497552cf26576d9767d%7Ctr%3Dslsl%7Csn%3D95694%7Chk%3Dbace937245956301ead5cd983d012fd6c9ca2ef4"))
            e1.delete(0, END)
            e1.insert(0, str(shoe))
        elif (archii == 2):
            shoe = "아디다스 듀라모 9, 정사이즈"
            link1.bind("<Button-1>", lambda e: callback("https://search.shopping.naver.com/catalog/15915225825?cat_id=50003854&frm=NVSCPRO&query=%EC%95%84%EB%94%94%EB%8B%A4%EC%8A%A4+%EB%93%80%EB%9D%BC%EB%AA%A89&NaPm=ct%3Dkqn49t9k%7Cci%3D1636652fbcd42e472ce29eb74e24c66a395b1070%7Ctr%3Dsls%7Csn%3D95694%7Chk%3D83d7a015d4196787e684356a10c7bfee180bbfad"))
            e1.delete(0, END)
            e1.insert(0, str(shoe))
        else:
            shoe = "아디다스 튜블라 쉐도우 CK, 반 치수 작게"
            link1.bind("<Button-1>", lambda e: callback("https://search.shopping.naver.com/catalog/14969764800?query=%EC%95%84%EB%94%94%EB%8B%A4%EC%8A%A4%20%ED%8A%9C%EB%B8%94%EB%9D%BC%20%EC%89%90%EB%8F%84%EC%9A%B0&NaPm=ct%3Dkqn4ahyg%7Cci%3Da6a27d2f722c3811ef14490b0535a9cb1bab0b14%7Ctr%3Dslsl%7Csn%3D95694%7Chk%3Df89e02367d52e14df20dae1630caa8fe75751040"))
            e1.delete(0, END)
            e1.insert(0, str(shoe))
    else:
        if (archii == 1):
            shoe = "아디다스 알파바운스 1, 한 사이즈 업"
            link1.bind("<Button-1>", lambda e: callback("https://search.shopping.naver.com/catalog/24201172677?query=%EC%95%84%EB%94%94%EB%8B%A4%EC%8A%A4%20%EC%95%8C%ED%8C%8C%EB%B0%94%EC%9A%B4%EC%8A%A4%201&NaPm=ct%3Dkqn4bnmg%7Cci%3De9bfddc9d7d091d1a4df2cfbf7cf45b9283ba2f1%7Ctr%3Dslsl%7Csn%3D95694%7Chk%3D6a05624c8d4666777cf91ab0c3e0c64a1a8b62c8"))
            e1.delete(0, END)
            e1.insert(0, str(shoe))
        elif(archii == 2):
            shoe = "아디다스 드레곤 OG, 정사이즈"
            link1.bind("<Button-1>", lambda e: callback("https://search.shopping.naver.com/catalog/19982758525?query=%EC%95%84%EB%94%94%EB%8B%A4%EC%8A%A4%20%EB%93%9C%EB%9E%98%EA%B3%A4&NaPm=ct%3Dkqn4c654%7Cci%3D140ed5565b28dbf01bf942b05c30ce0375d1cf05%7Ctr%3Dslsl%7Csn%3D95694%7Chk%3Dcf9747489c933962825dd2052c003c110c8d7677"))
            e1.delete(0, END)
            e1.insert(0, str(shoe))
        else:
            shoe = "아디다스 이큅먼트 10, 반 치수 업"
            link1.bind("<Button-1>", lambda e: callback("https://search.shopping.naver.com/catalog/21925726520?query=%EC%95%84%EB%94%94%EB%8B%A4%EC%8A%A4%20%EC%9D%B4%ED%81%85%EB%A8%BC%ED%8A%B8%2010&NaPm=ct%3Dkqn4cu28%7Cci%3D6027ca5f7c4caeb221dc5de55e0ce98329dd67a2%7Ctr%3Dslsl%7Csn%3D95694%7Chk%3D3019c59b7c3e44713e31d88543c4475322614cc7"))
            e1.delete(0, END)
            e1.insert(0, str(shoe))
    
    e1.pack(fill=BOTH, expand =1)
    link1.pack(fill = Y)
            

def nike():
    global ball, archii
    
    if(ball == 1):
        if(archii == 1):
            shoe = "나이키 레볼루션, 정사이즈"
            link1.bind("<Button-1>", lambda e: callback("https://search.shopping.naver.com/catalog/21715897896?query=%EB%82%98%EC%9D%B4%ED%82%A4%20%EB%A0%88%EB%B3%BC%EB%A3%A8%EC%85%98&NaPm=ct%3Dkqn4lh0o%7Cci%3D79c8cd3c48bcc2b273709954405e7f75f95be2d4%7Ctr%3Dslsl%7Csn%3D95694%7Chk%3D4daa997b67281828f2c0790e578a326821045920"))
            e1.delete(0, END)
            e1.insert(0, str(shoe))
        elif(archii == 2):
            shoe = "나이키 테일 윈드 79, 반 사이즈 업"
            link1.bind("<Button-1>", lambda e: callback("https://search.shopping.naver.com/catalog/27361155601?query=%EB%82%98%EC%9D%B4%ED%82%A4%20%ED%85%8C%EC%9D%BC%EC%9C%88%EB%93%9C%2079&NaPm=ct%3Dkqn4kxq8%7Cci%3D0f1fcd1be93273cabd800cae6fe3cac5803f6173%7Ctr%3Dslsl%7Csn%3D95694%7Chk%3D46642172bf9e8ff632f7f8a9d9dbb244f93a9bd4"))
            e1.delete(0, END)
            e1.insert(0, str(shoe))
        else:
            shoe = "나이키 조던 MA2, 정사이즈"
            link1.bind("<Button-1>", lambda e: callback("https://search.shopping.naver.com/catalog/26856673329?query=%EB%82%98%EC%9D%B4%ED%82%A4%20%EC%A1%B0%EB%8D%98%20MA2&NaPm=ct%3Dkqn4kbco%7Cci%3D27896e486b516fd2b06110b019f8239adc2ef864%7Ctr%3Dslsl%7Csn%3D95694%7Chk%3D597fa8d866012d5f601bf075b0d6b0aeb5f78dc1"))
            e1.delete(0, END)
            e1.insert(0, str(shoe))
    elif(ball == 2):
        if(archii == 1):
            shoe = "나이키 에어 테일윈드 79, 정사이즈"
            link1.bind("<Button-1>", lambda e: callback("https://search.shopping.naver.com/catalog/27361155601?query=%EB%82%98%EC%9D%B4%ED%82%A4%20%ED%85%8C%EC%9D%BC%EC%9C%88%EB%93%9C%2079&NaPm=ct%3Dkqn4kxq8%7Cci%3D0f1fcd1be93273cabd800cae6fe3cac5803f6173%7Ctr%3Dslsl%7Csn%3D95694%7Chk%3D46642172bf9e8ff632f7f8a9d9dbb244f93a9bd4"))
            e1.delete(0, END)
            e1.insert(0, str(shoe))
        elif(archii == 2):
            shoe = "나이키 데이브레이크, 정사이즈"
            link1.bind("<Button-1>", lambda e: callback("https://search.shopping.naver.com/catalog/26713288122?query=%EB%82%98%EC%9D%B4%ED%82%A4%20%EB%8D%B0%EC%9D%B4%EB%B8%8C%EB%A0%88%EC%9D%B4%ED%81%AC&NaPm=ct%3Dkqn4o3xc%7Cci%3Db1ee97f8cfbf09dbaa9ddbb84943b5425963a45e%7Ctr%3Dslsl%7Csn%3D95694%7Chk%3D26d2409387c073e33fa64b9373077931924afc77"))
            e1.delete(0, END)
            e1.insert(0, str(shoe))
        else:
            shoe = "나이키 클래식 코르테즈 레더 스니커즈, 정사이즈"
            link1.bind("<Button-1>", lambda e: callback("https://search.shopping.naver.com/catalog/9935061904?query=%EB%82%98%EC%9D%B4%ED%82%A4%20%ED%81%B4%EB%9E%98%EC%8B%9D%20%EC%BD%94%EB%A5%B4%ED%85%8C%EC%A6%88%20%EB%A0%88%EB%8D%94&NaPm=ct%3Dkqn4p7a0%7Cci%3Df21c1c4597c19d6ebf41cebb53f100c657f55860%7Ctr%3Dslsl%7Csn%3D95694%7Chk%3Db0c237cce891a49754a4ed4d925ccc180832cd7b"))
            e1.delete(0, END)
            e1.insert(0, str(shoe))
    else:
        if(archii == 1):
            shoe = "나이키 포스 1 토글, 반 사이즈 업"
            link1.bind("<Button-1>", lambda e: callback("https://search.shopping.naver.com/catalog/25380860383?query=%EB%82%98%EC%9D%B4%ED%82%A4%20%ED%8F%AC%EC%8A%A4%20%ED%86%A0%EA%B8%80%201&NaPm=ct%3Dkqn4s5rc%7Cci%3D86f6a0da3d551ba40697607bf8310da744da700c%7Ctr%3Dslsl%7Csn%3D95694%7Chk%3D78b14d23a89642eaf4f1429c226f41a761b2ad65"))
            e1.delete(0, END)
            e1.insert(0, str(shoe))
        elif(archii == 2):
            shoe = "나이키 스타러너2 GS, 한 사이즈 업"
            link1.bind("<Button-1>", lambda e: callback("https://search.shopping.naver.com/catalog/20770686536?query=%EB%82%98%EC%9D%B4%ED%82%A4%20%EC%8A%A4%ED%83%80%EB%9F%AC%EB%84%882%20GS&NaPm=ct%3Dkqn4sp1s%7Cci%3D921d1b5bb38f386a1631bf6c7cc1318c7fa0e300%7Ctr%3Dslsl%7Csn%3D95694%7Chk%3D76a0a93b32e1e507a1030d115504d2d835796420"))
            e1.delete(0, END)
            e1.insert(0, str(shoe))
        else:
            shoe = "나이키 에어맥스 디아, 반 치수 업"
            link1.bind("<Button-1>", lambda e: callback("https://search.shopping.naver.com/catalog/24629096247?query=%EB%82%98%EC%9D%B4%ED%82%A4%20%EC%97%90%EC%96%B4%EB%A7%A5%EC%8A%A4%20%EB%94%94%EC%95%84&NaPm=ct%3Dkqn4t7kg%7Cci%3D34e2f8a7346c2334272568d00f3141b77a6ae3fd%7Ctr%3Dslsl%7Csn%3D95694%7Chk%3D65d9dd9ad81cc6687838d1fe2bc5bb5e0587d19d"))
            e1.delete(0, END)
            e1.insert(0, str(shoe))
    e1.pack(fill=BOTH, expand =1)
    link1.pack(fill = Y)
    
def vans():
    global ball, archii
    
    if(ball == 1):
        if(archii == 1):
            shoe = "반스 서피스, 정사이즈"
            link1.bind("<Button-1>", lambda e: callback("https://search.shopping.naver.com/catalog/19013986401?query=%EB%B0%98%EC%8A%A4%20%EC%84%9C%ED%94%BC%EC%8A%A4&NaPm=ct%3Dkqn4u0w0%7Cci%3Df1d11a5e610b326cba89e20c76ce3241cdf5eb44%7Ctr%3Dslsl%7Csn%3D95694%7Chk%3D7e1ae593f6308235bcf32ea6c630bf562a18f6b5"))
            e1.delete(0, END)
            e1.insert(0, str(shoe))
        elif(archii == 2):
            shoe = "반스 리퍼, 정사이즈"
            link1.bind("<Button-1>", lambda e: callback("https://smartstore.naver.com/thesutreet/products/5083358565?NaPm=ct%3Dkqn4vsxk%7Cci%3D972bab5e9d7dda29baff1498ab6f30810e2342ad%7Ctr%3Dslsl%7Csn%3D1184748%7Chk%3Df628fc4ed8f77a209adeb1bc69d015042023baa4"))
            e1.delete(0, END)
            e1.insert(0, str(shoe))
        else:
            shoe = "반스 스케이트 하이 38 DX, 한 사이즈 업"
            link1.bind("<Button-1>", lambda e: callback("https://smartstore.naver.com/doubbleg/products/5647703723?NaPm=ct%3Dkqn4wkpk%7Cci%3D045abd4d8e642f483a6ad56ebf53f57271464c5e%7Ctr%3Dslsl%7Csn%3D939638%7Chk%3D8e12d04df80afd8402bde0e95384b36031223f06"))
            e1.delete(0, END)
            e1.insert(0, str(shoe))
    elif(ball == 2):
        if(archii == 1):
            shoe = "반스 에라, 정사이즈"
            link1.bind("<Button-1>", lambda e: callback("https://search.shopping.naver.com/catalog/23543936099?query=%EB%B0%98%EC%8A%A4%20%EC%97%90%EB%9D%BC&NaPm=ct%3Dkqn4x1oo%7Cci%3D7c2ee0f4fa138d419d3d3365b65d83646b3b3b2e%7Ctr%3Dslsl%7Csn%3D95694%7Chk%3Dbafc9525e91d52e80bd2e961c0c41f26bee0e49f"))
            e1.delete(0, END)
            e1.insert(0, str(shoe))
        elif(archii == 2):
            shoe = "반스 스케이트 하이 리이슈, 사이즈 반 업"
            link1.bind("<Button-1>", lambda e: callback("https://search.shopping.naver.com/catalog/20958212527?query=%EB%B0%98%EC%8A%A4%20%EC%8A%A4%EC%BC%80%EC%9D%B4%ED%8A%B8%20%ED%95%98%EC%9D%B4%20%EB%A6%AC%EC%9D%B4%EC%8A%88&NaPm=ct%3Dkqn4xjfk%7Cci%3D467c95d3a1e3131729b4e8be5378c67d813bc151%7Ctr%3Dslsl%7Csn%3D95694%7Chk%3Dbd6d9ee6d6591009f11a40a8917a17b2bd829d76"))
            e1.delete(0, END)
            e1.insert(0, str(shoe))
        else:
            shoe = "반스 스케이트 하이 38 DX, 정사이즈"
            link1.bind("<Button-1>", lambda e: callback("https://smartstore.naver.com/doubbleg/products/5647703723?NaPm=ct%3Dkqn4wkpk%7Cci%3D045abd4d8e642f483a6ad56ebf53f57271464c5e%7Ctr%3Dslsl%7Csn%3D939638%7Chk%3D8e12d04df80afd8402bde0e95384b36031223f06"))
            e1.delete(0, END)
            e1.insert(0, str(shoe))
    else:
        if(archii == 1):
            shoe = "반스 팔켄, 정사이즈, 키즈 모델"
            link1.bind("<Button-1>", lambda e: callback("https://smartstore.naver.com/multivision/products/5598932927?NaPm=ct%3Dkqn53h60%7Cci%3D0ze0002TMrXu8Wqu9eXR%7Ctr%3Dpla%7Chk%3Da2114f228cdef68b5dbf6d27394f81a6d42962d6"))
            e1.delete(0, END)
            e1.insert(0, str(shoe))
        elif(archii == 2):
            shoe = "반스 올드스쿨 뮬, 한 사이즈 다운"
            link1.bind("<Button-1>", lambda e: callback("https://search.shopping.naver.com/catalog/25908920954?query=%EB%B0%98%EC%8A%A4%20%EC%98%AC%EB%93%9C%EC%8A%A4%EC%BF%A8%20%EB%AE%AC&NaPm=ct%3Dkqn57lbc%7Cci%3D9e00b5f8e84d65eea00539a0a86ab0dc221d5f5a%7Ctr%3Dslsl%7Csn%3D95694%7Chk%3Da25c04b934096484f22c2a0b5b16d7f0792ce207"))
            e1.delete(0, END)
            e1.insert(0, str(shoe))
        else:
            shoe = "반스 올드스쿨 플랫폼, 한 사이즈 다운"
            link1.bind("<Button-1>", lambda e: callback("https://search.shopping.naver.com/catalog/15805828393?query=%EB%B0%98%EC%8A%A4%20%EC%98%AC%EB%93%9C%EC%8A%A4%EC%BF%A8%20%ED%94%8C%EB%9E%AB%ED%8F%BC&NaPm=ct%3Dkqn587ow%7Cci%3D3331eed982582e5fcc02db6ff7ebe28830e58994%7Ctr%3Dslsl%7Csn%3D95694%7Chk%3D94626754783bec76374be098df2af4fc2d6bd1e4"))
            e1.delete(0, END)
            e1.insert(0, str(shoe))
    e1.pack(fill=BOTH, expand =1)
    link1.pack(fill = Y)
      
def fila():
    global ball, archii
    
    if(ball == 1):
        if(archii == 1):
            shoe = "휠라 웨이블렛, 한 사이즈 업"
            link1.bind("<Button-1>", lambda e: callback("https://search.shopping.naver.com/catalog/26789944964?query=%ED%9C%A0%EB%9D%BC%20%EC%9B%A8%EC%9D%B4%EB%B8%94%EB%A0%9B&NaPm=ct%3Dkqn5908o%7Cci%3D90251fec9a50a6606e2e0a0a8ce4750f9ef30413%7Ctr%3Dslsl%7Csn%3D95694%7Chk%3Df90f985926f26afa2af483f7dae9c7d651d2096d"))
            e1.delete(0, END)
            e1.insert(0, str(shoe))
        elif(archii == 2):
            shoe = "휠라 클래식 킥스, 정사이즈"
            link1.bind("<Button-1>", lambda e: callback("https://search.shopping.naver.com/catalog/23200013644?query=%ED%9C%A0%EB%9D%BC%20%ED%81%B4%EB%9E%98%EC%8B%9D%20%ED%82%A5%EC%8A%A4&NaPm=ct%3Dkqn59hzk%7Cci%3D6f0bd5dbad778c78f18c470d65305b4891f8073f%7Ctr%3Dslsl%7Csn%3D95694%7Chk%3D51078496d1ab11b7ede36d309fb9e6039d46a88f"))
            e1.delete(0, END)
            e1.insert(0, str(shoe))
        else:
            shoe = "휠라 스팔라인 스크립트, 정사이즈"
            link1.bind("<Button-1>", lambda e: callback("https://search.shopping.naver.com/catalog/24895616633?query=%ED%9C%A0%EB%9D%BC%EC%8A%A4%ED%94%8C%EB%9D%BC%EC%9D%B8%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8&NaPm=ct%3Dkqn5b334%7Cci%3Ded05e95559dc129757b56c201d84b914b435f09d%7Ctr%3Dslsl%7Csn%3D95694%7Chk%3D24d964766433cacc5eafec1c06d5b0c0c141ecc6"))
            e1.delete(0, END)
            e1.insert(0, str(shoe))
    elif(ball == 2):
        if(archii == 1):
            shoe = "휠라 범퍼, 한 치수 작게"
            link1.bind("<Button-1>", lambda e: callback("https://search.shopping.naver.com/catalog/27038082425?query=%ED%9C%A0%EB%9D%BC%20%EB%B2%94%ED%8D%BC&NaPm=ct%3Dkqn5bffk%7Cci%3D8650196da5787869fc7b2a66df47160ecb2d50c8%7Ctr%3Dslsl%7Csn%3D95694%7Chk%3Db62dbd5f1e3c6ec143c975cd0832e8e16842f2de"))
            e1.delete(0, END)
            e1.insert(0, str(shoe))
        elif(archii == 2):
            shoe = "휠라 스키퍼, 반 치수 업"
            link1.bind("<Button-1>", lambda e: callback("https://search.shopping.naver.com/catalog/25854190404?query=%ED%9C%A0%EB%9D%BC%20%EC%8A%A4%ED%82%A4%ED%8D%BC&NaPm=ct%3Dkqn5bsjs%7Cci%3D74eac97ea6971bfbad3e84ff368f39e4a885b5a9%7Ctr%3Dslsl%7Csn%3D95694%7Chk%3D28af70d026d5d1291a54fef8dcafd0ad5abcbb2e"))
            e1.delete(0, END)
            e1.insert(0, str(shoe))
        else:
            shoe = "휠라 스키퍼, 반 치수 업"
            link1.bind("<Button-1>", lambda e: callback("https://search.shopping.naver.com/catalog/25854190404?query=%ED%9C%A0%EB%9D%BC%20%EC%8A%A4%ED%82%A4%ED%8D%BC&NaPm=ct%3Dkqn5bsjs%7Cci%3D74eac97ea6971bfbad3e84ff368f39e4a885b5a9%7Ctr%3Dslsl%7Csn%3D95694%7Chk%3D28af70d026d5d1291a54fef8dcafd0ad5abcbb2e"))
            e1.delete(0, END)
            e1.insert(0, str(shoe))
    else:
        if(archii == 1):
            shoe = "휠라 엘리트 코트, 반 치수 업"
            link1.bind("<Button-1>", lambda e: callback("https://search.shopping.naver.com/catalog/22985418561?query=%ED%9C%A0%EB%9D%BC%20%EC%97%98%EB%A6%AC%ED%8A%B8%20%EC%BD%94%ED%8A%B8&NaPm=ct%3Dkqn5ch8o%7Cci%3Da95c9ac1c192063ec605ded59ad9c4605535ac3e%7Ctr%3Dslsl%7Csn%3D95694%7Chk%3D78c6af9f5b3c1aa0a78878afe43ca45461aeee59"))
            e1.delete(0, END)
            e1.insert(0, str(shoe))
        elif(archii == 2):
            shoe = "휠라 디스럽터 3 포메이션, 반 치수 업"
            link1.bind("<Button-1>", lambda e: callback("https://search.shopping.naver.com/catalog/18999717799?query=%ED%9C%A0%EB%9D%BC%20%EB%94%94%EC%8A%A4%EB%9F%BD%ED%84%B0%203%20%ED%8F%AC%EB%A9%94%EC%9D%B4%EC%85%98&NaPm=ct%3Dkqn5cv4o%7Cci%3D6f1ca26100e0496d4a8a186f7b408b4a51078089%7Ctr%3Dslsl%7Csn%3D95694%7Chk%3D27001daf0bd9905882f79aae03afd55ca97a8b52"))
            e1.delete(0, END)
            e1.insert(0, str(shoe))
        else:
            shoe = "휠라 디스럽터 어글리 슈즈, 한 사이즈 업"
            link1.bind("<Button-1>", lambda e: callback("https://search.shopping.naver.com/catalog/21445682267?query=%ED%9C%A0%EB%9D%BC%20%EB%94%94%EC%8A%A4%EB%9F%BD%ED%84%B0%20%EC%96%B4%EA%B8%80%EB%A6%AC%EC%8A%88%EC%A6%88&NaPm=ct%3Dkqn5dbc0%7Cci%3D77ef6f1d795b81aa218428d171e1dc3515ccadce%7Ctr%3Dslsl%7Csn%3D95694%7Chk%3Da76d99d3624ec7a7dbc54ef048d2fff17215475a"))
            e1.delete(0, END)
            e1.insert(0, str(shoe))
    e1.pack(fill=BOTH, expand =1)
    link1.pack(fill = Y)
    
def brand():
    global i
    
    label = Label(window)
    label['text'] = text[i]
    label.pack()
    
    adidasBt = Button(brandframe, text="아디다스", command = adidas)
    nikeBt = Button(brandframe, text="나이키", command = nike)
    vansBt = Button(brandframe, text="반스", command = vans)
    filaBt = Button(brandframe, text="휠라", command = fila)
    adidasBt.grid(row=0, column=0)
    nikeBt.grid(row=0, column=1)
    vansBt.grid(row=1, column=0)
    filaBt.grid(row=1, column=1)

    brandframe.pack()

for i in range(3):
    if(i == 0):
        boll()
    elif(i == 1):
        archie()
    elif(i == 2):
        brand()
        
window.mainloop()