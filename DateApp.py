from tkinter import *


class Person(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x400')
        self.title('My app')
        self.put_frames()

    def put_frames(self):
        self.frame_main = MainWindow(self)
        self.frame_main.place(relwidth=1, relheight=1)


class MainWindow(Frame):
    def __init__(self, parent):
        super().__init__()
        self._name = StringVar()
        self._surname = StringVar()
        self.entry_res = Label(self)
        self.entry_res.pack()
        self.res = f'{self._name.get()} {self._surname.get()} в возрасте 17 лет'
        self.put_widgets()

    def press(self):
    	self.res = f'{self._name.get()} {self._surname.get()} в возрасте 17 лет' 
    	FinishWindow().mainloop()

    def put_widgets(self):
        self.text = Label(self, text='Введите имя, фамилию и дату рождения сотрудника.').pack()
        self.entry_name = Entry(self, textvariable=self._name).pack()
        self.entry_surname = Entry(self, textvariable=self._surname).pack()
        self.but = Button(self, text='Отобразить запись', command=self.press).pack()


class FinishWindow(Tk):
	def __init__(self):
		super().__init__()
		self.title('My person class')
		self.geometry('250x150')
		help = MainWindow(parent=Person)
		self.mess = help.res
		print(help.res)
        self.dres = Label(self, text=self.mess)
        self.dres.pack()



if __name__ == '__main__':
    app = Person()
    app.mainloop()