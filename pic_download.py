# -*- coding:utf-8 -*-
'''
   爬蟲抓取照片 http://dangerlover9403.pixnet.net/blog/post/207823890-%5Bpython%5D-day14---python-%E5%BE%9E%E7%B6%B2%E8%B7%AF%E6%8A%93%E5%9C%96%E7%89%87
   視窗設計 http://andrewpythonarduino.blogspot.com/2018/04/python-gui.html
   視窗置中 https://blog.csdn.net/ppdyhappy/article/details/78175274
   輸出exe檔案(windows) https://kknews.cc/zh-tw/other/2blvyeg.html
       pyinstaller -F --icon=my.ico -w mycode.py
'''

import requests
import urllib.request
from bs4 import BeautifulSoup
import os
import time
import tkinter
import tkinter.messagebox

def get_screen_size(window):  
    return window.winfo_screenwidth(),window.winfo_screenheight()  
  
def get_window_size(window):  
    return window.winfo_reqwidth(),window.winfo_reqheight()  
  
def center_window(root, width, height):  
    screenwidth = root.winfo_screenwidth()  
    screenheight = root.winfo_screenheight()  
    size = '%dx%d+%d+%d' % (width, height, (screenwidth - width)/2, (screenheight - height)/2)  
    print('置中位置：',size)  
    my_window.geometry(size)

my_window = tkinter.Tk()
center_window(my_window, 230, 120) 
my_window.maxsize(400, 250)  
my_window.minsize(230, 120) 
my_window.title('圖片下載')
# my_window.geometry('250x100')

# search_var = tkinter.StringVar()
# search_var.set('名稱')
# my_label = tkinter.Label(my_window, textvariable = search_var)
# my_label.grid(row=0, column=0)

search_var = tkinter.StringVar()
search_var.set('名稱')

count_var = tkinter.StringVar()
count_var.set('數量')

my_label = tkinter.Label(my_window, text = '名稱')
my_label.grid(row=0, column=0)

my_enter = tkinter.Entry(my_window, width = 20)
my_enter.grid(row=0, column=1)
#///////////

my_label2 = tkinter.Label(my_window, text = '數量')
my_label2.grid(row=1, column=0)

my_enter2 = tkinter.Entry(my_window, width = 5)
my_enter2.grid(row=1, column=1)

#//////////////  

def click_me():
    search_var.set(my_enter.get())
    count_var.set(my_enter2.get())
    # print(my_enter.get())
    download_pic(my_enter.get(),my_enter2.get())


def download_pic(search_name,count):
    url_1 = 'https://www.google.com/search?q='
    url_2 = '&rlz=1C2CAFB_enTW617TW617&source=lnms&tbm=isch&sa=X&ved=0ahUKEwictOnTmYDcAhXGV7wKHX-OApwQ_AUICigB&biw=1000&bih=1000'
    # search = 'sana'
    url = url_1 + search_name + url_2
    photolimit = int(count)  #counts of pictures
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url,headers = headers) #使用header避免訪問受到限制
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.find_all('img')
    folder_path ='./photo/'

    if (os.path.exists(folder_path) == False): #判斷資料夾是否存在
        os.makedirs(folder_path) #Create folder

    for index , item in enumerate (items):

        if (item and index < photolimit):
            html = requests.get(item.get('src')) # use 'get' to get photo link path , requests = send request
            img_name = folder_path + str(index + 1) + '.jpg'

            with open(img_name,'wb') as file: #以byte的形式將圖片數據寫入
                file.write(html.content)
                file.flush()

            file.close() #close file
            print('第 %d 張' % (index + 1))
            time.sleep(0.001)

    print('Done')


my_button1 = tkinter.Button(my_window, text = '確認', command = click_me)
my_button1.grid(row=2, column=1)

def show_message():
    tkinter.messagebox.showinfo(title = '說明', message = '下載至多20張圖片，放置photo資料夾')
                               
# 多加一個 Button 物件
my_button2 = tkinter.Button(my_window, text = '說明', command = show_message)
my_button2.grid(row=3, column=1)

# 進入事件迴圈
my_window.mainloop()