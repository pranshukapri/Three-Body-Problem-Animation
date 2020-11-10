GlowScript 3.0 VPython

scene.height = 0
scene.background = color.white

running = 0
restart = 0
G=6.67e-11
dt = 1e4
srate = 0
R1, R2, R3 = 0.1, 0.1, 0.1
M1, M2, M3 = 1.5e10, 1.5e10, 1.5e10
i1, j1, k1 = -1, 0, 0
i2, j2, k2 = 1, 0, 0
i3, j3, k3 = 0, 0, 0
i4, j4, k4 = 0.347113, 0.532727, 0
i5, j5, k5 = 0.347113, 0.532727, 0
i6, j6, k6 = -0.694226, -1.065454, 0

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
  global initial_srate
  srate = sl.value * initial_srate
  ratevalue.text = '{:1.2f}'.format(s.value)
  
def cal_vdt():
  global G
  global dt
  global i1,i2,i3,i4,i5,i6,j1,j2,j3,j4,j5,j6,k1,k2,k3,k4,k5,k6,M1,M2,M3,R1,R2,R3
  dt = 1e4
  
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
  
  a1 = (f21-f13)/M1
  a2 = (-f21-f23)/M2
  a3 = (f13+f23)/M3
  
  while 1:
    #print(mag(vt1)," ",mag(vt2)," ",mag(vt3)," ")
    
    dr1 = v1*dt + a1*dt**2
    dr2 = v2*dt + a2*dt**2
    dr3 = v3*dt + a3*dt**2
    #print(dt," ",vdt)
    dr = max(mag(dr1),mag(dr2),mag(dr3))
    
    if((Rmax/dr)>=1000 & (Rmax/dr)<=10000):
      break
    dt = dt/1.01
  
  return (Rmax/dr)
  
def user_inputs():
  global i1,i2,i3,i4,i5,i6,j1,j2,j3,j4,j5,j6,k1,k2,k3,k4,k5,k6,M1,M2,M3,R1,R2,R3
  
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
  
def initial_conds(m):
  global i1,i2,i3,i4,i5,i6,j1,j2,j3,j4,j5,j6,k1,k2,k3,k4,k5,k6,M1,M2,M3,R1,R2,R3
  choice = m.selected
  
  if choice == "Figure 8":
    R1, R2, R3 = 0.1, 0.1, 0.1
    M1, M2, M3 = 1.5e10, 1.5e10, 1.5e10
    i1, j1, k1 = -1, 0, 0
    i2, j2, k2 = 1, 0, 0
    i3, j3, k3 = 0, 0, 0
    i4, j4, k4 = 0.347113, 0.532727, 0
    i5, j5, k5 = 0.347113, 0.532727, 0
    i6, j6, k6 = -0.694226, -1.065454, 0
    
  elif choice == "2":
    R1, R2, R3 = 0.1, 0.1, 0.1
    M1, M2, M3 = 1.5e10, 1.5e10, 1.5e10
    i1, j1, k1 = -1, 0, 0
    i2, j2, k2 = 1, 0, 0
    i3, j3, k3 = 0, 0, 0
    i4, j4, k4 = 0.405916, 0.230163, 0
    i5, j5, k5 = 0.405916, 0.230163, 0
    i6, j6, k6 = -0.811832, -0.460326, 0
  
  elif choice == "3":
    R1, R2, R3 = 0.1, 0.1, 0.1
    M1, M2, M3 = 1.5e10, 1.5e10, 1.5e10
    i1, j1, k1 = -1, 0, 0
    i2, j2, k2 = 1, 0, 0
    i3, j3, k3 = 0, 0, 0
    i4, j4, k4 = 0.306893, 0.125507, 0
    i5, j5, k5 = 0.306893, 0.125507, 0
    i6, j6, k6 = -0.613786, -0.251014, 0

  elif choice == "Moth":
    R1, R2, R3 = 0.1, 0.1, 0.1
    M1, M2, M3 = 1.5e10, 1.5e10, 7.5e9
    i1, j1, k1 = -1, 0, 0
    i2, j2, k2 = 1, 0, 0
    i3, j3, k3 = 0, 0, 0
    i4, j4, k4 = 0.2374365149, 0.2536896353, 0
    i5, j5, k5 = 0.2374365149, 0.2536896353, 0
    i6, j6, k6 = -0.9497460596, -1.0147585412, 0

  elif choice == "5":
    R1, R2, R3 = 1, 1, 1
    M1, M2, M3 = 1.5e12, 1.5e12, 1.5e12
    i1, j1, k1 = 4, 6, 6
    i2, j2, k2 = 8, 8, 3
    i3, j3, k3 = -3, -2, 0
    i4, j4, k4 = -2, 2, -2
    i5, j5, k5 = 2, -5, 1
    i6, j6, k6 = 0, 3, 1

  elif choice == "6":
    R1, R2, R3 = 1, 1, 1
    M1, M2, M3 = 1.49925037e12, 1.49925037e12, 1.49925037e12
    i1, j1, k1 = 1, 2, 3
    i2, j2, k2 = 5, 4, 0
    i3, j3, k3 = -6, -6, -3
    i4, j4, k4 = -2, 2, -2
    i5, j5, k5 = 2, -5, 1
    i6, j6, k6 = -2, 3, 1 

  elif choice == "Free Bodies":
    R1, R2, R3 = 0.1, 0.1, 0.1
    M1, M2, M3 = 1e12, 1e12, 1e12
    i1, j1, k1 = 1, 0, 0
    i2, j2, k2 = 0, 1, 0
    i3, j3, k3 = 0, 0, 1
    i4, j4, k4 = 0, 0, 0
    i5, j5, k5 = 0, 0, 0
    i6, j6, k6 = 0, 0, 0
    
  elif choice == "User Defined":
    user_inputs()
  
  initial_srate = cal_vdt()/10
  #print(initial_srate)
  #print(dt)
  Rerun()

wtext(text='Initial Conditions : ', pos=scene.title_anchor)
menu(choices=['Figure 8', '2', '3', 'Moth', '5', '6' , 'Free Bodies' , 'User Defined'], pos=scene.title_anchor, index=0, bind=initial_conds)
wtext(text='   ', pos=scene.title_anchor)

button(text="Play", pos=scene.title_anchor, bind=Run)
button(text="Restart", pos=scene.title_anchor, bind=Rerun)

initial_srate = cal_vdt()/10
#print(srate)
#print(dt)

wtext(text='\nAnimation Speed', pos=scene.title_anchor)

sl = slider(min=0.1, max=10, value=1, pos=scene.title_anchor, bind=Slider, top = 10)
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

  #print(dt)
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
    
    #calculate grav force on star 1 due to 2
      F21 = G*sun1.m*sun2.m*(r12)/mag(r12)**3
    #calculate the force on star3 due to star 1
      F13 = -G*sun1.m*sun3.m*(r13)/mag(r13)**3
    #calculate the force on planet due to star 2
      F23 = -G*sun2.m*sun3.m*(r23)/mag(r23)**3
    
      a1 = (F21-F13)/sun1.m
      a2 = (-F21-F23)/sun2.m
      a3 = (F13+F23)/sun3.m
    
      vr12 = dot(sun1.v,r12/mag(r12)) * r12/mag(r12)
      vr13 = dot(sun1.v,r13/mag(r13)) * r13/mag(r13)
      vr21 = dot(sun2.v,r12/mag(r12)) * r12/mag(r12)
      vr23 = dot(sun2.v,r23/mag(r23)) * r23/mag(r23)
      vr31 = dot(sun3.v,r13/mag(r13)) * r13/mag(r13)
      vr32 = dot(sun3.v,r23/mag(r23)) * r23/mag(r23)
      
      ar12 = dot(a1,r12/mag(r12)) * r12/mag(r12)
      ar13 = dot(a1,r13/mag(r13)) * r13/mag(r13)
      ar21 = dot(a2,r12/mag(r12)) * r12/mag(r12)
      ar23 = dot(a2,r23/mag(r23)) * r23/mag(r23)
      ar31 = dot(a3,r13/mag(r13)) * r13/mag(r13)
      ar32 = dot(a3,r23/mag(r23)) * r23/mag(r23)
      
      if mag(r12) <= (R1+R2):
        if mag(vr12) < mag(ar12)*dt or mag(vr21) < mag(ar21)*dt:
          sun1.v = sun1.v - vr12
          sun2.v = sun2.v - vr21
          a1 = a1 - ar12
          a2 = a2 - ar21
        else:
          p=(sun1.v-sun2.v)
          r=(2*(sun1.m*sun2.m)*dot(p,norm(r12)))/(sun2.m+sun1.m)
          sun1.v=sun1.v-((r*norm(r12))/sun1.m)
          sun2.v=sun2.v+((r*norm(r12))/sun2.m)
       
      if mag(r23) <= (R2+R3):
        if mag(vr23) < mag(ar23)*dt or mag(vr32) < mag(ar32)*dt:
          sun2.v = sun2.v - vr23
          sun3.v = sun3.v - vr32
          a2 = a2 - ar23
          a3 = a3 - ar32
        else:
          p=(sun2.v-sun3.v)
          r=(2*(sun2.m*sun3.m)*dot(p,norm(r23)))/(sun2.m+sun3.m)
          sun2.v=sun2.v-((r*norm(r23))/sun2.m)
          sun3.v=sun3.v+((r*norm(r23))/sun3.m)
       
      if mag(r13) <= (R1+R3):
        if mag(vr13) < mag(ar13)*dt or mag(vr31) < mag(ar31)*dt:
          sun1.v = sun1.v - vr13
          sun3.v = sun3.v - vr31
          a1 = a1 - ar13
          a3 = a3 - ar31
        else:
          p=(sun1.v-sun3.v)
          r=(2*(sun1.m*sun3.m)*dot(p,norm(r13)))/(sun3.m+sun1.m)
          sun1.v=sun1.v-((r*norm(r13))/sun1.m)
          sun3.v=sun3.v+((r*norm(r13))/sun3.m)
      
    #update position
      sun1.pos = sun1.pos + sun1.v*dt + a1*dt**2
      sun2.pos = sun2.pos + sun2.v*dt + a2*dt**2
      sun3.pos = sun3.pos + sun3.v*dt + a3*dt**2
      
    #update velocities    
      sun1.v = sun1.v + a1*dt
      sun2.v = sun2.v + a2*dt
      sun3.v = sun3.v + a3*dt
      
      #print(mag(r12),mag(r23),mag(r13),dot(sun1.v,r12)*dt,dot(sun2.v,r12)*dt,mag(a2*dt*dt),mag(a3*dt*dt))      
      
      #print(dt,dr,Rmax)