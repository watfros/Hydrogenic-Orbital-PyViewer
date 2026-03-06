import sys
import os  # Library for interacting with the operating system
os.environ['ETS_TOOLKIT'] = 'qt4'
#Add code to suppress warnings
import warnings
warnings.filterwarnings('ignore')
#End of code
import tkinter as tk
from tkinter import ttk, messagebox  # Import messagebox for error prompts
import main_R
import main_Y2D, main_squY2D, main_Psi2D, main_Psi2D_n, main_squPsi2D
import main_squY3D, main_Y3D
import main_isoPsi, main_cloudPsi, main_isoPsi_n, main_2Psi

class Application(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)

        for index in range(2):
            self.columnconfigure(index=index, weight=1, )
        self.rowconfigure(index=0, weight=1)

        self.te = ["Radial Wave Function", "Polar plot of Y", "Polar plot of Y", "Polar plot of Y Squared", "Polar plot of Y Squared",
                   "Contour of Ψ", "Contours of Ψ", "Contour of Ψ Squared", "Isosurface of Ψ", "Isosurfaces of Ψ",
                   "Electron Cloud", "Superposition of 2 Ψ", "Square of Radial Function", "Radial Distribution Function"]

        self.var_0 = tk.IntVar()
        self.var_1 = tk.IntVar()
        self.var_2 = tk.IntVar()
        self.var_3 = tk.IntVar()

        self.widgets()

    # Frame and widget layout
    def widgets(self):

        # LabelFrame1 construction
        self.label_frame_1 = ttk.LabelFrame(self, text="Image type", padding=(20, 20),)
        self.label_frame_1.grid(row=0, column=0, padx=(30, 30), pady=(30, 30), sticky="nsew")
        self.label_frame_1.grid_propagate(0)

        # Widgets inside LabelFrame1
        self.label_frame_1.columnconfigure(index=0, weight=1)
        for index in [0, 1, 2]:
            self.label_frame_1.rowconfigure(index=index, weight=1)
        self.button_1 = ttk.Button(self.label_frame_1, text="Line Plot", command=lambda: self.right_frame(1))
        self.button_1.grid(row=0, column=0, padx=(30, 30), pady=(30, 30), sticky="nsew")
        self.button_2 = ttk.Button(self.label_frame_1, text="2D Plot", command=lambda: self.right_frame(2))
        self.button_2.grid(row=1, column=0, padx=(30, 30), pady=(30, 30), sticky="nsew")
        self.button_3 = ttk.Button(self.label_frame_1, text="3D Plot", command=lambda: self.right_frame(3))
        self.button_3.grid(row=2, column=0, padx=(30, 30), pady=(30, 30), sticky="nsew")

        # LabelFrame2 construction
        self.label_frame_2 = ttk.LabelFrame(self, text="Function select", padding=(20, 20))
        self.label_frame_2.grid(row=0, column=1, padx=(30, 30), pady=(30, 30), sticky="nsew")
        self.label_frame_2.grid_propagate(0)

        # Widgets inside LabelFrame2
        self.frame_2_configure(1, 1)
        self.label = ttk.Label(self.label_frame_2, text="Please select image type", justify="center", foreground="gray")
        self.label.grid()

    # Right widget response layout
    def right_frame(self, i):
        # Destroy original right widgets
        self.label_frame_2.destroy()

        # Line plot response layout
        if i == 1:
            self.label_frame_2 = ttk.LabelFrame(self, text="Line Plot", padding=(20, 20))
            self.label_frame_2.grid(row=0, column=1, padx=(30, 30), pady=(30, 30), sticky="nsew")
            self.label_frame_2.grid_propagate(0)
            self.frame_2_configure(1, 4)

            self.check_1 = ttk.Checkbutton(self.label_frame_2, text=self.te[0], variable=self.var_1, )
            self.check_1.grid(row=0, column=0, padx=(90, 0), sticky="nsew")
            self.check_2 = ttk.Checkbutton(self.label_frame_2, text=self.te[12], variable=self.var_2, )
            self.check_2.grid(row=1, column=0, padx=(90, 0), sticky="nsew")
            self.check_3 = ttk.Checkbutton(self.label_frame_2, text=self.te[13], variable=self.var_3, )
            self.check_3.grid(row=2, column=0, padx=(90, 0), sticky="nsew")
            self.button = ttk.Button(self.label_frame_2, text="Confirm", command=lambda: self.child_window1(
                self.var_1.get(), self.var_2.get(), self.var_3.get(), ))
            self.button.grid()

        # 2D plot response layout
        elif i == 2:
            self.label_frame_2 = ttk.LabelFrame(self, text="2D Plot", padding=(20, 20))
            self.label_frame_2.grid(row=0, column=1, padx=(30, 30), pady=(30, 30), sticky="nsew")
            self.label_frame_2.grid_propagate(0)
            self.frame_2_configure(1, 6)

            self.radio_1 = ttk.Radiobutton(self.label_frame_2, text=self.te[2], variable=self.var_0, value=2)
            self.radio_1.grid(row=0, column=0, padx=(90, 0), sticky="nsew")
            self.radio_2 = ttk.Radiobutton(self.label_frame_2, text=self.te[4], variable=self.var_0, value=4)
            self.radio_2.grid(row=1, column=0, padx=(90, 0), sticky="nsew")
            self.radio_3 = ttk.Radiobutton(self.label_frame_2, text=self.te[5], variable=self.var_0, value=5)
            self.radio_3.grid(row=2, column=0, padx=(90, 0), sticky="nsew")
            self.radio_4 = ttk.Radiobutton(self.label_frame_2, text=self.te[6], variable=self.var_0, value=6)
            self.radio_4.grid(row=3, column=0, padx=(90, 0), sticky="nsew")
            self.radio_5 = ttk.Radiobutton(self.label_frame_2, text=self.te[7], variable=self.var_0, value=7)
            self.radio_5.grid(row=4, column=0, padx=(90, 0), sticky="nsew")
            self.button = ttk.Button(self.label_frame_2, text="Confirm", command=lambda: self.child_window2(self.var_0.get()))
            self.button.grid()

        # 3D plot response layout
        elif i == 3:
            self.label_frame_2 = ttk.LabelFrame(self, text="3D Plot", padding=(20, 20))
            self.label_frame_2.grid(row=0, column=1, padx=(30, 30), pady=(30, 30), sticky="nsew")
            self.label_frame_2.grid_propagate(0)
            self.frame_2_configure(1, 7)

            self.radio_1 = ttk.Radiobutton(self.label_frame_2, text=self.te[1], variable=self.var_0, value=1)
            self.radio_1.grid(row=0, column=0, padx=(90, 0), sticky="nsew")
            self.radio_2 = ttk.Radiobutton(self.label_frame_2, text=self.te[3], variable=self.var_0, value=3)
            self.radio_2.grid(row=1, column=0, padx=(90, 0), sticky="nsew")
            self.radio_3 = ttk.Radiobutton(self.label_frame_2, text=self.te[8], variable=self.var_0, value=8)
            self.radio_3.grid(row=2, column=0, padx=(90, 0), sticky="nsew")
            self.radio_4 = ttk.Radiobutton(self.label_frame_2, text=self.te[9], variable=self.var_0, value=9)
            self.radio_4.grid(row=3, column=0, padx=(90, 0), sticky="nsew")
            self.radio_5 = ttk.Radiobutton(self.label_frame_2, text=self.te[10], variable=self.var_0, value=10)
            self.radio_5.grid(row=4, column=0, padx=(90, 0), sticky="nsew")
            self.radio_6 = ttk.Radiobutton(self.label_frame_2, text=self.te[11], variable=self.var_0, value=11)
            self.radio_6.grid(row=5, column=0, padx=(90, 0), sticky="nsew")
            self.button = ttk.Button(self.label_frame_2, text="Confirm", command=lambda: self.child_window2(self.var_0.get()))
            self.button.grid()

    # Right frame cell settings
    def frame_2_configure(self, x, y):
        for index in range(x):
            self.label_frame_2.columnconfigure(index=index, weight=1)
        for index in range(y):
            self.label_frame_2.rowconfigure(index=index, weight=1)

    def child_window1(self, j_1, j_2, j_3):
        # Verify at least one line plot option is selected
        if not (j_1 or j_2 or j_3):
            messagebox.showerror("Error", "Please select at least one line plot option")
            return
        print(str(j_1))
        print(str(j_2))
        print(str(j_3))
        main_R.start(j_1, j_2, j_3)

    def child_window2(self, j):
        # Verify a 2D plot or 3D plot option is selected
        if j == 0:  # IntVar default value is 0, remains 0 when no option is selected
            messagebox.showerror("Error", "Please select an option")
            return
        print(str(j))
        print(self.var_0.get())
        if j == 1:
            main_Y3D.start()
        elif j == 2:
            main_Y2D.start()
        elif j == 3:
            main_squY3D.start()
        elif j == 4:
            main_squY2D.start()
        elif j == 5:
            main_Psi2D.start()
        elif j == 6:
            main_Psi2D_n.start()
        elif j == 7:
            main_squPsi2D.start()
        elif j == 8:
            main_isoPsi.start()
        elif j == 9:
            main_isoPsi_n.start()
        elif j == 10:
            main_cloudPsi.start()
        elif j == 11:
            main_2Psi.start()



if __name__ == "__main__":
    root = tk.Tk()
    root.title("Hydrogenic Orbital PyViewer")
    root.geometry("900x600")
    root.resizable(False, False)

    # Call theme
    #root.tk.call("source", "sun-valley.tcl")
    #root.tk.call("set_theme", "light")

    app = Application(root)
    app.pack(fill="both", expand=True)


    root.mainloop()