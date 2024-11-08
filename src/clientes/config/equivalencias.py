

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
                ['No.','viaje'],
                ['VEHÍCULO', 'unidad'],
                ['OPERADOR', 'operador'],
                ['FECHA VIAJE', 'fecha_salida'],
                ['FECHA CIERRE', 'fecha_recuperacion'],
                ['KMS. VACIOS', 'km_vacio'],
                ['KMS. TOTALES', 'km_cargado'], #It must be extracted the empty km.
                ['TOTAL_x', 'liquidacion'],
                ['CLIENTE','cliente'],
                ['LITROS ASIGNADOS','ejemplo1'],
                ['ORIGEN', 'Origen ejemplo']
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