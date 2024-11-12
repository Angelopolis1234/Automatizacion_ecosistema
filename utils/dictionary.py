tables=[
    ["CLIENTES",1],
    ["DIVISIONES",1],
    ["SUPERVISORES",1],
    ["PROPIETARIOS",1],
    ["EQUIPOS",1],
    ["STATUS",1],
    ["OBJETIVOS_CLIENTES",2],
    ["RESPONSABLES_CLIENTES",2],
    ["OBJETIVOS_DIVISION",2],
    ["PEDIDOS",3],
    ["VIAJES",4],
    ["FACTURAS",5],
    ["LIQUIDACIONES",5],
    ["HISTORIAL_EQUIPO",5]
]

'''
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
'''


database_dict={
    "CLIENTES":{
        "id_cliente":["#Cte.", "Cliente","Cte."],
        "cliente":["#Cte.Nombre","Nombre"]
    },
    "OBJETIVOS_CLIENTES": {
        "objetivo_recuperacion":[], 
        "objetivo_revision":[], 
        "objetivo_cobro":[],
        "fecha_asignacion":[],
        "objetivos_clientes":[],
        "is_actual":[],
        "id_cliente":[]
    },
    "RESPONSABLES_CLIENTES":{
        "id_responsable":[],
        "responsable":[],
        "fecha_asignacion":[],
        "is_actual":[],
        "id_cliente":[]
    },
    "DIVISIONES":{
        "id_division":[],
        "division":["División"],
        "operacion":[]
    },
    "OBJETIVOS_DIVISION":{
        "objetivo_division":[],
        "objetivo_ingreso":[],
        "objetivo_sueldo":[], 
        "fecha_asignacion":[],
        "is_actual":[],
        "id_division":[]
    },
    "PEDIDOS":{
        "pedido":["NUMERO"],
        "fecha_cancelacion":[],
        "id_division":[],
        "id_cliente":["RAZON"] 
    },
    "VIAJES":{
        "id_viaje":["Guia",'No.'],
        "unidad":["Unidad"],
        "operador":["#Ope",'OPERADOR'],
        "fecha_salida":["Fecha",'FECHA VIAJE_x'],
        "fecha_recuperacion":['FECHA CIERRE'],
        "km_cargado":['KMS. RUTA'],
        "km_vacio":['KMS. VACIOS'],
        "liquidacion":['FOLIO LIQUIDACIÓN'],
        "fecha_cancelacion":[],
        "id_pedido":[],
        "id_equipo":['VEHÍCULO']
    },
    "FACTURAS":{
        'factura':['FOLIO FACTURA'],
        "total_facturado":['TOTAL_x'],
        "fecha_revision":['FECHA ENVIO REVISION'],
        "total_cobrado":[],
        "fecha_cobro":['FECHA COBRO'],
        "saldo":[],
        "fecha_cancelacion":[],
        "id_viaje":['No.']
    },
    "LIQUIDACIONES":{
        "liquidacion":["NUMEROL","FOLIO LIQUIDACIÓN"],
        "km_liquidados":["KMS_REALES"],
        "litros_liquidados":["LITROS"],
        "sueldo_liquidado":["SUELDO",'COMISIÓN'],
        "fecha_liquidacion":["FECHAL",'FECHA LIQUIDACIÓN'],
        "fecha_cancelacion":[],
        "id_viaje":['No.']
    },
    "EQUIPOS":{
        "id_equipo":["UNIDAD",'VEHÍCULO'],
        "equipo":[], 
        "tipo":[], 
        "subtipo":[], 
        "marca":[], 
        "modelo":[]
    },
    "HISTORIAL_EQUIPO":{
        "equipos_id_equipo":["UNIDAD"],
        "uso":[],
        "fecha_uso":["FFIN"],
        "id_supervisor":[],
        "fecha_supervisor":[],
        "id_propietario":["OPERADOR"],
        "fecha_propietario":[],
        "is_Actual":[],
        "id_status":[],
        "fecha_status":[]
    },
    "SUPERVISORES":{
        "id_supervisor":[],
        "nombre":[]
    },
    "PROPIETARIOS":{
        "id_propietario":["#Ope"],
        "nombre":["#OpeNombre"]
    },
    "STATUS":{
        "id_supervisor":[],
        "nombre":[]
    }

}