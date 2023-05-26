import re

def total_salary(path):

    fh = open(path, 'r')
    itog = float()
    res = ""
    while True:
        line = fh.readline()
        if not line:
            break
        res = res + line
    k = re.findall(r"[\d]+",res)
    for item in k:
        l = int(item)
        itog += l 
    fh.close()
    return itog

path = "D:/Github/git-home-work-06/test01.txt"
print(total_salary(path))
        
            
            
                
            
            
    
        
    
