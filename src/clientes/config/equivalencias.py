

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
                ['No.','id_viaje'],
                ['OPERADOR', 'operador'],
                ['FECHA VIAJE_x', 'fecha_salida'],
                ['FECHA CIERRE', 'fecha_recuperacion'],
                ['KMS. RUTA', 'km_cargado'],
                ['KMS. VACIOS', 'km_vacio'],
                ['FOLIO LIQUIDACIÓN', 'liquidacion'],
                ['No.', 'id_pedido'],
                ['VEHÍCULO', 'ID_equipo'],
            ],
            'facturas':[
                ['FOLIO FACTURA', 'factura'],
                ['TOTAL_x', 'total_facturado'],
                ['FECHA COBRO', 'fecha_cobro'],
                ['FECHA ENVIO REVISION', 'fecha_revision'],
                ['No.', 'id_viaje']
            ],
            'liquidaciones': [
                ['FOLIO LIQUIDACIÓN', 'liquidacion'],
                ['COMISIÓN', 'sueldo_liquidado'],
                ['FECHA LIQUIDACIÓN','fecha_liquidacion'],
                ['No.', 'id_viaje']
            ],
            
        } 

        #Client ticarsa
        self.ticarsa={
            'cliente':'cliente'
        }
    
    def get_leo(self) -> None:
        return self.leo