from tkinter import*
import pyautogui


class Teste(Tk):
    def __init__(self) -> None:
        super().__init__()

        self.pega = StringVar()

        self.entrda = Entry(self,font='arial 15',textvariable=self.pega)
        self.entrda.bind('<KeyRelease>',self.da)
        self.entrda.place(x=100,y=100)

    def da(self,s):
        print('ok')
        res = self.entrda.get()
        re = len(res)
        if re == 3:
            print('passou')
            self.pega.set(str(res) +'.')
            pyautogui.press['left']
           
        


if __name__=='__main__':
    res = Teste()
    res.geometry('900x500')
    res.mainloop()