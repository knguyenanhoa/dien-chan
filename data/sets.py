class Sets():
    def __init__(self):
        pass

    def list(self, *args, **kwargs):
        """
        Meta function to fetch list according to letter
        """
        func_name = "list_"+kwargs['key']
        func = getattr(self, func_name) 
        return func()

    def list_A(self):
        return {
            "Amidan 1": {
                "Day an": [12,38],
                "Go va ho": [14,275,277,274],
            },
            "Amidan 2": {
                "Day an": [26,3,87,100,143],
            },
            "Amidan 3": {
                "Day an": [26,3,87,15,],
            },
            "An than": {
                "Day an (danh cho nguoi kho ngu hoac mat ngu)": [26],
                "Moi toi truoc khi ngu, day an vai phut ket hop voi xoa nong 2 ban chan, chu yeu la long ban chan": [],
            },
            "An kem": {
                "Day an": [22,127,63,7,113,17,19,64,50,39,37,1,290,0,],
                "Day la bo Bo Am Huyet va Tang Luc, dung cho moi lua tuoi. Neu thay an kem, xanh xao gay om thi dung bo nay. Nguoi muon len can, 1 ngay day an 3 lan (sang chieu toi) co the len den 8-9 kg/thang": [],
            },
            "An khong tieu": {
                "Day an": [19],
                "Ho vung ron va lan quanh mieng vai chuc vong": [],
                "Lan mat 3 lan cach quang (chu yeu la vung tran, vung mieng va cam). Het day hoi cam thay doi bung": [],
            },
            "Am dao (tu cung) dau": {
                "Gach 2 bo nhan trung va bo moi tren": [],
                "Gach vung ranh nhan trung tu 19 den 53 nhieu lan": [],
                "Day an": [19,63,53,7,],
            },
        }
    
    def list_B(self):
        return {
            "Ba vai dau 1": {
                "Lan": [332,360,16,],
            },
            "Ba vai dau 2": {
                "Lan 73 xeo len 330": [73,330,],
            },
            "Ba vai dau 3": {
                "Day an": [477,97,99,98,106,34],
            },
            "Ba vai dau 4 (dau khop vai)": {
                "Day an": [26,88,65,278,],
            },
            "Ba vai dau 5 (dau khop vai)": {
                "Day an": [26,19,97,564,],
            },
            "Ba vai dau 6 (dau khop vai)": {
                "Vach vien mui nhieu lan": [],
            },
            "Bach bi bach bien": {
                "Day an": [64,3,132,106,],
            },
            "Ban tay lo loet 1": {
                "Day an Tieu Viem Tieu Doc (xem them Ban tay lo loet 2)": [41,143,127,19],
                "Ho tai cho": [],
            },
            "Ban tay lo loet 2": {
                "Day an Tieu Viem Tieu Doc (xem them Ban tay lo loet 1)": [26,38,61,60,41,3,],
                "Ho tai cho": [],
            },
            "Bao tu (da day) dau 1": {
                "Day an": [124,34,61,39,120,121,19,64,73,162,62,189,126,59,],
                "Neu kho tho, nang nguc them": [73,162,62,189,],
                "Neu kho o them": [126,59,],
            },
            "Bao tu (da day) dau 2": {
                "Day an (de cat con dau)": [61,],
                "Cham deep heat hoac ho vao tam giac vi": [120,39,121,],
            },
            "Bao tu (da day) dau 3": {
                "Day an": [235,37,124,630,],
            },
            "Bao tu (da day) dau 4": {
                "Cham deep heat": [61,39,64,630],
            },
            "Bao tu (da day) dau 5": {
                "Sang som luc doi uong 1 muong mat ong": [],
            },
            "Bam mau va sung do chan thuong": {
                "Go va day an (chi lam ben trai)  nhieu lan cac huyet": [156,7,50,3,61,290,16,37,],
                "Ho phan chieu noi bam hoac sung": [],
                "Chu y: Phac do nay co 3 tac dung lam ngung chay mau, tan mau bam va xep cho sung. No rat can thiet cho truong hop bai liet do chan thuong so nao hoac tai bien mach mau nao co xuat huyet, khong phai giai phau": [],
            },
            "Bi tieu": {
                "Day an": [220,26,174,87,51,375,29,60,57,50,],
                "Vuot cam": [],
                "Day 126 khoang 10 phut": [126],
            },
            "Bon (tao bon) 1": {
                "Cham deep heat": [41,143,38,],
            },
            "Bon (tao bon) 2": {
                "Cham deep heat": [26,61,38,41,365,],
            },
            "Bon (tao bon) 3": {
                "Vuot quanh moi 60 lan roi ho vanh moi tren": [],
            },
            "Bon (tao bon) 4": {
                "Dung 3 dau ngon tay - ngon cai o duoi, ngon tro va ngon giua chum lai o tren vuot dau mui. Vuot den khi thay rung minh la duoc": [],
            },
            "Bon (tao bon) 5": {
                    "Cha cung may va vuot quanh moi tu phai qua trai den giua u cam (huyet 87) moi lan 60 cai. Ngay lam 6 lan": [87,],
            },
            "Bon (tao bon) 6": {
                "Uong bot san day (uong song), moi ngay uong 2 ly coi": [],
            },
            "Bon (tao bon) 7": {
                "Bo ket nuong vang roi do nuoc soi ngam 15 phut. Lay nuoc bo ket dac am xit vao hau mon, di cau ngay": [],
            },
            "Bo mau 1": {
                "Day an": [50,19,39],
            },
            "Bo mau 2": {
                "Day an": [127,42,35,290,1,],
            },
            "Bo mau 3": {
                "Day an": [22,127,63,7,113,17,19,64,50,39,37,1,290,0,],
            },
            "Bui vao mat": {
                "The luoi ra liem khoe mieng cheo voi ben mat dang co bui. Liem do vai giay la het bui": [],
            },
            "Bung dau 1": {
                "Ho ron va lan quanh mieng do vai phut": [],
            },
            "Bung dau 2": {
                "Dung cau gai doi lan long 2 ban tay. Vai phut sau het dung bung": [],
            },
            "Bung dau 3": {
                "Ho ngai cuu vao 2 long hai ban chan do 10 phut": [],
            },
            "Bung dau 4": {
                "Neu cung co thanh bung, day an them": [61,28,3,],
            },
            "Bung dau 5": {
                "Neu tieu chay day an them": [365,22,127,19,50,1,37,61,0,],
            },
            "Bung dau 6": {
                "Neu trun lai them": [19,127,39,3,38,63,41,],
            },
            "Bung dau 7": {
                "Neu kiet ly them": [26,61,3,143,38,],
                "Hoac gia 1 nam bot ngot lay nuoc cot uong hoac bot san day": [],
            },
            "Buou 1": {
                "(Buou co don thuan) Day an": [8,12,61,38,60,275,14,50,37,19,127,],
                "Xong ho co tay va noi co buou. Cuoi cung co the lan truc tiep cai buou nhieu lan trong ngay": [],
            },
            "Buou 2": {
                "Cham deep heat cac huyet": [8,12,60,39,38,50,14,275,],
                "Xong ho va lan nhu Buou 1": [],
            },
            "Buou 3": {
                "Day an": [26,196,12,8,61,19,],
                "Xong ho va lan nhu Buou 1": [],
            },
            "Buou doc (Basedow) 1": {
                "Day an va go": [39,38,287,7,113,156,74,64,87,57,60,100,],
                "Xong ho va lan nhu Buou 1": [],
            },
            "Buou doc (Basedow) 2": {
                "Day an va go": [14,64,8,12,37,17,50,39,87,51,124,34,],
                "Xong ho va lan nhu Buou 1": [],
            },
            "Buou co cac dang": {
                "Day an": [26,8,12,61,3,50,233,39,51,286,235,113,14,308,],
                "Xong ho va lan nhu Buou 1": [],
            },
            "Buou dau duong vat, di tieu rat kho": {
                "Day an": [143,17,38,61,3,26,60,57,127,50,37,103,],
            },
            "Buou buong trung 1": {
                "Day an": [124,26,37,50,63,7,],
                "Neu can thiet co the day an 3 lan 1 ngay": [],
            },
            "Buou buong trung 2": {
                "Day an": [26,65,3,37,16,87,27,],
                "Neu can thiet co the day an 3 lan 1 ngay": [],
            },
            "Buou cac loai tich tu trong co the": {
                "Day an nhieu lan bo Tieu u buou": [41,143,127,19,37,38],
                "Ho phan chieu noi co u buou": [],
            },
        }

    def list_C(self):
        return {
            "Cai thuoc la - cai ruou 1": {
                "Day an": [124,19,51,],
            },
            "Cai thuoc la - cai ruou 2": {
                "Day an": [124,19,127,57,3,],
            },
            "Cai thuoc la - cai ruou 3": {
                "Lan va go 2 ben mang tai va dai tai (vung huyet 275 - 14) sau do day an": [127,37,50,19,1,106,103,300,0,],
            },
            "Cam lanh - ret run 1": {
                "Day an": [127,63,19,61,1,106,103,300,],
            },
            "Cam lanh - ret run 2": {
                "Day an": [127,50,19,37,1,73,103,0,],
            },
            "Cam lanh - ret run 3": {
                "Lan cau gai 2 long ban tay khoang 10 phut, nguoi nong bung, ra mo hoi uot ao": [],
            },
            "Cam lanh - ret run 4": {
                "Day an Bo Thang": [127,50,19,37,1,73,189,103,300,0,],
                "Xoa dau cu la va lan khap mat nhieu lan": [],
            },
            "Cam nong 1": {
                "Day an": [26,3,1,39,38,222,4,43,156,87],
                "Ket hop chuom nuoc da o tran": [],
            },
            "Cam nong 2": {
                "Day an Bo Giang": [124,34,26,61,3,143,222,14,156,87,],
            },
            "Canh tay dau 1": {
                "Day an": [60,97,98,99],
            },
            "Canh tay dau 2": {
                "Ho va lan go may": [],
            },
            "Canh tay dau 3": {
                "Lan sat chan toc tran lan xuong thai duong (dau ben nao lan ben do)": [],
            },
            "Cam mau 1": {
                "Day an": [16,61,0,],
            },
            "Cam mau 2": {
                "Day an": [16,61,50,37,0,],
            },
            "Cam mau 3": {
                "Day an, lan huyet 16 cho den khi mau ngung chay": [16,],
            },
            "Can thi 1": {
                "Day an": [34,6,],
                "Lan cac sinh huyet quanh mat": [],
            },
            "Can thi 2": {
                "Day an": [34,1,127,],
                "Lan quanh mat": [],
            },
            "Can thi 3": {
                "Day an": [267,130,3,388,],
            },
            "Co giat lien tuc": {
                "Day an": [19,127,8,34,124,0,],
            },
            "Co luoi": {
                "Day an": [14,],
            },
            "Co gay cung moi 1": {
                "Day an": [16,61,287,],
            },
            "Co gay cung moi 2": {
                "Day an": [65,106,16,],
            },
            "Co gay cung moi 3": {
                "Day an": [65,8,290,127,87,],
            },
            "Co gay cung moi 4": {
                "Day an": [188,477,34,97,98,99,100,],
            },
            "Co gay cung moi 5": {
                "An, ho, lan": [8,20,12,65,],
            },
            "Co gay cung moi 6": {
                "Ho vung thai duong": [],
            },
            "Co gay cung moi 7": {
                "Boi kem deep heat": [7,],
            },
            "Co gay cung moi 8": {
                "Gach mi toc tran, sau do ho": [],
            },
            "Co gay cung moi 9": {
                "Gach vung 156": [156,],
            },
            "Cot song dau 1": {
                "Ho va lan": [342,348,],
            },
            "Cot song dau 2": {
                "Ho va lan mat ngoai dot giua nong tay giua (ban tay trai)": [],
            },
            "Cot song dau 3": {
                "Neu cup cot song, day an 19 va 2. Hoac day an 19-64-63 hoac 45-43-300": [19,64,63,45,43,300,],
            },
            "Cot song dau 4": {
                "Neu khong cui xuong duoc an 275 (ben trai)": [275,],
            },
            "Cot song dau 5": {
                "Neu khong ngua len duoc an 175 hoac 127": [175,127,],
            },
            "Cot song dau 6": {
                "Neu dau co lung": [423,99,467,],
            },
            "Cot song dau 7": {
                "Neu dau ngang that lung": [],
            },
            "Cot song dau 9": {
                "Ho lan song mui tu 1 den 8": [1,8,],
                "Lan 2 go may": [],
            },
            "Cot song dau 10": {
                "Day an": [1,189,8,106,103,],
            },
            "Cot song dau 11": {
                "Ho song tai (khoang 1/3 ben trai)": [],
            },
            "Cot song dau 12": {
                "Neu dau lung vung than, day an": [0,300,15,38,17,],
            },
            "Cot song dau 13": {
                "Day an" [45,173,],
            },
            "Cot song dau 14": {
                "Day an": [210,300,560,],
            },
            "Cot song dau 14": {
                "Ho truoc tai": [138,],
                "Ho tai diem dau": [],
            },
            "Cot song dau 15": {
                "Neu dau cot song co, day an": [26,8,1,],
            },
            "Cot song dau 16": {
                "Neu dau cot song cung cut, day an": [23,143,19,],
            },
            "Cot song dau 18": {
                "Neu dot song cung dau, ngoi khong duoc thi go nhe tu 53 den 19": [53,19,],
                "Day an": [63,19,],
            },
            "Cot song dau 19": {
                "Neu gai cot song ho va lan sinh huyet o mat, sau do lan truc tiep noi co gai o lung. Lay bua to dap vao cho dau, mau het hon lan": [],
            },
            "Cuong duong 1": {
                "Gach nhieu lan bo moi tren hoac lan moi": [],
            },
            "Cuong duong 2": {
                "Ngoi ep dau hui vao phan duong vat (3 lan 1 ngay, moi lan 5 phut)": [],
                "An sam bo luong + cu sen": [],
                "Re cau ngam ruou, uong moi toi (manh ngang voi ca ngua)": [],
            },
            "Chai chan 1": {
                "Day an": [26,51,],
            },
            "Chai chan 2": {
                "Ho phan chieu ben chan doi xung, ho vai lan trong ngay": [],
            },
            "Cham lac 1": {
                "Day an roi ho truc tiep": [61,38,50,51,],
            },
            "Cham lac 2": {
                "Day an roi ho truc tiep": [3,347,51,],
            },
            "Cham lac 3": {
                "Day an roi ho truc tiep": [62,51,38,],
            },
            "Cham lac 4": {
                "Day an roi ho truc tiep": [124,34,3,39,156,26,60,],
            },
            "Chay nuoc mat song 1": {
                "Day an": [16,61,],
            },
            "Chay nuoc mat song 2": {
                "Day an": [16,195,87,51,],
            },
            "Chan dau - dau mong, dau than kinh toa 1": {
                "Day an": [41,210,5,253,3,51,],
            },
            "Chan dau - dau mong, dau than kinh toa 2": {
                "Day an": [1,45,43,74,64,5,253,210,14,15,16,0,],
            },
            "Chan dau - dau mong, dau than kinh toa 3": {
                "Day an": [87,210,5,143,174,],
            },
            "Chan dau - dau mong, dau than kinh toa 4": {
                "Gach, ho, lan tren tran theo do hinh so 2": [],
            },
            "Chan dau - dau mong, dau than kinh toa 5": {
                "Cao dau theo do hinh so 11": [],
            },
            "Chan dau - dau khop hang": {
                "Day an": [64,74,210,],
                "Vach vien mui": [],
            },
            "Chan dau - dau khop goi 1": {
                "Day an": [17,38,197,300,45,0,],
            },
            "Chan dau - dau khop goi 2": {
                "Day an": [17,38,9,96,],
            },
            "Chan dau - dau khop goi 3": {
                "Day an": [129,100,156,39,],
            },
            "Chan dau - dau khop goi 4": {
                "Ho cui cho": [],
            },
            "Chan dau - dau kheo (nhuong) chan 1": {
                "Day an": [29,222,],
            },
            "Chan dau - dau kheo (nhuong) chan 2": {
                "Ho kheo tay": [],
            },
            "Chan dau - dau co chan 1": {
                "Day an": [347,127,],
            },
            "Chan dau - dau co chan 2": {
                "Ho va go co tay": [],
            },
            "Chan dau - dau got chan (hoac gai got chan) 1": {
                "Day an": [461,127,107,],
            },
            "Chan dau - dau got chan (hoac gai got chan) 2": {
                "Day an": [9,63,127,156,],
            },
            "Chan dau - dau got chan (hoac gai got chan) 3": {
                "Ho got chan doi xung": [],
            },
            "Chan dau - dau got chan (hoac gai got chan) 4": {
                "Day do tai cho (truc tiep noi dau)": [],
            },
            "Chan thuong so nao va hon me 1": {
                "An ho": [127,53,63,19,50,37,39,106,103,126,0],
            },
            "Chan thuong so nao va hon me 2": {
                "Go ho": [26,38,156,7,50,3,61,290,16,37,],
                "Go ho them bo vi chan thuong": [],
            },
            "Chong mat - binh thuong 1": {
                "Day an": [61,8,63,],
            },
            "Chong mat - binh thuong 2": {
                "Day an": [8,19,63,],
            },
            "Chong mat - binh thuong 3": {
                "Day an": [63,19,127,0],
            },
            "Chong mat - binh thuong 4": {
                "Day an": [34,290,156,70,],
            },
            "Chong mat - roi loan tien dinh 1": {
                "Day an": [124,34,65,189,3,],
            },
            "Chong mat - roi loan tien dinh 2": {
                "Day an": [127,63,8,60,65,103,0,],
            },
        }

    def list_D(self):
        return {
            "Di mong tinh 1": {
                "Day an": [0,1,45,8,],
            },
            "Di mong tinh 2": {
                "Day an": [124,34,45,],
            },
            "Di mong tinh 3": {
                "Day an": [43,45,0,],
            },
            "Di mong tinh 4": {
                "Day an": [300,1,45,127,0,],
            },
            "Di ung noi me day 1": {
                "Day an": [61,3,184,50,87,],
            },
            "Di ung noi me day 2": {
                "Day an": [41,50,17,7,60,85,],
            },
            "Di ung noi me day 3": {
                "Day an": [124,34,26,61,3,60,50,],
            },
            "Doi an 1": {
                "Day an va ho truc tiep": [61,38,50,],
            },
            "Doi an 2": {
                "Day an va ho truc tiep": [61,64,],
            },
            "Doi an 3": {
                "La muop rua sach, nhai song dap vo": [],
            },
            "Duong nuy": {
                "Day an": [1,50,19,39,7,127,103,],
            },
            "Dau bung kinh 1": {
                "Day an": [127,],
            },
            "Dau bung kinh 2": {
                "Day an": [1,63,50,7,127,],
            },
            "Dau bung kinh 3": {
                "Day an": [63,19,50,127,],
            },
            "Dau bung kinh 4": {
                "Vuot moi tren do vai phut": [],
            },
            "Dau bung sau khi tam": {
                "Day an": [0,17,],
            },
            "Dang mieng 1": {
                "Day an": [235,],
            },
            "Dang mieng 2": {
                "Day an": [26,184,235,227,],
            },
            "Day hoi": {
                "Lan long ban tay bang cau gai doi mot luc": [],
            },
            "Dinh rau": {
                "Day an": [3,38,41,61,104,0,],
            },
            "Dieu chinh am duong 1": {
                "Day an": [34,290,156,39,19,50,],
            },
            "Dieu chinh am duong 2": {
                "Day an": [1,39,19,50,57,],
            },
            "Dieu chinh am duong 3": {
                "Day an": [103,1,127,],
            },
        }

    def list_E(self):
        return {
            "NA": [],
        }

    def list_G(self):
        return {
            "NA": [],
        }

    def list_H(self):
        return {
            "Ham mat dau cung ben trai 1": {
                "Day an (ben dau)": [156,7,61,300,94,],
                "Day an (ben khong dau)": [3,],
            },
            "Ham mat dau cung ben trai 2": {
                "Day an": [8,12,20,196,188,73,276,14,15,275,],
                "Ho va lan truc tiep vung dau": [],
            },
            "Ham mat dau cung ben trai 3": {
                "Ho mat ngoai ngon tay cai (cung ben dau) tu ngoai den giap co tay": [],
            },
            "Hat hoi 1": {
                "An": [209,],
            },
            "Hat hoi 2": {
                "Day an": [19,63,1,0],
            },
            "Hat hoi 3": {
                "Ho tu 103 den 26": [103,26,],
            },
            "Hernie 1": {
                "An": [132,],
            },
            "Hernie 2": {
                "Day an": [342,19,38,9,143,104,105,561,98,],
            },
            "Hiem muon 1": {
                "Day an": [7,113,63,127,0,],
            },
            "Hiem muon 2": {
                "Day an": [127,156,87,50,37,65,0,],
            },
            "Ho - ho ngua co 1": {
                "Day an": [61,74,64,14,],
                "Ho co tay": [],
            },
            "Ho - ho ngua co 2": {
                "Day an": [8,20,12,],
            },
            "Ho - ho ngua co 3": {
                "Cha sat 2 co tay vao nhau nhieu lan": [],
            },
            "Ho - ngua co lien hoi, khong dam": {
                "Neu trong trang mat co gan mau do la ho nhiet thi day an": [8,127,20,176,275,467,],
                "Neu trong trang mat khong co gan mau do la ho han thi day an": [8,12,20,176,275,467,],
            },
            "Ho - ho khan 1":{
                "Day an": [14,275,60,74,180,],
            },
            "Ho - ho khan 2": {
                "Day an": [73,3,276,],
            },
            "Ho - ho khan 3": {
                "Day an": [26,61,3,51,],
            },
            "Ho - ho khan 4": {
                "Day an": [17,38,275,],
            },
            "Ho - ho khan lau ngay": {
                "Ho": [14,275,277,],
                "Ho them 2 ben suon mui va co tay": [],
                "Chung cach thuy 3 trai tac + 1 cu gung bang ngon tay cai. Chia 2 lan an": [],
            },
            "Ho - ho dam 1": {
                "Day an": [37,58,132,3,],
                "Go": [275,274,],
            },
            "Ho - ho dam 2": {
                "Day an": [61,467,491,],
                "Go": [275,274,],
            },
            "Ho - ho dam 3": {
                "Day an": [8,12,20,],
                "Go": [275,274,],
            },
            "Ho - ho dam 4": {
                "Day an va ho": [61,74,64,26,],
            },
            "Ho - ho dam 5": {
                "4 cong hanh (lay phan re va than trang) 4 lat gung nau liu riu 1 chen uong": [],
            },
            "Ho - ho lau ngay": {
                "Day an": [300,301,14,61,64,127,156,0,],
            },
            "Ho - suyen nhiet": {
                "Day an": [26,3,51,87,85,21,275,14,312,],
            },
            "Ho - suyen han": {
                "Day an": [0,17,19,61,491,467,28,275,240,],
            },
            "Hoc": {
                "Bam manh 19 nhieu lan": [],
                "Day an": [19,63,14,],
            },
            "Hong dau": {
                "An": [14,],
                "Ho vung mang tai tu 0 den 275 va tai cho": [0, 275,],
            },
            "Huyet ap - thap 1": {
                "Bam nhieu lan 19": [19,],
            },
            "Huyet ap - thap 2": {
                "Day an": [17,19,139,0,],
            },
            "Huyet ap - thap 3": {
                "Day an": [6,19,50,],
            },
            "Huyet ap - thap 4": {
                "Day an": [127,19,1,50,103],
            },
            "Huyet ap - thap 5": {
                "Bam Bo Thang": [],
            },
            "Huyet ap - cao 1": {
                "Day an": [15,0,],
            },
            "Huyet ap - cao 2": {
                "Day an": [14,15,16,],
            },
            "Huyet ap - cao 3": {
                "Day an": [124,34,16,14,],
            },
            "Huyet ap - cao 4": {
                "Day an": [285,23,188,],
            },
            "Huyet ap - cao 5": {
                "Lan vung Son Can - An Duong (tu 106 den 8) hoac 2 cung may (tu 65 den 100) hoac 2 mang tai (tu 16 den 14)": [],
            },
            "Huyet ap - kep": {
                "Huyet ap kep la khoang cac giua huyet ap tam thu va huyet ap tam truong xich lai gan nhau thi bam 127 kep xuong u cam do vai phut de cho huyet pa tam truong nho dan": [127,],
            },
            "Huyet ap - qua cao": {
                "Thuong tren 20, nguoi di lao dao, tim dap nhanh, tay chan te dai, luoi do": [],
                "Day an ngay 57 de dieu hoa nhip tim": [57,],
                "De on dinh lai co the, day an tiep": [19,96,88,127,50,37,1,0,],
            },
            "Huyet ap - te liet nua nguoi": {
                "De on dinh nao, dac biet chua benh nhun nao, day an": [34,290,100,156,37,41,],
                "De hoi phuc tay, lan 2 go may va go": [65,100,],
                "De hoi phuc chan, lan phan chieu chan theo do hinh so 1": [],
                "Ho nhuong tay, cui cho, dau xuong cac ngon tay": [],
                "Lan truc tiep tay, xuoi tu ba vai den cui cho, tu cui cho den co tay, tu co tay ra nam dau ngon tay": [],
                "Lan truc tiep chan, xuoi tu hong den dau goi, tu dau goi den co cahn, tu co chan ra nam dau ngon chan": [],
                "Lan lung nguoc tu xuong cung den xuong co": [],
                "Cao dau theo do hinh so 11": [],
            },
            "Huyet trang 1": {
                "Day an": [0,61,1,7,],
            },
            "Huyet trang 2": {
                "Day an": [53,275,],
            },
            "Huyet trang 3": {
                "Day an": [16,287,63,],
            },
            "Huyet trang 4": {
                "Day an": [53,38,14,],
            },
            "Huyet trang 5": {
                "Day an": [38,17,127,156,87,],
            },
            "Huyet trang 6": {
                "Day an": [26,3,63,287,7,16,22,0,],
            },
            "Huyet trang 7": {
                "Dung ngon tay tro va ngon tay giua cha xat 2 bo moi tren va duoi 200-300 lan 1 ngay": [],
            },
            "Huyet trang 8": {
                "Day an va go": [127,156,51,63,7,1,],
            },
        }

    def list_I(self):
        return {
            "NA": [],
        }

    def list_K(self):
        return {
            "Kem tri nho 1": {
                "Go": [103,300,],
            },
            "Kem tri nho 2": {
                "Day an": [124,34,103,106,],
            },
            "Kem tri nho 3": {
                "Day an": [60,50,1,106,103,124,34,],
            },
            "Kem tri nho 4": {
                "Moi toi nen go 20 den 30 cai bang dau ngon tay cho vao giua tran (huyet 103) cho cac chua nho, se tang cuong tri nho cho cac chau": [103,],
                "Nguoi lon can go them huyet 300 ben trai": [300,],
            },
            "Kinh nguyet - khong deu 1": {
                "Day an": [124,26,37,50,63,7,],
            },
            "Kinh nguyet - khong deu 2": {
                "Day an": [26,63,3,37,158,87,],
            },
            "Kinh nguyet - dau bung kinh 1": {
                "Day an": [127,156,],
            },
            "Kinh nguyet - dau bung kinh 2": {
                "Day an": [63,7,19,],
            },
            "Kinh nguyet - rong kinh 1": {
                "Go": [127,7,37,16,],
            },
            "Kinh nguyet - rong kinh 2": {
                "Day an": [16,61,50,7,37,],
            },
            "Kinh nguyet - rong kinh 3": {
                "Day an": [7,1,103,0,],
            },
            "Kinh nguyet - rong kinh 4": {
                "Day an": [22,127,7,1,50,37,103,],
            },
            "Kinh nguyet - tre kinh 1": {
                "Day an": [1,63,7,50,127,],
            },
            "Kinh nguyet - tre kinh 2": {
                "Day an": [50,58,37,],
            },
            "Kinh nguyet - tre kinh 3": {
                "Day an": [26,65,3,50,7,37,156,51,],
            },
            "Kinh nguyet - be kinh (mat kinh) 1": {
                "Day an": [85,87,63,7,247,127,275,],
            },
            "Kinh nguyet - be kinh (mat kinh) 2": {
                "Cha moi tren 100 cai moi ngay": [],
            },
            "Kinh nguyet - be kinh (mat kinh) 3": {
                "Dung lan cau gai doi lan tu ron xuong hang cho den khi bung nong len. Lan tu 3 den 5 ngay": [],
            },
            "Khan tieng 1": {
                "Cha xat vung gay cho nong len do vai lan la het": [],
            },
            "Khan tieng 2": {
                "Dung nong tay tro go manh vung truoc dai tai nhieu lan trong ngay": [],
            },
            "Khan tieng 3": {
                "Day an": [26,312,8,14,275,3,],
            },
            "Kho tho - binh thuong 1": {
                "Vach va ho vung tam that trai": [120,37,3,],
            },
            "Kho tho - binh thuong 2": {
                "Vach ranh nhan trung": [19,63,53,],
            },
            "Kho tho - do met tim 1": {
                "Day an": [189,73,],
            },
            "Kho tho - do met tim 2": {
                "Day an": [321,],
            },
            "Kho tho - do met tim 3": {
                "Day an": [28,],
            },
            "Kho tho - do tuc nguc": {
                "Ho long ban tay va day an": [0,28],
            },
            "Kho tho - do nong nguc": {
                "Day an": [34,290,156,3,],
            },
            "Kho tho - do thieu nang vanh": {
                "Ho tu 0 den 61": [0,61,],
            },
            "Kho tho - do roi loan tam that (tim dap nhanh, manh)": {
                "Ho": [26,113,235,],
                "Ho gan ban tay trai duoi ngon ut": [],
                "Ve ngon tay giua (tay trai) mot luc": [],
            },
            "Kho tho - do nhoi tim va tho gap": {
                "An (432 va 60 chi an ben phai)": [432,19,60,],
                "Ho va lan do hinh tim tren mui": [],
            },
            "Kho tho - do ngop tho muon xiu": {
                "Day an": [189,61,127,28,],
            },
            "Khoc dem": {
                "An": [19,],
            },
            "Kho dich cac khop 1": {
                "Day an": [38,],
                "Day an bo vi": [],
            },
            "Kho dich cac khop 2": {
                "Day an": [26,61,38,],
                "Day an bo vi": [],
            },
            "Khop ngon tay kho co duoi 1": {
                "Day an": [19,50,],
            },
            "Khop ngon tay kho co duoi 2": {
                "Day an": [0,19,130,],
            },
            "Khop ngon tay kho co duoi 1": {
                "Ho dau xuong cac ngon tay roi lan nhieu lan": [],
            },
        }

    def list_L(self):
        return {
            "La mia dau (do uong ruou manh)": {
                "Day an": [113,7,63,38,37,],
            },
            "Lai - lai dua 1": {
                "Day an": [127,9,],
            },
            "Lai - lai dua 2": {
                "Day an": [19,127,39,3,38,63,41,],
            },
            "Lai - lai dua 3": {
                "Day an": [184,64,63,22,28,85,11,],
            },
            "Lai - lai kim": {
                "Day an": [26,61,38,365,],
            },
            "Leo mat 1": {
                "Day an": [332,38,],
            },
            "Leo mat 2": {
                "Day an": [283,38,3,215,],
            },
            "Leo mat 3": {
                "Day an": [38,],
                "Day an ngay chan mun leo": [],
            },
            "Liet duong 1": {
                "Day an": [287,63,7,],
            },
            "Liet duong 2": {
                "Day an": [184,290,64,3,],
            },
            "Liet duong 3": {
                "Day an": [103,1,19,127,50,39,7,132,],
            },
            "Liet duong 4": {
                "Day an (300 ben trai)": [300,63,7,127,0,],
            },
            "Liet duong 5": {
                "Day an (300 ben trai)": [19,1,50,300,0,],
            },
            "Liet duong 6": {
                "Day an": [63,7,19,],
            },
            "Liet duong 7": {
                "Day an": [124,34,60,1,19,],
            },
            "Liet duong 8": {
                "Lan go (300 ben trai)": [19,1,50,300,7,63,287,45,0,],
            },
            "Liet duong 9": {
                "Gach nhieu lan tu 53 den 19": [53,19,],
            },
            "Liet duong 10": {
                "Lan cau gai 2 ben canh mui ra toi mi toc mai nhieu lan roi lan": [],
                "Lan doc tu 126 xuong dinh cam bo qua 26 den 8": [126,],
                "Ket hop chung cach thuy: cat heo (bo vung nuoc tieu) + oc heo (bo chi do) + cu sen + thuc dia": [],
            },
            "Liet mat 1": {
                "Day an": [127,19,39,9,10,29,267,],
            },
            "Liet mat 2": {
                "Day an": [15,88,96,156,222,],
            },
            "Liet mat 3": {
                "Day an": [103,106,34,129,131,16,28,29,9,96,215,],
            },
            "Lo luoi 1": {
                "Day an": [63,7,113,],
            },
            "Lo luoi 2": {
                "Day an": [60,8,38,61,3,79,51,],
            },
            "Lo mom 1": {
                "Day an": [39,38,3,14,16,],
            },
            "Lo mom 2": {
                "Day an": [26,61,3,38,39,85,87,51,],
            },
            "Lo phao mong tay": {
                "Ho ngon tay ben ben tay doi xung hoac ngon chan cung ben": [],
            },
        }

    def list_M(self):
        return {
            "Mac co (hoc xuong, hot trai cay)": {
                "Day an": [14,19,63,],
            },
            "Mat - can thi 1": {
                "Day an": [34,6,],
            },
            "Mat - can thi 2": {
                "Day an": [34,1,127,],
            },
            "Mat - co mu 1": {
                "An": [41,143,127,19,],
                "Lan quanh mat nhieu vong": [],
            },
            "Mat - co mu 2": {
                "Day an": [197,34,16,39,50,38,],
            },
            "Mat - co mu 3": {
                "Ho mat doi xung": [],
            },
            "Mat - dau mat do 1": {
                "Day an": [98,17,7,50,60,100,215,],
            },
            "Mat - dau mat do 2": {
                "Day an": [16,97,180,73,3,50,],
            },
            "Mat - dau mat do 3": {
                "Gach cac sinh huyet theo do hinh mat, chu yeu la long ban tay va dau ngon tay ut do vai phut": [],
            },
            "Mat - mat mang, mong 1": {
                "Lan go": [34,65,195,267,197,],
            },
            "Mat - mat mang, mong 2": {
                "Go": [195,16,130,3,38,17,],
            },
            "Mat - mat mang, mong 3": {
                "Day an": [195,16,130,3,100,50,],
            },
            "Mat - chay nuoc mat song": {
                "Day an": [16,196,87,51,],
                "Dung cau gai nho lan khap mi mat": [],
            },
            "Mat - cuom nuoc, cuom kho 1": {
                "Day an": [324,131,41,437,235,290,184,34,16,199,],
                "Gach cac sinh huyet theo do hinh mat": [],
            },
            "Mat - cuom nuoc, cuom kho 2": {
                "Do sinh huyet tren chan may roi dung cau gai lan nhieu lan trong ngay": [],
            },
            "Mat - thi luc kem 1": {
                "Day an": [6,34,130,],
            },
            "Mat - thi luc kem 2": {
                "Day an": [50,195,197,],
            },
            "Mat - mat mo 1": {
                "Day an": [34,6,21,50,],
            },
            "Mat - mat mo 2": {
                "Ho": [197,34,73,130,12,102,],
            },
            "Mat - mat mo 3": {
                "Vach vung quanh mat giua 188 va 65": [188,65,],
                "Cac huyet tren go may 97,99,98": [97,99,98,],
            },
            "Mat - mat mo vi gian dong tu": {
                "Day an": [34,65,179,267,102,100,4,2,],
                "Gach cac sinh huyet theo do hinh mat": [],
            },
            "Mat - khong cu dong duoc vi liet day than kinh thi giac": {
                "Day an": [34,184,],
            },
            "Mat - mat nhuc 1": {
                "Day an": [16,],
            },
            "Mat - mat nhuc 2": {
                "Day an": [34,21,6,],
            },
            "Mat - mat nhay (giat)": {
                "Day an": [97,98,102,99,],
                "Ho tu 126 den 87": [126,87,],
                "Ho tu 0 den nhan trung": [0,],
                "Go cac vung mat theo do hinh": [],
                "Day an": [179,],
            },
            "Mat - quang tham": {
                "Day an": [290,113,7,],
                "Ho truc tiep cho quang tham": [],
            },
            "Mat - sup mi": {
                "Day an": [124,34,267,102,100,50],
            },
            "Khuon mat - nam mun 1": {
                "Day an": [60,61,3,156,38,143,],
            },
            "Khuon mat - nam mun 2": {
                "Day an": [300,0,45,61,17,3,73,],
            },
            "Khuon mat - nam mun 3": {
                "Day an": [34,26,3,28,],
            },
            "Khuon mat - nam mun 4": {
                "Day an": [45,17,51,],
            },
            "Khuon mat - nam mun 5": {
                "Day an": [17,113,38,73,103,106,138,275,63,53,19,],
            },
            "Khuon mat - nam mun 6": {
                "Dung long trang hot ga va nuoc nghe tuoi xoa mat moi toi": [],
            },
            "Mat ngu 1": {
                "Day an": [163,],
            },
            "Mat ngu 2": {
                "Go khoang 20-30 cai cac huyet": [124,34,],
            },
            "Mat ngu 3": {
                "Day an": [53,],
            },
            "Mat ngu 4": {
                "Day an": [16,14,0,],
            },
            "Mat ngu 5": {
                "Day an": [124,101,321,],
            },
            "Mat ngu 6": {
                "Day an": [124,34,267,217,51,],
            },
            "Mat ngu 7": {
                "Day an": [124,34,103,100,51,0,],
            },
            "Mat ngu 8": {
                "Cao dau truoc khi di ngu": [],
                "Lan cau gai doi tu chan len hang": [],
                "Dat ban chan len cau gai, lan di lan lai khoang 10 phut": [],
                "Dung cau gai doi lan lung va bung duoi moi toi truoc khi ngu": [],
                "Xoa dau cu la va cha xat manh 2 gan ban chan. Sau do dung dau ngon tay giua ben trai xoa vao 26": [26,],
            },
            "Me day 1": {
                "Day an": [61,63,184,50,87,],
            },
            "Me day 2": {
                "Day an": [41,50,17,7,60,85],
            },
            "Me day 3": {
                "Day an": [61,50,3,184,87,17,34,],
            },
            "Me day 4": {
                "Ho ngai cuu tai cho": [],
            },
            "Moi co gay 1": {
                "Ho go 240 hoac 195": [240,195,],
            },
            "Moi co gay 2": {
                "Day an": [422,],
            },
            "Moi co gay 3": {
                "Ho lan vung An duong va Son can": [],
                "Lan dau go may": [],
                "Ho lan vung co tay ngoai, hoac xoa dau cu la roi vuot manh nhieu lan vung co tay trai (duoi ngon tay cai) khoang vai phut": [],
                "Ho khoang giua ngon tay giua va ngon tay tro (tai trai)": [],
            },
            "Mo trong mau (hoac gan nhiem mo) 1": {
                "Day an": [50,41,233,37,127,],
            },
            "Mo trong mau (hoac gan nhiem mo) 2": {
                "Go va ho": [300,103,106,26,],
            },
            "Mo trong mau (hoac gan nhiem mo) 3": {
                "Day an": [51,29,85,7,113,38,41,50,173,290,3,73,],
            },
            "Mo hoi - tay chan 1": {
                "Day an": [60,16,],
            },
            "Mo hoi - tay chan 2": {
                "Day an": [37,127,87,50,1,],
            },
            "Mo hoi - tay chan 3": {
                "Day an": [103,1,19,127,36,],
            },
            "Mo hoi - tay chan 4": {
                "Day an": [127,156,87,60,0,],
            },
            "Mo hoi - tay chan 5": {
                "Day an": [50,60,61,16,0,],
            },
            "Mo hoi - tay chan 6": {
                "Day an": [50,51,61,127,0,],
            },
            "Mo hoi - tay chan 7": {
                "Day an": [300,103,106,73,1,290,17,],
                "Ho cac vung phan chieu tay chan": [],
            },
            "Mo hoi - toan than": {
                "Day an": [61,16,127,19,63,103,],
                "Day an cac sinh huyet o cung may": [],
                "Ho vung giua tran va tim": [],
            },
            "Mong dau": {
                "Ho": [277,104,219,],
                "Ho vung Go Kim Tinh (tuong tu nhu cai mong) duoi goc ngon tay cai": [],
            },
            "Mui khong ngui thay mui 1": {
                "Lan va day an": [138,],
            },
            "Mui khong ngui thay mui 2": {
                "Day an": [34,290,156,100,555,],
            },
            "Mun coc 1": {
                "Day an": [26,3,50,51,0,],
            },
            "Mun coc 2": {
                "Day an": [26,3,50,51,0,129,460,98,461,156,],
            },
        }

    def list_N(self):
        return {
            "Nac cut 1": {
                "Day an": [19,],
            },
            "Nac cut 2": {
                "Day an": [26,312,],
            },
            "Nac cut 3": {
                "Day an": [124,34,61,],
            },
            "Nac cut 4": {
                "Day an": [26,312,61,],
                "Moi huyet day an o tren phai dem thanh tieng. Lam 7 vong": [],
            },
            "Nac cut 5": {
                "Vach doc giua dau 10 cai": [],
                "Neu nac cut, nghet: vuot xuong canh chan mui ben trai": [],
            },
            "No hoi": {
                "Ho vung phan chieu gan o ban tay": [],
            },
            "Non oi 1": {
                "Day an": [124,34,50,79,0,],
            },
            "Non oi 2": {
                "(Ap dung khi non oi luc vua an xong) Day an": [0,19,124,34,50,37,29,300,41,50,45,],
            },
            "Non oi 3": {
                "(Ap dung khi non oi do co thai) Day an": [37,27,1,39,14,],
            },
            "Nong sot, kinh giat 1": {
                "Day an": [16,],
            },
            "Nong sot, kinh giat 2": {
                "Day an": [26,106,61,3,290,143,29,85,],
            },
            "Nong sot, kinh giat 3": {
                "Day an": [51,16,15,],
            },
            "Ngu hay giat minh": {
                "Day an": [124,34,50,19,],
            },
            "Ngu (buon ngu) nhiu mat": {
                "Vo 2 lo tai": [],
            },
            "Ngua 1": {
                "Day an": [61,38,50,],
            },
            "Ngua 2": {
                "Day an": [17,7,50,61,],
            },
            "Ngua 3": {
                "Day an": [26,61,3,51,],
            },
            "Ngua co": {
                "Ngoay lo tai bang dau khuynh diep": [],
            },
            "Ngua do bi doi leo": {
                "Day kem deep heat (lam 2-3 ngay, moi ngay 2-3 lan)": [61,38,50,],
            },
            "Nghet mui 1": {
                "Day an": [360,330,],
            },
            "Nghet mui 2": {
                "Day an": [3,23,],
            },
            "Nghet mui 3": {
                "Day an": [7,61,423,565,],
            },
            "Nghet mui 4": {
                "Day an, ho": [184,300,287,61,0,],
            },
            "Nghet mui 5": {
                "Ho do hinh mui tren tran tu 103 den 26 khoang vai chuc giay": [103,26,],
            },
            "Nghet mui 6": {
                "Ho canh ban tay hoac vanh tai, ho di ho lai cho bat nong nhat": [],
            },
            "Nghet mui 6": {
                "Ho long ban tay thay mao mach o mui no ra, thong ngay": [],
            },
            "Ngua thai 1": {
                "Day an": [26,63,7,287,],
            },
            "Ngua thai 2": {
                "Day an": [26,127,156,87,235,180,],
            },
            "Ngua thai 3": {
                "Day an": [287,63,127,235,87,26,3,],
            },
            "Ngua thai 4": {
                "Cha moi nhieu lan": [],
            },
            "Nhay mui": {
                "Keo manh 287 xuong vai chuc cai la het": [287,],
            },
            "Nhuc dau - nhuc dinh dau 1": {
                "Day an": [103,50,87,51,61,87,127,19,37,],
            },
            "Nhuc dau - nhuc dinh dau 2": {
                "Ho 103 hoac 126": [103, 126,],
                "Ho dau ngon tay giua (tay trai)": [],
                "Ho dau gu xuong ngon giua (cua ban tay nam lai)": [],
                "Lan cac dau ngon tay chum lai": [],
            },
            "Nhuc dau - nhuc mot ben 1": {
                "Day an": [249,278,],
            },
            "Nhuc dau - nhuc mot ben 2": {
                "Day an": [320,131,235,41,437,],
            },
            "Nhuc dau - nhuc mot ben 3": {
                "Day an": [320,131,100,180,61,3,54,55,56,51,130,],
            },
            "Nhuc dau - nhuc mot ben 4": {
                "Neu nhuc nua dau ben phai, ho nua mu ban tay (ban tay nam lai) ben phai. Hoac ho canh phai dot dau ngon giua. Lam nguoc lai voi nhuc dau ben trai": [],
            },
            "Nhuc dau - nhuc co gay 1": {
                "Day an": [139,278,16,287,],
            },
            "Nhuc dau - nhuc co gay 2": {
                "Day an": [34,97,98,99,100,477,],
            },
            "Nhuc dau - nhuc co gay 3": {
                "Day an": [22,235,127,63,19,50,1,37,61,],
            },
            "Nhuc dau - nhuc co gay 4": {
                "Ho va lan vung 26 hoac co tay ngoai ban tay trai": [26,],
            },
            "Nhuc dau - nhuc tran": {
                "Day an": [103,106,60,39,127,51,61,26,],
            },
            "Nhuc dau - nhuc thai duong": {
                "Neu nhuc mot ben, ho thai duong doi xung. HOac ho goc mong tay giua ben dau. Neu nhuc 2 ben ho ca 2 ben": [],
            },
            "Nhuc dau - xay xam": {
                "Dung cau gai lan cung may roi lan dai xuong 8": [8,],
            },
            "Nhuc dau - nhuc nhu bua bo": {
                "Day an": [34,16,14,180,185,195,191,],
            },
            "Nhuc canh tay va lung tren": {
                "Ho ke mu ban tay": [],
            },
            "Nhuc chan va lung duoi": {
                "Ho ke mu ban chan": [],
            },
            "Nhuc moi toan than": {
                "Day an": [34,21,1,6,],
                "Lan khap mat": [],
            },
        }

    def list_O(self):
        return {
            "On lanh": {
                "Day an": [0,17,61,127,],
            },
        }

    def list_P(self):
        return {
            "Phong xu, kinh gian": {
                "Day an": [1,290,50,106,3,],
            },
            "Phong 1": {
                "Dap con dam len cho phong": [],
                "Xoa dau an": [],
                "Xoa mat ong": [],
                "Xoa long trang trung": [],
            },
            "Phong 2": {
                "Day an": [26,3,61,60,29,85,14,15,16,17,38,0,],
            },
            "Phu toan than (bang quang khong nuoc tieu) 1": {
                "Go": [38,17,222,],
            },
            "Phu toan than (bang quang khong nuoc tieu) 2": {
                "Day an": [60,26,3,290,29,85,87,19,61,300,],
            },
        }

    def list_Q(self):
        return {
            "Quai bi 1": {
                "Day an": [0,3,477,275,14,],
            },
            "Quai bi 2": {
                "Day an 14 (ben dau) roi ho ben doi xung hoac tai cho deu duoc": [14,],
            },
        }

    def list_R(self):
        return {
            "Ren tri nho 1": {
                "Go": [124,34,106,103,],
            },
            "Ren tri nho 2": {
                "Dac biet chu y: de tren tri nho va luyen tri thong minh cho cac chau nho, moi toi truoc khi di ngu nen dung dau ngon tay giua go vao 103 giua tran khoang 20-30 cai cho cac chau. Neu la nguoi lon can go them 300": [103,300,],
            },
            "Rang nhuc, sung 1": {
                "Day an (dau ben nao lam ben do)": [13,3,],
            },
            "Rang nhuc, sung 2": {
                "An ben nhuc": [61,],
            },
            "Rang nhuc, sung 3": {
                "Dan an": [209,188,179,57,300,0,],
            },
            "Rang nhuc, sung 4": {
                "Ho ngai cuu vung ma bi sung": [],
            },
            "Rang nhuc, sung 5": {
                "Day an sinh huyet ngang 106 doc tren dinh tai (trong oc)": [106,],
            },
            "Rang nhuc, sung 6": {
                "Day an": [188,196,8,],
            },
            "Rang nhuc, sung 7": {
                "Day an": [34,60,57,180,188,196,0,],
            },
            "Rong kinh 1": {
                "Vuot mui tu 64 len dau may": [64,],
                "Ho": [87,63,19,],
                "Chu y: dung 2 ngon tay tro vuot nguoc tu chan canh mui len dau may con chua duoc ben sa tu cung": [],
            },
            "Rong kinh 2": {
                "Day an": [16,7,63,287,],
            },
            "Rong kinh 3": {
                "Day an": [16,61,45,37,0,],
            },
            "Roi loan nhip tim": {
                "Dau cau gai lan vung duoi ngon tay ut (ben trai)": [],
                "Ho cac sinh huyet giua hai vu va quanh duoi vu": [],
            },
            "Roi loan tien dinh": {
                "Day an": [124,34,65,189,3,],
            },
            "Roi loan tieu hoa": {
                "Day an": [127,19,143,1,103,],
            },
            "Run tay": {
                "Day an, ho": [45,300,127,124,100,130,131,61,180,39,0,],
            },
            "Rung toc 1": {
                "Day an": [127,145,103,],
            },
            "Rung toc 2": {
                "Day an": [50,37,39,107,175,],
            },
            "Rung toc 3": {
                "Day an": [156,258,175,39,],
            },
            "Rung toc 4": {
                "Day an": [300,1,45,3,0,],
            },
            "Rung toc 5": {
                "Goi dau bang nuoc bo ket (nuong) va vo buoi": [],
                "Cao dau (co thoi gian la cao, sau vai ngay la het rung toc). Cao dao con giup cho dau hoi moc toc lai": [],
            },
        }

    def list_S(self):
        return {
            "Sa ruot 1": {
                "Day an": [195,195],
                "Lan quanh mieng": [],
            },
            "Sa ruot 2": {
                "Day an": [104,222,38,63,22,127,19,1,103,],
            },
            "Sa tu cung 1": {
                "Day an": [557],
            },
            "Sa tu cung 2": {
                "Day an": [103,126,16,0,],
            },
            "Sa tu cung 3": {
                "Day an": [22,127,63,19,1,37,50,],
            },
            "Sa tu cung 4": {
                "Day an": [26,3,14,15,16,365,127,63,19,1,50,103,],
            },
            "Sa tu cung 5": {
                "Vuot mui tu 64 len dau may nhieu lan trong ngay. Sau 1 thang het": [64,],
            },
            "San (soi) than 1": {
                "Day an": [113,3,106,],
            },
            "San (soi) than 2": {
                "Day an": [184,290,64,3,],
            },
            "San (soi) than 3": {
                "Day an": [0,275,277,87,85,3,290,26,103,300,38,64,],
            },
            "San (soi) than 4": {
                "Got trai dua (thom) lay cuc phen chua nhet vao ruot dua, nuong chin roi ep lay nuoc uong": [],
                "Hot chuoi hot phoi kho, sao vang tan nhuyen, uong moi lan 2 muong": [],
                "Chuoi hot chin phoi kho ngam ruou, uong moi lan 1 ly nho": [],
            },
            "Say nang 1": {
                "Day an": [143,],
            },
            "Say nang 2": {
                "Cat 5 lat chanh mong dat vao 26 va 2 huyet 100, 130 (ca 2 ben). Co the uong them bot san day pha voi nuoc nguoi": [26,100,130,],
            },
            "Say ruou": {
                "Day an 57 hoac 28": [57,28,],
            },
            "Say song": {
                "Day an": [63,],
            },
            "Say xe": {
                "Dan 1 mieng nho salonpas voa giua ron": [],
                "Ngam 2 lat gung tuoi": [],
                "Khoai tay song (da cat lat) bo vao ly, nhung 1 chut vao nuoc soi roi an truoc khi len xe 15 phut": [],
            },
            "Sinh bung 1": {
                "Day an": [19,],
            },
            "Sinh bung 2": {
                "Lan bo moi tren mot luc (trung tien nhieu, het sinh bung)": [],
                "Ho ron va quanh vung ron": [],
            },
            "So mui 1": {
                "Day an mot trong cac huyet": [287,143,126,219,],
            },
            "So mui 2": {
                "Gach 197 nguoc len": [197,],
            },
            "So mui 3": {
                "Day an": [34,21,6,],
            },
            "So mui 4": {
                "Day an": [61,184,16,],
            },
            "So mui 5": {
                "Day an": [87,127,37,0,],
            },
            "So mui 6": {
                "Day an": [16,126,287,0,],
            },
            "So mui 7": {
                "Boi dau danh nong vung mang tai roi day an": [16,138,275,0,],
            },
            "Sot ret 1": {
                "Day an": [50,19,39,15,],
            },
            "Sot ret 2": {
                "Sot ret nang (bung chuong) day an": [50,19,39,15,1,26,132,],
            },
            "Sot ret 3": {
                "Neu chi lanh nguoi va ret run, ho nong cac huyet": [127,156,63,3,300,],
                "Uong tra nong + vai lat gung + vai muong duong": [],
                "Uong 1 ly nuoc gung + duong pha nong (1 mieng gung gia bang ngon tay cai, nuong len, cao vo den di, gia nho them 1 muong duong, pha nuoc soi quay vua tan duong, uong nong)": [],
            },
            "Suy nhuoc co the 1": {
                "Day an": [41,50,19,45,39,37,0,],
            },
            "Suy nhuoc co the 2": {
                "Day an": [37,28,50,14,41,19,0,],
            },
            "Suy nhuoc co the 3": {
                "Day an": [0,22,62,162,1,460,300,301,],
            },
            "Suy nhuoc co the 4": {
                "Day an": [61,432,565,12,7,19,37,1,50,312,103,],
            },
            "Suy nhuoc co the 5": {
                "Nhung truong hop nhu the nay dung Bo Bo Am Huyet rat tot": [22,127,63,7,113,19,64,50,39,37,1,290,0,],
                "Co the day an nhieu lan trong ngay": [],
            },
            "Suy nhuoc than kinh 1": {
                "Day an": [127,37,1,50,73,106,103,],
            },
            "Suy nhuoc than kinh 2": {
                "Day an": [22,127,63,19,1,61,188,477,97,103,],
            },
            "Suy nhuoc than kinh 3": {
                "Day an": [127,19,50,1,37,103,300,324,340,175,106,107,0,],
            },
        }

    def list_T(self):
        return {
            "Tai - diec 1": { "Day an": [150,0,],
            },
            "Tai - diec 2": {
                "Day an": [8,189,1,38,57,132,],
            },
            "Tai - diec 3": {
                "Day an": [43,45,65,399,235,0,],
            },
            "Tai - tai giua co mu 1": {
                "Day an": [14,15,16,0,],
            },
            "Tai - tai giua co mu 2": {
                "Day an": [65,45,17,38,],
                "Thoi hoi nong vao lo tai co mu": [],
            },
            "Tai - tai nhuc khi may bay gan ha canh": {
                "Bit mui, mo mieng hit vao co nuot xuong ba lan": [],
            },
            "Tai - tai u 1": {
                "Day an": [57,54,15,0,],
            },
            "Tai - tai u 2": {
                "Day an": [0,14,15,16,138,3,179,567,],
                "Ho lan chi thu 3 cua ngon tay tro co lai": [],
            },
            "Tai - tai u 3": {
                "Day an, ho": [65,290,1,3,61,300,60,16,138,0,],
            },
            "Tai - tai u 4": {
                "Ho vao lo tai u va day huyet tren tai va ho sinh huyet tai o ngon tro": [],
                "Ho phan chieu tai o mat (do hinh am) va quanh mat ca chan": [],
            },
            "Tay dau - canh tay 1": {
                "Go": [559,560,],
            },
            "Tay dau - canh tay 2": {
                "Day an": [98,100,217,],
            },
            "Tay dau - canh tay 3": {
                "Day an": [60,97,98,99,],
            },
            "Tay dau - ba vai 1": {
                "Day an": [477,97,98,99,106,34,],
            },
            "Tay dau - ba vai 2": {
                "Go": [65,],
            },
            "Tay dau - khop vai 1": {
                "Day an": [26,88,65,278,],
            },
            "Tay dau - khop vai 2": {
                "Day an": [26,19,97,564,],
            },
            "Tay dau - khop vai 3": {
                "Lan vung phan chieu vai": [],
                "Go": [65,34,],
            },
            "Tay dau - khuyu tay 1": {
                "Day an": [98,28,10,191,],
            },
            "Tay dau - khuyu tay 2": {
                "Ho khuyu tay doi xung hoac go": [98,],
            },
            "Tay dau - co tay 1": {
                "Day an": [3,100,179,180,],
            },
            "Tay dau - co tay 2": {
                "Ho va go": [100,],
            },
            "Tay dau - nam ngon tay": {
                "Day an": [460,60,45,17,300,],
            },
            "Tay dau - tay khong gio len duoc 1": {
                "Go vai chuc cai vao": [65,100,],
            },
            "Tay dau - tay khong gio len duoc 2": {
                "Go": [219,],
            },
            "Tay dau - tay khong gio len duoc 3": {
                "Day an": [278,88,50,],
            },
            "Tay dau - canh tay, ban tay te": {
                "Lan vung go may (do hinh phan chieu canh tay tren mat) xong day an": [0,19,130,],
                "Ve cau gai 1 luc la het": [],
            },
            "Tao tinh 1": {
                "Day an": [127,63,1,103,37,50,0,],
            },
            "Tao tinh 2": {
                "Day an": [124,34,26,300,1,290,19,127,156,0,],
            },
            "Tao tinh 3": {
                "Luc sap xuat tinh, dung ba dau ngon tay vuot nhe dau mui nhieu lan": [143,],
            },
            "Tac tia sua": {
                "An": [73,],
            },
            "Tac tieng 1": {
                "Day an": [19,61,204,],
            },
            "Tac tieng 2": {
                "Go": [14,275,274,277,],
            },
            "Tam than phan liet": {
                "Go va ho": [103,106,300,126,127,19,50,37,1,290,],
            },
            "Tieu chay 1": {
                "Day an, ho": [87,22,127,132,],
            },
            "Tieu chay 2": {
                "Day an": [127,63,38,113,37,143,41,50,233,300,],
            },
            "Tieu chay 3": {
                "Day an, ho": [127,22,365,],
            },
            "Tieu chay 4": {
                "Ho 2 ban chan khoang 10 phut": [],
                "Vuot quanh moi tu trai sang phai nhieu lan (Chu y: Neu vuot nguoc lai tu pahi sang trai la chong tao bon)": [],
            },
            "Tieu chay 5": {
                "Neu tieu chay cho lanh (han thap) thi day an va ho": [365,22,127,],
            },
            "Tieu chay 5": {
                "Neu tieu chay cho nong (nhiet thap) thi day an va ho": [26,3,143,365,],
            },
            "Tieu chay 6": {
                "Co the dung toa tac nghe voi luong nghe nhieu hon tac o benh tieu chay do han va nguoc lai voi benh tieu chay do nhiet": [],
            },
            "Te luoi - cung luoi": {
                "Day an": [282,79,],
                "Ho, lan ngon cai ban tay trai": [],
            },
            "Tieu - tieu dam 1": {
                "Day an": [124,34,60,87,],
            },
            "Tieu - tieu dam 2": {
                "Day an": [124,34,19,37,],
            },
            "Tieu - tieu dem 1": {
                "Day an": [19,37,],
            },
            "Tieu - tieu dem 2": {
                "Day an": [124,34,21,],
            },
            "Tieu - tieu dem 3": {
                "Day an": [0,37,45,300,],
            },
            "Tieu - tieu dem 4": {
                "Day an": [32,19,45,100,],
            },
            "Tieu - tieu duc 1": {
                "Day an": [85,87,],
            },
            "Tieu - tieu duc 2": {
                "Day an": [29,222,85,87,300,0,],
            },
            "Tieu - tieu duong 1": {
                "Day an": [73,3,37,156,],
            },
            "Tieu - tieu duong 2": {
                "Day an": [26,113,63,100,236,3,],
            },
            "Tieu - tieu duong 3": {
                "Day an": [127,156,63,113,143,38,50,37,1,3,73,],
            },
            "Tieu - tieu duong 4": {
                "Di bo moi ngay 3-4 km": [],
                "Tra (che) tuoi xac nhuyen ham nuoc soi uong": [],
                "Cham kem deep heat va sau do day an vao cac huyet": [63,7,113,37,40,],
            },
            "Tieu - tieu tac 1": {
                "Day an": [26,3,38,85,87,],
            },
            "Tieu - tieu tac 2": {
                "Day an": [342,43,87,],
            },
            "Tieu - tieu tac 3": {
                "Day an": [37,87,],
            },
            "Tieu - tieu tac 4": {
                "Day an": [29,85,],
            },
            "Tieu - tieu it 1": {
                "Day an": [26,3,85,],
            },
            "Tieu - tieu it 2": {
                "Day an": [87,235,29,],
            },
            "Tieu - tieu lien tuc khong kim duoc 1": {
                "Day an": [16,37,9,],
                "Vuot u cam": [],
            },
            "Tieu - tieu lien tuc khong kim duoc 2": {
                "Day an": [138,16,87,0,],
            },
            "Tieu - tieu nhieu 1": {
                "Day an": [87,19,1,],
            },
            "Tieu - tieu nhieu 2": {
                "Day an": [0,37,103,],
            },
            "Tieu - tieu nhieu 3": {
                "Day an": [19,37,],
            },
            "Tieu - tieu nhieu, tieu gat 1": {
                "Lan khap mat roi go": [87,],
            },
            "Tieu - tieu nhieu, tieu gat 2": {
                "Day an": [87,19,37,41,103,],
                "Ho phan chieu bang quang co tay": [],
            },
            "Tieu - tieu nhieu, tieu gat 3": {
                "Day an": [37,19,87,300,],
            },
            "Tim - tim lon 1": {
                "Day an": [34,61,269,37,88,],
            },
            "Tim - tim lon 2": {
                "Day an": [26,174,87,51,357,29,220,60,57,50,],
            },
            "Tim - thieu mau co tim, hep van tim": {
                "Lan va bop qua cau gai 1 luc": [],
                "Thuong xuyen lan song mui tu 189 den 1, lan hang ngay 2 lan (sang toi)": [189,1,],
            },
            "Tinh hoan dau nhuc": {
                "Day an": [38,61,127,5,],
            },
            "Toc bac": {
                "Ha thu o do nau nuoc roi co lai (bo xac) de tu lanh xai dan. Moi bua dung 1 ly nho pha them chut ruou co hoa mat ong, uong truoc bua an": [],
                "49 hay dau den rua sach cho vao am nuoc 15 phut sau uong het (nuot chung) khong nhat. Moi sang uong nhu vay cho den khi toc den tro lai": [],
            },
            "To dia": {
                "Day an": [26,61,50,38,156,],
                "Ho va lan nhung cho nut": [],
            },
            "Tu cung - dau thuong": {
                "Day an": [19,63,53,7,],
            },
            "Tu cung - co cac loai viem buou": {
                "Day an": [106,267,1,36,127,],
            },
            "Tu cung - u xo to cung": {
                "Day an": [19,76,3,50,1,103,39,127,],
            },
            "Than kinh lien suon": {
                "Day an": [41,28,60,100,0,],
            },
            "Than kinh toa 1": {
                "Day an": [1,19,5,219,421,143,3,43,],
            },
            "Than kinh toa 2": {
                "Day an": [210,197,34,],
            },
            "Than kinh toa 3": {
                "Dung cau gai doi nho lan tren tran theo do hinh so 2": [],
                "Dung cao cao tren da dau theo do hinh so 11. Bi ben nao cao ben con lai": [],
            },
            "Than kinh so 5 1": {
                "Day an": [34,100,555,16,277,156,61,],
            },
            "Than kinh so 5 2": {
                "Day an (so 3 ben doi, con lai ben dau)": [156,7,61,3,300,94,],
            },
            "Thieu sua": {
                "Day an": [26,73,39,3,50,],
            },
            "Thoat vi ben": {
                "Day an": [19,7,65,126,],
            },
            "Tri 1": {
                "Go": [64,74,],
            },
            "Tri 2": {
                "Lan va go": [365,7,3,37,],
            },
            "Tri 3": {
                "Day an": [19,143,23,43,103,348,0,],
            },
            "Tri 4": {
                "Cha nuoc da": [365,19,1,103,38,],
            },
            "Tri 5": {
                "Day an": [143,173,23,43,103,348,126,],
            },
            "Tri 6": {
                "Ho ngai cuu cach bui tri khoang 10cm": [],
            },
            "Tri 7": {
                "Day an": [34,124,300,103,126,],
            },
            "Tri 8": {
                "Day an": [127,38,50,143,37,],
            },
        }

    def list_U(self):
        return {
            "NA": [],
        }

    def list_V(self):
        return {
            "NA": [],
        }

    def list_X(self):
        return {
            "NA": [],
        }

    def list_Y(self):
        return {
            "NA": [],
        }

