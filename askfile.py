def akf():
    import tkinter.filedialog, tkinter
    root = tkinter.Tk()
    fts = [('Images', '.jpg .png .jpeg .jfif .bmp .tif')]
    x = tkinter.filedialog.askopenfilename(title="Select image", filetypes=fts)
    root.destroy()
    return x

def aks():
    import tkinter.filedialog, tkinter
    root = tkinter.Tk()
    fts = [('Image file', '.png')]
