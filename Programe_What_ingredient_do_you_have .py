from tkinter import *
from tkinter import ttk
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from def_function_change_vacab import change_vacab
from pandastable import Table, TableModel
from def_function_find_menu import find_menu
from def_function_find_menu import gen_column, get_all_menu
from def_function_connect_method import get_total_method
from def_function_connect_ingretotal import get_total_ingredient
from PIL import ImageTk, Image
import os
import webbrowser

root = Tk()
root.title('What ingredient do you have ?')
Indredient_input_list = []
Type_Food_list = []

def callback(url):
    webbrowser.open_new(url)

def select():
    # clear Frame ------------------------------------
    for widget in labelframe5.winfo_children():
       widget.destroy()

    # for widget in Frame1.winfo_children():
    #    widget.destroy()
    # clear Frame ------------------------------------

    # clear tv_suggest ------------------------------------
    x = tv_suggest.get_children()
    for ch in x:
        tv_suggest.delete(ch)
    # clear tv_suggest ------------------------------------


    list_selecrt_all_nfood = []
    list_select_food = []
    curItems_multiple = tv.selection()
    # print('11111111')
    # print(curItems_multiple)
    for i in curItems_multiple:
        list_selecrt_nfood_temp =[]
        x_str = tv.item(i)['values']
        # print(tv.item(i)['values'])
        # print(type(x_str))
        for j in x_str:
            if j in ['ต้ม','ปิ้งย่าง','อาหารเจ','ผัด','นึ่ง','ยำ','ทอด']:
                list_selecrt_nfood_temp.append(j)
            elif j in get_all_menu() :
                list_selecrt_nfood_temp.append(j)
                list_select_food.append(j)
        list_selecrt_all_nfood.append(list_selecrt_nfood_temp)
    print(list_selecrt_all_nfood)
    print('bbbbbbbbbbbb')
    print(list_select_food)
    

    new_list_multiple = []
    for sf,l_all_s in zip(list_select_food,list_selecrt_all_nfood):
        
        
        df_list_ingredient = get_total_ingredient(sf).values.tolist()
        df_manu,list_same = find_menu(Type_Food_list,Indredient_input_list)
    
        for i in list_same:
            if sf in i:
                curr_l = i
                # print('aaaaa')
                # print(curr_l)
            

        for i_row in range(len(df_list_ingredient)):
            new_list_temp =[]
            for l in l_all_s:
                new_list_temp.append(l)
            str_i_row = df_list_ingredient[i_row][0]
            # print('aaaaaaaaaaaaa1')
            # print(str_i_row)
            if str(i_row) in curr_l:
                pass
            else:
                new_list_temp.append(str_i_row)
                new_list_temp.append('ออกไปซื้อนะจ่ะ')
            new_list_multiple.append(new_list_temp)
    
    # print(new_list_multiple)
    
    for p in new_list_multiple:
        for pp in list_selecrt_all_nfood:
            if p == pp:
                new_list_multiple.remove(p)

    num_cul = []
    for ii in new_list_multiple:
        # print(ii)
        n_count = 0
        for c in ii:
            # print(c)
            if c in ['ต้ม','ปิ้งย่าง','อาหารเจ','ผัด','นึ่ง','ยำ','ทอด']:
                n_count+=1
        num_cul.append(n_count)
    
    max_num_cul = int(max(num_cul))
    

    r_new_list_multiple = []
    for r,n in zip(new_list_multiple,num_cul):
        
        if max_num_cul-n != 0:
            range_c  = max_num_cul-n

            for nn in range(range_c):
                r.insert(n+nn,'')
                # print(r)
            r_new_list_multiple.append(r)
            
        else:
            r_new_list_multiple.append(r)
    print(r_new_list_multiple)
    

    create_colum_select_multi = []
    for c in range(max_num_cul):
        create_colum_select_multi.append(f'ประเภท {c+1}')
    create_colum_select_multi.append('เมนูอาหาร')    
    create_colum_select_multi.append('ส่วนผสม')
    create_colum_select_multi.append('Inforamtion') 
    print(create_colum_select_multi)

    column_selcet_multiple = tuple(create_colum_select_multi)
    # print(column_gen)

 
    tv_suggest.configure(columns = column_selcet_multiple)
    for i in range(len(column_selcet_multiple)):
        tv_suggest.heading(i,text=column_selcet_multiple[i])
        tv_suggest.column(i, anchor="e")


    for row in r_new_list_multiple:
        # print(row)
        tv_suggest.insert("","end",values=row)     



    #### Frame suparmarket ----------------------------------------------------------------------------------------------------------------------
    frame=ttk.LabelFrame(labelframe5, text='Find Supermarket')
    frame.pack(side='left', padx=5, pady=5, ipadx=15, ipady=15, expand='yes', fill='both')


    link1 = Label(frame, text="Big C Supermarket", fg="blue", cursor="hand2",anchor=W)
    link1.grid(row=0, column=0,padx=5, pady=5,sticky=W)
    link1.bind("<Button-1>", lambda e: callback("https://www.google.co.th/maps/search/big+c/"))

    link2 = Label(frame, text="Lotus Supermarket", fg="blue", cursor="hand2",anchor=W)
    link2.grid(row=1, column=0,padx=5, pady=5,sticky=W)
    link2.bind("<Button-1>", lambda e: callback("https://www.google.co.th/maps/search/lotus/"))

    link3 = Label(frame, text="Tops Supermarket", fg="blue", cursor="hand2",anchor=W)
    link3.grid(row=2, column=0,padx=5, pady=5,sticky=W)
    link3.bind("<Button-1>", lambda e: callback("https://www.google.co.th/maps/search/tops+supermarket/"))

    link4 = Label(frame, text="Maxvalu Supermarket", fg="blue", cursor="hand2",anchor=W)
    link4.grid(row=3, column=0,padx=5, pady=5,sticky=W)
    link4.bind("<Button-1>", lambda e: callback("https://www.google.co.th/maps/search/maxvalu/"))

    link5 = Label(frame, text="market", fg="blue", cursor="hand2",anchor=W)
    link5.grid(row=4, column=0,padx=5, pady=5,sticky=W)
    link5.bind("<Button-1>", lambda e: callback("https://www.google.co.th/maps/search/market/"))
    #### Frame suparmarket ----------------------------------------------------------------------------------------------------------------------

    #### Frame1 suparmarket online----------------------------------------------------------------------------------------------------------------------
    frame1=ttk.LabelFrame(labelframe5, text=' Supermarke Online')
    frame1.pack(side='left', padx=5, pady=5, ipadx=15, ipady=15, expand='yes', fill='both')

    link1 = Label(frame1, text="Big C shoponline", fg="blue", cursor="hand2",anchor=W)
    link1.grid(row=0, column=0,padx=5, pady=5,sticky=W)
    link1.bind("<Button-1>", lambda e: callback("https://www.bigc.co.th/dailydeal"))

    link2 = Label(frame1, text="Lotus shoponline", fg="blue", cursor="hand2",anchor=W)
    link2.grid(row=1, column=0,padx=5, pady=5,sticky=W)
    link2.bind("<Button-1>", lambda e: callback("https://shoponline.tescolotus.com/groceries/th-TH/shop/%E0%B8%AD%E0%B8%B2%E0%B8%AB%E0%B8%B2%E0%B8%A3%E0%B8%AA%E0%B8%94,-%E0%B9%81%E0%B8%8A%E0%B9%88%E0%B9%81%E0%B8%82%E0%B9%87%E0%B8%87-&-%E0%B9%80%E0%B8%9A%E0%B9%80%E0%B8%81%E0%B8%AD%E0%B8%A3%E0%B8%B5%E0%B9%88/all"))

    link3 = Label(frame1, text="Tops shoponline", fg="blue", cursor="hand2",anchor=W)
    link3.grid(row=2, column=0,padx=5, pady=5,sticky=W)
    link3.bind("<Button-1>", lambda e: callback("https://www.tops.co.th/th/?gclid=Cj0KCQiA48j9BRC-ARIsAMQu3WQw2c8WpxSJn44RREBrg8sGioAEk9lERWFSh7pzRw-2tNyS5HSgmSEaAj5yEALw_wcB"))


    #### Frame1 suparmarket online----------------------------------------------------------------------------------------------------------------------


    


    # Label(labelframe5, text="\n".join([str(i) for i in list_select_food])).pack()
          
def sortby(tv, col, descending):
    """sort tree contents when a column header is clicked on"""
    # grab values to sort
    data = [(tv.set(child, col), child) for child in tv.get_children('')]
    # if the data to be sorted is numeric change to float
    list_data = []
    for l in data:
        list_data_temp = []
        for i in range(len(l)):
            if i == 0:
                int_num = float(l[i] )
                list_data_temp.append(int_num)
            else:
                list_data_temp.append(l[i])
        list_data.append(list_data_temp)
    # print(list_data)
    # data =  float(data)
    # now sort the data in place
    list_data.sort(reverse=descending)
    # print(list_data.sort(reverse=descending))
    for ix, item in enumerate(list_data):
        tv.move(item[1], '', str(ix))
    # switch the heading so it will sort in the opposite direction
    tv.heading(col, command=lambda col=col: sortby(tv, col, int(not descending)))

def delete():
    Indredient_input_list.pop(Ingredient_list.curselection()[0])
    Ingredient_list.delete(0, END)
    for x in Indredient_input_list:
        Ingredient_list.insert(END, x + '\n')
    
def append_ingredient():
    if Entry_Ingredient.get() != "":
        correct_ingredient = change_vacab(Entry_Ingredient.get())
        Ingredient_list.delete(0, END)  #clear listbox
        Indredient_input_list.append(correct_ingredient)
        for x in Indredient_input_list:
            Ingredient_list.insert(END, x + '\n')
        Entry_Ingredient.delete(0, END)

def pop_window(event):

    data =  tv.selection()[0]
    print(data)
    # print(get_all_menu())
    data_item = tv.item(data,'values')
    # print('aaaaaaaaaa')
    list_data_item =list(data_item)
    
    # print(list_data_item)
    for nf in list_data_item:
        # print(nf)
        if nf in get_all_menu() :
            currfood = nf
            # print(currfood)

    top = Toplevel(root)
    top.title('Food Information')
    # top = tk.Toplevel(root)

    # Label Frame pic---------------------------------------------------------------------------------------------------
    labelframe_pic = LabelFrame(top, text=currfood ,padx=15, pady=15,font='Helvetica 12 bold')
    labelframe_pic.pack(fill="both", expand="yes",padx=5, pady=5)
    # Label Frame pic ---------------------------------------------------------------------------------------------------

    # Label Frame pop 1---------------------------------------------------------------------------------------------------
    labelframe_pop_1 = LabelFrame(top, text="ส่วนผสม",padx=15, pady=15,font='Helvetica 12 bold')
    labelframe_pop_1.pack(fill="both", expand="yes",padx=5, pady=5)
    # Label Frame pop 1 ---------------------------------------------------------------------------------------------------

    # Label Frame pop 2---------------------------------------------------------------------------------------------------
    labelframe_pop_2 = LabelFrame(top, text="วิธีทำ",padx=15, pady=15,font='Helvetica 12 bold')
    labelframe_pop_2.pack(fill="both", expand="yes",padx=5, pady=5)

    # Label Frame ---------------------------------------------------------------------------------------------------

    # Label Frame pop 3---------------------------------------------------------------------------------------------------
    labelframe5 = LabelFrame(top, text="Supermarket near me !",padx=15, pady=15,font='Helvetica 12 bold')
    labelframe5.pack(fill="both", expand="yes",padx=5, pady=5)

    # Label Frame ---

    # Ingredient ---------------------------------------------------------------------------------------------------
    
    style = ttk.Style()
    style.configure("style.Treeview", highlightthickness=0, bd=0, font=('Calibri', 12)) 
    style.configure("style.Treeview.Heading", font=('Calibri', 13,'bold')) 
    style.configure("style.Treeview.Heading",background="blue") 
    
    
    ac= ('A','B')
    column_ingredient = 'ส่วนผสม'+currfood 
    # print(column_ingredient)

    df_list_ingredient = get_total_ingredient(currfood).values.tolist()
    df_manu,list_same = find_menu(Type_Food_list,Indredient_input_list)
    
    for i in list_same:
        if currfood in i:
            curr_l = i
            # print('aaaaaaaaaaaaa')
            # print(curr_l)

    new_list = []
    for i_row in range(len(df_list_ingredient)):
        new_list_temp =[]
        str_i_row = df_list_ingredient[i_row][0]
        # print('aaaaaaaaaaaaa1')
        # print(str_i_row)
        if str(i_row) in curr_l:
            new_list_temp.append(str_i_row)
            new_list_temp.append('no')
        else:
            new_list_temp.append(str_i_row)
            new_list_temp.append('ออกไปซื้อนะจ่ะ')
        new_list.append(new_list_temp)
    tuple_new_list = new_list
    # print(tuple_new_list)

    tv_ingredient = ttk.Treeview(labelframe_pop_1,columns = ac ,show="headings",height="5",style= "style.Treeview")

    yscrollbar = ttk.Scrollbar(labelframe_pop_1,orient="vertical",command = tv_ingredient.yview)
    yscrollbar.pack(side=RIGHT,fill = "y")

    xscrollbar = ttk.Scrollbar(labelframe_pop_1,orient="horizontal",command = tv_ingredient.xview)
    xscrollbar.pack(side=BOTTOM,fill = "x")



    tv_ingredient.configure(yscrollcommand =yscrollbar.set,xscrollcommand =xscrollbar.set)
    tv_ingredient.configure(columns = ac)
   
    for i in range(2):
        tv_ingredient.column(ac[i],width = 70 ,anchor="w")
        tv_ingredient.heading(ac[i],text=column_ingredient[i])

    tv_ingredient.heading('A',text=column_ingredient,anchor="w")
    tv_ingredient.column('A' ,minwidth=0 ,width=100)  
    tv_ingredient.heading('B' ,text= 'information',anchor="w")
    tv_ingredient.column('B' ,minwidth=0 ,width=200) 
  
    # df_list_ingredient = get_total_ingredient(currfood).values.tolist()
    
    for row in tuple_new_list:
        if 'ออกไปซื้อนะจ่ะ' in row:
            # print(row)
            # print('1111')
            # tv_ingredient.tag_configure('sale', background="#008001")
            tv_ingredient.insert("","end",values=row ,text="Agente1",tags =('sale'))
           
        else:
            # print(row)
            tv_ingredient.insert("","end",values=row ,text="Agente1",tags =('no_sale'))
            


    tv_ingredient.tag_configure('sale', background="#E8E8E8")
    tv_ingredient.tag_configure('no_sale', background="#DFDFDF")
    tv_ingredient.pack(fill="both", expand=True)

    # Method ---------------------------------------------------------------------------------------------------
    style = ttk.Style()
    style.configure("style.Treeview", highlightthickness=0, bd=0, font=('Calibri', 12)) 
    style.configure("style.Treeview.Heading", font=('Calibri', 13,'bold')) 
    style.configure("style.Treeview.Heading",background="blue") 

    column_method = 'วิธีทำ'+currfood
    # print(column_method)
    tv_method = ttk.Treeview(labelframe_pop_2,columns = 0,show="headings",height="5",style= "style.Treeview")

    yscrollbar = ttk.Scrollbar(labelframe_pop_2,orient="vertical",command = tv_method.yview)
    yscrollbar.pack(side=RIGHT,fill = "y")

    xscrollbar = ttk.Scrollbar(labelframe_pop_2,orient="horizontal",command = tv_method.xview)
    xscrollbar.pack(side=BOTTOM,fill = "x")



    tv_method.configure(yscrollcommand =yscrollbar.set,xscrollcommand =xscrollbar.set)
  
    tv_method.configure(columns = column_method)
   

    tv_method.heading(0,text=column_method,anchor="w")
    tv_method.column(0 ,width=500,minwidth=5000)   
    
    

    df_manu,list_same = find_menu(Type_Food_list,Indredient_input_list)
    df = df_manu
    df_list_method = get_total_method(currfood).values.tolist()
    for row in df_list_method:
        # print(row)
        tv_method.insert("","end",values=row ,text="Agente1")
    tv_method.pack(fill="both", expand=True)

    
    # display pic --------------------------------------------------------------------------------------------------

     
    stim_filename = 'image\\'+currfood+".jpg"
    Img_pil = Image.open(stim_filename)
    Img_pil = Img_pil.resize((400, 300), Image.ANTIALIAS)
    Img_TK = ImageTk.PhotoImage(Img_pil)

    label1 = Label(labelframe_pic,image = Img_TK)
    label1.image = Img_TK
    label1.pack()
    
    #### Frame suparmarket ----------------------------------------------------------------------------------------------------------------------
    frame=ttk.LabelFrame(labelframe5, text='Find Supermarket')
    frame.pack(side='left', padx=5, pady=5, ipadx=15, ipady=15, expand='yes', fill='both')


    link1 = Label(frame, text="Big C Supermarket", fg="blue", cursor="hand2",anchor=W)
    link1.grid(row=0, column=0,padx=5, pady=5,sticky=W)
    link1.bind("<Button-1>", lambda e: callback("https://www.google.co.th/maps/search/big+c/"))

    link2 = Label(frame, text="Lotus Supermarket", fg="blue", cursor="hand2",anchor=W)
    link2.grid(row=1, column=0,padx=5, pady=5,sticky=W)
    link2.bind("<Button-1>", lambda e: callback("https://www.google.co.th/maps/search/lotus/"))

    link3 = Label(frame, text="Tops Supermarket", fg="blue", cursor="hand2",anchor=W)
    link3.grid(row=2, column=0,padx=5, pady=5,sticky=W)
    link3.bind("<Button-1>", lambda e: callback("https://www.google.co.th/maps/search/tops+supermarket/"))

    link4 = Label(frame, text="Maxvalu Supermarket", fg="blue", cursor="hand2",anchor=W)
    link4.grid(row=3, column=0,padx=5, pady=5,sticky=W)
    link4.bind("<Button-1>", lambda e: callback("https://www.google.co.th/maps/search/maxvalu/"))

    link5 = Label(frame, text="market", fg="blue", cursor="hand2",anchor=W)
    link5.grid(row=4, column=0,padx=5, pady=5,sticky=W)
    link5.bind("<Button-1>", lambda e: callback("https://www.google.co.th/maps/search/market/"))
    #### Frame suparmarket ----------------------------------------------------------------------------------------------------------------------

    #### Frame1 suparmarket online----------------------------------------------------------------------------------------------------------------------
    frame1=ttk.LabelFrame(labelframe5, text=' Supermarke Online')
    frame1.pack(side='left', padx=5, pady=5, ipadx=15, ipady=15, expand='yes', fill='both')

    link1 = Label(frame1, text="Big C shoponline", fg="blue", cursor="hand2",anchor=W)
    link1.grid(row=0, column=0,padx=5, pady=5,sticky=W)
    link1.bind("<Button-1>", lambda e: callback("https://www.bigc.co.th/dailydeal"))

    link2 = Label(frame1, text="Lotus shoponline", fg="blue", cursor="hand2",anchor=W)
    link2.grid(row=1, column=0,padx=5, pady=5,sticky=W)
    link2.bind("<Button-1>", lambda e: callback("https://shoponline.tescolotus.com/groceries/th-TH/shop/%E0%B8%AD%E0%B8%B2%E0%B8%AB%E0%B8%B2%E0%B8%A3%E0%B8%AA%E0%B8%94,-%E0%B9%81%E0%B8%8A%E0%B9%88%E0%B9%81%E0%B8%82%E0%B9%87%E0%B8%87-&-%E0%B9%80%E0%B8%9A%E0%B9%80%E0%B8%81%E0%B8%AD%E0%B8%A3%E0%B8%B5%E0%B9%88/all"))

    link3 = Label(frame1, text="Tops shoponline", fg="blue", cursor="hand2",anchor=W)
    link3.grid(row=2, column=0,padx=5, pady=5,sticky=W)
    link3.bind("<Button-1>", lambda e: callback("https://www.tops.co.th/th/?gclid=Cj0KCQiA48j9BRC-ARIsAMQu3WQw2c8WpxSJn44RREBrg8sGioAEk9lERWFSh7pzRw-2tNyS5HSgmSEaAj5yEALw_wcB"))


    # #### Find suparmarket near me ----------------------------------------------------------------------------------------------------------------------
    # #### Frame suparmarket ----------------------------------------------------------------------------------------------------------------------
    # frame=ttk.LabelFrame(labelframe5, text='Find Supermarket')
    # frame.pack(side='left', padx=5, pady=5, ipadx=15, ipady=15, expand='yes', fill='both')
    # link1 = Label(frame, text="Big C Supermarket", fg="blue", cursor="hand2",anchor=W)
    # link1.pack(fill=X)
    # link1.bind("<Button-1>", lambda e: callback("https://www.google.co.th/maps/search/big+c/"))

    # link2 = Label(frame, text="Lotus Supermarket", fg="blue", cursor="hand2",anchor=W)
    # link2.pack(fill=X)
    # link2.bind("<Button-1>", lambda e: callback("https://www.google.co.th/maps/search/lotus/"))

    # link3 = Label(frame, text="Tops Supermarket", fg="blue", cursor="hand2",anchor=W)
    # link3.pack(fill=X)
    # link3.bind("<Button-1>", lambda e: callback("https://www.google.co.th/maps/search/tops+supermarket/"))

    # link4 = Label(frame, text="Maxvalu Supermarket", fg="blue", cursor="hand2",anchor=W)
    # link4.pack(fill=X)
    # link4.bind("<Button-1>", lambda e: callback("https://www.google.co.th/maps/search/maxvalu/"))

    # link5 = Label(frame, text="market", fg="blue", cursor="hand2",anchor=W)
    # link5.pack(fill=X)
    # link5.bind("<Button-1>", lambda e: callback("https://www.google.co.th/maps/search/market/"))
    # #### Frame suparmarket ----------------------------------------------------------------------------------------------------------------------

    # #### Frame1 suparmarket online----------------------------------------------------------------------------------------------------------------------
    # frame1=ttk.LabelFrame(labelframe5, text=' Supermarke Online')
    # frame1.pack(side='left', padx=5, pady=5, ipadx=15, ipady=15, expand='yes', fill='both')

    # link1 = Label(frame1, text="Big C shoponline", fg="blue", cursor="hand2",anchor=W)
    # link1.pack(fill=X)
    # link1.bind("<Button-1>", lambda e: callback("https://www.bigc.co.th/dailydeal"))

    # link2 = Label(frame1, text="Lotus shoponline", fg="blue", cursor="hand2",anchor=W)
    # link2.pack(fill=X)
    # link2.bind("<Button-1>", lambda e: callback("https://shoponline.tescolotus.com/groceries/th-TH/shop/%E0%B8%AD%E0%B8%B2%E0%B8%AB%E0%B8%B2%E0%B8%A3%E0%B8%AA%E0%B8%94,-%E0%B9%81%E0%B8%8A%E0%B9%88%E0%B9%81%E0%B8%82%E0%B9%87%E0%B8%87-&-%E0%B9%80%E0%B8%9A%E0%B9%80%E0%B8%81%E0%B8%AD%E0%B8%A3%E0%B8%B5%E0%B9%88/all"))

    # link3 = Label(frame1, text="Tops shoponline", fg="blue", cursor="hand2",anchor=W)
    # link3.pack(fill=X)
    # link3.bind("<Button-1>", lambda e: callback("https://www.tops.co.th/th/?gclid=Cj0KCQiA48j9BRC-ARIsAMQu3WQw2c8WpxSJn44RREBrg8sGioAEk9lERWFSh7pzRw-2tNyS5HSgmSEaAj5yEALw_wcB"))
    #### Frame1 suparmarket online----------------------------------------------------------------------------------------------------------------------
    #### Find suparmarket near me ----------------------------------------------------------------------------------------------------------------------
    
def type_food():
    x = tv_suggest.get_children()
    for ch in x:
        tv_suggest.delete(ch)

    global Type_Food_list
    x = tv.get_children()
    # print(var_boil.get(),var_food_j.get(),var_fried.get(),var_grill.get(),var_puff.get(),var_steam.get(),var_yum.get())
    for child in x:
        tv.delete(child)
    Type_Food_list = []
    if var_sellectall.get() == 1:
        all_type=['ต้ม','ปิ้งย่าง','อาหารเจ','ผัด','ยำ','ทอด']
        for t in all_type:
            Type_Food_list.append(t)
    if var_boil.get() == 1:
        Type_Food_list.append('ต้ม')
    if var_grill.get() == 1:
        Type_Food_list.append('ปิ้งย่าง')
    if var_food_j.get() == 1:
        Type_Food_list.append('อาหารเจ')
    if var_puff.get() == 1:
        Type_Food_list.append('ผัด') 
    if var_steam.get() == 1:
        Type_Food_list.append('นึ่ง')
    if var_yum.get() == 1:
        Type_Food_list.append('ยำ')
    if var_fried.get() == 1:
        Type_Food_list.append('ทอด')

    Type_Food_list = set(Type_Food_list)
    
    # print('00000000')
    # print(Type_Food_list)
    column_gen = tuple(gen_column(Type_Food_list,Indredient_input_list))
    # print(column_gen)

 
    tv.configure(columns = column_gen)
    for i in range(len(column_gen)):
        tv.heading(i,text=column_gen[i],command=lambda c=column_gen[i]: sortby(tv,c, 0))
        tv.column(i, anchor="e")

    df_manu,list_same = find_menu(Type_Food_list,Indredient_input_list)
    df = df_manu
    # print(df)
    df_list = df.values.tolist()
    for row in df_list:
        # print(row)
        tv.insert("","end",values=row)

    tv.bind("<Double-Button-1>", pop_window)
    tv.bind("<Return>", lambda e: select())


    
    df_list_ingredient = get_total_ingredient(currfood).values.tolist()
    df_manu,list_same = find_menu(Type_Food_list,Indredient_input_list)
    
    for i in list_same:
        if currfood in i:
            curr_l = i
            # print('aaaaaaaaaaaaa')
            # print(curr_l)

    new_list = []
    for i_row in range(len(df_list_ingredient)):
        new_list_temp =[]
        str_i_row = df_list_ingredient[i_row][0]
        # print('aaaaaaaaaaaaa1')
        # print(str_i_row)
        if str(i_row) in curr_l:
            new_list_temp.append(str_i_row)
            new_list_temp.append('no')
        else:
            new_list_temp.append(str_i_row)
            new_list_temp.append('ออกไปซื้อนะจ่ะ')
        new_list.append(new_list_temp)
    tuple_new_list = new_list

    


# Label Frame ---------------------------------------------------------------------------------------------------
labelframe = LabelFrame(root, text="สั่งอาหาร",padx=15, pady=15,font='Helvetica 12 bold')
labelframe.pack(fill="both", expand="yes",padx=5, pady=5)
# Label Frame ---------------------------------------------------------------------------------------------------

# Let Go botton ---------------------------------------------------------------------------------------------------
Button_Delete_Ingredient = Button(root, text ="Let Go!",command = type_food, bg='blue', fg='white')
Button_Delete_Ingredient.pack(fill="both", expand="yes",padx=5, pady=5)
# Let Go botton ---------------------------------------------------------------------------------------------------

# Label Frame 3 ---------------------------------------------------------------------------------------------------
labelframe3 = LabelFrame(root, text="Result",padx=15, pady=15,font='Helvetica 12 bold')
labelframe3.pack(fill="both", expand="yes",padx=5, pady=5)
scrollbar = Scrollbar(labelframe3)
scrollbar.pack(side=RIGHT, fill=Y)
tv = ttk.Treeview(labelframe3,columns = (1,2,3),show="headings",height="5")
tv.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=tv.yview)
tv.pack(fill="both", expand=True)
# Label Frame 3 ---------------------------------------------------------------------------------------------------

# Label Frame 4 ---------------------------------------------------------------------------------------------------
labelframe4 = LabelFrame(root, text="consumtion",padx=15, pady=15,font='Helvetica 12 bold')
labelframe4.pack(fill="both", expand="yes",padx=5, pady=5)
scrollbar_4 = Scrollbar(labelframe4)
scrollbar_4.pack(side=RIGHT, fill=Y)
tv_suggest = ttk.Treeview(labelframe4,columns = (1,2,3),show="headings",height="5")
tv_suggest.config(yscrollcommand=scrollbar_4.set)
scrollbar_4.config(command=tv_suggest.yview)
tv_suggest.pack(fill="both", expand=True)
# Label Frame 4 ---------------------------------------------------------------------------------------------------

# Label Frame 5 ---------------------------------------------------------------------------------------------------
labelframe5 = LabelFrame(root, text="Supermarket near me !",padx=15, pady=15,font='Helvetica 12 bold')
labelframe5.pack(fill="both", expand="yes",padx=5, pady=5)
# Label Frame 5 ---------------------------------------------------------------------------------------------------


# Dropdown Type ---------------------------------------------------------------------------------------------------
# label text 
textngongo = Label(labelframe, text ='Select type of Food',font='Helvetica 10 bold')
textngongo.grid(row=0, column=0,padx=5, pady=5)

# check buttons 
var_sellectall = IntVar()
boil = Checkbutton(labelframe, text ='เลือกทั้งหมด',variable=var_sellectall,  onvalue = 1,  offvalue = 0)
boil.grid(row=1, column=0,padx=5, pady=5,sticky=W)

var_boil = IntVar()
grill = Checkbutton(labelframe, text ='ต้ม',variable=var_boil,  onvalue = 1,  offvalue = 0)
grill.grid(row=2, column=0,padx=5, pady=5,sticky=W)

var_grill = IntVar()
food_j = Checkbutton(labelframe, text ='ปิ้งย่าง',variable=var_grill,  onvalue = 1,  offvalue = 0)
food_j.grid(row=3, column=0,padx=5, pady=5,sticky=W)

var_food_j = IntVar()
puff = Checkbutton(labelframe, text ='อาหารเจ',variable=var_food_j,  onvalue = 1,  offvalue = 0)
puff.grid(row=4, column=0,padx=5, pady=5,sticky=W)

var_puff = IntVar()
steam = Checkbutton(labelframe, text ='ผัด',variable=var_puff,  onvalue = 1,  offvalue = 0)
steam.grid(row=1, column=1,padx=5, pady=5,sticky=W)

var_steam = IntVar()
yum = Checkbutton(labelframe, text ='นึ่ง',variable=var_steam,  onvalue = 1,  offvalue = 0)
yum.grid(row=2, column=1,padx=5, pady=5,sticky=W)

var_yum = IntVar()
fried = Checkbutton(labelframe, text ='ยำ',variable=var_yum, takefocus = 0)
fried.grid(row=3, column=1,padx=5, pady=5,sticky=W)

var_fried = IntVar()
fried = Checkbutton(labelframe, text ='ทอด',variable=var_fried, takefocus = 0)
fried.grid(row=4, column=1,padx=5, pady=5,sticky=W)

# Input ---------------------------------------------------------------------------------------------------
Ingredient_Input_label = Label(labelframe, text="Input Ingredient",font='Helvetica 10 bold')
Ingredient_Input_label.grid(row=0, column=3,padx=5, pady=5,sticky=W)
Entry_Ingredient = Entry(labelframe)
Entry_Ingredient.grid(row=0, column=4,padx=5, pady=5)

Ingredient_Input_label = Label(labelframe, text="Ingredient",font='Helvetica 10 bold')
Ingredient_Input_label.grid(row=1, column=3,padx=5, pady=5,sticky=W)
# Input ---------------------------------------------------------------------------------------------------

Button_Ingredient = Button(labelframe, text ="Input",command = append_ingredient, bg='#ffb3fe')
Button_Ingredient.grid(row=0, column=5,padx=5, pady=5)

Button_Delete_Ingredient = Button(labelframe, text ="Delete",command = delete, bg='#ffb3fe')
Button_Delete_Ingredient.grid(row=1, column=5,padx=5, pady=5)

# Button_Delete_Ingredient = Button(root, text ="Let Go!",command = type_food)
# Button_Delete_Ingredient.pack(fill="both", expand="yes",padx=5, pady=5)


scrollbar_lb = Scrollbar(labelframe, orient="vertical")
scrollbar_lb.grid(row=2, column=5, pady=1,sticky=NW,rowspan = 3)


Ingredient_list = Listbox(labelframe)
# Ingredient_list = Listbox(labelframe,yscrollcommand = scrollbar_lb.set)
# Ingredient_list.pack(expand=True, fill=Y)
Ingredient_list.grid(row=1, column=4, pady=5,rowspan = 5)

scrollbar_lb.config(command=Ingredient_list.yview)



# pt = Table(labelframe3,dataframe=find_menu(Type_Food_list,Indredient_input_list),showtoolbar=False, showstatusbar=False)
# pt.show()
# pt.redraw()




root.mainloop()