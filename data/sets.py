class Sets():
    def __init__(self):
        pass

    def list(self, *args, **kwargs):
        func_name = "list_"+kwargs['key']
        func = getattr(self, func_name) 
        return func()

    def list_A(self):
        pass
    
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

