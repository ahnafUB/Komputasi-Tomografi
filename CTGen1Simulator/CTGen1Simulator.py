import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, ArtistAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from pathlib import Path
from skimage import io
from skimage.color import rgb2gray
from skimage.data import shepp_logan_phantom
from skimage.transform import radon, rotate, iradon
from tkinter import *
from tkinter import Tk, Canvas, Button, PhotoImage, ttk, messagebox

if getattr(sys, "frozen", False):
    import pyi_splash


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r".\Images")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def create_home_page(window, pages, show_page, images):
    pages["home"].pack(expand=True, fill="both")

    canvas = Canvas(
        pages["home"],
        bg = "#FFFFFF",
        height = 600,
        width = 1150,
        bd = 0,
        highlightthickness = 0,
        relief = "flat"
    )
    canvas.place(x = 0, y = 0)

    button_image_1 = PhotoImage(
        file=relative_to_assets("home_button_1.png"))
    button_image_1_hover = PhotoImage(
        file=relative_to_assets("home_button_1_hover.png"))
    button_image_1_click = PhotoImage(
        file=relative_to_assets("home_button_1_click.png"))
    def on_enter_1(event):
        button_1['image']= button_image_1_hover
    def on_leave_1(event):
        button_1['image']= button_image_1
    def on_press_1(event):
        button_1['image']= button_image_1_click
    def on_release_1(event):
        button_1['image']= button_image_1_hover
    button_1 = Button(
        pages["home"],
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=window.destroy,
        relief="flat",
        cursor="hand2",
    )
    button_1.place(
        x=742.0,
        y=429.0,
        width=286.0,
        height=48.0
    )
    button_1.bind("<Enter>", on_enter_1)
    button_1.bind("<Leave>", on_leave_1)
    button_1.bind("<Button-1>", on_press_1)
    button_1.bind("<ButtonRelease-1>", on_release_1)

    #button about
    button_image_2 = PhotoImage(
        file=relative_to_assets("home_button_2.png"))
    button_image_2_hover = PhotoImage(
        file=relative_to_assets("home_button_2_hover.png"))
    button_image_2_click = PhotoImage(
        file=relative_to_assets("home_button_2_click.png"))
    def on_enter_2(event):
        button_2['image']= button_image_2_hover
    def on_leave_2(event):
        button_2['image']= button_image_2
    def on_press_2(event):
        button_2['image']= button_image_2_click
    def on_release_2(event):
        button_2['image']= button_image_2_hover
    button_2 = Button(
        pages["home"],
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: show_page("about"),
        relief="flat",
        cursor="hand2"
    )
    button_2.place(
        x=742.0,
        y=353.0,
        width=286.0,
        height=48.0
    )
    button_2.bind("<Enter>", on_enter_2)
    button_2.bind("<Leave>", on_leave_2)
    button_2.bind("<Button-1>", on_press_2)
    button_2.bind("<ButtonRelease-1>", on_release_2)

    #button tutorial
    button_image_3 = PhotoImage(
        file=relative_to_assets("home_button_3.png"))
    button_image_3_hover = PhotoImage(
        file=relative_to_assets("home_button_3_hover.png"))
    button_image_3_click = PhotoImage(
        file=relative_to_assets("home_button_3_click.png"))
    def on_enter_3(event):
        button_3['image']= button_image_3_hover
    def on_leave_3(event):
        button_3['image']= button_image_3
    def on_press_3(event):
        button_3['image']= button_image_3_click
    def on_release_3(event):
        button_3['image']= button_image_3_hover
    button_3 = Button(
        pages["home"],
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: show_page("tutorial"),
        relief="flat",
        cursor="hand2"
    )
    button_3.place(
        x=742.0,
        y=276.0,
        width=286.0,
        height=48.0
    )
    button_3.bind("<Enter>", on_enter_3)
    button_3.bind("<Leave>", on_leave_3)
    button_3.bind("<Button-1>", on_press_3)
    button_3.bind("<ButtonRelease-1>", on_release_3)

    #button play
    button_image_4 = PhotoImage(
        file=relative_to_assets("home_button_4.png"))
    button_image_4_hover = PhotoImage(
        file=relative_to_assets("home_button_4_hover.png"))
    button_image_4_click = PhotoImage(
        file=relative_to_assets("home_button_4_click.png"))
    def on_enter_4(event):
        button_4['image']= button_image_4_hover
    def on_leave_4(event):
        button_4['image']= button_image_4
    def on_press_4(event):
        button_4['image']= button_image_4_click
    def on_release_4(event):
        button_4['image']= button_image_4_hover
    button_4 = Button(
        pages["home"],
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: show_page("play"),
        relief="flat",
        cursor="hand2"
    )
    button_4.place(
        x=742.0,
        y=200.0,
        width=286.0,
        height=48.0
    )
    button_4.bind("<Enter>", on_enter_4)
    button_4.bind("<Leave>", on_leave_4)
    button_4.bind("<Button-1>", on_press_4)
    button_4.bind("<ButtonRelease-1>", on_release_4)

    image_1 = canvas.create_image(
        575.0,
        69.0,
        image=images["image_image_1"]
    )

    image_2 = canvas.create_image(
        353.0,
        338.0,
        image=images["image_image_2"]
    )

    image_3 = canvas.create_image(
        1106.0,
        374.0,
        image=images["image_image_3"]
    )

    image_4 = canvas.create_image(
        586.0,
        169.0,
        image=images["image_image_4"]
    )

    image_5 = canvas.create_image(
        72.0,
        539.0,
        image=images["image_image_5"]
    )

    image_6 = canvas.create_image(
        674.0,
        381.0,
        image=images["image_image_6"]
    )

    image_7 = canvas.create_image(
        961.0,
        531.0,
        image=images["image_image_7"]
    )

    image_8 = canvas.create_image(
        62.0,
        349.0,
        image=images["image_image_8"]
    )

    image_9 = canvas.create_image(
        950.0,
        78.0,
        image=images["image_image_9"]
    )

    image_10 = canvas.create_image(
        474.0,
        560.0,
        image=images["image_image_10"]
    )

    image_11 = canvas.create_image(
        630.0,
        529.0,
        image=images["image_image_11"]
    )

    image_12 = canvas.create_image(
        165.0,
        89.0,
        image=images["image_image_12"]
    )

    image_13 = canvas.create_image(
        627.0,
        286.0,
        image=images["image_image_13"]
    )

    image_14 = canvas.create_image(
        1070.0,
        121.0,
        image=images["image_image_14"]
    )

    image_15 = canvas.create_image(
        62.0,
        192.0,
        image=images["image_image_15"]
    )

def create_about_page(pages, show_page, images):
    canvas = Canvas(
        pages["about"],
        bg = "#68686a",
        height = 600,
        width = 1150,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge",
        scrollregion=(0,0,2000,1550)
    )
    canvas.place(x = 0, y = 0)

    image_1 = canvas.create_image(
        575.0,
        740.0,
        image=images["image_image_1"]
    )

    canvas2 = Canvas(
        pages["about"],
        height=31,
        width=1150,
        bg="#68686a",
        bd = 0,
        highlightthickness = 0
    )
    canvas2.pack(side=TOP,fill=BOTH)

    canvas3 = Canvas(
        pages["about"],
        height=83,
        width=1150,
        bg="#68686a",
        bd = 0,
        highlightthickness = 0)
    canvas3.pack(side=BOTTOM,fill=BOTH)

    
    button_image_1 = PhotoImage(
        file=relative_to_assets("about_button_1.png"))
    button_image_1_hover = PhotoImage(
        file=relative_to_assets("about_button_1_hover.png"))
    button_image_1_click = PhotoImage(
        file=relative_to_assets("about_button_1_click.png"))
    def on_enter_1(event):
        button_1['image']= button_image_1_hover
    def on_leave_1(event):
        button_1['image']= button_image_1
    def on_press_1(event):
        button_1['image']= button_image_1_click
    def on_release_1(event):
        button_1['image']= button_image_1_hover
    button_1 = Button(
        pages["about"],
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: show_page("home"),
        relief="flat",
        cursor="hand2"
    )
    button_1.place(
        x=505.0,
        y=539.0,
        width=141.0,
        height=51.0
    )
    button_1.bind("<Enter>", on_enter_1)
    button_1.bind("<Leave>", on_leave_1)
    button_1.bind("<Button-1>", on_press_1)
    button_1.bind("<ButtonRelease-1>", on_release_1)

    def on_mousewheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
    scrollbar = ttk.Scrollbar(
        pages["about"],
        orient = "vertical",
        command = canvas.yview,
        cursor="hand2"
    )
    canvas.configure(yscrollcommand=scrollbar.set)
    scrollbar.place(relx=1,rely=0,relheight=1,anchor="ne")
    canvas.bind_all("<MouseWheel>", on_mousewheel)

def create_tutorial_page(pages, show_page, images):
    canvas = Canvas(
        pages["tutorial"],
        bg = "#FFFFFF",
        height = 600,
        width = 1150,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    canvas.propagate(False)
    canvas.place(x = 0, y = 0)

    image_1 = canvas.create_image(
        575.0,
        300.0,
        image=images["image_image_1"]
    )

    image_2 = canvas.create_image(
        579.0,
        270.0,
        image=images["image_image_2"]
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("tutorial_button_1.png"))
    button_image_1_hover = PhotoImage(
        file=relative_to_assets("tutorial_button_1_hover.png"))
    button_image_1_click = PhotoImage(
        file=relative_to_assets("tutorial_button_1_click.png"))
    def on_enter_1(event):
        button_1['image']= button_image_1_hover
    def on_leave_1(event):
        button_1['image']= button_image_1
    def on_press_1(event):
        button_1['image']= button_image_1_click
    def on_release_1(event):
        button_1['image']= button_image_1_hover
    button_1 = Button(
        pages["tutorial"],
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: show_page("home"),
        relief="flat",
        cursor="hand2"
    )
    button_1.place(
        x=505.0,
        y=522.0,
        width=141.0,
        height=51.0
    )
    button_1.bind("<Enter>", on_enter_1)
    button_1.bind("<Leave>", on_leave_1)
    button_1.bind("<Button-1>", on_press_1)
    button_1.bind("<ButtonRelease-1>", on_release_1)

def create_play_page(pages, images):
    def rekonstruksi_canvas():
        # Sembunyikan canvas_bawah
        canvas_akuisisi.pack_forget()

        # Tampilkan canvas_pengganti
        canvas_rekonstruksi.pack(side=TOP)
    
    def akuisisi_canvas():
        # Sembunyikan canvas_bawah
        canvas_rekonstruksi.pack_forget()

        # Tampilkan canvas_pengganti
        canvas_akuisisi.pack(side=TOP)

    canvas_nav = Canvas(
    pages["play"],
    bg = "#FFFFFF",
    height = 65,
    width = 1150,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )
    canvas_nav.pack(side=TOP)

    image_1 = canvas_nav.create_image(
        575.0,
        32.0,
        image=images["image_image_1"]
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_image_1_hover = PhotoImage(
        file=relative_to_assets("button_1_hover.png"))
    button_image_1_click = PhotoImage(
        file=relative_to_assets("button_1_click.png"))
    button_image_1_indi = PhotoImage(
        file=relative_to_assets("button_1_indi.png"))
    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_image_2_hover = PhotoImage(
        file=relative_to_assets("button_2_hover.png"))
    button_image_2_click = PhotoImage(
        file=relative_to_assets("button_2_click.png"))
    button_image_2_indi = PhotoImage(
        file=relative_to_assets("button_2_indi.png"))
    def on_enter_1(event):
        button_1['image']= button_image_1_hover
    def on_leave_1(event):
        button_1['image']= button_image_1
    def on_press_1(event):
        button_1['image']= button_image_1_click
    def on_release_1(event):
        button_1['image']= button_image_1_indi
        button_2['image']= button_image_2
        button_1.unbind("<Leave>")
        button_1.unbind("<Enter>")
        button_1.unbind("<Button-1>")
        button_2.bind("<Enter>", on_enter_2)
        button_2.bind("<Leave>", on_leave_2)
        button_2.bind("<Button-1>", on_press_2)
        button_2.bind("<ButtonRelease-1>", on_release_2)

    button_1 = Button(
        canvas_nav,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=rekonstruksi_canvas,
        relief="flat",
        cursor="hand2"
    )
    button_1.place(
        x=625.0,
        y=8.0,
        width=515.0,
        height=48.0
    )
    button_1.bind("<Enter>", on_enter_1)
    button_1.bind("<Leave>", on_leave_1)
    button_1.bind("<Button-1>", on_press_1)
    button_1.bind("<ButtonRelease-1>", on_release_1)

    def on_enter_2(event):
        button_2['image']= button_image_2_hover
    def on_leave_2(event):
        button_2['image']= button_image_2
    def on_press_2(event):
        button_2['image']= button_image_2_click
    def on_release_2(event):
        button_2['image']= button_image_2_indi
        button_1['image']= button_image_1
        button_2.unbind("<Leave>")
        button_2.unbind("<Enter>")
        button_2.unbind("<Button-1>")
        button_1.bind("<Enter>", on_enter_1)
        button_1.bind("<Leave>", on_leave_1)
        button_1.bind("<Button-1>", on_press_1)
        button_1.bind("<ButtonRelease-1>", on_release_1)


    button_2 = Button(
        canvas_nav,
        image=button_image_2_indi,
        borderwidth=0,
        highlightthickness=0,
        command=akuisisi_canvas,
        relief="flat",
        cursor="hand2"
    )
    button_2.place(
        x=101.0,
        y=8.0,
        width=515.0,
        height=48.0
    )

    def home_button():
        answer = messagebox.askyesno(title='Confirmation',
                        message='Apakah anda yakin ingin berhenti?',
                        default="yes")
        if answer:
            akuisisi_canvas()
            button_1['image']= button_image_1
            button_2['image']= button_image_2_indi
            button_2.unbind("<Leave>")
            button_2.unbind("<Enter>")
            button_2.unbind("<Button-1>")
            button_1.bind("<Enter>", on_enter_1)
            button_1.bind("<Leave>", on_leave_1)
            button_1.bind("<Button-1>", on_press_1)
            button_1.bind("<ButtonRelease-1>", on_release_1)
            show_page("home", pages)

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_image_3_hover = PhotoImage(
        file=relative_to_assets("button_3_hover.png"))
    button_image_3_click = PhotoImage(
        file=relative_to_assets("button_3_click.png"))
    def on_enter_3(event):
        button_3['image']= button_image_3_hover
    def on_leave_3(event):
        button_3['image']= button_image_3
    def on_press_3(event):
        button_3['image']= button_image_3_click
    def on_release_3(event):
        button_3['image']= button_image_3_hover
    button_3 = Button(
        canvas_nav,
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=home_button,
        relief="flat",
        cursor="hand2"
    )
    button_3.place(
        x=31.0,
        y=8.0,
        width=48.0,
        height=48.0
    )
    button_3.bind("<Enter>", on_enter_3)
    button_3.bind("<Leave>", on_leave_3)
    button_3.bind("<Button-1>", on_press_3)
    button_3.bind("<ButtonRelease-1>", on_release_3)

    #=================================================================CANVAS BAWAH(AKUISISI DATA)=================================================================
    canvas_akuisisi = Canvas(
        pages["play"],
        bg = "#FFFFFF",
        height = 535,
        width = 1150,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    canvas_akuisisi.pack(side=TOP)

    combobox_1 = ttk.Combobox(canvas_akuisisi, values=["demo","phantom","head","abdomen"], height=4, state="readonly", width=45, justify="center")
    combobox_1.current(0)
    combobox_1.place(
        x=322.0,
        y=40.0
    )

    combobox_2 = ttk.Combobox(canvas_akuisisi, values=["pencil beam"], height=3, state="readonly", width=45, justify="center")
    combobox_2.current(0)
    combobox_2.place(
        x=322.0,
        y=83.0
    )

    combobox_3 = ttk.Combobox(canvas_akuisisi, values=["90","180","360"], height=3, state="readonly", width=45, justify="center")
    combobox_3.current(1)
    combobox_3.place(
        x=322.0,
        y=126.0
    )

    combobox_4 = ttk.Combobox(canvas_akuisisi, values=["45","90","180"], height=4, state="readonly", width=45, justify="center")
    combobox_4.current(0)
    combobox_4.place(
        x=322.0,
        y=169.0
    )

    def sudut():
        theta = np.linspace(0,int(combobox_3.get()),int(combobox_4.get()))
        return theta

    def objek(pilihan):
        if pilihan == "demo":
            img = np.ones([100,100])
            # Resize Image
            diag = len(np.diag(img)//2)
            img = np.pad(img, pad_width=diag+10)
            _ = np.linspace(-1, 1, len(img) )#img.shape[0])
            xv, yv = np.meshgrid(_,_)
            img[(xv-0.1)**2+(yv-0.2)**2<0.01] = 2
        elif pilihan == "phantom":
            img =  shepp_logan_phantom()
        else:
            # Membaca gambar
            file=relative_to_assets(f"{pilihan}.png")
            img = rgb2gray(io.imread(file))
        return img

    image_2 = canvas_akuisisi.create_image(
        379.0,
        140.0,
        image=images["image_image_2"]
    )

    image_3 = canvas_akuisisi.create_image(
        575.0,
        407.0,
        image=images["image_image_3"]
    )

    image_4 = canvas_akuisisi.create_image(
        927.0,
        140.0,
        image=images["image_image_4"]
    )

    image_5 = canvas_akuisisi.create_image(
        225.0,
        114.0,
        image=images["image_image_5"]
    )

    canvas_objinput = Canvas(
        canvas_akuisisi,
        height = 0,
        width = 0,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    canvas_objinput.place(
        x=794.0,
        y=25.0
    )

    objek_di_loadObjek = None
    objek_di_scanning = None
    objek_di_loadSinogram = None

    fig_objek = None  # Variabel global untuk menyimpan objek fig
    canvas_objek = None  # Variabel global untuk menyimpan objek canvas
    def load_objek():
        nonlocal fig_objek, canvas_objek, objek_di_loadObjek
        objek_di_loadObjek = combobox_1.get()
        if canvas_objek:
            canvas_objek.get_tk_widget().destroy()
        plt.rcParams["figure.figsize"] = [2.66, 2.3]
        plt.rcParams["figure.autolayout"] = True
        fig_objek = plt.Figure(dpi=100)
        axobj = fig_objek.add_subplot()
        axobj.axis("off")
        axobj.imshow(objek(combobox_1.get()),cmap='Greys_r', aspect='auto')
        canvas_objek = FigureCanvasTkAgg(fig_objek, master=canvas_objinput)
        canvas_objek.draw()
        canvas_objek.get_tk_widget().pack()

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_image_4_hover = PhotoImage(
        file=relative_to_assets("button_4_hover.png"))
    button_image_4_click = PhotoImage(
        file=relative_to_assets("button_4_click.png"))
    def on_enter_4(event):
        button_4['image']= button_image_4_hover
    def on_leave_4(event):
        button_4['image']= button_image_4
    def on_press_4(event):
        button_4['image']= button_image_4_click
        button_5.bind("<Enter>", on_enter_5)
        button_5.bind("<Leave>", on_leave_5)
        button_5.bind("<Button-1>", on_press_5)
        button_5.bind("<ButtonRelease-1>", on_release_5)
    def on_release_4(event):
        button_4['image']= button_image_4_hover
        button_5.config(state=NORMAL, cursor="hand2")
        def on_release_5(event):
            button_6.config(state=NORMAL,cursor="hand2")
            button_5['image']= button_image_5_hover
            def on_release_6(event):
                button_7.config(state=NORMAL,cursor="hand2")
                button_6['image']= button_image_6_hover
            button_6.bind("<ButtonRelease-1>", on_release_6)
        button_5.bind("<ButtonRelease-1>", on_release_5)

    button_4 = Button(
        canvas_akuisisi,
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=load_objek,
        relief="flat",
        cursor="hand2"
    )
    button_4.place(
        x=135.0,
        y=206.0,
        width=230.0,
        height=42.0
    )
    button_4.bind("<Enter>", on_enter_4)
    button_4.bind("<Leave>", on_leave_4)
    button_4.bind("<Button-1>", on_press_4)
    button_4.bind("<ButtonRelease-1>", on_release_4)

    canvas_scanning = Canvas(
        canvas_akuisisi,
        bg = "#FFFFFF",
        height = 0,
        width = 0,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    canvas_scanning.place(
        x=84,
        y=288.0
    )

    #-------

    canvas_sinogram = Canvas(
        canvas_akuisisi,
        bg = "blue",
        height = 0,
        width = 0,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    canvas_sinogram.place(
        x=430.0,
        y=288.0
    )

    #------
    canvas_profil = Canvas(
        canvas_akuisisi,
        bg = "red",
        height = 0,
        width = 0,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    canvas_profil.place(
        x=776.0,
        y=288.0
    )

    sudut_di_scanning = None
    proyeksi_di_scanning = None
    sudut_di_loadSinogram = None
    proyeksi_di_loadSinogram = None
    
    fig_scanning = None  # Variabel global untuk menyimpan objek fig
    canvas1 = None  # Variabel global untuk menyimpan objek canvas
    def scanning():
        theta = sudut()
        nonlocal fig_scanning, canvas1
        # Jika canvas sudah ada (plot sebelumnya), maka hapus sebelum membuat yang baru
        if canvas1:
            canvas1.get_tk_widget().destroy()
        # Inisialisasi objek scanning dan nilai theta
        scanning_object = objek(combobox_1.get())

        # Inisialisasi plot Matplotlib
        plt.rcParams["figure.figsize"] = [2.90, 2.40]
        plt.rcParams["figure.autolayout"] = True
        plt.rcParams['font.size'] = '7'
        fig_scanning = plt.Figure(dpi=100)
        ax = fig_scanning.add_subplot()
        ax.axis("off")
        im = ax.imshow(scanning_object, cmap='gray',aspect="auto")  # Menampilkan objek awal (misalnya dalam bentuk grayscale)

        def update(frame):
            # Mengatur sudut rotasi sesuai dengan nilai theta
            angle = theta[frame]
            rotated_object = rotate(scanning_object, angle)  # Fungsi rotate objek sesuai dengan sudut theta
            
            # Menampilkan objek yang sudah diputar pada frame saat ini
            im.set_array(rotated_object)
            ax.set_title(f'Proyeksi {frame+1}')
            return im,

        canvas1 = FigureCanvasTkAgg(fig_scanning, master=canvas_scanning)
        canvas1.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
            
        # Membuat animasi
        ani = FuncAnimation(fig_scanning, update, frames=int(combobox_4.get()), interval=500, repeat= False)
        #canvas1.draw()
        return ani
    
    fig_sinogram = None  # Variabel global untuk menyimpan objek fig
    canvas2 = None  # Variabel global untuk menyimpan objek canvas
    fig_profil = None
    canvas3 = None
    def sinogram__profil():
        theta = sudut()
        nonlocal fig_sinogram, canvas2, fig_profil, canvas3
        global sinogram, frames_sinogram
        # Jika canvas sudah ada (plot sebelumnya), maka hapus sebelum membuat yang baru
        if canvas2:
            canvas2.get_tk_widget().destroy()
        # List kosong untuk menyimpan step sinogram
        frames_sinogram = []
        # Mendapatkan data dan meletakkan ke ruang radon
        for i in range(len(theta)):
            sinogram = radon(objek(combobox_1.get()), theta=theta[:i+1],circle=False)
            frames_sinogram.append(sinogram)      #menyimpannya di list "frames_sinogram"
        # Membuat bingkai untuk tempat animasi
        plt.rcParams["figure.figsize"] = [2.90, 2.40]
        plt.rcParams["figure.autolayout"] = True
        plt.rcParams['font.size'] = '7'
        fig_sinogram = plt.Figure(dpi=100)
        ax2 = fig_sinogram.add_subplot()
        ax2.set_title('Sinogram')  # Set judul awal
        ax2.set_xlabel('Proyeksi')
        ax2.set_ylabel('Jumlah Detektor')
        sinogram_obj = ax2.imshow(frames_sinogram[0], cmap='gray')
        
        # Membuat list untuk menyimpan objek gambar
        artists = [[sinogram_obj]]

        # Membuat animasi
        for i in range(1, len(frames_sinogram)):
            sinogram_obj = ax2.imshow(frames_sinogram[i], cmap='gray', aspect='auto')
            artists.append([sinogram_obj])

        canvas2 = FigureCanvasTkAgg(fig_sinogram, master=canvas_sinogram)
        canvas2.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        # Mengatur animasi menggunakan ArtistAnimation
        ani = ArtistAnimation(fig_sinogram, artists, interval=500, blit=True, repeat=False)
        
        if canvas3:
            canvas3.get_tk_widget().destroy()
        sudut_scanning = int(combobox_3.get())
        if sudut_scanning == 90 or sudut_scanning == 180:
            if sudut_scanning == 90:
                array_0_to_90 = sudut()
                # Menambahkan setiap elemen dalam array dengan 90
                theta = array_0_to_90 + 90
                frames_sinogram_local = []
                 # Mendapatkan data dan meletakkan ke ruang radon
                for i in range(len(theta)):
                    sinogram_local = radon(objek(combobox_1.get()), theta=theta[:i + 1], circle=False)
                    frames_sinogram_local.append(sinogram_local)
            elif sudut_scanning == 180:
                frames_sinogram_local = frames_sinogram
                sinogram_local = sinogram

            # Fungsi untuk membuat setiap frame animasi
            def update(frame):
                ax3.clear()
                ax3.plot(np.flip(frames_sinogram_local[-1][:,-(frame+1)]))
                ax3.set_xlabel('Index')
                ax3.set_ylabel('Intensitas')
                ax3.set_title(f'Plot Profil Serapan ke-{frame + 1} Sinogram')

            # Bingkai untuk tempat animasi
            plt.rcParams["figure.figsize"] = [2.90, 2.40]
            plt.rcParams["figure.autolayout"] = True
            plt.rcParams['font.size'] = '7'
            fig_profil = plt.Figure(dpi=100)
            ax3 = fig_profil.add_subplot()

            canvas3 = FigureCanvasTkAgg(fig_profil, master=canvas_profil)
            canvas3.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

            # Membuat animasi dengan FuncAnimation
            ani2 = FuncAnimation(fig_profil, update, frames=len(sinogram_local[0]), interval=500, repeat=False)

        else:
            # Bingkai untuk tempat animasi
            plt.rcParams["figure.figsize"] = [2.90, 2.40]
            plt.rcParams["figure.autolayout"] = True
            plt.rcParams['font.size'] = '7'
            fig_profil = plt.Figure(dpi=100)
            ax3 = fig_profil.add_subplot()

            # Fungsi untuk membuat setiap frame animasi
            def update(frame):
                ax3.clear()
                ax3.plot(frames_sinogram[-1][:, -(frame + 1)])
                ax3.set_xlabel('Index')
                ax3.set_ylabel('Intensitas')
                ax3.set_title(f'Plot Profil Serapan ke-{frame + 1} Sinogram')

            canvas3 = FigureCanvasTkAgg(fig_profil, master=canvas_profil)
            canvas3.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

            # Membuat animasi dengan FuncAnimation
            ani2= FuncAnimation(fig_profil, update, frames=len(sinogram[0]), interval=500, repeat=False)
        return ani2, ani
    
    def scanning_button():
        nonlocal objek_di_scanning, sudut_di_scanning, proyeksi_di_scanning
        if objek_di_loadObjek == combobox_1.get():
            objek_di_scanning = combobox_1.get()
            sudut_di_scanning = combobox_3.get()
            proyeksi_di_scanning = combobox_4.get()
            messagebox.showinfo(
                "Information", 
                "Proses scanning membutuhkan waktu beberapa saat. Tekan [OK] untuk melanjutkan dan tunggu sebentar.")
            out1 = scanning()
            out2 = sinogram__profil()
            canvas1.draw()
            canvas2.draw()
            canvas3.draw()
        else:
            messagebox.showerror(
                "Error", 
                "Mesin CT Scan tidak dapat melakukan scanning. Load objek yang anda pilih terlebih dahulu.")
            
    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_image_5_hover = PhotoImage(
        file=relative_to_assets("button_5_hover.png"))
    button_image_5_click = PhotoImage(
        file=relative_to_assets("button_5_click.png"))
    def on_enter_5(event):
        button_5['image']= button_image_5_hover
    def on_leave_5(event):
        button_5['image']= button_image_5
    def on_press_5(event):
        button_5['image']= button_image_5_click
        button_6.bind("<Enter>", on_enter_6)
        button_6.bind("<Leave>", on_leave_6)
        button_6.bind("<Button-1>", on_press_6)
        button_6.bind("<ButtonRelease-1>", on_release_6)
    def on_release_5(event):
        button_5['image']= button_image_5_hover
    button_5 = Button(
        canvas_akuisisi,
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=scanning_button,
        relief="flat",
        state=DISABLED
    )
    button_5.place(
        x=393.0,
        y=206.0,
        width=230.0,
        height=42.0
    )


    #=================================================================CANVAS BAWAH (REKONSTRUKSI CITRA)=================================================================
    canvas_rekonstruksi = Canvas(
        pages["play"],
        bg = "#FFFFFF",
        height = 535,
        width = 1150,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    combobox_5 = ttk.Combobox(canvas_rekonstruksi, values=["filtered backprojection"], height=2, state="readonly", width=35, justify="center")
    combobox_5.current(0)
    combobox_5.place(
        x=382.0,
        y=41.0
    )

    combobox_6 = ttk.Combobox(canvas_rekonstruksi, values=["ramp", "shepp-logan", "cosine", "hamming", "hann"], height=5, state="readonly", width=35, justify="center")
    combobox_6.current(3)
    combobox_6.place(
        x=382.0,
        y=95.0
    )

    combobox_7 = ttk.Combobox(canvas_rekonstruksi, values=["linear", "nearest", "cubic"], height=3, state="readonly", width=35, justify="center")
    combobox_7.current(0)
    combobox_7.place(
        x=382.0,
        y=149.0
    )

    image_6 = canvas_rekonstruksi.create_image(
        379.0,
        140.0,
        image=images["image_image_6"]
    )

    image_7 = canvas_rekonstruksi.create_image(
        927.0,
        140.0,
        image=images["image_image_7"]
    )

    image_8 = canvas_rekonstruksi.create_image(
        575.0,
        407.0,
        image=images["image_image_8"]
    )

    image_9 = canvas_rekonstruksi.create_image(
        255.0,
        105.0,
        image=images["image_image_9"]
    )

    canvas_objinputsin = Canvas(
        canvas_rekonstruksi,
        height = 0,
        width = 0,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    canvas_objinputsin.place(
        x=794.0,
        y=25.0
    )

    
    fig_objeksin = None  # Variabel global untuk menyimpan objek fig
    canvas_objeksin = None  # Variabel global untuk menyimpan objek canvas
    def load_objeksin():
        nonlocal fig_objeksin, canvas_objeksin, objek_di_loadSinogram, sudut_di_loadSinogram, proyeksi_di_loadSinogram
        if objek_di_scanning == combobox_1.get() and sudut_di_scanning == combobox_3.get() and proyeksi_di_scanning == combobox_4.get():
            objek_di_loadSinogram = combobox_1.get()
            sudut_di_loadSinogram = combobox_3.get()
            proyeksi_di_loadSinogram = combobox_4.get()
            if canvas_objeksin:
                canvas_objeksin.get_tk_widget().destroy()
            plt.rcParams["figure.figsize"] = [2.66, 2.3]
            plt.rcParams["figure.autolayout"] = True
            fig_objeksin = plt.Figure(dpi=100)
            axobjsin = fig_objeksin.add_subplot()
            axobjsin.axis("off")
            axobjsin.imshow(frames_sinogram[-1],cmap='Greys_r', aspect='auto')

            canvas_objeksin = FigureCanvasTkAgg(fig_objeksin, master=canvas_objinputsin)
            canvas_objeksin.draw()
            canvas_objeksin.get_tk_widget().pack()
        else:
            messagebox.showerror(
                "Error", 
                "Mesin CT Scan tidak dapat memuat sinogram. Selesaikan proses akuisisi data terlebih dahulu.")
        
    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    button_image_6_hover = PhotoImage(
        file=relative_to_assets("button_6_hover.png"))
    button_image_6_click = PhotoImage(
        file=relative_to_assets("button_6_click.png"))
    def on_enter_6(event):
        button_6['image']= button_image_6_hover
    def on_leave_6(event):
        button_6['image']= button_image_6
    def on_press_6(event):
        button_6['image']= button_image_6_click
        button_7.bind("<Enter>", on_enter_7)
        button_7.bind("<Leave>", on_leave_7)
        button_7.bind("<Button-1>", on_press_7)
        button_7.bind("<ButtonRelease-1>", on_release_7)
    def on_release_6(event):
        button_6['image']= button_image_6_hover
    button_6 = Button(
        canvas_rekonstruksi,
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=load_objeksin,
        relief="flat",
        state=DISABLED
    )
    button_6.place(
        x=135.0,
        y=206.0,
        width=230.0,
        height=42.0
    )

    canvas_objoutput = Canvas(
        canvas_rekonstruksi,
        bg = "#FFFFFF",
        height = 0,
        width = 0,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    canvas_objoutput.place(
        x=84,
        y=288.0
    )

    #-------

    canvas_rekonwofilter = Canvas(
        canvas_rekonstruksi,
        bg = "blue",
        height = 0,
        width = 0,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    canvas_rekonwofilter.place(
        x=430.0,
        y=288.0
    )

    #------
    canvas_rekonwithfilter = Canvas(
        canvas_rekonstruksi,
        bg = "red",
        height = 0,
        width = 0,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
    canvas_rekonwithfilter.place(
        x=776.0,
        y=288.0
    )

        
    fig_objekout = None  # Variabel global untuk menyimpan objek fig
    canvas4 = None  # Variabel global untuk menyimpan objek canvas
    def load_objekout():
        nonlocal fig_objekout, canvas4
        if canvas4:
            canvas4.get_tk_widget().destroy()
        plt.rcParams["figure.figsize"] = [2.90, 2.40]
        plt.rcParams["figure.autolayout"] = True
        plt.rcParams['font.size'] = '7'
        fig_objekout = plt.Figure(dpi=100)
        ax4 = fig_objekout.add_subplot()
        ax4.axis("off")
        ax4.set_title('Objek Scanning')  # Set judul awal
        ax4.imshow(objek(combobox_1.get()),cmap='Greys_r', aspect='auto')

        canvas4 = FigureCanvasTkAgg(fig_objekout, master=canvas_objoutput)
        canvas4.get_tk_widget().pack()
        return canvas4

    fig_rekonbp = None  # Variabel global untuk menyimpan objek fig
    canvas5 = None  # Variabel global untuk menyimpan objek canvas
    def rekonstruksibp():
        theta = sudut()
        nonlocal fig_rekonbp, canvas5
        # Jika canvas sudah ada (plot sebelumnya), maka hapus sebelum membuat yang baru
        if canvas5:
            canvas5.get_tk_widget().destroy()
        #List kosong untuk menyimpan step rekonstruksi
        frames_rekonstruksi = []

        for i in range(len(theta)):
            rekonstruksi = iradon(
                frames_sinogram[i], 
                theta=theta[:i+1], 
                filter_name= None, 
                interpolation=combobox_7.get() ,
                circle=False)
            frames_rekonstruksi.append(rekonstruksi)

        # Membuat bingkai untuk tempat animasi
        #fig3, ax3 = plt.subplots()
        plt.rcParams["figure.figsize"] = [2.90, 2.40]
        plt.rcParams["figure.autolayout"] = True
        plt.rcParams['font.size'] = '7'
        fig_rekonbp = plt.Figure(dpi=100)
        ax5 = fig_rekonbp.add_subplot()
        ax5.axis("off")
        ax5.set_title('BP Rekonstruksi')  # Set judul awal
        rekonstruksi_obj = ax5.imshow(frames_rekonstruksi[0], cmap='gray')

        # Membuat list untuk menyimpan objek gambar
        artists2 = [[rekonstruksi_obj]]

        # Membuat animasi
        for i in range(1, len(frames_rekonstruksi)):
            rekonstruksi_obj = ax5.imshow(frames_rekonstruksi[i], cmap='gray', aspect='auto')
            artists2.append([rekonstruksi_obj])
        
        canvas5 = FigureCanvasTkAgg(fig_rekonbp, master=canvas_rekonwofilter)
        canvas5.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        # Mengatur animasi menggunakan ArtistAnimation
        ani = ArtistAnimation(fig_rekonbp, artists2, interval=100, repeat=False)
        return ani

    fig_rekonfbp = None  # Variabel global untuk menyimpan objek fig
    canvas6 = None  # Variabel global untuk menyimpan objek canvas
    def rekonstruksifbp():
        theta = sudut()
        nonlocal fig_rekonfbp, canvas6
        # Jika canvas sudah ada (plot sebelumnya), maka hapus sebelum membuat yang baru
        if canvas6:
            canvas6.get_tk_widget().destroy()
        #List kosong untuk menyimpan step rekonstruksi
        frames_rekonstruksi = []

        #mendapatkan data dan menyimpannya di list kosong
        for i in range(len(theta)):
            rekonstruksi = iradon(
                frames_sinogram[i], 
                theta=theta[:i+1], 
                filter_name= combobox_6.get(), 
                interpolation=combobox_7.get() ,
                circle=False)
            frames_rekonstruksi.append(rekonstruksi)

        # Membuat bingkai untuk tempat animasi
        plt.rcParams["figure.figsize"] = [2.90, 2.40]
        plt.rcParams["figure.autolayout"] = True
        plt.rcParams['font.size'] = '7'
        fig_rekonfbp = plt.Figure(dpi=100)
        ax6 = fig_rekonfbp.add_subplot()
        ax6.axis("off")
        ax6.set_title('FBP Rekonstruksi')  # Set judul awal
        rekonstruksi_obj = ax6.imshow(frames_rekonstruksi[0], cmap='gray')

        # Membuat list untuk menyimpan objek gambar
        artists2 = [[rekonstruksi_obj]]

        # Membuat animasi
        for i in range(1, len(frames_rekonstruksi)):
            rekonstruksi_obj = ax6.imshow(frames_rekonstruksi[i], cmap='gray', aspect='auto')
            artists2.append([rekonstruksi_obj])

        canvas6 = FigureCanvasTkAgg(fig_rekonfbp, master=canvas_rekonwithfilter)
        canvas6.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

        # Mengatur animasi menggunakan ArtistAnimation
        ani = ArtistAnimation(fig_rekonfbp, artists2, interval=100, repeat=False)
        return ani

    def rekonstruksi_button():
        if objek_di_loadSinogram == combobox_1.get() and sudut_di_loadSinogram == combobox_3.get() and proyeksi_di_loadSinogram == combobox_4.get():
            messagebox.showinfo(
                "Information", 
                "Proses rekonstruksi membutuhkan waktu beberapa saat. Tekan [OK] untuk melanjutkan dan tunggu sebentar.")
            out1 = load_objekout()
            out2 = rekonstruksibp()
            out3 = rekonstruksifbp()
            canvas4.draw()
            canvas5.draw()
            canvas6.draw()
        else:
            messagebox.showerror(
                "Error", 
                "Mesin CT Scan tidak dapat melakukan rekonstruksi. Pastikan proses akuisisi data telah selesai dan anda telah memuat sinogram terlebih dahulu.")
            
    button_image_7 = PhotoImage(
        file=relative_to_assets("button_7.png"))
    button_image_7_hover = PhotoImage(
        file=relative_to_assets("button_7_hover.png"))
    button_image_7_click = PhotoImage(
        file=relative_to_assets("button_7_click.png"))
    def on_enter_7(event):
        button_7['image']= button_image_7_hover
    def on_leave_7(event):
        button_7['image']= button_image_7
    def on_press_7(event):
        button_7['image']= button_image_7_click
    def on_release_7(event):
        button_7['image']= button_image_7_hover
    button_7 = Button(
        canvas_rekonstruksi,
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=rekonstruksi_button,
        relief="flat",
        state=DISABLED
    )
    button_7.place(
        x=393.0,
        y=206.0,
        width=230.0,
        height=42.0
    )

def show_page(page_name, pages):
    if pages["current_page"]:
        pages[pages["current_page"]].pack_forget()

    pages["current_page"] = page_name
    pages[pages["current_page"]].pack(expand=True, fill="both")

def main():
    window = Tk()
    window.title("CTGen1Simulator")
    lebar = 1150
    tinggi = 600
    x = window.winfo_screenwidth()
    y = window.winfo_screenheight()
    centerx = int(x/2 - lebar/2)
    centery = int(y/2 - tinggi/2) - 25
    window.geometry(f'{lebar}x{tinggi}+{centerx}+{centery}')
    window.configure(bg = "#FFFFFF")
    window.resizable(False, False)

    home_image = {}
    for idx in range(1,16):
        home_image[f"image_image_{idx}"] = PhotoImage(file=relative_to_assets(f"home_image_{idx}.png"))
    
    about_image = {
        "image_image_1" : PhotoImage(file=relative_to_assets("about_image_1.png"))
    }

    tutorial_image = {} 
    for idx in range(1,3):
        tutorial_image[f"image_image_{idx}"] = PhotoImage(file=relative_to_assets(f"tutorial_image_{idx}.png"))

    play_image = {}
    for idx in range(1,10):
            play_image[f"image_image_{idx}"] = PhotoImage(file=relative_to_assets(f"image_{idx}.png"))

    pages = {
        "home": Frame(window),
        "play": Frame(window),
        "tutorial": Frame(window),
        "about": Frame(window),
        "current_page": None
    }

    create_home_page(window, pages, lambda page: show_page(page, pages),home_image)
    create_about_page(pages, lambda page: show_page(page, pages), about_image)
    create_tutorial_page(pages, lambda page: show_page(page, pages), tutorial_image)
    create_play_page(pages, play_image)

    show_page("home", pages)
    if getattr(sys, "frozen", False):
        pyi_splash.close()

    window.mainloop()

if __name__ == "__main__":
    main()
