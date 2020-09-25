GlowScript 3.0 VPython

scene.height = 0
scene.background = color.white

running = 0
restart = 0
G=6.67e-11
dt = 1e6

def Run(b):
    global running
    running = not running
    if running: b.text = "Pause"
    else: b.text = "Play"
    
def Rerun(b):
    global restart
    restart = not restart
    
def Slider(s):
    global srate
    srate = sl.value
    ratevalue.text = '{:1.2f}'.format(s.value)
    
def cal_vdt():
    global G
    global dt
    global i1,i2,i3,i4,i5,i6,j1,j2,j3,j4,j5,j6,k1,k2,k3,k4,k5,k6,M1,M2,M3
    #print(a)    
    v1 = vector(i4,j4,j4)
    v2 = vector(i5,j5,k5)
    v3 = vector(i6,j6,k6)
    
    R12 = vector(i2,j2,k2) - vector(i1,j1,k1)
    R23 = vector(i3,j3,k3) - vector(i2,j2,k2)
    R13 = vector(i3,j3,k3) - vector(i1,j1,k1)
    Rmax = max(mag(R12),mag(R23),mag(R13))
  
    f21=G*M1*M2*(R12)/mag(R12)**3
    f13=-G*M1*M3*(R13)/mag(R13)**3
    f23=-G*M2*M3*(R23)/mag(R23)**3
    
    while 1:
      vt1=v1+((f21-f13)/M1)*dt
      vt2=v2+((-f21-f23)/M2)*dt
      vt3=v3+((f13+f23)/M3)*dt
      #print(mag(vt1)," ",mag(vt2)," ",mag(vt3)," ")
      
      vdt = max(mag(vt1)*dt,mag(vt2)*dt,mag(vt3)*dt)
      #print(dt," ",vdt)
      
      if((Rmax/vdt)>=1000 & (Rmax/vdt)<=10000):
        break
      dt = dt/10
    
    return (Rmax/vdt)
    
button(text="Play", pos=scene.title_anchor, bind=Run)
button(text="Restart", pos=scene.title_anchor, bind=Rerun)

R1, R2, R3 = map(float,input("Enter Radii (R1 R2 R3):").split(' '))

M1, M2, M3 = map(float,input("Enter Masses (M1 M2 M3):").split(' '))

i1, j1, k1 = map(float,input("Enter Position of 1 (i j k):").split(' '))

while 1:
  i2, j2, k2 = map(float,input("Enter Position of 2 (i j k):").split(' '))
  if (mag(vector(float(i1),float(j1),float(k1)) - vector(float(i2),float(j2),float(k2))) >= R1+R2):
    break
while 1:
  i3, j3, k3 = map(float,input("Enter Position of 3 (i j k):").split(' '))
  if (mag(vector(float(i3),float(j3),float(k3)) - vector(float(i2),float(j2),float(k2))) >= R3+R2  &  mag(vector(float(i3),float(j3),float(k3)) - vector(float(i1),float(j1),float(k1))) >= R3+R1):
    break
  
i4, j4, k4 = map(float,input("Enter velocity of 1 (i j k):").split(' '))
i5, j5, k5 = map(float,input("Enter velocity of 2 (i j k):").split(' '))
i6, j6, k6 = map(float,input("Enter velocity of 3 (i j k):").split(' '))

srate = cal_vdt()/10
#print(srate)
#print(dt)

wtext(text='\nAnimation Speed', pos=scene.title_anchor)

sl = slider(min=srate/10, max=srate*10, value=srate, pos=scene.title_anchor, bind=Slider, top = 10)
ratevalue = wtext(text='{:1.2f}'.format(sl.value), pos=scene.title_anchor)

wtext(text='\n\n', pos=scene.title_anchor)

while 1:
  
  scene1 = canvas()
  scene1.background = color.white
  
  sun1=sphere(pos=(vector(float(i1),float(j1),float(k1))), radius=R1, color=color.yellow, make_trail=True, trail_radius=R1/12)
  sun2=sphere(pos=(vector(float(i2),float(j2),float(k2))), radius=R2, color=color.orange, make_trail=True, trail_radius=R2/12)
  sun3=sphere(pos=(vector(float(i3),float(j3),float(k3))), radius=R3, color=color.red, make_trail=True, trail_radius=R3/12)

  sun1.m=M1
  sun2.m=M2
  sun3.m=M3

  sun1.v=(vector(float(i4),float(j4),float(k4)))
  sun2.v=(vector(float(i5),float(j5),float(k5)))
  sun3.v=(vector(float(i6),float(j6),float(k6)))

  while 1:
    rate(srate)
    com = sphere(pos=(sun1.pos*M1 + sun2.pos*M2 + sun3.pos*M3)/(M1 + M2 + M3), radius = 0)
    scene1.camera.follow(com)
    
    if restart:
      scene1.delete()
      restart = 0
      break
    
    if running:  
    #vector from star 1 to 2
      r12=sun2.pos-sun1.pos
    #vector from star 1 to star 3
      r13=sun3.pos-sun1.pos
    #vector from star 2 to star 3
      r23=sun3.pos-sun2.pos
    
    #print(mag(r12),mag(r23),mag(r13))
    
      if mag(r12)<(R1+R2):
         p=(sun2.v-sun1.v)
         r=(2*(sun1.m+sun2.m)*dot(p,norm(r12)))/(sun2.m*sun1.m)
         sun1.v=sun1.v+((r*norm(r12))/sun1.m)
         sun2.v=sun2.v-((r*norm(r12))/sun2.m)
       
      if mag(r23)<(R2+R3):
         p=(sun3.v-sun2.v)
         r=(2*(sun2.m+sun3.m)*dot(p,norm(r23)))/(sun2.m*sun3.m)
         sun2.v=sun1.v+((r*norm(r23))/sun2.m)
         sun3.v=sun2.v-((r*norm(r23))/sun3.m)
       
      if mag(r13)<(R1+R3):
         p=(sun3.v-sun1.v)
         r=(2*sun1.m*sun3.m*dot(p,norm(r13)))/(sun3.m*sun1.m)
         sun1.v=sun1.v+((r*norm(r13))/sun1.m)
         sun3.v=sun3.v-((r*norm(r13))/sun3.m)
       
    #calculate grav force on star 1 due to 2
      F21=G*sun1.m*sun2.m*(r12)/mag(r12)**3
    
    #calculate the force on star3 due to star 1
      F13=-G*sun1.m*sun3.m*(r13)/mag(r13)**3
    
    #calculate the force on planet due to star 2
      F23=-G*sun2.m*sun3.m*(r23)/mag(r23)**3
    
    #update momentum (with total vector force)
      sun1.v=sun1.v+((F21-F13)/sun1.m)*dt
      sun2.v=sun2.v+((-F21-F23)/sun2.m)*dt
      sun3.v=sun3.v+((F13+F23)/sun3.m)*dt
    
    #update position
      sun1.pos=sun1.pos+sun1.v*dt
      sun2.pos=sun2.pos+sun2.v*dt
      sun3.pos=sun3.pos+sun3.v*dt