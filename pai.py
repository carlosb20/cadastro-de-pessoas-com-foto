from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image,ImageTk

foto = b''

class Cadastro(Tk):
    def __init__(self ) -> None:
        super().__init__()

        self.frame_foto = Frame(self,bg='red',width=600,height=190)
        self.frame_foto.pack()

        self.texto = Label(self.frame_foto,text='cadastro de pessoas ',font=('arial 15 bold'),bg='red',fg='white')
        self.texto.place(relx=0.30,rely=0.01)

        self.origem = Image.open('usuario10.png')
        self.origem = self.origem.resize((150,150))
        self.origem = ImageTk.PhotoImage(self.origem)

        self.label_foto = Label(self.frame_foto,image=self.origem)
        self.label_foto.place(x=5,y=30,relwidth=0.25,relheight=0.80)

        self.bt_img = Button(self.frame_foto,text='imagem',width=10,command=self.dados_imag)
        self.bt_img.place(x=170,y=151)

        self.bt_DELETA = Button(self.frame_foto,text='Excluir',width=10,command=self.deleta_img)
        self.bt_DELETA.place(x=260,y=151)

    def dados_imag(self):
        global foto,img

        path = askopenfilename()
        if path:
            ler_img = open(path,'rb')
            foto = ler_img.read()
            ler_img.close()

            img = Image.open(path)
            img = img.resize((150,150))
            img = ImageTk.PhotoImage(img)
            self.label_foto['image'] = img

    def deleta_img(self):
        pass




if __name__=='__main__':
    ja = Cadastro()
    ja.geometry('600x640+400+10')
    ja.resizable(0,0)
    ja.mainloop()
