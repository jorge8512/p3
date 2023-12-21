#!/usr/bin/env python3.6
from kivy.app import App
import sqlite3

class FormularioApp(App):

    def clic_1(self):
        self.root.ids['btn1'].background_color = 66/255,255/255,0/255,1
        self.root.ids['etiqueta_1'].text = self.root.ids['entrada_1'].text

    def clic_2(self):
        self.root.ids['btn2'].background_color = 66/255,255/255,0/255,1
        self.root.ids['etiqueta_2'].text = self.root.ids['entrada_2'].text

    def build(self):
       
        #Create database or connect to one
        conn = sqlite3.connect('first_db.db')

        #Create A Cursor
        c = conn.cursor()

        #Create a Table 
        c.execute("""CREATE TABLE  if not exists customers(name text)""")

        
        #Commit our changes
        conn.commit()

              
        #Close our connection 
        conn.close()    

    def submit(self):
        #Create database or connect to one
        conn = sqlite3.connect('first_db.db')

        #Create A Cursor
        c = conn.cursor()

       #Add A Record 
         #c.execute("INSERT INTO customers VALUES (:first)",
        #    {
        #        'first': self.root.ids.word_input.text,
        #    })   
        c.execute("INSERT INTO customers VALUES ('GEORGE')")
        
        #Add A little a message
        self.root.ids.etiqueta_1.text = f'{self.root.ids.entrada_1} Added'

        #Clear the input box
        self.root.ids.entrada_1 = ''

        #Commit our changes
        conn.commit()

        #Close our connection 
        conn.close()

    def show_records(self):
        #Create database or connect to one
        conn = sqlite3.connect('first_db.db')

        #Create A Cursor
        c = conn.cursor()

        #Grab Records from database 
        c.execute("SELECT * FROM customers") 
        Records = c.fetchall()
       
        word = ''
        # Loop thru records
        for Record in Records:
            word = f'{word}\n{Record}'
            self.root.ids.etiqueta_2.text = f'{word}'
        
        #Commit our changes
        conn.commit()

              
        #Close our connection 
        conn.close()    


app = FormularioApp()
app.run()