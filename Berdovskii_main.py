from PIL import Image,ImageDraw,ImageFont, ImageTk
import tkinter as tk

class GraphDrawer:
    node_width = 10
    node_width_space = 20
    node_height_space = 40
    node_height = 10
    pic_width = 800
    pic_height = 800
    draw_step = 0
    last_drawed_line = None
    def find_max_depth(self):
        #BFS implementation for graph depth search
        used = [False for i in range(self.tree_size)]
        deep = [0 for i in range(self.tree_size)]
        layer_size = [0 for i in range(self.tree_size)]
        stack = []
        stack.append(0)
        used[0]=True
        while not len(stack)==0:
            x = stack[-1]
            layer_size[deep[x]]+=1
            used[x]=True
            stack.pop(-1)
            for i in self.graph[x]:
                if not used[i]:
                    stack.append(i)
                    deep[i]=deep[x]+1
        return max(deep),max(layer_size)


    def __init__(self,sequence):
        # start initialization
        self.sequence = list(sequence)
        self.tree_size = len(self.sequence) + 2
        # the coordinates of the nodes in the figure
        self.node_coord = [[] for i in range(self.tree_size)]
        self.edge_order = []
        # image and draw instrument
        self.totalImage = Image.new('RGBA', (self.pic_width, self.pic_height))
        self.Drawer = ImageDraw.Draw(self.totalImage)
        self.Drawer.rectangle([(0, 0), (self.pic_width, self.pic_height)], fill='white')
        #decoding of the Prufer code
        num_range = [i + 1 for i in range(self.tree_size)]
        self.graph = [[] for i in range(self.tree_size)]
        for j in range(self.tree_size - 2):
            for i in range(len(num_range)):
                if not num_range[i] in self.sequence:
                    self.edge_order.append([self.sequence[0]-1,num_range[i]-1])
                    self.graph[self.sequence[0] - 1].append(num_range[i] - 1)
                    self.graph[num_range[i] - 1].append(self.sequence[0] - 1)
                    self.sequence.pop(0)
                    num_range.pop(i)
                    break

        self.edge_order.append([num_range[0]-1,num_range[1]-1])
        self.graph[num_range[0] - 1].append(num_range[1] - 1)
        self.graph[num_range[1] - 1].append(num_range[0] - 1)
        dep,wid = self.find_max_depth()
        self.node_height_space = self.pic_height/(dep+3)
        self.node_height = self.node_height_space/8
        self.node_width_space = self.pic_width/(3*wid+3)
        self.node_width = self.node_height
        self.font = ImageFont.truetype("FreeMono.ttf", int(self.node_height*0.9))
        self.layer_processing()


    def draw_one_step(self):
        if self.draw_step == len(self.edge_order):
            last_first_node = self.last_drawed_line[0]
            last_second_node = self.last_drawed_line[1]
            self.Drawer.line([self.node_coord[last_first_node], self.node_coord[last_second_node]], fill='blue', width=2)
            self.draw_node(self.node_coord[last_first_node],last_first_node+1)
            self.draw_node(self.node_coord[last_second_node],last_second_node+1)
        else:
            edge_for_draw = self.edge_order[self.draw_step]
            first_node = edge_for_draw[0]
            second_node = edge_for_draw[1]
            self.Drawer.line([self.node_coord[first_node], self.node_coord[second_node]], fill='red', width=2)
            if not self.last_drawed_line is None:
                last_first_node = self.last_drawed_line[0]
                last_second_node = self.last_drawed_line[1]
                self.Drawer.line([self.node_coord[last_first_node], self.node_coord[last_second_node]], fill='blue', width=2)
                self.draw_node(self.node_coord[last_first_node],last_first_node+1)
                self.draw_node(self.node_coord[last_second_node],last_second_node+1)
            self.draw_node(self.node_coord[first_node],first_node+1)
            self.draw_node(self.node_coord[second_node],second_node+1)
            self.last_drawed_line = edge_for_draw
            self.draw_step+=1


    #drow node by center coordinates
    def draw_node(self, xy,n=-1):
        x=xy[0]
        y=xy[1]
        self.Drawer.ellipse([(x-self.node_width/2, y-self.node_height/2),
                               (x + self.node_width / 2, y + self.node_height / 2)],fill='red',outline='black',width=2)
        if n != -1:
            self.Drawer.text((x+self.node_width/1.8,y-self.node_height/2),text=str(n),fill='black',font=self.font)
    #calculate node mid positions
    def layer_processing(self, n=2, last_drawed_layer=[0], drawed=set()):
        if drawed == set():
            self.node_coord[0]=(self.pic_width/2+self.node_width/2,self.node_height_space+self.node_height/2)
        layer_size=0
        drawed = drawed.union(set(last_drawed_layer))
        new_layer=[]
        for i in last_drawed_layer:
            layer_size +=len(set(self.graph[i]).difference(drawed))
        leftest = self.pic_width/2-(layer_size-1)/2*self.node_width_space
        for i in last_drawed_layer:
            for j in self.graph[i]:
                if(not j in drawed):
                    new_layer.append(j)
                    self.node_coord[j] = (leftest+self.node_width/2, n*self.node_height_space+self.node_height/2)
                    leftest+=self.node_width_space
        if len(new_layer)!=0:
            self.layer_processing(n+1,new_layer,drawed)


#initial whitescreen
x = GraphDrawer("")
#GUI implementation
root = tk.Tk()
img = ImageTk.PhotoImage(x.totalImage)
panel = tk.Label(root, image=img)
panel.grid(row=1,column=0,columnspan=5,rowspan=5)
def button_start():
    s = e1.get()
    for i in s:
        if not i.isdigit() and not i==' ':
            l1['text']="Unexpected symbols"
            return
    s = list(map(int,s.split(" ")))
    if min(s)<1 or max(s)>len(s)+2:
        l1['text'] = "Wrong sequence"
        return
    global x
    x = GraphDrawer(s)
    l1['text']="Enter the sequence"
    but1['state']="disable"
    but2['state']="normal"
    but3['state']="normal"


def button_step():
    but3['state']='disable'
    global x
    if (x.draw_step == len(x.edge_order)):
        but1['state'] = "normal"
        but2['state'] = "disable"
    x.draw_one_step()
    img2 = ImageTk.PhotoImage(x.totalImage)
    panel.configure(image=img2)
    panel.image = img2

def final():
    for i in range(len(x.edge_order)+1):
        button_step()
        but3['state'] = "disable"

but1 = tk.Button(root,text="Start",command=button_start)
but2 = tk.Button(root,text="Step",command=button_step,state="disable")
but3 = tk.Button(root,text="Final",command=final,state="disable")
e1 = tk.Entry(root)
l1 = tk.Label(root,text="Enter the sequence")
l1.grid(row=0,column=0)
e1.grid(row=0,column=1)
but1.grid(row=0,column=2)
but2.grid(row=0,column=3)
but3.grid(row=0,column=4)
root.mainloop()
