import pandas as pd
import os
import string
import tabulate # pretty print, optional dependency
import customtkinter
from tkinter import StringVar
import tkinter.messagebox


customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


ALPHABET = string.ascii_letters + string.digits
     

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()


        #----------------------------------------GUI---------------------------
        
       
        # configure window
        self.title("One8 Manager")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create footer frame 
        self.footer_frame = customtkinter.CTkFrame(self, height=25,corner_radius=0, fg_color="#007ACC")
        self.footer_frame.grid(row=3, column=1,padx=0, pady=(5, 0), sticky="ew")
        self.footer_frame.grid_columnconfigure(0, weight=1)# center, fill space
        self.footer_label = customtkinter.CTkLabel( master=self.footer_frame, text="Developed by SandeepImandi © 2024",text_color=("#FFFFFF"),font=customtkinter.CTkFont(size=12),justify="center" )
        self.footer_label.grid(row=0, column=0,sticky="nsew")

        # create side frame
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=5, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(5, weight=1)
        
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 10))

        # create welcome frame
        self.welcome_frame = customtkinter.CTkFrame(self)
        self.welcome_frame.grid(row=1, column=1, sticky="ns")
        self.welcome_label = customtkinter.CTkLabel(self.welcome_frame,  justify="left", text="\n Welcome ! \n\n THIS APPLICATION USES A MASTER PASSWORD\
                    \n TO ENCRYPT & DECRYPT YOUR DATA.\
                    \n USE ANY ALPHANUMERIC PASSWORD (RECOMMENDED)\
                    \n AND REMEMBER THAT.\
                    \n\n WARNING: IF YOU LOSE YOUR MASTER PASSWORD, THEN YOU\
                    \n WILL NOT BE ABLE TO RECOVER YOUR SAVED PASSWORDS.\
                    \n\n VISIT: https://github.com/SandeepImandi01/One8_Manager", font=customtkinter.CTkFont(size=14))
        self.welcome_label.grid(row=0, column=0, padx=(20,0), pady=(20, 30))
        self.welcome_button = customtkinter.CTkButton(self.welcome_frame, text="Next", command=self.welcome_button_event, width=200)
        self.welcome_button.grid(row=3, column=0, padx=30, pady=(15, 15))
    
        # create login frame
        self.login_frame = customtkinter.CTkFrame(self)
        self.login_frame.grid(row=1, column=1, sticky="ns")
        self.login_label = customtkinter.CTkLabel(self.login_frame, text="One8Manager\n\n",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.login_label.grid(row=0, column=0, padx=150, pady=(50, 100))
        self.masterpassword_entry = customtkinter.CTkEntry(master=self.login_frame, width=300,height=40,border_width=1, show="*", placeholder_text=" ENTER MASTER PASSWORD")
        self.masterpassword_entry.grid(row=2, column=0, padx=30, pady=(0, 15))
        self.login_label2 = customtkinter.CTkLabel(self.login_frame, text="( Must have a minimum of 8 characters )")
        self.login_label2.grid(row=3, column=0, padx=20, pady=(5, 5))
        self.login_button = customtkinter.CTkButton(self.login_frame, text="Submit", command=self.login_button_event, width=200)
        self.login_button.grid(row=4, column=0, padx=30, pady=(30, 30))
        

        # create sidebar frame with widgets and buttons
        self.sidebar_button_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_button_frame.grid(row=0, column=0, rowspan=5, sticky="nsew")
        self.sidebar_button_frame.grid_rowconfigure(5, weight=1)
        self.logo_label = customtkinter.CTkLabel(self.sidebar_button_frame, text="Select Option: ", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_button_frame, text="Add New", command=self.add_button_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_button_frame,text="Search", command=self.search_button_event)
        self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
        self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_button_frame, text="Edit", command=self.edit_button_event)
        self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_button_frame, text="Delete", command=self.delete_button_event)
        self.sidebar_button_4.grid(row=4, column=0, padx=20, pady=10)
        self.sidebar_button_4 = customtkinter.CTkButton(self.sidebar_button_frame, text="Back", command=self.back_button_event)
        self.sidebar_button_4.grid(row=6, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_button_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_button_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 10))

        
        # create main entry field and button
        self.entry_frame = customtkinter.CTkFrame(self,width=250)
        self.entry_frame.grid(row=0, column=1,padx=(20,0),pady=(20,0), sticky="nsew")
        self.entry_label = customtkinter.CTkLabel(self.entry_frame, text="Add your credentials: ", font=customtkinter.CTkFont(size=16))
        self.entry_label.grid(row=0, column=1, padx=20, pady=(20, 10))
                              
        self.label_name = customtkinter.CTkLabel(self.entry_frame, text="ENTER URL OR APP NAME, YOU WANT TO SAVE: ",justify="right",anchor="e",width=350, font=customtkinter.CTkFont(size=14))
        self.label_name.grid(row=1, column=0, padx=(20,5), pady=(5, 5))
        self.entry_name = customtkinter.CTkEntry(master=self.entry_frame,width=350,height=40,border_width=1)
        self.entry_name.grid(row=1, column=1, padx=5, pady=(5, 5))

        self.label_uname = customtkinter.CTkLabel(self.entry_frame, text="ENTER NAME/USERNAME, YOU WANT TO SAVE: ",justify="right",anchor="e",width=350, font=customtkinter.CTkFont(size=14))
        self.label_uname.grid(row=2, column=0, padx=(20,5), pady=(5, 5))
        self.entry_uname = customtkinter.CTkEntry(master=self.entry_frame, width=350,height=40,border_width=1)
        self.entry_uname.grid(row=2, column=1,  padx=5, pady=(5, 5))
        
        self.label_password = customtkinter.CTkLabel(self.entry_frame, text="ENTER PASSWORD, YOU WANT TO SAVE: ",justify="right",anchor="e",width=350, font=customtkinter.CTkFont(size=14))
        self.label_password.grid(row=3, column=0, padx=(20,20), pady=(5, 5))
        self.entry_password = customtkinter.CTkEntry(master=self.entry_frame,width=350,height=40,border_width=1, show="*")
        self.entry_password.grid(row=3, column=1,  padx=5, pady=(5, 5))
        
        self.entry_button = customtkinter.CTkButton(self.entry_frame, text="Submit") #entry field submit button, no initial command
        self.entry_button.grid(row=4, column=1, padx=30, pady=(10, 10))

        # create textbox
        self.textbox = customtkinter.CTkTextbox(self, width=400,
                                                border_width=1,
                                                border_color="#007ACC",
                                                scrollbar_button_color="#007ACC",
                                                wrap="word",
                                                font=("Courier", 16)) #Monospaced font
        self.textbox.grid(row=1, column=1,padx=(20, 0), pady=(20, 0), sticky="nsew")



    
        # set default values
        self.appearance_mode_optionemenu.set("Light")
        self.textBox(text='') # text box (clear)
      
       
        
    
        data_file = os.path.isfile('data.csv')#check whether data file is there or not
        if not data_file:  # if csv not found
            self.create_csv()  # call function and create csv
            self.welcome_event()# start with welcome frame
           
        else :
            self.login_event()#start with login frame
            



    #-------------------------------------GUIOperation----------------------------

            

    def welcome_event(self): #bundel
         #Show only the welcome frame, by removing everything else
         print("Welcome \n")
         self.login_frame.grid_forget()
         self.sidebar_button_frame.grid_forget()
         self.entry_frame.grid_forget()
         self.textbox.grid_forget()

    def login_event(self): #bundel
        # Show only the login frame
        print("Login \n")
        self.welcome_frame.grid_forget()# forget frame
        self.sidebar_button_frame.grid_forget()# forget frame
        self.entry_frame.grid_forget()# forget frame
        self.textbox.grid_forget()# forget frame
        self.login_frame.grid(row=1, column=1, sticky="ns")  # show login frame
        
    def main_event(self): #bundel
        print("Main menu\n") 
        self.welcome_frame.grid_forget()# forget frame (make sure)
        self.login_frame.grid_forget()  # forget frame (make sure)
        self.sidebar_button_frame.grid(row=0, column=0, rowspan=5, sticky="nsew")# show frame
        self.entry_frame.grid(row=0, column=1,padx=(20,0),pady=(20,0), sticky="nsew")# show frame
        self.textbox.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")# show frame
        self.add_button_event() # start with add menu
        
        
        
    def welcome_button_event(self):
         print("Next button pressed\n") 
         self.login_event()
        
    def change_appearance_mode_event(self, new_appearance_mode: str):
        print("Appearance changed :" , new_appearance_mode)
        customtkinter.set_appearance_mode(new_appearance_mode)

    def login_button_event(self):
        print("Login button pressed\n")
        login_status = self.login_menu_op()# call, for check
        if login_status:
            self.main_event()#call main window function
        else:
            self.login_event() #do not preceded,repet
            self.masterpassword_entry.delete(0,'end') #clear entry field 
        
    def back_button_event(self):
        print("Back button pressed\n")
        self.login_event() # call function to start with login window
        # clear entry field
        self.masterpassword_entry.delete(0,'end')# clear
        self.entry_name.delete(0, 'end')
        self.entry_uname.delete(0, 'end')
        self.entry_name.delete(0, 'end')
        self.textBox(text='') # text box (clear)

    def add_button_event(self):
        print("Add button pressed\n")      
        self.entry_label.configure(text="Add your credentials: ")#label
        self.label_name.grid(row=1, column=0, padx=(20,5), pady=(5, 5)) #add label
        self.label_uname.grid(row=2, column=0, padx=(20,5), pady=(5, 5)) #add label
        self.label_password.grid(row=3, column=0, padx=(20,5), pady=(5, 5)) #add label
        self.label_name.configure(text="ENTER URL OR APP NAME, YOU WANT TO SAVE: ")#changelabel
        self.label_uname.configure(text="ENTER NAME/USERNAME, YOU WANT TO SAVE: ")#change label
        self.label_password.configure(text="ENTER PASSWORD, YOU WANT TO SAVE")#change label
        self.entry_password.grid(row=3, column=1,  padx=20, pady=(5, 5))# add (make sure)
        self.entry_uname.grid(row=2, column=1,  padx=20, pady=(5, 5))# add
        # clear entry field
        self.entry_name.delete(0, 'end')
        self.entry_uname.delete(0, 'end')
        self.entry_password.delete(0, 'end')
        self.textBox(text='') # clear box
        self.entry_button.configure(command=self.add_menu_op) # call this function, when submit button is pressed
        
    def search_button_event(self):
        print("Search button pressed\n")
        self.entry_label.configure(text="Search your credentials: ")#label
        self.label_uname.grid_forget()#remove
        self.label_password.grid_forget()#remove
        self.entry_uname.grid_forget()# remove
        self.entry_password.grid_forget()# remove
        # clear entry field
        self.entry_name.delete(0, 'end')
        self.label_name.configure(text="ENTER URL OR APP NAME, YOU WANT TO SEARCH: ")#configure the label text
        print("HINT: Clicking the submit button will show all saved credentials.\n")
        self.textBox("HINT: Clicking the submit button will show all saved credentials")
        self.entry_button.configure(command=self.search_menu_op) # call this function, when submit button is pressed
                
        
    def edit_button_event(self):
        print("Edit button pressed\n")
        self.entry_label.configure(text="Edit your credentials: ")#label
        self.label_uname.grid_forget()#remove
        self.label_password.grid_forget()#remove
        self.entry_uname.grid_forget()#remove
        self.entry_password.grid_forget()#remove
        # clear entry field
        self.entry_name.delete(0, 'end')
        self.entry_uname.delete(0, 'end')
        self.entry_password.delete(0, 'end')
        self.label_name.configure(text="ENTER URL OR APP NAME, YOU WANT TO EDIT: ")#configure the label text
        print("HINT: Clicking the submit button will show all saved credentials.\n")
        self.textBox("HINT: Clicking the submit button will show all saved credentials")
        self.entry_button.configure(command=self.edit_menu_op) # call this function, when submit button is pressed
          

    def delete_button_event(self):
        print("Delete button pressed\n")
        self.entry_label.configure(text="Delete your credentials: ")#label
        self.label_uname.grid_forget()#remove
        self.label_password.grid_forget()#remove
        self.entry_uname.grid_forget()#remove
        self.entry_password.grid_forget()#remove
        # clear entry field
        self.entry_name.delete(0, 'end')
        self.label_name.configure(text="ENTER URL OR APP NAME, YOU WANT TO DELETE: ")#configure the label text
        print("HINT: Clicking the submit button will show all saved credentials.\n")
        self.textBox("HINT: Clicking the submit button will show all saved credentials")
        self.entry_button.configure(command=self.delete_menu_op) # call this function, when submit button is pressed
          




    #----------------------------------MenuOperation----------------------------------

    def login_menu_op(self):
        master_pass = self.masterpassword_entry.get() #fetch from entry box
        print("Checked master password: ", master_pass,'\n')
        if len(master_pass) >= 8: #if sucessfull, then move to main window
            return master_pass
        else:
            return False
            print("WARNING: Master password must be at least 8 characters long\n")
            #pass
        


    def add_menu_op(self): #when, entry button is presed under Add menu
        print("Operation : Add\n")
        nameVariable = self.entry_name.get() # fetch entry box inputs
        unameVariable = self.entry_uname.get()
        passwordVariable = self.entry_password.get()
        masterpassVariable = self.login_menu_op() #call function, fetch
        print("Adding: ",nameVariable,",",unameVariable,",", passwordVariable)
        print("With: ",masterpassVariable,"\n")
        if (unameVariable == ''):  # if found empty, replace it by 'Unavailable' label
            unameVariable = 'UNAVAILABLE'
        if (passwordVariable == ''):
            passwordVariable = 'UNAVAILABLE'
        if (nameVariable == ''): # URL/App name
            print("WARNING: URL or App Name cannot be empty.\n")
            self.textBox("WARNING : URL or App Name cannot be empty.")
        else:
            encrypted_pass = self.encrypt(passwordVariable, masterpassVariable)# call encrypt function to encrypt password
            self.add(unameVariable, encrypted_pass, nameVariable)# call function to add user data
            #clear entry box
            self.entry_uname.delete(0,'end')
            self.entry_name.delete(0,'end')
            self.entry_password.delete(0,'end')
            self.entry_button.configure(command=self.add_menu_op) # call this function, when submit button is pressed

            
    def search_menu_op(self):
        print("Operation : Search\n")
        nameVariable = self.entry_name.get() # fetch entry box inputs
        masterpassVariable = self.login_menu_op() #call function, fetch
        print("Searching: ",nameVariable)
        print("With: :",masterpassVariable , "\n")
        show_result = self.search(masterpassVariable,nameVariable)# call function
        show_tabulate = tabulate.tabulate(show_result, headers='keys', tablefmt='pipe', showindex=False)#Pretty Print
        self.textBox(show_tabulate) # print in textbox area
        #print(show_tabulate)
        #clear entry box
        self.entry_name.delete(0,'end')
        self.entry_button.configure(command=self.search_menu_op) # call this function, when submit button is pressed
   



    def edit_menu_op(self):
        print("Operation: Edit\n")
        nameVariable = self.entry_name.get()  # fetch entry box inputs
        masterpassVariable = self.login_menu_op()  # call function, fetch
        print("Searching: ", nameVariable)
        print("With: ", masterpassVariable, "\n")
        show_result = self.search(masterpassVariable, nameVariable)  # call search function
        show_tabulate = tabulate.tabulate(show_result, headers='keys', tablefmt='pipe', showindex=False)  # Pretty Print
        self.textBox(show_tabulate)  # print in textbox area

        if len(show_result) > 1:  # multiple credentials found, len = rows
            print("Multiple credentials found, going for index\n")
            self.label_name.configure(text="ENTER AN INDEX VALUE, YOU WANT TO EDIT: ")#change label
            self.entry_button.configure(command=lambda: self.edit_multi_index(show_result, masterpassVariable))  # call this function, to handle indexes, when submit button is pressed
        else:
            print("Single credential found\n")
            indexVariable = show_result.index.values[0]  # take default index
            print("Default Index input:", indexVariable, "\n")
            self.entry_uname.grid(row=2, column=1, padx=20, pady=(5, 5))  # add
            self.entry_password.grid(row=3, column=1, padx=20, pady=(5, 5))  # add
            self.label_uname.grid(row=2, column=0, padx=(20,5), pady=(5, 5)) #add label
            self.label_password.grid(row=3, column=0, padx=(20,5), pady=(5, 5)) #add label
            self.label_uname.configure(text="ENTER NEW NAME/USERNAME: ")#change label
            self.label_password.configure(text="ENTER NEW PASSWORD: ")#change label
            self.entry_button.configure(command=lambda: self.edit_new_input(show_result, masterpassVariable, indexVariable))  # call this function, to handle indexes, when submit button is pressed

    def edit_multi_index(self, show_result, masterpassVariable): #part of edit_menu_op()
        print("Operation: Edit Index \n")
        indexVariable = self.entry_name.get()  # fetch index input
        print("Index input:", indexVariable, "\n")
        if indexVariable:  # not empty
            indexVariable = int(indexVariable)
            self.entry_uname.grid(row=2, column=1, padx=20, pady=(5, 5))  # add
            self.entry_password.grid(row=3, column=1, padx=20, pady=(5, 5))  # add
            self.label_uname.grid(row=2, column=0, padx=(20,5), pady=(5, 5)) #add label
            self.label_password.grid(row=3, column=0, padx=(20,5), pady=(5, 5)) #add label
            self.label_uname.configure(text="ENTER NEW NAME/USERNAME: ")#change label
            self.label_password.configure(text="ENTER NEW PASSWORD: ")#change label
            self.entry_button.configure(command=lambda: self.edit_new_input(show_result, masterpassVariable, indexVariable))  # call this function, to handle indexes, when submit button is pressed

    def edit_new_input(self, show_result, masterpassVariable, indexVariable): #part of edit_menu_op()
        new_uameVariable = self.entry_uname.get()  # fetch entry box input
        new_passwordVariable = self.entry_password.get()  # fetch entry box input
        # exception
        if not new_uameVariable:  # if found empty, take old data
            old_name = show_result.loc[indexVariable, 'Username']  # index of that row, column id; get old Username
            new_uameVariable = old_name
        if not new_passwordVariable:
            old_password = show_result.loc[indexVariable, 'Password']  # get old password
            new_passwordVariable = old_password
        print("New Username:", new_uameVariable, ", New Password:", new_passwordVariable,"\n")
        new_passwordVariable = self.encrypt(new_passwordVariable, masterpassVariable)  # call function, to encrypted
        self.edit(indexVariable, new_uameVariable, new_passwordVariable)  # call edit function
        # clear entry field
        self.entry_uname.delete(0, 'end')
        self.entry_name.delete(0, 'end')
        self.entry_password.delete(0, 'end')
        self.label_uname.grid_forget()#remove
        self.label_password.grid_forget()#remove
        self.entry_uname.grid_forget()#remove
        self.entry_password.grid_forget()#remove
        self.label_name.configure(text="ENTER URL OR APP NAME, YOU WANT TO EDIT: ")#configure the label text
        self.entry_button.configure(command=self.edit_menu_op) # call this function, when submit button is pressed


      
    
    def delete_menu_op(self):
        print("Operation: Delete\n")
        nameVariable = self.entry_name.get()  # fetch entry box inputs
        masterpassVariable = self.login_menu_op()  # call function, fetch
        print("Searching: ", nameVariable)
        print("With: ", masterpassVariable, "\n")
        show_result = self.search(masterpassVariable, nameVariable)  # call search function
        show_tabulate = tabulate.tabulate(show_result, headers='keys', tablefmt='pipe', showindex=False)  # Pretty Print
        self.textBox(show_tabulate)  # print in textbox area

        if len(show_result) > 1:  # multiple credentials found, len = rows
            print("Multiple credentials found, going for index\n")
            self.label_name.configure(text="ENTER AN INDEX VALUE, YOU WANT TO DELETE: ")#change label
            self.entry_button.configure(command=lambda: self.delete_multi_index(show_result, masterpassVariable))  # call this function, to handle indexes, when submit button is pressed
        else:
            print("Single credential found\n")
            indexVariable = show_result.index.values[0]  # take default index
            print("Default Index input:", indexVariable, "\n")
            self.delete_dialog = customtkinter.CTkInputDialog(text="Type 'Yes' to confirm delete", title="Do you want to delete?")
            confirm = self.delete_dialog.get_input()
            print("Confirm: " ,confirm)
            if confirm in ["Yes", "yes"]:
                self.delete(indexVariable)# call delete function
            else:
                self.textBox("Delete  Cancelled ")
            # clear entry box
            self.entry_name.delete(0, 'end')
            self.label_name.configure(text="ENTER URL OR APP NAME, YOU WANT TO DELETE: ")#configure the label text
            self.entry_button.configure(command=self.delete_menu_op) # call this function, when submit button is pressed
       
            
    def delete_multi_index(self, show_result, masterpassVariable): #part of edit_menu_op()
        print("Operation: Edit Index \n")
        indexVariable = self.entry_name.get()  # fetch index input
        print("Index input:", indexVariable, "\n")
        if indexVariable:  # not empty
            indexVariable = int(indexVariable)
            self.delete_dialog = customtkinter.CTkInputDialog(text="Type 'Yes' to confirm delete", title="Do you want to delete?")
            confirm = self.delete_dialog.get_input()
            print("Confirm: " ,confirm)
            if confirm in ["Yes", "yes"]:
                self.delete(indexVariable)# call delete function
            else:
                self.textBox("Delete  Cancelled ")
             # clear entry box
            self.entry_name.delete(0, 'end')
            self.label_name.configure(text="ENTER URL OR APP NAME, YOU WANT TO DELETE: ")#configure the label text
            self.entry_button.configure(command=self.delete_menu_op) # call this function, when submit button is pressed

            
            
            


    

    #--------------------------------Backend-------------------------------------------

    def textBox(self, text):
         self.textbox.configure(state="normal")  # configure textbox to be normal
         self.textbox.delete("0.0", "end")  # delete all text
         self.textbox.insert("0.0",text)
         self.textbox.configure(state="disabled")  # configure textbox to be read-only

            
    def create_csv(self):
        data = {'Url/App name': [], 'Username': [], 'Password': []} # empty value dict
        df = pd.DataFrame(data)  # create new pandas DataFrame
        df.to_csv('data.csv', index=False)  # Write DataFrame to a new CSV file
        print("CSV created\n")


    def encrypt(self, password, master_pass):
        iteration_count = len(master_pass)
        # Encrypt password string with master password
        encrypted_password = ""
        for i in range(len(password)):
            shift = (ord(master_pass[i % len(master_pass)]) + i) % len(ALPHABET)
            if password[i] in ALPHABET:
                new_pos = (ALPHABET.find(password[i]) + shift) % len(ALPHABET)
                encrypted_password += ALPHABET[new_pos]
            else:
                encrypted_password += password[i]
        
        return encrypted_password

    
    def decrypt(self, encrypted_password, master_pass):
        iteration_count = len(master_pass)
        # Decrypt the encrypted password string with master password
        decrypted_password = ""
        for i in range(len(encrypted_password)):
            shift = (ord(master_pass[i % len(master_pass)]) + i) % len(ALPHABET)
            if encrypted_password[i] in ALPHABET:
                new_pos = (ALPHABET.find(encrypted_password[i]) - shift) % len(ALPHABET)
                decrypted_password += ALPHABET[new_pos]
            else:
                decrypted_password += encrypted_password[i]
        
        return decrypted_password


    def add(self, name, encrypted_pass, url):
        user_data = {'Url/App name': [url], 'Username': [name],'Password': [encrypted_pass]}# will save in same order
        df = pd.DataFrame(user_data)  # pack user data into data frame
        df.to_csv('data.csv', mode='a', header=False, index=False)# save to CSV file, append new row
        print("Credentials Added Successfully.","\n")
        self.textBox("Credentials Added Successfully.\n")
        self.backup()#call function


    def search(self, master_pass, url=''):
        # Extract form CSV file
        df = pd.read_csv('data.csv')
        dfS = df[df['Url/App name'].str.contains(url, na=False, case=False)]# pass the string to search related words
        # if on argument were pass (url='') ,then it will fetch entire dataframe
        # print(dfS)
        index_d = dfS.index.values  # take default index
        # Logic/Sontrol str. to decrypt all found passwords
        password = []  # empty list to store decrypted password from for loop data
        dfS = dfS.reset_index()  # make sure indexes pair with number of row
        for index, row in dfS.iterrows():  # iterate over all rows
            found_password = dfS.loc[index, 'Password']# go through all the rows of column
            dec_password = self.decrypt(found_password,  master_pass)  # decrypt that
            password.append(dec_password)

        dfS = dfS.set_index(index_d)  # set to default/original index for reference
        dfS['Password'] = password  # update password column with decrypted passwords

        return dfS
    


    def edit(self, index, new_name, new_password):
        df = pd.read_csv("data.csv")  # using 0th column (Url) as index
        # Edit row at given 'index'
        df.loc[index, ['Username', 'Password']] = [new_name, new_password]  # replace it with new user data
        df.to_csv('data.csv', index=False)  # save it
        print("Credentials Edited Successfully.","\n")
        self.textBox("Credentials Edited Successfully.\n")
        self.backup()#call function
      


    def delete(self, index):
        df = pd.read_csv("data.csv")
        # Delete row at given 'index'
        df.drop([index], axis=0, inplace=True)
        df.to_csv('data.csv', index=False)  # save it
        print("Credentials Deleted Successfully.","\n")
        self.textBox("Credentials Deleted Successfully.\n")
        self.backup()#call function
      

    def backup(self):
        df = pd.read_csv("data.csv")  # read the orignal file
        dp = os.getcwd()  # get the default path, initial directory
        os.chdir("..")  # change the current working directory, one dir back
        cp = os.getcwd()  # get the current path
        cp = cp + r"\MYPmanager_Backup\data.csv"  # add FolderName & FileName to obtained path
        if not os.path.isdir('MYPmanager_Backup'):  # If 'BackupMYPmanager' not exists
            os.makedirs('MYPmanager_Backup')  # Create one, for back up
        df.to_csv(cp, index=False)  # save a copy of same, cp = path
        os.chdir(dp)  # Restoring the default path



if __name__ == "__main__":
    app = App()
    app.mainloop()
