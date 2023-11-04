import tkinter as tk
from socket import *


s = socket(AF_INET, SOCK_DGRAM)
s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)
PORT = 37020
s.bind(('', PORT))

print('Listening for broadcast at ', s.getsockname())
while True:
    data, address = s.recvfrom(1024)
    print('Server received from {}:{}'.format(address, data.decode('utf-8')))
    if address is not None:
        break

def click():
    client.send(bytes("\00", 'ascii'))

def finish():
    win.destroy()


win = tk.Tk()

win.title('POPcat')
win.geometry("500x300+400+300")
win.config(bg='#C45B90')
btn = tk.Button(win, text='POP', font="Arial 40", width=5, height=2, command=click)
btn.place(relx=0.5, rely=0.5, anchor='center')
client = socket(AF_INET, SOCK_STREAM)
client.connect((address[0], 7000))
win.mainloop()
client.close()