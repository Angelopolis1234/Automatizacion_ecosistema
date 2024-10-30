
from clientes.config import equivalencias
from clientes import get_info

equivalencias = equivalencias.equivalencias()
get_info = get_info.gral()

class leo:
    def __init__(self, diesel_report:str='clientes/clientes_ecosistema/leo/Reporte_Diesel.xlsx', serviciostmp:str='clientes/clientes_ecosistema/leo/Serviciostmp.xlsx') -> None:
        '''
            Initial configuration, if no one file was provided the program will take the following routes:
                * diesel report: clientes/clientes_ecosistema/leo/Reporte_Diesel.xlsx
                * serviciostmp: clientes/clientes_ecosistema/leo/Serviciostmp.xlsx
        '''

        #Get each file and transform all the data
        diesel_report = get_info.get_data('clientes/clientes_ecosistema/leo/Reporte_Diesel.xlsx')
        serviciostmp = get_info.get_data('clientes/clientes_ecosistema/leo/Serviciostmp.xlsx')

        #Asign the data to basic dictionary to be used with the equivalences
        self.data = {
            'serviciostmp' : serviciostmp,
            'diesel_report' : diesel_report
        }

    
    def create_files(self, path:str='archivos_salida') -> None:
        '''
            This method generate all the files to be uploaded in google
            Params:
                *path: Is the path for the file.
                    -default: archivos_salida/leo/viajes.xlsx
        '''
        self.create_viajes_file(path)


    def create_viajes_file(self, path:str='archivos_salida') -> bool:
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
            aux_df = self.data['serviciostmp'][aux[0]]
            aux_df.rename(columns=aux[1], inplace=True)
            minus0 = 0
            
            for i in range(len(aux_df['km_cargado'])):
                aux_df.loc[i,'km_cargado'] = aux_df.loc[i,'km_cargado'] - aux_df.loc[i,'km_vacio']
                if aux_df.loc[i,'km_cargado'] < 0:
                    print(aux_df.loc[i])
                    minus0 += 1
            
            print(aux_df)#Auxiliar, to be erased
            print(minus0)#Auxiliar, to be erased

            aux_df.to_excel(path, index=False)
            return True
        except Exception as error:
            print('An error happened: ' + error)
            return False

    def create_facturas_file(self, path:str='archivos_salida'):
        pass

    
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
            crafting.append(element[1])
            new_names[element[1]] = element[2]
        
        return crafting, new_names