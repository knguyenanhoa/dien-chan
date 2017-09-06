class Sets():
    def __init__(self):
        pass

    def list(self, *args, **kwargs):
        func_name = "list_"+kwargs['key']
        func = getattr(self, func_name) 
        return func()

    def list_A(self):
        return {
            "Amidan 1": ['12L','12R','38L','38R','14L','14R','275A','277A','274A'],
            "Amidan 2": ['26','3L','3R','87','100L','100R','143A'],
            "Amidan 3": ['26','3L','3R','87','15A',],
            "An than": ['26'],
            "An kem": ['22','127','63','7L','7R','113L','113R','17L','17R','19','64L','64R','50','39','37','1','290L','290R','0L','0R',],
            "An khong tieu": ['19'],
            "Am dao (tu cung) dau": ['19','63','53','7L','7R',],
        }
    
    def list_B(self):
        return {
            "Ba vai dau 1": ['332L','332R','360L','360R','16A',],
            "Ba vai dau 2": ['73L','73R','330L','330R',],
            "Ba vai dau 3": ['477L','477R','97L','97R','99L','99R','98L','98R','106','34L','34R'],
            "Ba vai dau 4 (dau khop vai)": ['26','88A','65L','65R','278L','278R','278A'],
            "Ba vai dau 5 (dau khop vai)": ['26','19','97L','97R','564L','564R',], #
            "Ba vai dau 6 (dau khop vai)": [],
            "Bach bi bach bien": ['64','3','132','106',],
        }

    def list_C(self):
        return {
            "Test": ['195R','195L'],
        }
    
    def list_D(self):
        return {
            "Test": ['195R','195L'],
        }

    def list_E(self):
        return {
            "Test": ['195R','195L'],
        }

    def list_G(self):
        return {
            "Test": ['195R','195L'],
        }

    def list_H(self):
        return {
            "Test": ['195R','195L'],
            'Ho ngua co 1': ['61L','61R','74L','74R','64L','64R','14L','14R'],
            'Ho ngua co 2': ['8','20L','20R','12L','12R'],
            'Ho ngua co 3': [],
        }

    def list_I(self):
        return {
            "Test": ['195R','195L'],
        }

    def list_K(self):
        return {
            "Test": ['195R','195L'],
        }

    def list_L(self):
        return {
            "Test": ['195R','195L'],
        }

    def list_M(self):
        return {
            "Test": ['195R','195L'],
        }

    def list_N(self):
        return {
            "Test": ['195R','195L'],
        }

    def list_O(self):
        return {
            "Test": ['195R','195L'],
        }

    def list_P(self):
        return {
            "Test": ['195R','195L'],
        }

    def list_Q(self):
        return {
            "Test": ['195R','195L'],
        }

    def list_R(self):
        return {
            "Test": ['195R','195L'],
        }

    def list_S(self):
        return {
            "Test": ['195R','195L'],
        }

    def list_T(self):
        return {
            "Test": ['195R','195L'],
        }

    def list_U(self):
        return {
            "Test": ['195R','195L'],
        }

    def list_V(self):
        return {
            "Test": ['195R','195L'],
        }

    def list_X(self):
        return {
            "Test": ['195R','195L'],
        }

    def list_Y(self):
        return {
            "Test": ['195R','195L'],
        }

