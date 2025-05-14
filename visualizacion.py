# Librerías necesarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import messagebox

from Analisis import DataAnalyzer

data = pd.read_csv('adult.csv')
analizar = DataAnalyzer(data)



def informacion():
    try:
        text_area.delete("1.0",tk.END)
        info=analizar.summary()
        text_area.insert(tk.END,info)
    except:
        messagebox.showerror("Error","No se puede")



ventana=tk.Tk()





ventana.title("Visualización de Datos")
boton_sumary=tk.Button(ventana,text="Info", command=informacion)
boton_sumary.pack()

text_area=ScrolledText(ventana,width=70,height=30)
text_area.pack()

ventana.mainloop()


###