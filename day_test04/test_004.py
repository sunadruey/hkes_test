import  os
os.mkdir('testdir')
print(os.listdir('./'))
os.removedirs('testdir')
os.getcwd()
if not os.path.exists("b"):
    os.mkdir('b')
if not os.path.exists("b/test.txt"):
   f= open("b/test.txt","w")
   f.write("hello,os using")
   f.close()
