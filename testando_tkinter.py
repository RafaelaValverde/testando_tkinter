import tkinter as tk


def window_dates():

    def botao_acionado():
        data_inicial = data_inicial_txt.get()
        data_final = data_final_txt.get()
        print(f'Data inicial: {data_inicial}')
        print(f'Data final: {data_final}')
        print(type(data_inicial))
        if data_inicial != '' and data_final != '':
            root.destroy()

    root = tk.Tk()

    root.title('Robô')
    root.geometry('320x230')
    root.configure(background='#dde')

    data_inicial_label = tk.Label(
        root, text='Data inicial XX/XX/XXXX:', background='#dde', foreground='#009', anchor='w')
    data_inicial_label.place(x=30, y=20, width=200, height=30)

    data_inicial_txt = tk.Entry(root)
    data_inicial_txt.place(x=30, y=50, width=150, height=30)
    data_inicial_txt.focus()

    data_final_label = tk.Label(
        root, text='Data final XX/XX/XXXX:', background='#dde', foreground='#009', anchor='w')
    data_final_label.place(x=30, y=80, width=200, height=30)

    data_final_txt = tk.Entry(root)
    data_final_txt.place(x=30, y=110, width=150, height=30)

    button = tk.Button(root, text='Continuar', command=botao_acionado)
    button.place(x=30, y=160, width=100, height=30)

    root.mainloop()
