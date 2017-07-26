class Sets():
    def __init__(self):
        pass

    def list(self, *args, **kwargs):
        func_name = "list_"+kwargs['key']
        func = getattr(self, func_name) 
        return func()

    def list_H(self):
        return {
            "Ho ngua co": ['61L','61R','74L','74R','64L','64R','14L','14R'],
            "Test": ['61R']
        }

