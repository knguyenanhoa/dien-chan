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
        }

    def list_C(self):
        return {
            "Test": [195,195],
        }
    
    def list_D(self):
        return {
            "Test": [195,195],
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

