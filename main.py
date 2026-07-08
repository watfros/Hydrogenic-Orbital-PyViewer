import sys
import os
os.environ['ETS_TOOLKIT'] = 'qt4'
import warnings
warnings.filterwarnings('ignore')

import tkinter as tk
from tkinter import ttk, messagebox

# 导入所有绘图模块
import main_R
import main_Y2D, main_squY2D, main_Psi2D, main_Psi2D_n, main_squPsi2D
import main_squY3D, main_Y3D
import main_isoPsi, main_cloudPsi, main_isoPsi_n, main_2Psi
import main_isoPsi_z   # 新增模块


class Application(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self)

        for index in range(2):
            self.columnconfigure(index=index, weight=1)
        self.rowconfigure(index=0, weight=1)

        # 所有图像类型名称（用于显示）
        self.te = [
            "Radial Wave Function",
            "Polar plot of Y",
            "Polar plot of Y",
            "Polar plot of Y Squared",
            "Polar plot of Y Squared",
            "Contour of Ψ",
            "Contours of Ψ",
            "Contour of Ψ Squared",
            "Isosurface of Ψ",
            "Isosurfaces of Ψ",
            "Electron Cloud",
            "Superposition of 2 Ψ",
            "Square of Radial Function",
            "Radial Distribution Function",
            "Isosurface of Ψ for different Z"   # 新增
        ]

        # 变量用于复选框 / 单选按钮
        self.var_0 = tk.IntVar()   # 用于 2D/3D 单选
        self.var_1 = tk.IntVar()   # 用于 Line Plot 复选框
        self.var_2 = tk.IntVar()
        self.var_3 = tk.IntVar()

        # 绘图函数映射（值 -> 函数）
        self.plot_funcs = {
            1: main_Y3D.start,
            2: main_Y2D.start,
            3: main_squY3D.start,
            4: main_squY2D.start,
            5: main_Psi2D.start,
            6: main_Psi2D_n.start,
            7: main_squPsi2D.start,
            8: main_isoPsi.start,
            9: main_isoPsi_n.start,
            10: main_cloudPsi.start,
            11: main_2Psi.start,
            12: main_isoPsi_z.start,   # 新增
        }

        # 定义 2D 和 3D 选项数据（文本，对应值）
        self.plot_options = {
            # 2D 选项（值固定为 2,4,5,6,7）
            2: [
                (self.te[2], 2),
                (self.te[4], 4),
                (self.te[5], 5),
                (self.te[6], 6),
                (self.te[7], 7),
            ],
            # 3D 选项（值固定为 1,3,8,9,10,11,12）
            3: [
                (self.te[1], 1),
                (self.te[3], 3),
                (self.te[8], 8),
                (self.te[9], 9),
                (self.te[10], 10),
                (self.te[11], 11),
                (self.te[14], 12),
            ]
        }

        self.widgets()

    # 主布局
    def widgets(self):
        # 左侧 LabelFrame（图像类型）
        self.label_frame_1 = ttk.LabelFrame(self, text="Image type", padding=(20, 20))
        self.label_frame_1.grid(row=0, column=0, padx=(30, 30), pady=(30, 30), sticky="nsew")
        self.label_frame_1.grid_propagate(0)
        self.label_frame_1.columnconfigure(index=0, weight=1)
        for index in [0, 1, 2]:
            self.label_frame_1.rowconfigure(index=index, weight=1)

        self.button_1 = ttk.Button(self.label_frame_1, text="Line Plot", command=lambda: self.right_frame(1))
        self.button_1.grid(row=0, column=0, padx=(30, 30), pady=(30, 30), sticky="nsew")
        self.button_2 = ttk.Button(self.label_frame_1, text="2D Plot", command=lambda: self.right_frame(2))
        self.button_2.grid(row=1, column=0, padx=(30, 30), pady=(30, 30), sticky="nsew")
        self.button_3 = ttk.Button(self.label_frame_1, text="3D Plot", command=lambda: self.right_frame(3))
        self.button_3.grid(row=2, column=0, padx=(30, 30), pady=(30, 30), sticky="nsew")

        # 右侧 LabelFrame（初始提示）
        self.label_frame_2 = ttk.LabelFrame(self, text="Function select", padding=(20, 20))
        self.label_frame_2.grid(row=0, column=1, padx=(30, 30), pady=(30, 30), sticky="nsew")
        self.label_frame_2.grid_propagate(0)
        self.frame_2_configure(1, 1)
        self.label = ttk.Label(self.label_frame_2, text="Please select image type", justify="center", foreground="gray")
        self.label.grid()

    # 右侧响应布局
    def right_frame(self, i):
        # 销毁原有右侧框架
        self.label_frame_2.destroy()

        if i == 1:  # Line Plot
            self.label_frame_2 = ttk.LabelFrame(self, text="Line Plot", padding=(20, 20))
            self.label_frame_2.grid(row=0, column=1, padx=(30, 30), pady=(30, 30), sticky="nsew")
            self.label_frame_2.grid_propagate(0)
            self.frame_2_configure(1, 4)

            self.check_1 = ttk.Checkbutton(self.label_frame_2, text=self.te[0], variable=self.var_1)
            self.check_1.grid(row=0, column=0, padx=(90, 0), sticky="nsew")
            self.check_2 = ttk.Checkbutton(self.label_frame_2, text=self.te[12], variable=self.var_2)
            self.check_2.grid(row=1, column=0, padx=(90, 0), sticky="nsew")
            self.check_3 = ttk.Checkbutton(self.label_frame_2, text=self.te[13], variable=self.var_3)
            self.check_3.grid(row=2, column=0, padx=(90, 0), sticky="nsew")
            self.button = ttk.Button(self.label_frame_2, text="Confirm",
                                     command=lambda: self.child_window1(self.var_1.get(), self.var_2.get(), self.var_3.get()))
            self.button.grid()

        elif i in (2, 3):  # 2D 或 3D
            title = "2D Plot" if i == 2 else "3D Plot"
            self.label_frame_2 = ttk.LabelFrame(self, text=title, padding=(20, 20))
            self.label_frame_2.grid(row=0, column=1, padx=(30, 30), pady=(30, 30), sticky="nsew")
            self.label_frame_2.grid_propagate(0)

            options = self.plot_options[i]
            rows = len(options)
            self.frame_2_configure(1, rows)

            # 动态生成单选按钮
            for idx, (text, value) in enumerate(options):
                rb = ttk.Radiobutton(self.label_frame_2, text=text, variable=self.var_0, value=value)
                rb.grid(row=idx, column=0, padx=(90, 0), sticky="nsew")

            self.button = ttk.Button(self.label_frame_2, text="Confirm",
                                     command=lambda: self.child_window2(self.var_0.get()))
            self.button.grid()

    # 右侧框架行列配置
    def frame_2_configure(self, x, y):
        for index in range(x):
            self.label_frame_2.columnconfigure(index=index, weight=1)
        for index in range(y):
            self.label_frame_2.rowconfigure(index=index, weight=1)

    # Line Plot 确认
    def child_window1(self, j_1, j_2, j_3):
        if not (j_1 or j_2 or j_3):
            messagebox.showerror("Error", "Please select at least one line plot option")
            return
        main_R.start(j_1, j_2, j_3)

    # 2D / 3D 确认
    def child_window2(self, j):
        if j == 0:
            messagebox.showerror("Error", "Please select an option")
            return
        func = self.plot_funcs.get(j)
        if func:
            func()
        else:
            messagebox.showerror("Error", f"Unknown plot type: {j}")


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Hydrogenic Orbital PyViewer")
    root.geometry("900x600")
    root.resizable(False, False)

    # 可选主题（已注释，如需要可启用）
    # root.tk.call("source", "sun-valley.tcl")
    # root.tk.call("set_theme", "light")

    app = Application(root)
    app.pack(fill="both", expand=True)
    root.mainloop()