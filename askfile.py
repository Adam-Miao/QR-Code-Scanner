def akf(tl='Select an image'):
    import tkinter.filedialog, tkinter
    root = tkinter.Tk()
    fts = [('Images', '.jpg .png .jpeg .jfif .bmp .tif')]
    x = tkinter.filedialog.askopenfilename(filetypes=fts, title=tl)
    root.destroy()
    return x

def aks():
    import tkinter.filedialog, tkinter
    root = tkinter.Tk()
    fts = [('Image file', '.png')]
    x = tkinter.filedialog.asksaveasfilename(filetypes=fts, title='Save as...')
    root.destroy()
    return x
