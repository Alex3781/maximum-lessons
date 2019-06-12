
import tkinter
window=tkinter.Tk()
window.title("Красная кнопка")
window.geometry("800x600")
label=tkinter.Label(fg="black",text="0")
label.place(x=400,y=100)
def change_lavel():
    if int(label["text"])==20:
        label["text"]="обосрись от страха"
    old_value=int(label["text"])
    label["text"]=(old_value+1)
button=tkinter.Button(fg="#0b093f",bg="#e8f2f4",text="Кнопка", command=change_lavel)
button.place(x=380,y=300)
window.mainloop()
