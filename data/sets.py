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
        pass

    def list_C(self):
        pass
    
    def list_D(self):
        pass

    def list_E(self):
        pass

    def list_G(self):
        pass

    def list_H(self):
        return {
            "Test": ['195R','195L'],
            'Ho ngua co 1': ['61L','61R','74L','74R','64L','64R','14L','14R'],
            'Ho ngua co 2': ['8','20L','20R','12L','12R'],
            'Ho ngua co 3': [],
        }

