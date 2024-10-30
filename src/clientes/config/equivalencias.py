

class equivalencias:
    def __init__(self) -> None:
        '''
        Initial configuration for the complete equivalences for the files. It's following the down below structure:
            self.client = {
                "destination_table" : ["original_file", "original_field", "destination_field"]
            }
        '''
        
        #Client leo
        self.leo = {
            'viajes': [
                ['serviciostmp', 'No.','viaje'],
                ['serviciostmp', 'VEHÍCULO', 'unidad'],
                ['serviciostmp', 'OPERADOR', 'operador'],
                ['serviciostmp', 'FECHA VIAJE', 'fecha_salida'],
                ['serviciostmp', 'FECHA CIERRE', 'fecha_recuperacion'],
                ['serviciostmp', 'KMS. VACIOS', 'km_vacio'],
                ['serviciostmp', 'KMS. TOTALES', 'km_cargado'], #It must be extracted the empty km.
                ['serviciostmp', 'TOTAL', 'liquidacion'],
                ['serviciostmp','CLIENTE','cliente']
            ],
            'facturas':[
                ['serviciostmp', 'FOLIO FACTURA', 'factura'],
                ['serviciostmp', 'TOTAL', 'total_facturado'],
                ['serviciostmp', 'FECHA COBRO', 'fecha_cobro'],
                ['serviciostmp', 'TBD', 'saldo'] #To be determinate the logic or the field to be extracted.
            ]
        } 

        #Client ticarsa
        self.ticarsa={
            'cliente':'cliente'
        }
    
    def get_leo(self) -> None:
        return self.leo