
"""Girma Dingeto, CSD325-300O, Module 10-2 Assignment"""

import tkinter as tk
import tkinter.messagebox as msg

class Todowindow(tk.Tk):
    def __init__(self,tasks=None):
        super().__init__()

        if not tasks:
            self.tasks=[]

        else:
            self.tasks=tasks

       
        #1. Change the Title to Lastname-ToDo

        self.title("Dingeto-ToDo") 
        self.geometry("300x400")
        #2. Add Menu Bar with complementary colors and Exit functionality
        self.menu=tk.Menu(self,bg="navy",fg="white") #Navy/white as complementery colors
        self.config(menu=self.menu)

        self.file_menu= tk.Menu(self.menu, tearoff=0, bg="ivory",fg="black")
        self.menu.add_cascade(label="File",menu=self.file_menu)

        #5. Add File - Exit menu item
        self.file_menu.add_command(label="Exit", command=self.quit)

        #4. Provide instructions in the label
        self.label=tk.Label(self,text="Right-Click a task to delete it",pady=10)
        self.label.pack

        self.tasks_canvas=tk.Canvas(self)

        self.tasks_frame=tk.Frame(self.tasks_canvas)
        self.text_frame=tk.Frame(self)


        self.scrollbar=tk.Scrollbar(self,orient="vertical",command=self. tasks_canvas.yview)

        self.tasks_canvas.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=tk.RIGHT,fill=tk.Y)



        self.task_create=tk.Text(self.text_frame,height=3,bg="white",fg="black")

        self.tasks_canvas.pack(side="right",fill="both",expand=True)

        self.canvas_frame=self.tasks_canvas.create_window((0,0),window=self.
            tasks_frame,anchor="nw")

    

        self.task_entry=tk.Entry(self)
        self.task_entry.pack(fill="x")
        self.task_entry.bind("<Return>", self.add_task)
    

        

        todo1=tk.Label(self.tasks_frame,text="Add---** Right-Click a task to delete **",bg="slateblue1",
            fg="black",relief="raised",bd=8,padx=10,font=('Arial',10,'bold'))
        todo1.bind("<Button-3>",self.remove_task)

        self.tasks.append(todo1)

        for task in self.tasks:
            task.pack(side=tk.TOP,fill=tk.X)

        self.bind("<Return>",self.add_task)
        self.bind("<Configure>",self.on_frame_configure)
        self.bind_all("<MouseWheel>",self.mouse_scroll)
        self.bind_all("<Button-4>",self.mouse_scroll)
        self.bind_all("<Button-5>",self.mouse_scroll)
        self.tasks_canvas.bind("<Configure>",self.task_width)

        self.colour_schemes=[{"bg":"lightgrey","fg":"black"},{"bg":"grey","fg":" white"}]

        todo2=tk.Label(self.tasks_frame,text="---Grade 325 Discussion board---",bg="gold2",
            fg="black",relief="raised",bd=8,font=('Arial',10,'bold'),pady=10,padx=10)
        todo2.bind("<Button-3>",self.remove_task)

        self.tasks.append(todo2)

        for task in self.tasks:
            task.pack(side=tk.TOP,fill=tk.X)

        self.bind("<Return>",self.add_task)
        self.bind("<Configure>",self.on_frame_configure)
        self.bind_all("<MouseWheel>",self.mouse_scroll)
        self.bind_all("<Button-4>",self.mouse_scroll)
        self.bind_all("<Button-5>",self.mouse_scroll)
        self.tasks_canvas.bind("<Configure>",self.task_width)

        self.colour_schemes=[{"bg":"lightgrey","fg":"black"},{"bg":"grey","fg":" white"}]

       
        todo3=tk.Label(self.tasks_frame,text="---Grade 325 Tkinter program---",bg="slateblue1",
            fg="black",relief="raised",bd=8,font=('Arial',10,'bold'),pady=10,padx=10)
        todo3.bind("<Button-3>",self.remove_task)

        self.tasks.append(todo3)

        for task in self.tasks:
            task.pack(side=tk.TOP,fill=tk.X)

        self.bind("<Return>",self.add_task)
        self.bind("<Configure>",self.on_frame_configure)
        self.bind_all("<MouseWheel>",self.mouse_scroll)
        self.bind_all("<Button-4>",self.mouse_scroll)
        self.bind_all("<Button-5>",self.mouse_scroll)
        self.tasks_canvas.bind("<Configure>",self.task_width)

        self.colour_schemes=[{"bg":"lightgrey","fg":"black"},{"bg":"grey","fg":" white"}]


    
    def add_task(self,event=None):
        task_text=self.task_entry.get()

        if len(task_text)>0:
            new_task=tk.Label(self.tasks_frame,text=task_text,pady=5)

            new_task.pack(fill="x")
            # 3. Change left-click(<Button-1>) to right-click (<Button-3>)
            new_task.bind("<Button-3>" ,self.remove_task)

            self.task_entry.delete(0,tk.END)
            self.tasks_frame.update_idletasks
            self.tasks_canvas.configure(scrollregion=self.tasks_canvas.bbox("all"))
            
            self.set_task_colour(len(self.tasks),new_task)

            new_task.bind("<Button-3>",self.remove_task)
            new_task.pack(side=tk.TOP,fill=tk.X)

            self.tasks.append(new_task)

        self.task_create.delete(1.0,tk.END)

    def remove_task(self,event):
       event.widget.destroy()
       self.tasks_frame.update_idletasks()
       self.tasks_canvas.configure(scrollregion=self.tasks_canvas.bbox())
       task=event.widget
       if msg.askyesno("Really Delete?","Delete"+task.cget("text")+"?"):
            self.tasks.remove(event.widget)
            event.widget.destroy()
            self.recolour_tasks()

    def recolour_tasks(self):
        for index,task in enumerate(self.tasks):
            self.set_task_colour(index,task)

    def set_task_colour(self,position,task):
        _,task_style_choice=divmod(position,2)

        my_scheme_choice=self.colour_schemes[task_style_choice]

        task.configure(bg=my_scheme_choice["bg"])
        task.configure(fg=my_scheme_choice["fg"])

    def on_frame_configure(self,event=None):
        self.tasks_canvas.configure(scrollregion=self.tasks_canvas.bbox("all"))

    def task_width(self,event):
        canvas_width=event.width
        self.tasks_canvas.itemconfig(self.canvas_frame,width=canvas_width)

    def mouse_scroll(self,event):
        if event.delta:
            self.tasks_canvas.yview_scroll(int(-1*(event.delta/120)),"units")
        else:
            if event.num==5:
                move=1
            else:
                move=-1

                self.tasks_canvas.yview_scroll(move,"units")

if __name__=="__main__":
    todo=Todowindow()
    todo.mainloop()
