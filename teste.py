from tkinter import*

class Teste_entry:
    def __init__(self,master):
        self.root = master

        self.valor = StringVar()
        

        self.log = Entry(self.root,textvariable=self.valor)
        self.log.bind("<KeyRelease>",self.vas)
        self.b = Entry(self.root)

        self.log.pack()
        self.b.pack()

    def vas(self,*s):
        print('ok')
        res = int(self.log.get())
        print(res)
        
        if res == 123:
            print('sim')
            self.valor.set('.')




root = Tk()
b = Teste_entry(root)
root.mainloop()