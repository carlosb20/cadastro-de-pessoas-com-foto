from tkinter import *


class Cadastro(Tk):
    def __init__(self ) -> None:
        super().__init__()


        self.frame_foto = Frame(self,bg='red',bd=1,relief='groove')
        self.frame_foto.place(relx=0.00,rely=0.01,relwidth=0.99,relheight=0.20)

        self.texto = Label(self.frame_foto,text='cadastro de pessoas ',font=('arial 12 bold'),bg='blue',fg='white')
        self.texto.pack(fill='x')

        



if __name__=='__main__':
    ja = Cadastro()
    ja.geometry('600x640+400+10')
    ja.mainloop()
