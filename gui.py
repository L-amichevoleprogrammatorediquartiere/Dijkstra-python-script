from tkinter import *
import dijkstra

#variabili
array_entry_nodi=[] #cerchio, entry, x e y
array_entry_coll=[] #linea, xp  yp, xa  ya, Entry xe  ye

window=Tk()
window.geometry("800x800")

window.title("Dijkstra")

operation=StringVar()
insertNode=Radiobutton(window,text="insert node", 
                       value="insertNode",variable=operation)
insertNode.place(x=5,y=10)
deleteNode=Radiobutton(window,text="delete node", 
                       value="deleteNode",variable=operation)
deleteNode.place(x=5,y=40)
insertLine=Radiobutton(window,text="insert coll", 
                       value="insertColl",variable=operation)
insertLine.place(x=5, y=70)
deleteLine=Radiobutton(window,text="delete coll", 
                       value="deleteColl",variable=operation)
deleteLine.place(x=5, y=100)
selectNode=Radiobutton(window,text="select node->calculate", 
                       value="select",variable=operation)
selectNode.place(x=560,y=10)



tela=Canvas(window,width=800,height=800)
tela.place(x=0,y=140)

def select_nodo(x,y):
    for nodo in array_entry_nodi:
        if (nodo[2]> x-50 and nodo[2]< x+50) and (nodo[3]> y-50 and nodo[3]< y+50):
            return nodo[1].get()
    return None


def click_left(event):
    if operation.get() =="insertNode":     
        array_entry_nodi.append([tela.create_oval(event.x -50,event.y -50, event.x +50,event.y +50),
                                Entry(window,width=1),event.x,event.y])
        tela.create_window(event.x,event.y,window=array_entry_nodi[len(array_entry_nodi)-1][1])
    elif operation.get() =="deleteNode":
        for nodi in array_entry_nodi:
            if (nodi[2]> event.x-50 and nodi[2]< event.x+50) and (nodi[3]> event.y-50 and nodi[3]< event.y+50):
                nodi[1].destroy()
                tela.delete(nodi[0])
                array_entry_nodi.remove(nodi)
    elif operation.get() =="deleteColl":
        for coll in array_entry_coll:
            if(coll[6]> event.x-50 and coll[6]< event.x+50) and (coll[7]> event.y-50 and coll[7]< event.y+50):
                coll[5].destroy()
                tela.delete(coll[0])
                array_entry_coll.remove(coll)
    elif operation.get() =="select":
        found=BooleanVar()
        nodo_selected=IntVar()
        for nodo in array_entry_nodi:
            if (nodo[2]> event.x-50 and nodo[2]< event.x+50) and (nodo[3]> event.y-50 and nodo[3]< event.y+50):
                nodo_selected=nodo[1].get()[0]
                found=True
                break
        if(found):
            collegamenti_peso=[]
            #ora bisogna crare l'array collegamenti peso nodo a, nodo b e costo
            for coll in array_entry_coll:
                nodoA=select_nodo(coll[1],coll[2])
                nodoB=select_nodo(coll[3],coll[4])
                if nodoA !=None and nodoB !=None:
                    collegamenti_peso.append([nodoA,nodoB,int(coll[5].get())])
            dijkstra.calculate(collegamenti_peso,nodo_selected)

def drag_handler(event):
    if operation.get() =="insertColl":
        if not array_entry_coll: #la lista è vuota
            array_entry_coll.append([tela.create_line(event.x,event.y,event.x,event.y),
                                     event.x,event.y,event.x,event.y,Entry(window,width=2),event.x,event.y])
            tela.create_window(event.x,event.y,window=array_entry_coll[len(array_entry_coll)-1][5])
        else: #la lista non è vuota
            #verifico se sto finendo di fare la vecchia linea o una linea nuova
            index=len(array_entry_coll)-1
            #verifico se la posizione attuale è uguale con range di x e y di 10
            if((array_entry_coll[index][3]> event.x -50 and array_entry_coll[index][3]< event.x +50) and 
               (array_entry_coll[index][4]> event.y -50 and array_entry_coll[index][4]< event.y +50)): 
                tela.delete(array_entry_coll[index][0])
                array_entry_coll[index][5].destroy()
                oldPos=[array_entry_coll[index][1],array_entry_coll[index][2]]
                newPos=[oldPos[0],oldPos[1]]
                if(event.x<oldPos[0]):
                    newPos[0]=oldPos[0]-((oldPos[0]-event.x)/2)
                else:
                    newPos[0]=oldPos[0]+((event.x-oldPos[0])/2)
                
                if(event.y<oldPos[1]):
                    newPos[1]=oldPos[1]-((oldPos[1]-event.y)/2)
                else:
                    newPos[1]=oldPos[1]+((event.y-oldPos[1])/2)

                array_entry_coll[index]=[tela.create_line(oldPos[0],oldPos[1],event.x,event.y),oldPos[0],oldPos[1],
                                         event.x,event.y,Entry(window,width=2),newPos[0],newPos[1]]

                tela.create_window(newPos[0],newPos[1],window=array_entry_coll[len(array_entry_coll)-1][5])
            else:
                array_entry_coll.append([tela.create_line(event.x,event.y,event.x,event.y),
                                     event.x,event.y,event.x,event.y,Entry(window,width=2),event.x,event.y]) # xp yp, xa ya, Entry
                tela.create_window(event.x,event.y,window=array_entry_coll[len(array_entry_coll)-1][5])

tela.bind("<Button-1>",click_left)
tela.bind("<B1-Motion>",drag_handler)

window.mainloop()