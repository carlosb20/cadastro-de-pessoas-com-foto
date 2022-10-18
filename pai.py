from tkinter import *


class Cadastro(Tk):
    def __init__(self ) -> None:
        super().__init__()


        self.frame_foto = Frame(self,bg='red',bd=1,relief='groove',width=100,height=160,)
        self.frame_foto.pack(fill='x')

        self.texto = Label(self.frame_foto,text='cadastro de pessoas ',font=('arial 12 bold'),bg='blue',fg='white')
        self.texto.pack(fill='x')

        self.canvas = Canvas(self.frame_foto,width=120,height=120,bg='silver')
        self.canvas.pack(anchor='w',pady=25,padx=5)

        self.btn = Button(self.frame_foto,text='foto',width=10)
        self.btn.place(x=150,y=147)



if __name__=='__main__':
    ja = Cadastro()
    ja.geometry('600x640+400+10')
    ja.mainloop()
