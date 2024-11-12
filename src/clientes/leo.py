
from clientes.config import equivalencias
from clientes import get_info
import pandas as pd

equivalencias = equivalencias.equivalencias()
get_info = get_info.gral()

class leo:
    def __init__(self, 
                 diesel_report:str='clientes/clientes_ecosistema/leo/Reporte_Diesel.xlsx', 
                 serviciostmp:str='clientes/clientes_ecosistema/leo/Serviciostmp.xlsx',
                 contrarecibo:str='clientes/clientes_ecosistema/leo/Contrarecibo.xlsx'
                 ) -> None:
        '''
            Initial configuration, if no one file was provided the program will take the following routes:
                * diesel report: clientes/clientes_ecosistema/leo/Reporte_Diesel.xlsx
                * serviciostmp: clientes/clientes_ecosistema/leo/Serviciostmp.xlsx
        '''

        #Get each file and transform all the data
        diesel_report = get_info.get_data('clientes/clientes_ecosistema/leo/Reporte_Diesel.xlsx')
        serviciostmp = get_info.get_data('clientes/clientes_ecosistema/leo/Serviciostmp.xlsx')
        contrarecibo = get_info.get_data(contrarecibo)

        #Asign the data to basic dictionary to be used with the equivalences
        self.data = pd.merge(serviciostmp,diesel_report, left_on='VEHÍCULO',right_on='N° ECONOMICO', how='left')
        self.data = self.data.drop_duplicates()
        self.data = pd.merge(self.data,contrarecibo, left_on='FOLIO FACTURA',right_on='FOLIO FACTURA', how='left')
        self.data = self.data.drop_duplicates()

        print(self.data)

    
    def create_files(self, path:str='archivos_salida') -> list:
        '''
            This method generate all the files to be uploaded in google
            Params:
                *path: Is the path for the file.
                    -default: archivos_salida/leo/viajes.xlsx
        '''
        #to_be_return = []
        #to_be_return.append(self.create_viajes_file(path))
        #to_be_return.append(self.create_facturas_file(path))
        #return self.create_all(path)
    
    def create_all(self, Path:str='archivos_salida') -> list:
        to_be_return = []
        for file in equivalencias.leo:
            print(file)
            try:
                path = f'{Path}/leo/{file}.xlsx'
                print(path)
                aux = self.craft_query(file)
                data = self.data[aux[0]]
                data.rename(columns=aux[1], inplace=True)

                
                
                data = self.data.drop_duplicates()
                data.to_excel(path, index=False)
                to_be_return.append([file,True])
            except Exception as error:
                print('An error happened: ' + str(error))
                to_be_return.append([file,False])
        return to_be_return


    def create_viajes_file(self, path:str='archivos_salida') -> list:
        '''
            This method create the viajes file and return a True if it has been created well.
            Params:
                *path: Is the path for the file.
                    -default: archivos_salida/leo/viajes.xlsx
            Return: True if the file has been created or False if the file has not been created.
        '''
        try:
            path = f'{path}/leo/viajes.xlsx'
            aux = self.craft_query('viajes')
            data = self.data[aux[0]]
            data.rename(columns=aux[1], inplace=True)

            for i in range(len(data['km_cargado'])):
                data.loc[i,'km_cargado'] = data.loc[i,'km_cargado'] - data.loc[i,'km_vacio']
            
            data = self.data.drop_duplicates()
            data.to_excel(path, index=False)
            return ['viajes',True]
        except Exception as error:
            print('An error happened: ' + str(error))
            return ['viajes',False]

    def create_facturas_file(self, path:str='archivos_salida'):
        try:
            path = f'{path}/leo/facturas.xlsx'
            aux = self.craft_query('facturas')
            data = self.data[aux[0]]
            data.rename(columns=aux[1], inplace=True)
            
            data = data.drop_duplicates()
            data.to_excel(path, index=False)
            return ['facturas',True]
        except Exception as error:
            print('An error happened: ' + str(error))
            return ['facturas',False]
    
    def craft_query(self, file:str) -> list:
        '''
            This method craft the query to get the complete info from the desired file to create the previus data to be export as a file
            Params:
                -file: The file to be created, do not have a default value
            Returns: Return a list type with the list to be passed as a param to get the info
        '''
        crafting = []
        new_names = {}
        for element in equivalencias.leo[file]:
            crafting.append(element[0])
            new_names[element[0]] = element[1]
        
        return crafting, new_names