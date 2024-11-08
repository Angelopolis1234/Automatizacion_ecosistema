

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
                ['ORIGEN', 'Origen ejemplo']
            ],
            'facturas':[
                ['FOLIO FACTURA', 'factura'],
                ['TOTAL_x', 'total_facturado'],
                ['FECHA COBRO', 'fecha_cobro'],
            ]
        } 

        #Client ticarsa
        self.ticarsa={
            'cliente':'cliente'
        }
    
    def get_leo(self) -> None:
        return self.leo