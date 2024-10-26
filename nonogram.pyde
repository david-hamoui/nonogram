page = "menu"
reload = True
m = 0
tick = 0
mapping = []
cMapping = []
ccMapping = []
tips = []


def setup():
    size(800,800)
    background(255)
    rectMode(CENTER)
    textAlign(CENTER)
    textFont(createFont("arial",30))
    


def draw():
    global tick
    
    if page == "play":
        play()
    elif page == "menu":
        menu()
    

    tick+=1


def play():
    global reload,page,mapping,tips,cMapping,ccMapping
    
    if reload:
        background(255)
        
        if m == 10:
            s = 50
        elif m == 15:
            s = 33.33
        
        for x in range(m):
            for y in range(m):
                j = button2(150+x*s,150+y*s,s,s,cMapping[x+y+x*(m-1)])
                if j == "t":
                    cMapping[x+y+x*(m-1)] = "t"
                elif j == "f":
                    cMapping[x+y+x*(m-1)] = "f"
                elif j == "b":
                    cMapping[x+y+x*(m-1)] = "b"
                
        #rectMode(CENTER)
        
        reload = True
        
        textSize(10)
        fill(0)
    
        for x in range(m):
            p=50
            for num in tips[x]:
                if num != 0:
                    text(num,150+x*s,p)
                    p+=15
        
        for y in range(m):
            p=50
            for num in tips[y+m]:
                if num != 0:
                    text(num,p,150+y*s)
                    p+=15
        textSize(30)
    
    if button1(50,50,50,50):
        page = "menu"
        mapping = []
        cMapping = []
        tips = []
    
    if button1(650,750,200,50):
        ccMapping = list(cMapping)
        
        for i in range(m*m):
        
            if ccMapping[i] == "b":
                ccMapping[i] = "f"

        if ccMapping == mapping:
            correct()
        else:
            wrong()
        
        ccMapping = []
    
    fill(0)
    text("Check",650,760)


def menu():
    global reload,page,m
    
    if reload:
        background(255)
        fill(0)
        text("Menu",400,200)
        reload = False
    
    
    if button1(400,310,200,50):
        m = 10
        page = "play"
        mapDrawing()
    if button1(400,380,200,50):
        m = 15
        page = "play"
        mapDrawing()
        
    fill(0)
    text("10x10",400,320)
    text("15x15",400,390)
    

def mapDrawing():
    global mapping,tips,cMapping

    for i in range(m*m):
        cMapping.append("f")
    
    for i in range(m*m):
        if random(1) > 0.8:
            mapping.append("f")
        else:
            mapping.append("t")
    
    
    for i in range(m*2):
        tips.append([0])
    
    
    for x in range(m):
        n=0
        
        for y in range(m):
            if mapping[x+y+x*(m-1)] == "t":
                tips[x][n] += 1
            elif mapping[x+y+x*(m-1)] == "f":
                tips[x].append(0)
                n+=1
    
    for y in range(m):
        n=0
        
        for x in range(m):
            if mapping[x+y+x*(m-1)] == "t":
                tips[m+y][n] += 1
            elif mapping[x+y+x*(m-1)] == "f":
                tips[m+y].append(0)
                n+=1
    
    


def button1(xpos,ypos,xsize,ysize):
    global tick,reload
    
    fill(255)
    stroke(255)
    rect(xpos,ypos,xsize,ysize,8)
    
    if xpos-xsize/2 < mouseX < xpos+xsize/2 and ypos-ysize/2 < mouseY < ypos+ysize/2:
        fill(180)
        if mousePressed and tick > 40:
            tick = 0
            reload = True
            return True
    else:
        fill(230)
    stroke(0)
    rect(xpos,ypos,xsize,ysize,8)
    

def button2(xpos,ypos,xsize,ysize,situation):
    global tick,reload
    
    fill(255)
    stroke(255)
    rect(xpos,ypos,xsize,ysize)
    
    if tick > 20 and mousePressed and xpos-xsize/2 < mouseX < xpos+xsize/2 and ypos-ysize/2 < mouseY < ypos+ysize/2:
        tick = 0
        reload = True
        if keyPressed:
            return "b"
        elif situation == "f":
            return "t"
        else:
            return "f"    
        
    else:
        if situation == "t":
            fill(20,10,93)
        elif situation == "f":
            fill(255)
        else:
            fill(200,30,30)
    stroke(0)
    rect(xpos,ypos,xsize,ysize)
    

def correct():
    global tick
    
    tick = 50
    textSize(70)
    fill(50,230,50)
    text("Correct!",400,400)
    
def wrong():
    global tick
    
    tick = 50
    textSize(70)
    fill(230,50,50)
    text("Wrong!",400,400)
    
