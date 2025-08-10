import pandas as pd
import datetime
import numpy as np
import warnings

semana = int(input('Ingrese el numero de la semana: '))

dfb = pd.read_excel('C:/Users/Admin/Desktop/GK/BASE DE DATOS 2025.xlsx', sheet_name='GK2025')

df_nombres = pd.read_excel('C:/Users/Admin/Desktop/GK/PS.xlsx', sheet_name = 'g')
nombres = df_nombres.iloc[:, 0].tolist()

warnings.simplefilter("ignore", category=UserWarning)


N_B_M = pd.read_excel('C:/Users/Admin/Desktop/GK/Notas docentes/P.M.xlsx', sheet_name='NOTAS')
N_B_C = pd.read_excel('C:/Users/Admin/Desktop/GK/Notas docentes/P.C.xlsx', sheet_name='NOTAS')
N_B_S = pd.read_excel('C:/Users/Admin/Desktop/GK/Notas docentes/P.S.xlsx', sheet_name='NOTAS')
N_B_L = pd.read_excel('C:/Users/Admin/Desktop/GK/Notas docentes/P.L.xlsx', sheet_name='NOTAS')
N_B_E = pd.read_excel('C:/Users/Admin/Desktop/GK/Notas docentes/P.E.xlsx', sheet_name='NOTAS')

N_B_C['FECHA'] = pd.to_datetime(N_B_C['FECHA'], errors='coerce')
N_B_S['FECHA'] = pd.to_datetime(N_B_S['FECHA'], errors='coerce')
N_B_L['FECHA'] = pd.to_datetime(N_B_L['FECHA'], errors='coerce')
N_B_M['FECHA'] = pd.to_datetime(N_B_M['FECHA'], errors='coerce')
N_B_E['FECHA'] = pd.to_datetime(N_B_E['FECHA'], errors='coerce')

###cambiar cada periodo (año,mes,dia) que inicia. Cada periodo siempre debe iniciar un lunes 

inicio = datetime.date(2025, 2, 3)
fin = datetime.date(2025, 12, 31)
rango_fechas = pd.date_range(inicio, fin)

cal = pd.DataFrame({'Fecha': rango_fechas, 'Día de la Semana': rango_fechas.day_name()})
df_semana = pd.DataFrame({'Número': np.repeat(range(1, 11), 7)})

calendario = pd.concat([cal, df_semana], ignore_index=True, axis=1)

calendario_por_semana = {}  

for i in range(1, 11):
    calendario_semana_i = calendario[calendario.iloc[:, 2] == i]
    calendario_por_semana[i] = calendario_semana_i
    
notas_b_c  = N_B_C[N_B_C.iloc[:, 0].isin(calendario_por_semana[semana].iloc[:, 0])]
notas_b_s  = N_B_S[N_B_S.iloc[:, 0].isin(calendario_por_semana[semana].iloc[:, 0])]
notas_b_l  = N_B_L[N_B_L.iloc[:, 0].isin(calendario_por_semana[semana].iloc[:, 0])]
notas_b_m  = N_B_M[N_B_M.iloc[:, 0].isin(calendario_por_semana[semana].iloc[:, 0])]
notas_b_e = N_B_E[N_B_E.iloc[:, 0].isin(calendario_por_semana[semana].iloc[:, 0])]

notas_b_c = notas_b_c.dropna()
notas_b_s = notas_b_s.dropna()
notas_b_l = notas_b_l.dropna()
notas_b_m = notas_b_m.dropna()
notas_b_e = notas_b_e.dropna()


notas_b_c  = notas_b_c.reset_index(drop=True)
notas_b_s  = notas_b_s.reset_index(drop=True)
notas_b_l  = notas_b_l.reset_index(drop=True)
notas_b_m = notas_b_m.reset_index(drop=True)
notas_b_e = notas_b_e.reset_index(drop=True)


notas_b_c.insert(1, "AÑO", 2025)
notas_b_c.insert(8, "SEMANA", 'S' + str(semana))
notas_b_c["GRADO"]        = notas_b_c["GRADO"].astype("object")
notas_b_c["PERIODO"     ] = notas_b_c["PERIODO"].astype("int64")
notas_b_c["CALIFICACIÓN"] = notas_b_c["CALIFICACIÓN"].astype("object")

notas_b_s.insert(1, "AÑO", 2025)
notas_b_s.insert(8, "SEMANA", 'S' + str(semana))
notas_b_s["GRADO"]        = notas_b_s["GRADO"].astype("object")
notas_b_s["PERIODO"     ] = notas_b_s["PERIODO"].astype("int64")
notas_b_s["CALIFICACIÓN"] = notas_b_s["CALIFICACIÓN"].astype("object")

notas_b_l.insert(1, "AÑO", 2025)
notas_b_l.insert(8, "SEMANA", 'S' + str(semana))
notas_b_l["GRADO"]        = notas_b_l["GRADO"].astype("object")
notas_b_l["PERIODO"     ] = notas_b_l["PERIODO"].astype("int64")
notas_b_l["CALIFICACIÓN"] = notas_b_l["CALIFICACIÓN"].astype("object")

notas_b_m.insert(1, "AÑO", 2025)
notas_b_m.insert(8, "SEMANA", 'S' + str(semana))
notas_b_m["GRADO"]        = notas_b_m["GRADO"].astype("object")
notas_b_m["PERIODO"     ] = notas_b_m["PERIODO"].astype("int64")
notas_b_m["CALIFICACIÓN"] = notas_b_m["CALIFICACIÓN"].astype("object")

notas_b_e.insert(1, "AÑO", 2025)
notas_b_e.insert(8, "SEMANA", 'S' + str(semana))
notas_b_e["GRADO"]        = notas_b_e["GRADO"].astype("object")
notas_b_e["PERIODO"     ] = notas_b_e["PERIODO"].astype("int64")
notas_b_e["CALIFICACIÓN"] = notas_b_e["CALIFICACIÓN"].astype("object")

notas_b_c['FECHA']  = notas_b_c['FECHA'].dt.strftime('%d/%m/%Y')
notas_b_s['FECHA']  = notas_b_s['FECHA'].dt.strftime('%d/%m/%Y')
notas_b_l['FECHA']  = notas_b_l['FECHA'].dt.strftime('%d/%m/%Y')
notas_b_m['FECHA'] = notas_b_m['FECHA'].dt.strftime('%d/%m/%Y')
notas_b_e['FECHA'] = notas_b_e['FECHA'].dt.strftime('%d/%m/%Y')

notas_b_m  = notas_b_m.sort_values(by=['ESTUDIANTE', 'ASIGNATURA', 'BLOQUE', 'ETAPA'])
notas_b_c  = notas_b_c.sort_values(by=['ESTUDIANTE', 'ASIGNATURA', 'BLOQUE', 'ETAPA'])
notas_b_s  = notas_b_s.sort_values(by=['ESTUDIANTE', 'ASIGNATURA', 'BLOQUE', 'ETAPA'])
notas_b_l  = notas_b_l.sort_values(by=['ESTUDIANTE', 'ASIGNATURA', 'BLOQUE', 'ETAPA'])
notas_b_e = notas_b_e.sort_values(by=['ESTUDIANTE', 'ASIGNATURA', 'BLOQUE', 'ETAPA'])

bloq = ['A','B','C','D']

notas_b_c     = notas_b_c[notas_b_c.iloc[:,6].isin(bloq)]
notas_b_s     = notas_b_s[notas_b_s.iloc[:,6].isin(bloq)]
notas_b_l     = notas_b_l[notas_b_l.iloc[:,6].isin(bloq)]
notas_b_m     = notas_b_m[notas_b_m.iloc[:,6].isin(bloq)]
notas_b_e    = notas_b_e[notas_b_e.iloc[:,6].isin(bloq)]

notas_b_c  = notas_b_c.reset_index(drop=True)
notas_b_s  = notas_b_s.reset_index(drop=True)
notas_b_l  = notas_b_l.reset_index(drop=True)
notas_b_m  = notas_b_m.reset_index(drop=True)
notas_b_e = notas_b_e.reset_index(drop=True)


longitud_bloque = pd.DataFrame({'Bloque': np.repeat(['A','B','C','D'], 5)})

D1 = 'D1'
D2 = 'D2'
D3 = 'D3'
D4 = 'D4'
D5 = 'D5'

longitud_desempeno1 = [D1, D2, D3, D4, D5, D1, D2, D3, D4, D5, D1, D2, D3, D4, D5, D1, D2, D3, D4, D5]
longitud_desempeno = pd.DataFrame({'Etapa': longitud_desempeno1})

longitud_bloque = pd.concat([longitud_bloque, longitud_desempeno],axis = 1, ignore_index=True)

asignaturas= ['Biología','Química','Medio ambiente','Física',
              'Historia', 'Geografía', 'Participación política','Pensamiento religioso',
              'Comunicación y sistemas simbólicos','Producción e interpretación de textos',
              'Aritmética','Animaplanos','Estadística', 'Geometría', 'Dibujo técnico', 'Sistemas']



################################################## MATEMATICAS ##################################################################

print('-----------------------------------------Errores M:-----------------------------------------------------')

indices_a_eliminar_m = []

for i in range(len(notas_b_m)):

    # error en nombre de asignaturas
    
    if notas_b_m.iloc[i, 5] not in asignaturas:
        
        print(f"{notas_b_m.iloc[i, 5]} no es una asignatura, se elimina nota del{notas_b_m.iloc[i, 0]} de {notas_b_m.iloc[i, 2]}")
        print(' ')
        indices_a_eliminar_m.append(i)
        continue
    
    
    
    
    # nombres que no están en el listado general

    if notas_b_m.iloc[i, 2] not in nombres:
        
        print(f"{notas_b_m.iloc[i, 2]} no está en el listado general se elimina nota del {notas_b_m.iloc[i, 0]} de la asignatura {notas_b_m.iloc[i, 5]}")
        print(' ')
        indices_a_eliminar_m.append(i)
        continue
         

    # desempeños duplicados
    
    notas_estudiante = dfb[(dfb.iloc[:, 2] == notas_b_m.iloc[i, 2]) &
                           (dfb.iloc[:, 5] == notas_b_m.iloc[i, 5]) &
                           (dfb.iloc[:, 3] == notas_b_m.iloc[i, 3])]

    for k in range(len(notas_estudiante)):
        
        if ((notas_b_m.iloc[i, 6] == notas_estudiante.iloc[k, 6]) &
            (notas_b_m.iloc[i, 9] == notas_estudiante.iloc[k, 9])):
            
            print(f"{notas_b_m.iloc[i, 2]}, reportado el día {notas_b_m.iloc[i, 0]}, de la asignatura {notas_b_m.iloc[i, 5]}, bloque {notas_b_m.iloc[i, 6]}, etapa {notas_b_m.iloc[i, 9]}, ya está reportado, se elimina.")
            print(' ')
            indices_a_eliminar_m.append(i)
            continue
            
    fila_actual = notas_b_m.iloc[i]
    
    for j in range(i + 1, len(notas_b_m)):
        
        fila_comparar = notas_b_m.iloc[j]
        
        # Verificar si las columnas 2, 5, 6 y 9 son iguales en ambas filas
        if (fila_actual.iloc[2] == fila_comparar.iloc[2] and
            fila_actual.iloc[5] == fila_comparar.iloc[5] and
            fila_actual.iloc[6] == fila_comparar.iloc[6] and
            fila_actual.iloc[9] == fila_comparar.iloc[9]):
            print(f'{fila_actual.iloc[2]} de la materia {fila_actual.iloc[5]} del bloque {fila_actual.iloc[6]} la etapa {fila_actual.iloc[9]} se reporto dos veces')
            print(f'los dias {fila_actual.iloc[0]} y {fila_comparar.iloc[0]}')
            print(f'se elimina el del dia {fila_comparar.iloc[0]} que tiene nota {fila_comparar.iloc[10]} ')
            print(' ')
            indices_a_eliminar_m.append(j)

notas_b_m.drop(indices_a_eliminar_m, inplace=True)
notas_b_m = notas_b_m.reset_index(drop=True)

# desempeños reportados que no siguen el orden de la base de datos

indices_a_eliminar_m_1 = []

for i in range(len(notas_b_m)):
    evaluado = False 
    if evaluado:
        continue 
    estudiante = notas_b_m.iloc[i, 2]
    grado      = notas_b_m.iloc[i, 3]
    materia    = notas_b_m.iloc[i, 5]
    dia        = notas_b_m.iloc[i, 0]
    bloque     = notas_b_m.iloc[i, 6]
    desempeno  = notas_b_m.iloc[i, 9]
    notas_estudiante = dfb[(dfb.iloc[:, 2] == estudiante) &
                           (dfb.iloc[:, 5] == materia)    &
                           (dfb.iloc[:, 3] == grado)       ]
    bloque_etapa = notas_estudiante.iloc[:, [6, 9]]
    bloque_etapa = bloque_etapa.reset_index(drop=True)
    for r in range(len(longitud_bloque)):
        if evaluado:
            break
        if (bloque == 'D') and (desempeno =='D5') and (len(notas_estudiante) != 19):
            print(f'{estudiante} reportado el dia {dia} de la asignatura {materia}, bloque {bloque}, etapa {desempeno}')
            print('no coincide con una nota faltante o que sea el siguiente desempeño a reportar y se elimina.')
            print(' ')
            indices_a_eliminar_m_1.append(i)
            break
        if ((bloque    == longitud_bloque.iloc[r, 0]) &
            (desempeno == longitud_bloque.iloc[r, 1])):
            if len(notas_estudiante) != r:
                #evaluar cada fila del vector que da longitud de bloques y desempeños del bloque y desempeño siguiente al reportado
                for h in range(r+1, len(longitud_bloque)):
                    #comparar con bloque y etapa de notas del estudiante
                    for p in range(len(bloque_etapa)): 
                        if (longitud_bloque.iloc[h,0] == bloque_etapa.iloc[p,0]) and (longitud_bloque.iloc[h,1] == bloque_etapa.iloc[p,1]):
                            fila_para_agregar = notas_b_m.iloc[i].to_frame().T 
                            dfb = pd.concat([dfb, fila_para_agregar], ignore_index=True)
                            evaluado = True
                            break               
                if evaluado:
                    break    
                print(f'{estudiante} reportado el dia {dia} de la asignatura {materia}, bloque {bloque}, etapa {desempeno}')
                print('no coincide con una nota faltante o que sea el siguiente desempeño a reportar y se elimina.')
                print(' ')
                indices_a_eliminar_m_1.append(i)
                evaluado = True
                break                        
            if len(notas_estudiante) == r:
                fila_para_agregar = notas_b_m.iloc[i].to_frame().T
                dfb = pd.concat([dfb, fila_para_agregar], ignore_index=True)
                break    
notas_b_m.drop(indices_a_eliminar_m_1, inplace=True)
notas_b_m = notas_b_m.reset_index(drop=True)

             

####################################################### CIENCIAS ################################################################
                
print('-----------------------------------------Errores C:-----------------------------------------')

indices_a_eliminar_c = []

for i in range(len(notas_b_c)):
    
    # error en nombre de asignaturas
    
    if notas_b_c.iloc[i, 5] not in asignaturas:
        
        print(f"{notas_b_c.iloc[i, 5]} no es una asignatura, se elimina nota del{notas_b_c.iloc[i, 0]} de {notas_b_c.iloc[i, 2]}")
        print(' ')
        indices_a_eliminar_c.append(i)
        continue

    # nombres que no están en el listado general
    
    if notas_b_c.iloc[i, 2] not in nombres:
        
        print(f"{notas_b_c.iloc[i, 2]} no está en el listado general se elimina nota del {notas_b_c.iloc[i, 0]} de la asignatura {notas_b_c.iloc[i, 5]}")
        print(' ')
        indices_a_eliminar_c.append(i)
        continue
    
            

    # desempeños duplicados
    
    notas_estudiante = dfb[(dfb.iloc[:, 2] == notas_b_c.iloc[i, 2]) &
                           (dfb.iloc[:, 5] == notas_b_c.iloc[i, 5]) &
                           (dfb.iloc[:, 3] == notas_b_c.iloc[i, 3])]

    for k in range(len(notas_estudiante)):
        
        if ((notas_b_c.iloc[i, 6] == notas_estudiante.iloc[k, 6]) &
            (notas_b_c.iloc[i, 9] == notas_estudiante.iloc[k, 9])):
            
            print(f"{notas_b_c.iloc[i, 2]}, reportado el día {notas_b_c.iloc[i, 0]}, de la asignatura {notas_b_c.iloc[i, 5]}, bloque {notas_b_c.iloc[i, 6]}, etapa {notas_b_c.iloc[i, 9]}, ya está reportado, se elimina.")
            print(' ')
            indices_a_eliminar_c.append(i)
            continue
            
    fila_actual = notas_b_c.iloc[i]
    
    for j in range(i + 1, len(notas_b_c)):
        
        fila_comparar = notas_b_c.iloc[j]
        
        # Verificar si las columnas 2, 5, 6 y 9 son iguales en ambas filas
        if (fila_actual.iloc[2] == fila_comparar.iloc[2] and
            fila_actual.iloc[5] == fila_comparar.iloc[5] and
            fila_actual.iloc[6] == fila_comparar.iloc[6] and
            fila_actual.iloc[9] == fila_comparar.iloc[9]):
            print(f'{fila_actual.iloc[2]} de la materia {fila_actual.iloc[5]} del bloque {fila_actual.iloc[6]} la etapa {fila_actual.iloc[9]} se reporto dos veces')
            print(f'los dias {fila_actual.iloc[0]} y {fila_comparar.iloc[0]}')
            print(f'se elimina el del dia {fila_comparar.iloc[0]} que tiene nota {fila_comparar.iloc[10]} ')
            print(' ')
            indices_a_eliminar_c.append(j)

notas_b_c.drop(indices_a_eliminar_c, inplace=True)
notas_b_c = notas_b_c.reset_index(drop=True)

# desempeños reportados que no siguen el orden de la base de datos

indices_a_eliminar_c_1 = []

for i in range(len(notas_b_c)):
    evaluado = False 
    if evaluado:
        continue 
    estudiante = notas_b_c.iloc[i, 2]
    grado      = notas_b_c.iloc[i, 3]
    materia    = notas_b_c.iloc[i, 5]
    dia        = notas_b_c.iloc[i, 0]
    bloque     = notas_b_c.iloc[i, 6]
    desempeno  = notas_b_c.iloc[i, 9]
    notas_estudiante = dfb[(dfb.iloc[:, 2] == estudiante) &
                           (dfb.iloc[:, 5] == materia)    &
                           (dfb.iloc[:, 3] == grado)       ]
    bloque_etapa = notas_estudiante.iloc[:, [6, 9]]
    bloque_etapa = bloque_etapa.reset_index(drop=True)
    for r in range(len(longitud_bloque)):
        if evaluado:
            break
        if (bloque == 'D') and (desempeno =='D5') and (len(notas_estudiante) != 19):
            print(f'{estudiante} reportado el dia {dia} de la asignatura {materia}, bloque {bloque}, etapa {desempeno}')
            print('no coincide con una nota faltante o que sea el siguiente desempeño a reportar y se elimina.')
            print(' ')
            indices_a_eliminar_c_1.append(i)
            break
        if ((bloque    == longitud_bloque.iloc[r, 0]) &
            (desempeno == longitud_bloque.iloc[r, 1])):
            if len(notas_estudiante) != r:
                #evaluar cada fila del vector que da longitud de bloques y desempeños del bloque y desempeño siguiente al reportado
                for h in range(r+1, len(longitud_bloque)):
                    #comparar con bloque y etapa de notas del estudiante
                    for p in range(len(bloque_etapa)): 
                        if (longitud_bloque.iloc[h,0] == bloque_etapa.iloc[p,0]) and (longitud_bloque.iloc[h,1] == bloque_etapa.iloc[p,1]):
                            fila_para_agregar = notas_b_c.iloc[i].to_frame().T 
                            dfb = pd.concat([dfb, fila_para_agregar], ignore_index=True)
                            evaluado = True
                            break               
                    if evaluado:
                        break    
                print(f'{estudiante} reportado el dia {dia} de la asignatura {materia}, bloque {bloque}, etapa {desempeno}')
                print('no coincide con una nota faltante o que sea el siguiente desempeño a reportar y se elimina.')
                print(' ')
                indices_a_eliminar_c_1.append(i)
                evaluado = True
                break                        
            if len(notas_estudiante) == r:
                fila_para_agregar = notas_b_c.iloc[i].to_frame().T
                dfb = pd.concat([dfb, fila_para_agregar], ignore_index=True)
                break    
notas_b_c.drop(indices_a_eliminar_c_1, inplace=True)
notas_b_c = notas_b_c.reset_index(drop=True)


#################################################### SOCIALES ######################################################################

print('-----------------------------------------Errores S:-----------------------------------------')

indices_a_eliminar_s = []

for i in range(len(notas_b_s)):
    
    # error en nombre de asignaturas
    
    if notas_b_s.iloc[i, 5] not in asignaturas:
        
        print(f"{notas_b_s.iloc[i, 5]} no es una asignatura, se elimina nota del{notas_b_s.iloc[i, 0]} de {notas_b_s.iloc[i, 2]}")
        print(' ')
        indices_a_eliminar_s.append(i)
        continue

    # nombres que no están en el listado general
    
    if notas_b_s.iloc[i, 2] not in nombres:
        
        print(f"{notas_b_s.iloc[i, 2]} no está en el listado general se elimina nota del {notas_b_s.iloc[i, 0]} de la asignatura {notas_b_s.iloc[i, 5]}")
        print(' ')
        indices_a_eliminar_s.append(i)
        continue
            

    # desempeños duplicados
    
    notas_estudiante = dfb[(dfb.iloc[:, 2] == notas_b_s.iloc[i, 2]) &
                           (dfb.iloc[:, 5] == notas_b_s.iloc[i, 5]) &
                           (dfb.iloc[:, 3] == notas_b_s.iloc[i, 3])]

    for k in range(len(notas_estudiante)):
        
        if ((notas_b_s.iloc[i, 6] == notas_estudiante.iloc[k, 6]) &
            (notas_b_s.iloc[i, 9] == notas_estudiante.iloc[k, 9])):
            
            print(f"{notas_b_s.iloc[i, 2]}, reportado el día {notas_b_s.iloc[i, 0]}, de la asignatura {notas_b_s.iloc[i, 5]}, bloque {notas_b_s.iloc[i, 6]}, etapa {notas_b_s.iloc[i, 9]}, ya está reportado, se elimina.")
            print(' ')
            indices_a_eliminar_s.append(i)
            continue
            
    fila_actual = notas_b_s.iloc[i]
    
    for j in range(i + 1, len(notas_b_s)):
        
        fila_comparar = notas_b_s.iloc[j]
        
        # Verificar si las columnas 2, 5, 6 y 9 son iguales en ambas filas
        if (fila_actual.iloc[2] == fila_comparar.iloc[2] and
            fila_actual.iloc[5] == fila_comparar.iloc[5] and
            fila_actual.iloc[6] == fila_comparar.iloc[6] and
            fila_actual.iloc[9] == fila_comparar.iloc[9]):
            print(f'{fila_actual.iloc[2]} de la materia {fila_actual.iloc[5]} del bloque {fila_actual.iloc[6]} la etapa {fila_actual.iloc[9]} se reporto dos veces')
            print(f'los dias {fila_actual.iloc[0]} y {fila_comparar.iloc[0]}')
            print(f'se elimina el del dia {fila_comparar.iloc[0]} que tiene nota {fila_comparar.iloc[10]} ')
            print(' ')
            indices_a_eliminar_s.append(j)

notas_b_s.drop(indices_a_eliminar_s, inplace=True)
notas_b_s = notas_b_s.reset_index(drop=True)

# desempeños reportados que no siguen el orden de la base de datos

indices_a_eliminar_s_1 = []

for i in range(len(notas_b_s)):
    evaluado = False 
    if evaluado:
        continue 
    estudiante = notas_b_s.iloc[i, 2]
    grado      = notas_b_s.iloc[i, 3]
    materia    = notas_b_s.iloc[i, 5]
    dia        = notas_b_s.iloc[i, 0]
    bloque     = notas_b_s.iloc[i, 6]
    desempeno  = notas_b_s.iloc[i, 9]
    notas_estudiante = dfb[(dfb.iloc[:, 2] == estudiante) &
                           (dfb.iloc[:, 5] == materia)    &
                           (dfb.iloc[:, 3] == grado)       ]
    bloque_etapa = notas_estudiante.iloc[:, [6, 9]]
    bloque_etapa = bloque_etapa.reset_index(drop=True)
    for r in range(len(longitud_bloque)):
        if evaluado:
            break
        if (bloque == 'D') and (desempeno =='D5') and (len(notas_estudiante) != 19):
            print(f'{estudiante} reportado el dia {dia} de la asignatura {materia}, bloque {bloque}, etapa {desempeno}')
            print('no coincide con una nota faltante o que sea el siguiente desempeño a reportar y se elimina.')
            print(' ')
            indices_a_eliminar_s_1.append(i)
            break
        if ((bloque    == longitud_bloque.iloc[r, 0]) &
            (desempeno == longitud_bloque.iloc[r, 1])):
            if len(notas_estudiante) != r:
                #evaluar cada fila del vector que da longitud de bloques y desempeños del bloque y desempeño siguiente al reportado
                for h in range(r+1, len(longitud_bloque)):
                    #comparar con bloque y etapa de notas del estudiante
                    for p in range(len(bloque_etapa)): 
                        if (longitud_bloque.iloc[h,0] == bloque_etapa.iloc[p,0]) and (longitud_bloque.iloc[h,1] == bloque_etapa.iloc[p,1]):
                            fila_para_agregar = notas_b_s.iloc[i].to_frame().T 
                            dfb = pd.concat([dfb, fila_para_agregar], ignore_index=True)
                            evaluado = True
                            break               
                    if evaluado:
                        break    
                print(f'{estudiante} reportado el dia {dia} de la asignatura {materia}, bloque {bloque}, etapa {desempeno}')
                print('no coincide con una nota faltante o que sea el siguiente desempeño a reportar y se elimina.')
                print(' ')
                indices_a_eliminar_s_1.append(i)
                evaluado = True
                break                        
            if len(notas_estudiante) == r:
                fila_para_agregar = notas_b_s.iloc[i].to_frame().T
                dfb = pd.concat([dfb, fila_para_agregar], ignore_index=True)
                break    
notas_b_s.drop(indices_a_eliminar_s_1, inplace=True)
notas_b_s = notas_b_s.reset_index(drop=True)



######################################################### LENGUAJE ###############################################################

print('-----------------------------------------Errores L:-----------------------------------------')

indices_a_eliminar_l = []

for i in range(len(notas_b_l)):
    
    # error en nombre de asignaturas
    
    if notas_b_l.iloc[i, 5] not in asignaturas:
        
        print(f"{notas_b_l.iloc[i, 5]} no es una asignatura, se elimina nota del{notas_b_l.iloc[i, 0]} de {notas_b_l.iloc[i, 2]}")
        print(' ')
        indices_a_eliminar_l.append(i)
        continue

    # nombres que no están en el listado general
    
    if notas_b_l.iloc[i, 2] not in nombres:
        
        print(f"{notas_b_l.iloc[i, 2]} no está en el listado general se elimina nota del {notas_b_l.iloc[i, 0]} de la asignatura {notas_b_l.iloc[i, 5]}")
        print(' ')
        indices_a_eliminar_l.append(i)
        continue     

    # desempeños duplicados
    
    notas_estudiante = dfb[(dfb.iloc[:, 2] == notas_b_l.iloc[i, 2]) &
                           (dfb.iloc[:, 5] == notas_b_l.iloc[i, 5]) &
                           (dfb.iloc[:, 3] == notas_b_l.iloc[i, 3])]

    for k in range(len(notas_estudiante)):
        
        if ((notas_b_l.iloc[i, 6] == notas_estudiante.iloc[k, 6]) &
            (notas_b_l.iloc[i, 9] == notas_estudiante.iloc[k, 9])):
            
            print(f"{notas_b_l.iloc[i, 2]}, reportado el día {notas_b_l.iloc[i, 0]}, de la asignatura {notas_b_l.iloc[i, 5]}, bloque {notas_b_l.iloc[i, 6]}, etapa {notas_b_l.iloc[i, 9]}, ya está reportado, se elimina.")
            print(' ')
            indices_a_eliminar_l.append(i)
            continue
            
    fila_actual = notas_b_l.iloc[i]
    
    for j in range(i + 1, len(notas_b_l)):
        
        fila_comparar = notas_b_l.iloc[j]
        
        # Verificar si las columnas 2, 5, 6 y 9 son iguales en ambas filas
        if (fila_actual.iloc[2] == fila_comparar.iloc[2] and
            fila_actual.iloc[5] == fila_comparar.iloc[5] and
            fila_actual.iloc[6] == fila_comparar.iloc[6] and
            fila_actual.iloc[9] == fila_comparar.iloc[9]):
            print(f'{fila_actual.iloc[2]} de la materia {fila_actual.iloc[5]} del bloque {fila_actual.iloc[6]} la etapa {fila_actual.iloc[9]} se reporto dos veces')
            print(f'los dias {fila_actual.iloc[0]} y {fila_comparar.iloc[0]}')
            print(f'se elimina el del dia {fila_comparar.iloc[0]} que tiene nota {fila_comparar.iloc[10]} ')
            print(' ')
            indices_a_eliminar_l.append(j)

notas_b_l.drop(indices_a_eliminar_l, inplace=True)
notas_b_l = notas_b_l.reset_index(drop=True)

# desempeños reportados que no siguen el orden de la base de datos

indices_a_eliminar_l_1 = []

for i in range(len(notas_b_l)):
    evaluado = False 
    if evaluado:
        continue 
    estudiante = notas_b_l.iloc[i, 2]
    grado      = notas_b_l.iloc[i, 3]
    materia    = notas_b_l.iloc[i, 5]
    dia        = notas_b_l.iloc[i, 0]
    bloque     = notas_b_l.iloc[i, 6]
    desempeno  = notas_b_l.iloc[i, 9]
    notas_estudiante = dfb[(dfb.iloc[:, 2] == estudiante) &
                           (dfb.iloc[:, 5] == materia)    &
                           (dfb.iloc[:, 3] == grado)       ]
    bloque_etapa = notas_estudiante.iloc[:, [6, 9]]
    bloque_etapa = bloque_etapa.reset_index(drop=True)
    for r in range(len(longitud_bloque)):
        if evaluado:
            break
        if (bloque == 'D') and (desempeno =='D5') and (len(notas_estudiante) != 19):
            print(f'{estudiante} reportado el dia {dia} de la asignatura {materia}, bloque {bloque}, etapa {desempeno}')
            print('no coincide con una nota faltante o que sea el siguiente desempeño a reportar y se elimina.')
            print(' ')
            indices_a_eliminar_l_1.append(i)
            break
        if ((bloque    == longitud_bloque.iloc[r, 0]) &
            (desempeno == longitud_bloque.iloc[r, 1])):
            if len(notas_estudiante) != r:
                #evaluar cada fila del vector que da longitud de bloques y desempeños del bloque y desempeño siguiente al reportado
                for h in range(r+1, len(longitud_bloque)):
                    #comparar con bloque y etapa de notas del estudiante
                    for p in range(len(bloque_etapa)): 
                        if (longitud_bloque.iloc[h,0] == bloque_etapa.iloc[p,0]) and (longitud_bloque.iloc[h,1] == bloque_etapa.iloc[p,1]):
                            fila_para_agregar = notas_b_l.iloc[i].to_frame().T 
                            dfb = pd.concat([dfb, fila_para_agregar], ignore_index=True)
                            evaluado = True
                            break               
                    if evaluado:
                        break    
                print(f'{estudiante} reportado el dia {dia} de la asignatura {materia}, bloque {bloque}, etapa {desempeno}')
                print('no coincide con una nota faltante o que sea el siguiente desempeño a reportar y se elimina.')
                print(' ')
                indices_a_eliminar_l_1.append(i)
                evaluado = True
                break                        
            if len(notas_estudiante) == r:
                fila_para_agregar = notas_b_l.iloc[i].to_frame().T
                dfb = pd.concat([dfb, fila_para_agregar], ignore_index=True)
                break    
notas_b_l.drop(indices_a_eliminar_l_1, inplace=True)
notas_b_l = notas_b_l.reset_index(drop=True)


######################################################### INGLES 1 ###############################################################

print('-----------------------------------------Errores E :-----------------------------------------')

indices_a_eliminar_e = []

for i in range(len(notas_b_e)):

    # nombres que no están en el listado general
    
    if notas_b_e.iloc[i, 2] not in nombres:
        
        print(f"{notas_b_e.iloc[i, 2]} no está en el listado general se elimina nota del {notas_b_e.iloc[i, 0]} de la asignatura {notas_b_e.iloc[i, 5]}")
        print(' ')
        indices_a_eliminar_e.append(i)
        continue

    # desempeños duplicados
    
    notas_estudiante = dfb[(dfb.iloc[:, 2] == notas_b_e.iloc[i, 2]) &
                           (dfb.iloc[:, 5] == notas_b_e.iloc[i, 5]) &
                           (dfb.iloc[:, 3] == notas_b_e.iloc[i, 3])]

    for k in range(len(notas_estudiante)):
        
        if ((notas_b_e.iloc[i, 6] == notas_estudiante.iloc[k, 6]) &
            (notas_b_e.iloc[i, 9] == notas_estudiante.iloc[k, 9])):
            
            print(f"{notas_b_e.iloc[i, 2]}, reportado el día {notas_b_e.iloc[i, 0]}, de la asignatura {notas_b_e.iloc[i, 5]}, bloque {notas_b_e.iloc[i, 6]}, etapa {notas_b_e.iloc[i, 9]}, ya está reportado, se elimina.")
            print(' ')
            indices_a_eliminar_e.append(i)
            continue
            
    fila_actual = notas_b_e.iloc[i]
    
    for j in range(i + 1, len(notas_b_e)):
        
        fila_comparar = notas_b_e.iloc[j]
        
        # Verificar si las columnas 2, 5, 6 y 9 son iguales en ambas filas
        if (fila_actual.iloc[2] == fila_comparar.iloc[2] and
            fila_actual.iloc[5] == fila_comparar.iloc[5] and
            fila_actual.iloc[6] == fila_comparar.iloc[6] and
            fila_actual.iloc[9] == fila_comparar.iloc[9]):
            print(f'{fila_actual.iloc[2]} de la materia {fila_actual.iloc[5]} del bloque {fila_actual.iloc[6]} la etapa {fila_actual.iloc[9]} se reporto dos veces')
            print(f'los dias {fila_actual.iloc[0]} y {fila_comparar.iloc[0]}')
            print(f'se elimina el del dia {fila_comparar.iloc[0]} que tiene nota {fila_comparar.iloc[10]} ')
            print(' ')
            indices_a_eliminar_e.append(j)

notas_b_e.drop(indices_a_eliminar_e, inplace=True)
notas_b_e = notas_b_e.reset_index(drop=True)

# desempeños reportados que no siguen el orden de la base de datos

indices_a_eliminar_e_ = []

for i in range(len(notas_b_e)):
    evaluado = False 
    if evaluado:
        continue 
    estudiante = notas_b_e.iloc[i, 2]
    grado      = notas_b_e.iloc[i, 3]
    materia    = notas_b_e.iloc[i, 5]
    dia        = notas_b_e.iloc[i, 0]
    bloque     = notas_b_e.iloc[i, 6]
    desempeno  = notas_b_e.iloc[i, 9]
    notas_estudiante = dfb[(dfb.iloc[:, 2] == estudiante) &
                           (dfb.iloc[:, 5] == materia)    &
                           (dfb.iloc[:, 3] == grado)       ]
    bloque_etapa = notas_estudiante.iloc[:, [6, 9]]
    bloque_etapa = bloque_etapa.reset_index(drop=True)
    for r in range(len(longitud_bloque)):
        if evaluado:
            break
        if (bloque == 'D') and (desempeno =='D5') and (len(notas_estudiante) != 19):
            print(f'{estudiante} reportado el dia {dia} de la asignatura {materia}, bloque {bloque}, etapa {desempeno}')
            print('no coincide con una nota faltante o que sea el siguiente desempeño a reportar y se elimina.')
            print(' ')
            indices_a_eliminar_e.append(i)
            break
        if ((bloque    == longitud_bloque.iloc[r, 0]) &
            (desempeno == longitud_bloque.iloc[r, 1])):
            if len(notas_estudiante) != r:
                #evaluar cada fila del vector que da longitud de bloques y desempeños del bloque y desempeño siguiente al reportado
                for h in range(r+1, len(longitud_bloque)):
                    #comparar con bloque y etapa de notas del estudiante
                    for p in range(len(bloque_etapa)): 
                        if (longitud_bloque.iloc[h,0] == bloque_etapa.iloc[p,0]) and (longitud_bloque.iloc[h,1] == bloque_etapa.iloc[p,1]):
                            fila_para_agregar = notas_b_e.iloc[i].to_frame().T 
                            dfb = pd.concat([dfb, fila_para_agregar], ignore_index=True)
                            evaluado = True
                            break               
                if evaluado:
                    break    
                print(f'{estudiante} reportado el dia {dia} de la asignatura {materia}, bloque {bloque}, etapa {desempeno}')
                print('no coincide con una nota faltante o que sea el siguiente desempeño a reportar y se elimina.')
                print(' ')
                indices_a_eliminar_e.append(i)
                evaluado = True
                break                        
            if len(notas_estudiante) == r:
                fila_para_agregar = notas_b_e.iloc[i].to_frame().T
                dfb = pd.concat([dfb, fila_para_agregar], ignore_index=True)
                break    
notas_b_e.drop(indices_a_eliminar_e, inplace=True)
notas_b_e = notas_b_e.reset_index(drop=True)



notas = pd.concat([notas_b_m,notas_b_c,notas_b_s,notas_b_l,notas_b_e],ignore_index = True)

notas.to_excel('C:/Users/Admin/Desktop/GK/Notas Para Subir Primaria.xlsx', index=False)







