from tkinter import*
import pyautogui


class Teste(Tk):
    def __init__(self) -> None:
        super().__init__()

        self.pega = StringVar()

        self.traco = StringVar()

        self.entrda = Entry(self,font='arial 15',textvariable=self.pega)
        self.entrda.bind('<KeyRelease>',self.da)
        self.entrda.place(x=100,y=100)

        self.cpf = Entry(self,font='arial 15',textvariable=self.traco)
        self.cpf.place(x=100,y=130)


        self.bt = Button(self,text='enviar',command=self.ver)
        self.bt.place(x=150,y=180)

        self.fromata = Button(self,text='formata',command=self.forme)
        self.fromata.place(x=200,y=180)

        self.d = Button(self,text='ponto e traco',command=self.coloca_ponto)
        self.d.place(x=300,y=180)

    def da(self,s):

        res = self.entrda.get()
        re = len(res)

        if re == 3:
            self.pega.set(str(res) +'.')
            pyautogui.press(['right'])
           
        if re == 7:
            self.pega.set(str(res) +'.')
            pyautogui.press(['right'])
           
        if re == 11:
            self.pega.set(str(res) +'-')
            pyautogui.press(['right'])

        elif re > 14:
            self.entrda.delete(14,'end')
            self.cpf.focus()

    def ver(self):
        print(self.entrda.get())

    def forme(self):
        
        self.novo = self.entrda.get()

        self.novo = self.novo.replace('.','').replace('-','')

        print(self.novo)

    def coloca_ponto(self):
        pass

if __name__=='__main__':
    res = Teste()
    res.geometry('900x500')
    res.mainloop()