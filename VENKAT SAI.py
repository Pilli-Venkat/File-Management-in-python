''' This is done by Venkat '''

print('''       HEALTH MANAGEMENT SYSTEM
       INSTRUCTION : Input should be given in integers( example : 1,2,3,4...)

      ''')

from datetime import datetime

present_time = datetime.now()



def choose():
    person = (int(input('''
          Who are you ?
          1.Clint
          2.Loki
          3.New User
          4.Quit
          ''')))
    if person == 1:
        print("Welcome,Clint")
        d1 = open("clintd.txt", "a+")
        e1 = open("clinte.txt", "a+")
        file(d1, e1)


    elif person == 2:
        print("Welcome,Loki")
        d2 = open("lokid.txt", "a+")
        e2 = open("lokie.txt", "a+")
        file(d2, e2)
    elif person == 3:
        new = input("What is your good name ? ")
        print("Welcome,", new)
        d = open(f"{new}d.txt", "a+")
        e = open(f"{new}e.txt", "a+")
        file(d, e)
    elif person == 4:
      pass

    else:
        choose()


def add(p):
    task = input("What you want to add ? ")
    t = "\n"+str(present_time)+"  : "+task+"\n"
    p.write(t)


def read(p):

    p.seek(0)
    print(p.read())



def file(p, q):
    f = int(input("Diet(1) or Exercise(2) or Go back(3)  "))
    if f == 1:
        do = int(input(('''
              1.ADD
              2.READ
              3.QUIT
             ''')))
        if do == 1:
            add(p)
            
            filee(p,q,f)
        elif do == 2:
           read(p)
           filee(p,q,f)
        elif do == 3:
            return file(p,q)
    if f == 2:
        do = int(input(('''
              1.ADD
              2.READ
              3.QUIT
             ''')))
        if do == 1:
            add(q)
            filee(p,q,f)
        elif do == 2:
           read(q)
           filee(p,q,f)
        elif do == 3:
            return file(p,q)
    if f==3:
       return choose()       
def filee(p,q,f):
  
   if f == 1:
        do = int(input(('''
              1.ADD
              2.READ
              3.QUIT
             ''')))
        if do == 1:
            add(p)
            
            filee(p,q,f)
        elif do == 2:
           read(p)
           filee(p,q,f)
        elif do == 3:
            return file(p,q)
   if f == 2:
        do = int(input(('''
              1.ADD
              2.READ
              3.QUIT
             ''')))
        if do == 1:
            add(q)
            filee(p,q,f)
        elif do == 2:
           read(q)
           filee(p,q)
        elif do == 3:
            return file(p,q,f)
   if f==3:
       return choose()     
choose()
