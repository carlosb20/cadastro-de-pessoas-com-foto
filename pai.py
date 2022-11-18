from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox

foto = b''

class Cadastro(Tk):
    def __init__(self ) -> None:
        super().__init__()

        self.primeiro()
        self.frame_dados()
        self.treev_tabela()

    def primeiro(self):

        self.frame_foto = Frame(self,bg='#00bfff',width=600,height=190)
        self.frame_foto.pack(fill='x')

        self.texto = Label(self.frame_foto,text='cadastro de pessoas ',font=('arial 15 bold'),bg='#00bfff',fg='white')
        self.texto.place(relx=0.40,rely=0.01)

        self.origem = Image.open('usuario10.png')
        self.origem = self.origem.resize((150,150))
        self.origem = ImageTk.PhotoImage(self.origem)

        self.label_foto = Label(self.frame_foto,image=self.origem)
        self.label_foto.place(x=5,y=30,relwidth=0.19,relheight=0.80)

        self.bt_img = Button(self.frame_foto,text='Imagem',width=10,command=self.dados_imag,fg='white')
        self.bt_img.config(font='arial 10')
        self.bt_img.config(bg='#4682b4')
        self.bt_img.place(x=170,y=151)

        self.bt_DELETA = Button(self.frame_foto,text='Excluir',width=10,command=self.deleta_img,fg='white')
        self.bt_DELETA.config(bg='#4682b4')
        self.bt_DELETA.config(font='arial 10')
        self.bt_DELETA.place(x=280,y=151)

    def frame_dados(self):

        self.frame_get_dados = Frame(self,width=600,height=200,bg='blue')
        self.frame_get_dados.pack(fill='x')


        self.label_nome = Label(self.frame_get_dados,text='Nome',font=('arial 12'),bg='blue',fg='white')
        self.label_nome.place(x =5,y = 6)

        self.entry_nome = Entry(self.frame_get_dados,font=('arial 13'),width=30)
        self.entry_nome.place(x=60,y=6)

        self.label_cpf = Label(self.frame_get_dados,text='Cpf',bg='blue',fg='white',font=('arial 12'))
        self.label_cpf.place(x=5,y=40)

        self.entry_cpf = Entry(self.frame_get_dados,font=('arial 13'),width=30)
        self.entry_cpf.place(x=60,y=40)

        self.label_rg = Label(self.frame_get_dados,text='RG',bg='blue',fg='white',font=('arial 12'))
        self.label_rg.place(x=5,y=80)

        self.entry_rg = Entry(self.frame_get_dados,font=('arial 13'),width=30)
        self.entry_rg.place(x=60,y=80)

        self.label_email = Label(self.frame_get_dados,text='E-mail',bg='blue',fg='white',font=('arial 12'))
        self.label_email.place(x=5,y=120)

        self.entry_egmail = Entry(self.frame_get_dados,font=('arial 13'),width=30)
        self.entry_egmail.place(x=60,y=120)
        #------------------------------------------------------------------------
        self.bt_enviar = Button(self.frame_get_dados,text='Enviar',font=('arial 13'),width=20,bg='orange',fg='black')
        self.bt_enviar.config(cursor='hand2')
        self.bt_enviar.config(overrelief='groove')
        self.bt_enviar.config(command=self.get_dados)
        self.bt_enviar.place(x=6,y=160)

        self.bt_limpa = Button(self.frame_get_dados,text='Limpa',font=('arial 13'),width=20,bg='orange',fg='black')
        self.bt_limpa.config(cursor='hand2')
        self.bt_limpa.config(overrelief='groove')
        #self.bt_limpa.config(command=self.get_dados)
        self.bt_limpa.place(x=205,y=160)

        self.bt_atualiza = Button(self.frame_get_dados,text='Atualizar',font=('arial 13'),width=20,bg='orange',fg='black')
        self.bt_atualiza.config(cursor='hand2')
        self.bt_atualiza.config(overrelief='groove')
        #self.bt_atualiza.config(command=self.get_dados)
        self.bt_atualiza.place(x=405,y=160)

        self.bt_deleta = Button(self.frame_get_dados,text='Excluir',font=('arial 13'),width=20,bg='orange',fg='black')
        self.bt_deleta.config(cursor='hand2')
        self.bt_deleta.config(overrelief='groove')
        #self.bt_deleta.config(command=self.get_dados)
        self.bt_deleta.place(x=605,y=160)

    def treev_tabela(self):

        self.trevv = ttk.Treeview(self,columns=['nome','cpf','rg','email'],show='headings')
        
        self.trevv.heading('nome',text='nome',anchor='w')
        self.trevv.heading('cpf',text='cpf')
        self.trevv.heading('rg',text='RG')
        self.trevv.heading('email',text='E-mail')
        self.trevv.column('email',width=180)
    
        self.barra = ttk.Scrollbar(self)
        
        self.trevv.config(yscrollcommand=self.barra.set)
        self.barra.config(command=self.trevv.yview)

        self.trevv.place(x=1,y=391,relheight=0.39)
        self.barra.place(x=784,y=393,relheight=0.38,relwidth=0.02)

        
    def get_dados(self):
        if self.entry_nome.get() != '' and self.entry_cpf.get() != '' and self.entry_rg.get() != '' and self.entry_egmail.get() != '' :
            self.trevv.insert('','end',values=(self.entry_nome.get(),
                self.entry_cpf.get(),
                self.entry_rg.get(),
                self.entry_egmail.get()))

            self.entry_nome.delete(0,'end')
            self.entry_cpf.delete(0,'end')
            self.entry_rg.delete(0,'end')
            self.entry_egmail.delete(0,'end')
            self.entry_nome.focus()

            self.label_foto.config(image=self.origem)

        else:
            messagebox.showerror('ERRO !','Preencha o Espaço Vazio')

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
        self.label_foto['image'] = self.origem




if __name__=='__main__':
    ja = Cadastro()
    ja['bg'] = '#dcdcdc'
    ja.geometry('800x640+400+10')
    ja.resizable(0,0)
    ja.mainloop()
