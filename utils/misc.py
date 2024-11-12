import os  
import openpyxl
import pandas as pd

def get_directories(path="",current=[]):
    contenido = os.listdir(path)
    if contenido!=[]:
        for c in contenido:
            if "." not in c:
                new_p=path+"/"+c
                current=get_directories(new_p,current)
            else:
                current.append(path+"/"+c)
    return current

def read_excel(file,sheet=0):
    df = pd.read_excel(file,sheet_name=sheet)
    columns=df.columns
    col=len(df.columns)
    rows=len(df.index)
    start=0
    names=[]
    main_c=0
    for j in columns:
        if str(j) not in ["nan","None",None,""]:
            main_c+=1
            names.append(j)
    if main_c*100/col<=90:
        for i in range(0,rows):
            main_c=0
            names=[]
            for j in columns:
                if str(df.loc[i,j])!="nan" and str(df.loc[i,j])!="None" and df.loc[i,j]!=None and str(df.loc[i,j])!="":
                    main_c+=1
                    names.append(df.loc[i,j])
            if main_c*100/col>=90:
                start=i
                break
        df.drop(df.index[:start+1],inplace=True)
        df.reset_index(drop=True,inplace=True)

    df.columns=check_duplicated_col(names)
    return df

def check_duplicated_col(columns):
    for col in columns:
        pos=0
        pos_a=[]
        for aux in columns:
            if col==aux:
                pos_a.append(pos)
            pos+=1
        if len(pos_a)==2:
            for i in pos_a:
                if i>0:
                    columns[i]=f'{columns[i-1]}{columns[i]}'
                else:
                    columns[i]=f'{columns[i]}{columns[i+1]}'
                    
    return columns


def create_excel(path,data,columns):
    wb = openpyxl.Workbook()

    hoja = wb.active
    # Crea la fila del encabezado con los títulos
    hoja.append((c for c in columns))
    for producto in data:
        hoja.append((p for p in producto))
    wb.save(path)