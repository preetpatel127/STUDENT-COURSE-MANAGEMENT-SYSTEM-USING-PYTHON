from tkinter import*
from PIL import Image, ImageTK


class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Course Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="grey")

        self.logo_dash = ImageTK.PhotoImage(file="images/logo_p.jpg")

        title = Label(self.root, text="Student Course Management System", image=self.logo_dash, font=(
            "goudy old style", 20, "bold"), bg="#033054", fg="white").place(x=0, y=0, relwidth=1, height=50)


if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()
