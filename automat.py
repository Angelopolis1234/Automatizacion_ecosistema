import pandas as pd
from utils import misc
from utils import dictionary as dc

files=misc.get_directories("input/leo")


def compare_array(value,array2):
    if value in array2:
        return True
    return False

def set_rows(df,col):
    aux=[]
    for i in range(len(df.index)):
        val=df.loc[i,col]
        aux.append(val)
    return aux

def set_empty(col,founds):
    total=0
    for i in founds: 
        if i[0] == True: 
            total=len(col[i[1]])
            break
    count=0
    for i in founds: 
        if i[0] == False:
            if count==0: 
                col[i[1]]=[0 for _ in range(total)] 
            else:
                col[i[1]]=['' for _ in range(total)] 
        count+=1
                
    return col
def set_value(table,df,new_table):
    col={}
    ini=""
    found=False
    foundcol=[]
    for i in dc.database_dict[table]:
        auxb=[False,i]
        col[i]=[]
        ini=i
        for a in dc.database_dict[table][i]:
            if compare_array(a,df.columns):
                col[i]=set_rows(df,a)
                found=True
                auxb=[True,i]
        foundcol.append(auxb)
    if found==True:
        col=set_empty(col,foundcol)
        for a in range(len(col[ini])):
            aux=[]
            for dic in col: 
                aux.append(col[dic][a])
            if aux!=[] and aux not in new_table: new_table.append(aux)
    return new_table
        

for t in dc.tables:
    table=[]
    for f in files:
        df=misc.read_excel(f)
        table=set_value(t[0],df,table)

    misc.create_excel(f"output/{t[0]}.xlsx",sorted(table, key=lambda tab: tab[0]),dc.database_dict[t[0]])