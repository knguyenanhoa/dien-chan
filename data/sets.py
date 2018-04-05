class Sets():
    def __init__(self):
        pass

    def list(self, *args, **kwargs):
        func_name = "list_"+kwargs['key']
        func = getattr(self, func_name) 
        return func()

    def list_A(self):
        return {
            "Amidan 1": [12,38,14,275,277,274],
            "Amidan 2": [26,3,87,100,143],
            "Amidan 3": [26,3,87,15,],
            "An than": [26],
            "An kem": [22,127,63,7,113,17,19,64,50,39,37,1,290,0,],
            "An khong tieu": [19],
            "Am dao (tu cung) dau": [19,63,53,7,],
        }
    
    def list_B(self):
        return {
            "Ba vai dau 1": [332,360,16,],
            "Ba vai dau 2": [73,330,],
            "Ba vai dau 3": [477,97,99,98,106,34],
            "Ba vai dau 4 (dau khop vai)": [26,88,65,278,],
            "Ba vai dau 5 (dau khop vai)": [26,19,97,564,],
            "Ba vai dau 6 (dau khop vai)": [],
            "Bach bi bach bien": [64,3,132,106,],
            "Ban tay lo loet": [],
            "Bao tu (da day) dau 1": [124,34,61,39,120,121,19,64,73,162,62,189,126,59,],
            "Bao tu (da day) dau 2": [61,120,39,121,],
            "Bao tu (da day) dau 3": [235,37,124,630,],
            "Bao tu (da day) dau 4": [61,39,64,630],
            "Bao tu (da day) dau 5": [],
            "Bam mau va sung do chan thuong": [156,7,50,3,61,290,16,37,],
            "Bi tieu": [220,26,174,87,51,375,29,60,57,50,],
            "Bon (tao bon) 1": [41,143,38,],
            "Bon (tao bon) 2": [26,61,38,41,365,],
            "Bon (tao bon) 3": [],
            "Bon (tao bon) 4": [],
            "Bon (tao bon) 5": [],
            "Bon (tao bon) 6": [],
            "Bon (tao bon) 7": [],
            "Bo mau 1": [50,19,39],
            "Bo mau 2": [127,42,35,290,1,],
            "Bo mau 3": [22,127,63,7,113,17,19,64,50,39,37,1,290,0,],
            "Bui vao mat": [],
            "Bung dau 1": [],
            "Bung dau 2": [],
            "Bung dau 3": [],
            "Bung dau 4": [61,28,3,],
            "Bung dau 5": [365,22,127,19,50,1,37,61,0,],
            "Bung dau 6": [19,127,39,3,38,63,41,],
            "Bung dau 7": [26,61,3,143,38,],
            "Buou 1": [8,12,61,38,60,275,14,50,37,19,127,],
            "Buou 2": [8,12,60,39,38,50,14,275,],
            "Buou 3": [26,196,12,8,61,19,],
            "Buou doc (Basedow) 1": [39,38,287,7,113,156,74,64,87,57,60,100,],
            "Buou doc (Basedow) 2": [14,64,8,12,37,17,50,39,87,51,124,34,],
            "Buou co cac dang 1": [26,8,12,61,3,50,233,39,51,286,235,113,14,308,],
            "Buou dau duong vat, di tieu rat kho": [143,17,38,61,3,26,60,57,127,50,37,103,],
            "Buou buong trung 1": [124,26,37,50,63,7,],
            "Buou buong trung 2": [26,65,3,37,16,87,27,],
            "Buou cac loai tich tu trong co the": [41,143,127,19,37,38],
        }

    def list_C(self):
        return {
            "Cai thuoc la - cai ruou 1": [124,19,51,],
            "Cai thuoc la - cai ruou 2": [124,19,127,57,3,],
            "Cai thuoc la - cai ruou 3": [127,37,50,19,1,106,103,300,0,],
            "Cam lanh - ret run 1": [127,63,19,61,1,106,103,300,],
            "Cam lanh - ret run 2": [127,50,19,37,1,73,103,0,],
            "Cam lanh - ret run 3": [],
            "Cam lanh - ret run 4": [127,50,19,37,1,73,189,103,300,0,],
            "Cam nong 1": [26,3,1,39,38,222,4,43,156,87],
            "Cam nong 2": [124,34,26,61,3,143,222,14,156,87,],
            "Canh tay dau 1": [60,97,98,99],
            "Canh tay dau 2": [],
            "Canh tay dau 3": [],
            "Cam mau 1": [16,61,0,],
            "Cam mau 2": [16,61,50,37,0,],
            "Cam mau 3": [],
            "Can thi 1": [34,6,],
            "Can thi 2": [34,1,127,],
            "Can thi 3": [267,130,3,388,],
            "Co giat lien tuc": [19,127,8,34,124,0,],
            "Co luoi": [14,],
            "Co gay cung moi 1": [16,61,287,],
            "Co gay cung moi 2": [65,106,16,],
            "Co gay cung moi 3": [65,8,290,127,87,],
            "Co gay cung moi 4": [188,477,34,97,98,99,100,],
            "Co gay cung moi 5": [8,20,12,65,],
            "Co gay cung moi 6": [],
            "Co gay cung moi 7": [7,],
            "Co gay cung moi 8": [],
            "Co gay cung moi 9": [156,],
            "Cot song dau 1": [342,348,],
            "Cot song dau 2": [],
            "Cot song dau 3": [],
            "Cot song dau 4": [19,64,63,45,43,300,],
            "Cot song dau 5": [275,],
            "Cot song dau 6": [175,127,],
            "Cot song dau 7": [423,99,467,],
            "Cot song dau 8": [],
            "Cot song dau 9": [],
            "Cot song dau 10": [1,189,8,106,103,],
            "Cot song dau 11": [],
            "Cot song dau 12": [0,300,15,38,17,],
            "Cot song dau 13": [210,300,560,],
            "Cot song dau 14": [138,],
            "Cot song dau 15": [],
            "Cot song dau 16": [26,8,1,],
            "Cot song dau 17": [23,143,19,],
            "Cot song dau 18": [],
            "Cot song dau 19": [],
            "Cuong duong 1": [],
            "Cuong duong 2": [],
            "Chai chan 1": [26,51,],
            "Chai chan 2": [],
            "Chai chan 3": [],
            "Cham lac 1": [61,38,50,51,],
            "Cham lac 2": [3,347,51,],
            "Cham lac 3": [62,51,38,],
            "Cham lac 4": [124,34,3,39,156,26,60,],
            "Chay nuoc mat song 1": [16,61,],
            "Chay nuoc mat song 2": [16,195,87,51,],
            "Chan dau - dau mong, dau than kinh toa 1": [41,210,5,253,3,51,],
            "Chan dau - dau mong, dau than kinh toa 2": [1,45,43,74,64,5,253,210,14,15,16,0,],
            "Chan dau - dau mong, dau than kinh toa 3": [87,210,5,143,174,],
            "Chan dau - dau mong, dau than kinh toa 4": [2,],
            "Chan dau - dau mong, dau than kinh toa 5": [11,],
            "Chan dau - dau khop hang 1": [64,74,210,],
            "Chan dau - dau khop hang 2": [],
            "Chan dau - dau khop goi 1": [17,38,197,300,45,0,],
            "Chan dau - dau khop goi 2": [17,38,9,96,],
            "Chan dau - dau khop goi 3": [129,100,156,39,],
            "Chan dau - dau khop goi 4": [],
            "Chan dau - dau kheo (nhuong) chan 1": [29,222,],
            "Chan dau - dau kheo (nhuong) chan 2": [],
            "Chan dau - dau co chan 1": [347,127,],
            "Chan dau - dau co chan 2": [],
            "Chan dau - dau got chan (hoac gai got chan) 1": [461,127,107,],
            "Chan dau - dau got chan (hoac gai got chan) 2": [9,63,127,156,],
            "Chan dau - dau got chan (hoac gai got chan) 3": [],
            "Chan dau - dau got chan (hoac gai got chan) 4": [],
            "Chan thuong so nao va hon me 1": [127,53,63,19,50,37,39,106,103,126,0],
            "Chan thuong so nao va hon me 2": [26,38,156,7,50,3,61,290,16,37,],
            "Chong mat - binh thuong 1": [61,8,63,],
            "Chong mat - binh thuong 2": [8,19,63,],
            "Chong mat - binh thuong 3": [63,19,127,0],
            "Chong mat - binh thuong 4": [34,290,156,70,],
            "Chong mat - roi loan tien dinh 1": [124,34,65,189,3,],
            "Chong mat - roi loan tien dinh 2": [127,63,8,60,65,103,0,],
        }

    def list_D(self):
        return {
            "Di mong tinh 1": [0,1,45,8,],
            "Di mong tinh 2": [124,34,45,],
            "Di mong tinh 3": [43,45,0,],
            "Di mong tinh 4": [300,1,45,127,0,],
            "Di ung noi me day 1": [61,3,184,50,87,],
            "Di ung noi me day 2": [41,50,17,7,60,85,],
            "Di ung noi me day 3": [124,34,26,61,3,60,50,],
            "Doi an 1": [61,38,50,],
            "Doi an 2": [61,64,],
            "Doi an 3": [],
            "Duong nuy": [1,50,19,39,7,127,103,],
            "Dau bung kinh 1": [127,],
            "Dau bung kinh 2": [1,63,50,7,127,],
            "Dau bung kinh 3": [63,19,50,127,],
            "Dau bung kinh 4": [],
            "Dau bung sau khi tam": [0,17,],
            "Dang mieng": [26,184,235,227],
            "Day hoi": [],
            "Dinh rau": [3,38,41,61,104,0,],
            "Dieu chinh am duong 1": [34,290,156,39,19,50,],
            "Dieu chinh am duong 2": [1,39,19,50,57,],
            "Dieu chinh am duong 3": [103,1,127,],
            "Ham mat dau cung ben trai 1": [156,7,61,300,94,3,],
            "Ham mat dau cung ben trai 2": [8,12,20,196,188,73,276,14,15,275,],
            "Ham mat dau cung ben trai 3": [],
            "Hat hoi 1": [209,],
            "Hat hoi 2": [19,63,1,0],
            "Hat hoi 3": [103,26,],
            "Hernie 1": [132,],
            "Hernie 2": [342,19,38,9,143,104,105,561,98,],
            "Hiem muon 1": [7,113,63,127,0,],
            "Hiem muon 2": [127,156,87,50,37,65,0,],
            "Ho - ho ngua co 1": [61,74,64,14,],
            "Ho - ho ngua co 2": [8,20,12,],
            "Ho - ho ngua co 3": [],
            "Ho - ngua co lien hoi, khong dam": [8,127,20,176,275,467,],
            "Ho - ho khan 1": [14,275,60,74,180,],
            "Ho - ho khan 2": [73,3,276,],
            "Ho - ho khan 3": [26,61,3,51,],
            "Ho - ho khan 4": [17,38,275,],
            "Ho - ho khan lau ngay": [14,275,277,],
            "Ho - ho dam 1": [37,58,132,3,275,274,],
            "Ho - ho dam 2": [61,467,491,],
            "Ho - ho dam 3": [8,12,20,],
            "Ho - ho dam 4": [61,74,64,26,],
            "Ho - ho dam 5": [],
            "Ho - ho lau ngay": [300,301,14,61,64,127,156,0,],
            "Ho - suyen nhiet": [26,3,51,87,85,21,275,14,312,],
            "Ho - suyen han": [],
        }

    def list_E(self):
        return {
            "Test": [195,195],
        }

    def list_G(self):
        return {
            "Test": [195,195],
        }

    def list_H(self):
        return {
            "Test": [195,195],
            "Ho ngua co 1": [61,61,74,74,64,64,14,14],
            "Ho ngua co 2": [8,20,20,12,12],
            "Ho ngua co 3": [],
        }

    def list_I(self):
        return {
            "Test": [195,195],
        }

    def list_K(self):
        return {
            "Test": [195,195],
        }

    def list_L(self):
        return {
            "Test": [195,195],
        }

    def list_M(self):
        return {
            "Test": [195,195],
        }

    def list_N(self):
        return {
            "Test": [195,195],
        }

    def list_O(self):
        return {
            "Test": [195,195],
        }

    def list_P(self):
        return {
            "Test": [195,195],
        }

    def list_Q(self):
        return {
            "Test": [195,195],
        }

    def list_R(self):
        return {
            "Test": [195,195],
        }

    def list_S(self):
        return {
            "Test": [195,195],
        }

    def list_T(self):
        return {
            "Test": [195,195],
        }

    def list_U(self):
        return {
            "Test": [195,195],
        }

    def list_V(self):
        return {
            "Test": [195,195],
        }

    def list_X(self):
        return {
            "Test": [195,195],
        }

    def list_Y(self):
        return {
            "Test": [195,195],
        }

