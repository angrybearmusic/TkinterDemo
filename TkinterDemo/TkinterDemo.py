import tkinter
import sqlite3

conn = sqlite3.connect('HTMLTemp.db')
c = conn.cursor()
tk = tkinter

#c.execute('DROP TABLE htmlTemplate')
#c.execute('CREATE TABLE htmlTemplate (Code TEXT)')


def main():
    def getEntries():
        c.execute('SELECT DISTINCT Code FROM htmlTemplate')
        return c.fetchall()
    
    def goHandler():
        textVar = str(htmltext.get('0.0', tk.END))
        file = open('NewWebPage.html', 'w')

        text = "<html>\n<body>\n" + textVar + "\n</body>\n</html>"

        file.write(text)
        file.close()
        
        c.execute('INSERT INTO htmlTemplate (Code) VALUES(?)', (textVar,))
        conn.commit()
        
        print (textVar)
    
    def getHandler():
        textVar = str(listbox.get(tk.ACTIVE))
        file = open('NewWebPage.html', 'w')

        text = "<html>\n<body>\n" + textVar + "\n</body>\n</html>"

        file.write(text)
        file.close()
        
        c.execute('INSERT INTO htmlTemplate (Code) VALUES(?)', (textVar,))
        conn.commit()
        
        print (textVar)
        







    base = tk.Tk()
    base.title("HTML Code Maker")
    #base.geometry('600x300')
   

    frame = tk.Frame(base, width = 300, height = 300)
    frame.pack( side = tk.RIGHT)
    gframe = tk.Frame(base, width = 300, height = 300)
    gframe.pack( side = tk.LEFT)

    entries = getEntries()
    
    listbox = tk.Listbox(gframe, selectmode=tk.SINGLE)

    for i in entries:
        
        listbox.pack()
        listbox.insert(tk.END, i)
        
    
    goButton = tk.Button(frame,text='Go', command = goHandler)
    goButton.pack()

    getButton = tk.Button(gframe, text = 'Get', command = getHandler)
    getButton.pack()

   
    textVar = tk.StringVar()
    textVar.set('Enter Text Right Here')
    htmltext = tk.Text(frame)
    htmltext.pack(fill=tk.X, expand = 1)
    
    
    
    tk.mainloop()
    

if __name__ == "__main__":
    main()













