
import pandas as pd
import datetime
import numpy as np
import warnings

semana = int(input('Ingrese el numero de la semana: '))

excepciones = ['GARZÓN POLO SARAH LUCÍA','GARZÓN POLO SARAH LUCÍA','GONZÁLEZ SUÁREZ MARIANA','VALCÁRCEL CASTRO VIOLETA','BOGOYA DÍAZ JUAN CAMILO,VARGAS CAMPOS LAURA TATIANA']

dfb = pd.read_excel('C:/Users/Admin/Desktop/GK/BASE DE DATOS 2025.xlsx', sheet_name='GK2025')

df_nombres = pd.read_excel('C:/Users/Admin/Desktop/GK/PS.xlsx', sheet_name = 'g')
nombres = df_nombres.iloc[:, 0].tolist()


warnings.simplefilter("ignore", category=UserWarning)

N_B_M1 = pd.read_excel('C:/Users/Admin/Desktop/GK/Notas docentes/B.M1.xlsx', sheet_name='NOTAS')
N_B_M2 = pd.read_excel('C:/Users/Admin/Desktop/GK/Notas docentes/B.M2.xlsx', sheet_name='NOTAS')
N_B_C1 = pd.read_excel('C:/Users/Admin/Desktop/GK/Notas docentes/B.C1.xlsx', sheet_name='NOTAS')
N_B_C2 = pd.read_excel('C:/Users/Admin/Desktop/GK/Notas docentes/B.C2.xlsx', sheet_name='NOTAS')
N_B_S1 = pd.read_excel('C:/Users/Admin/Desktop/GK/Notas docentes/B.S1.xlsx', sheet_name='NOTAS')
N_B_S2 = pd.read_excel('C:/Users/Admin/Desktop/GK/Notas docentes/B.S2.xlsx', sheet_name='NOTAS')
N_B_L  = pd.read_excel('C:/Users/Admin/Desktop/GK/Notas docentes/B.L.xlsx', sheet_name='NOTAS')
N_B_E1 = pd.read_excel('C:/Users/Admin/Desktop/GK/Notas docentes/B.E1.xlsx', sheet_name='NOTAS')
N_B_E2 = pd.read_excel('C:/Users/Admin/Desktop/GK/Notas docentes/B.E2.xlsx', sheet_name='NOTAS')
N_B_STEAM = pd.read_excel('C:/Users/Admin/Desktop/GK/Notas docentes/B.STEAM.xlsx', sheet_name='NOTAS')


N_B_C1['FECHA'] = pd.to_datetime(N_B_C1['FECHA'], errors='coerce')
N_B_C2['FECHA'] = pd.to_datetime(N_B_C2['FECHA'], errors='coerce')
N_B_S1['FECHA'] = pd.to_datetime(N_B_S1['FECHA'], errors='coerce')
N_B_S2['FECHA'] = pd.to_datetime(N_B_S2['FECHA'], errors='coerce')
N_B_L['FECHA'] = pd.to_datetime(N_B_L['FECHA'], errors='coerce')
N_B_M1['FECHA'] = pd.to_datetime(N_B_M1['FECHA'], errors='coerce')
N_B_M2['FECHA'] = pd.to_datetime(N_B_M2['FECHA'], errors='coerce')
N_B_E1['FECHA'] = pd.to_datetime(N_B_E1['FECHA'], errors='coerce')
N_B_E2['FECHA'] = pd.to_datetime(N_B_E2['FECHA'], errors='coerce')
N_B_STEAM['FECHA'] = pd.to_datetime(N_B_STEAM['FECHA'], errors='coerce')



# In[8]:


###cambiar cada periodo (año,mes,dia) que inicia cada periodo siempre debe iniciar un jueves##########
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
    
notas_b_c     = N_B_C1[N_B_C1.iloc[:, 0].isin(calendario_por_semana[semana].iloc[:, 0])]
notas_b_c2     = N_B_C2[N_B_C2.iloc[:, 0].isin(calendario_por_semana[semana].iloc[:, 0])]
notas_b_s1    = N_B_S1[N_B_S1.iloc[:, 0].isin(calendario_por_semana[semana].iloc[:, 0])]
notas_b_s2    = N_B_S2[N_B_S2.iloc[:, 0].isin(calendario_por_semana[semana].iloc[:, 0])]
notas_b_l     = N_B_L[N_B_L.iloc[:, 0].isin(calendario_por_semana[semana].iloc[:, 0])]
notas_b_m1    = N_B_M1[N_B_M1.iloc[:, 0].isin(calendario_por_semana[semana].iloc[:, 0])]
notas_b_m2    = N_B_M2[N_B_M2.iloc[:, 0].isin(calendario_por_semana[semana].iloc[:, 0])]
notas_b_e1    = N_B_E1[N_B_E1.iloc[:, 0].isin(calendario_por_semana[semana].iloc[:, 0])]
notas_b_e2    = N_B_E2[N_B_E2.iloc[:, 0].isin(calendario_por_semana[semana].iloc[:, 0])]
notas_b_steam = N_B_STEAM[N_B_STEAM.iloc[:, 0].isin(calendario_por_semana[semana].iloc[:, 0])]



notas_b_c = notas_b_c.dropna()
notas_b_c2 = notas_b_c2.dropna()
notas_b_s1 = notas_b_s1.dropna()
notas_b_s2 = notas_b_s2.dropna()
notas_b_l = notas_b_l.dropna()
notas_b_m1 = notas_b_m1.dropna()
notas_b_m2 = notas_b_m2.dropna()
notas_b_e1 = notas_b_e1.dropna()
notas_b_e2 = notas_b_e2.dropna()
notas_b_steam = notas_b_steam.dropna()

notas_b_c  = notas_b_c.reset_index(drop=True)
notas_b_c2  = notas_b_c2.reset_index(drop=True)
notas_b_s1  = notas_b_s1.reset_index(drop=True)
notas_b_s2  = notas_b_s2.reset_index(drop=True)
notas_b_l  = notas_b_l.reset_index(drop=True)
notas_b_m1 = notas_b_m1.reset_index(drop=True)
notas_b_m2 = notas_b_m2.reset_index(drop=True)
notas_b_e1 = notas_b_e1.reset_index(drop=True)
notas_b_e2 = notas_b_e2.reset_index(drop=True)
notas_b_steam = notas_b_steam.reset_index(drop=True)

notas_b_c.insert(1, "AÑO", 2025)
notas_b_c.insert(8, "SEMANA", 'S' + str(semana))
notas_b_c["GRADO"]        = notas_b_c["GRADO"].astype("object")
notas_b_c["PERIODO"     ] = notas_b_c["PERIODO"].astype("int64")
notas_b_c["CALIFICACIÓN"] = notas_b_c["CALIFICACIÓN"].astype("object")

notas_b_c2.insert(1, "AÑO", 2025)
notas_b_c2.insert(8, "SEMANA", 'S' + str(semana))
notas_b_c2["GRADO"]        = notas_b_c2["GRADO"].astype("object")
notas_b_c2["PERIODO"     ] = notas_b_c2["PERIODO"].astype("int64")
notas_b_c2["CALIFICACIÓN"] = notas_b_c2["CALIFICACIÓN"].astype("object")


notas_b_s1.insert(1, "AÑO", 2025)
notas_b_s1.insert(8, "SEMANA", 'S' + str(semana))
notas_b_s1["GRADO"]        = notas_b_s1["GRADO"].astype("object")
notas_b_s1["PERIODO"     ] = notas_b_s1["PERIODO"].astype("int64")
notas_b_s1["CALIFICACIÓN"] = notas_b_s1["CALIFICACIÓN"].astype("object")

notas_b_s2.insert(1, "AÑO", 2025)
notas_b_s2.insert(8, "SEMANA", 'S' + str(semana))
notas_b_s2["GRADO"]        = notas_b_s2["GRADO"].astype("object")
notas_b_s2["PERIODO"     ] = notas_b_s2["PERIODO"].astype("int64")
notas_b_s2["CALIFICACIÓN"] = notas_b_s2["CALIFICACIÓN"].astype("object")

notas_b_l.insert(1, "AÑO", 2025)
notas_b_l.insert(8, "SEMANA", 'S' + str(semana))
notas_b_l["GRADO"]        = notas_b_l["GRADO"].astype("object")
notas_b_l["PERIODO"     ] = notas_b_l["PERIODO"].astype("int64")
notas_b_l["CALIFICACIÓN"] = notas_b_l["CALIFICACIÓN"].astype("object")

notas_b_m1.insert(1, "AÑO", 2025)
notas_b_m1.insert(8, "SEMANA", 'S' + str(semana))
notas_b_m1["GRADO"]        = notas_b_m1["GRADO"].astype("object")
notas_b_m1["PERIODO"     ] = notas_b_m1["PERIODO"].astype("int64")
notas_b_m1["CALIFICACIÓN"] = notas_b_m1["CALIFICACIÓN"].astype("object")

notas_b_m2.insert(1, "AÑO", 2025)
notas_b_m2.insert(8, "SEMANA", 'S' + str(semana))
notas_b_m2["GRADO"]        = notas_b_m2["GRADO"].astype("object")
notas_b_m2["PERIODO"     ] = notas_b_m2["PERIODO"].astype("int64")
notas_b_m2["CALIFICACIÓN"] = notas_b_m2["CALIFICACIÓN"].astype("object")

notas_b_e1.insert(1, "AÑO", 2025)
notas_b_e1.insert(8, "SEMANA", 'S' + str(semana))
notas_b_e1["GRADO"]        = notas_b_e1["GRADO"].astype("object")
notas_b_e1["PERIODO"     ] = notas_b_e1["PERIODO"].astype("int64")
notas_b_e1["CALIFICACIÓN"] = notas_b_e1["CALIFICACIÓN"].astype("object")

notas_b_e2.insert(1, "AÑO", 2025)
notas_b_e2.insert(8, "SEMANA", 'S' + str(semana))
notas_b_e2["GRADO"]        = notas_b_e2["GRADO"].astype("object")
notas_b_e2["PERIODO"     ] = notas_b_e2["PERIODO"].astype("int64")
notas_b_e2["CALIFICACIÓN"] = notas_b_e2["CALIFICACIÓN"].astype("object")

notas_b_steam.insert(1, "AÑO", 2025)
notas_b_steam.insert(8, "SEMANA", 'S' + str(semana))
notas_b_steam["GRADO"]        = notas_b_steam["GRADO"].astype("object")
notas_b_steam["PERIODO"     ] = notas_b_steam["PERIODO"].astype("int64")
notas_b_steam["CALIFICACIÓN"] = notas_b_steam["CALIFICACIÓN"].astype("object")

notas_b_c['FECHA']  = notas_b_c['FECHA'].dt.strftime('%d/%m/%Y')
notas_b_c2['FECHA']  = notas_b_c2['FECHA'].dt.strftime('%d/%m/%Y')
notas_b_s1['FECHA']  = notas_b_s1['FECHA'].dt.strftime('%d/%m/%Y')
notas_b_s2['FECHA']  = notas_b_s2['FECHA'].dt.strftime('%d/%m/%Y')
notas_b_l['FECHA']  = notas_b_l['FECHA'].dt.strftime('%d/%m/%Y')
notas_b_m1['FECHA'] = notas_b_m1['FECHA'].dt.strftime('%d/%m/%Y')
notas_b_m2['FECHA'] = notas_b_m2['FECHA'].dt.strftime('%d/%m/%Y')
notas_b_e1['FECHA'] = notas_b_e1['FECHA'].dt.strftime('%d/%m/%Y')
notas_b_e2['FECHA'] = notas_b_e2['FECHA'].dt.strftime('%d/%m/%Y')
notas_b_steam['FECHA'] = notas_b_steam['FECHA'].dt.strftime('%d/%m/%Y')

notas_b_m2 = notas_b_m2.sort_values(by=['ESTUDIANTE', 'ASIGNATURA', 'BLOQUE', 'ETAPA'])
notas_b_m1 = notas_b_m1.sort_values(by=['ESTUDIANTE', 'ASIGNATURA', 'BLOQUE', 'ETAPA'])
notas_b_c = notas_b_c.sort_values(by=['ESTUDIANTE', 'ASIGNATURA', 'BLOQUE', 'ETAPA'])
notas_b_c2 = notas_b_c2.sort_values(by=['ESTUDIANTE', 'ASIGNATURA', 'BLOQUE', 'ETAPA'])
notas_b_s1 = notas_b_s1.sort_values(by=['ESTUDIANTE', 'ASIGNATURA', 'BLOQUE', 'ETAPA'])
notas_b_s2 = notas_b_s2.sort_values(by=['ESTUDIANTE', 'ASIGNATURA', 'BLOQUE', 'ETAPA'])
notas_b_l = notas_b_l.sort_values(by=['ESTUDIANTE', 'ASIGNATURA', 'BLOQUE', 'ETAPA'])
notas_b_e1 = notas_b_e1.sort_values(by=['ESTUDIANTE', 'ASIGNATURA', 'BLOQUE', 'ETAPA'])
notas_b_e2 = notas_b_e2.sort_values(by=['ESTUDIANTE', 'ASIGNATURA', 'BLOQUE', 'ETAPA'])
notas_b_steam = notas_b_steam.sort_values(by=['ESTUDIANTE', 'ASIGNATURA', 'BLOQUE', 'ETAPA'])

bloq = ['A','B','C','D']

notas_b_c     = notas_b_c[notas_b_c.iloc[:,6].isin(bloq)]
notas_b_c2    = notas_b_c2[notas_b_c2.iloc[:,6].isin(bloq)]
notas_b_s1    = notas_b_s1[notas_b_s1.iloc[:,6].isin(bloq)]
notas_b_s2    = notas_b_s2[notas_b_s2.iloc[:,6].isin(bloq)]
notas_b_l     = notas_b_l[notas_b_l.iloc[:,6].isin(bloq)]
notas_b_m1    = notas_b_m1[notas_b_m1.iloc[:,6].isin(bloq)]
notas_b_m2    = notas_b_m2[notas_b_m2.iloc[:,6].isin(bloq)]
notas_b_e1    = notas_b_e1[notas_b_e1.iloc[:,6].isin(bloq)]
notas_b_e2    = notas_b_e2[notas_b_e2.iloc[:,6].isin(bloq)]
notas_b_steam = notas_b_steam[notas_b_steam.iloc[:,6].isin(bloq)]

notas_b_c  = notas_b_c.reset_index(drop=True)
notas_b_c2  = notas_b_c2.reset_index(drop=True)
notas_b_s1 = notas_b_s1.reset_index(drop=True)
notas_b_s2 = notas_b_s2.reset_index(drop=True)
notas_b_l  = notas_b_l.reset_index(drop=True)
notas_b_m1 = notas_b_m1.reset_index(drop=True)
notas_b_m2 = notas_b_m2.reset_index(drop=True)
notas_b_e1 = notas_b_e1.reset_index(drop=True)
notas_b_e2 = notas_b_e2.reset_index(drop=True)
notas_b_steam = notas_b_steam.reset_index(drop=True)


longitud_bloque = pd.DataFrame({'Bloque': np.repeat(['A','B','C','D'], 5)})

D1 = 'D1'
D2 = 'D2'
D3 = 'D3'
D4 = 'D4'
D5 = 'D5'

longitud_desempeno1 = [D1, D2, D3, D4, D5, D1, D2, D3, D4, D5, D1, D2, D3, D4, D5, D1, D2, D3, D4, D5]
longitud_desempeno = pd.DataFrame({'Etapa': longitud_desempeno1})

longitud_bloque = pd.concat([longitud_bloque, longitud_desempeno],axis = 1, ignore_index=True)


# In[11]:


################################################## MATEMATICAS 1 ###############################################################

print('-------------------------------Errores M1-----------------------------')

indices_a_eliminar_m1 = []

materias_especificas_6_7 = ['Animaplanos','Aritmética', 'Geometría', 'Estadística', 'Dibujo técnico', 'Sistemas']
materias_especificas_8_9 = ['Animaplanos','Álgebra', 'Geometría', 'Estadística', 'Dibujo técnico', 'Sistemas','Metodología']
materias_especificas_10 = ['Animaplanos','Trigonometría', 'Matemática financiera', 'Estadística', 'Dibujo técnico', 'Sistemas','Metodología']
materias_especificas_11 = ['Animaplanos','Cálculo', 'Matemática financiera', 'Estadística', 'Dibujo técnico', 'Sistemas','Metodología']

for i in range(len(notas_b_m1)):

    # nombres que no están en el listado general
    
    if notas_b_m1.iloc[i, 2] not in nombres:
        
        print(f"{notas_b_m1.iloc[i, 2]} no está en el listado general se elimina nota del {notas_b_m1.iloc[i, 0]} de la asignatura {notas_b_m1.iloc[i, 5]}")
        print(' ')
        indices_a_eliminar_m1.append(i)
        continue
        

    # asignaturas que no son de acuerdo al grado
    
    if notas_b_m1.iloc[i,2] not in excepciones:
        
        if (notas_b_m1.iloc[i, 3] == 6) or (notas_b_m1.iloc[i, 3] == 7):
            if notas_b_m1.iloc[i, 5] not in materias_especificas_6_7:
                print(f"{notas_b_m1.iloc[i, 5]} no es de grado {int(notas_b_m1.iloc[i, 3])} se elimina nota de {notas_b_m1.iloc[i, 2]} ")
                print(f"del día {notas_b_m1.iloc[i, 0]}")
                print(' ')
                indices_a_eliminar_m1.append(i)
                continue
            

        if (notas_b_m1.iloc[i, 3] == 8) or (notas_b_m1.iloc[i, 3] == 9):
            if notas_b_m1.iloc[i, 5] not in materias_especificas_8_9:
                print(f"{notas_b_m1.iloc[i, 5]} no es de grado {int(notas_b_m1.iloc[i, 3])} se elimina nota de {notas_b_m1.iloc[i, 2]} ")
                print(f"del día {notas_b_m1.iloc[i, 0]}")
                print(' ')
                indices_a_eliminar_m1.append(i)
                continue
            

        if notas_b_m1.iloc[i, 3] == 10:
            if notas_b_m1.iloc[i, 5] not in materias_especificas_10:
                print(f"{notas_b_m1.iloc[i, 5]} no es de grado {int(notas_b_m1.iloc[i, 3])} se elimina nota de {notas_b_m1.iloc[i, 2]} ")
                print(f"del día {notas_b_m1.iloc[i, 0]}")
                print(' ')
                indices_a_eliminar_m1.append(i)
                continue
    
        if notas_b_m1.iloc[i, 3] == 11:
            if notas_b_m1.iloc[i, 5] not in materias_especificas_11:
                print(f"{notas_b_m1.iloc[i, 5]} no es de grado {int(notas_b_m1.iloc[i, 3])} se elimina nota de {notas_b_m1.iloc[i, 2]} ")
                print(f"del día {notas_b_m1.iloc[i, 0]}")
                print(' ')
                indices_a_eliminar_m1.append(i)
                continue
        
        
            

    # desempeños duplicados
    
    notas_estudiante = dfb[(dfb.iloc[:, 2] == notas_b_m1.iloc[i, 2]) &
                           (dfb.iloc[:, 5] == notas_b_m1.iloc[i, 5]) &
                           (dfb.iloc[:, 3] == notas_b_m1.iloc[i, 3])]

    for k in range(len(notas_estudiante)):
        
        if ((notas_b_m1.iloc[i, 6] == notas_estudiante.iloc[k, 6]) &
            (notas_b_m1.iloc[i, 9] == notas_estudiante.iloc[k, 9])):
            
            print(f"{notas_b_m1.iloc[i, 2]}, reportado el día {notas_b_m1.iloc[i, 0]}, de la asignatura {notas_b_m1.iloc[i, 5]}, bloque {notas_b_m1.iloc[i, 6]}, etapa {notas_b_m1.iloc[i, 9]}, ya está reportado, se elimina.")
            print(' ')
            indices_a_eliminar_m1.append(i)
            continue
            
            
    fila_actual = notas_b_m1.iloc[i]
    
    for j in range(i + 1, len(notas_b_m1)):
        
        fila_comparar = notas_b_m1.iloc[j]
    
    # Verificar si las columnas 2, 5, 6 y 9 son iguales en ambas filas
        if (fila_actual.iloc[2] == fila_comparar.iloc[2] and
            fila_actual.iloc[5] == fila_comparar.iloc[5] and
            fila_actual.iloc[6] == fila_comparar.iloc[6] and
            fila_actual.iloc[9] == fila_comparar.iloc[9]):
            print(f'{fila_actual.iloc[2]} de la materia {fila_actual.iloc[5]} del bloque {fila_actual.iloc[6]} la etapa {fila_actual.iloc[9]} se reporto dos veces')
            print(f'los dias {fila_actual.iloc[0]} y {fila_comparar.iloc[0]}')
            print(f'se elimina el del dia {fila_comparar.iloc[0]} que tiene nota {fila_comparar.iloc[10]} ')
            print(' ')
            indices_a_eliminar_m1.append(j)

notas_b_m1.drop(indices_a_eliminar_m1, inplace=True)
notas_b_m1 = notas_b_m1.reset_index(drop=True)


###### Desempeños que no sigen el orden de la base de datos ##########

indices_a_eliminar_m1_1 = []

for i in range(len(notas_b_m1)):
    evaluado = False 
    if evaluado:
        continue 
    estudiante = notas_b_m1.iloc[i, 2]
    grado      = notas_b_m1.iloc[i, 3]
    materia    = notas_b_m1.iloc[i, 5]
    dia        = notas_b_m1.iloc[i, 0]
    bloque     = notas_b_m1.iloc[i, 6]
    desempeno  = notas_b_m1.iloc[i, 9]
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
            indices_a_eliminar_m1_1.append(i)
            break
        if ((bloque    == longitud_bloque.iloc[r, 0]) &
            (desempeno == longitud_bloque.iloc[r, 1])):
            if len(notas_estudiante) != r:
                #evaluar cada fila del vector que da longitud de bloques y desempeños del bloque y desempeño siguiente al reportado
                for h in range(r+1, len(longitud_bloque)):
                    #comparar con bloque y etapa de notas del estudiante
                    for p in range(len(bloque_etapa)): 
                        if (longitud_bloque.iloc[h,0] == bloque_etapa.iloc[p,0]) and (longitud_bloque.iloc[h,1] == bloque_etapa.iloc[p,1]):
                            fila_para_agregar = notas_b_m1.iloc[i].to_frame().T 
                            dfb = pd.concat([dfb, fila_para_agregar], ignore_index=True)
                            evaluado = True
                            break               
                if evaluado:
                    break    
                print(f'{estudiante} reportado el dia {dia} de la asignatura {materia}, bloque {bloque}, etapa {desempeno}')
                print('no coincide con una nota faltante o que sea el siguiente desempeño a reportar y se elimina.')
                print(' ')
                indices_a_eliminar_m1_1.append(i)
                evaluado = True
                break                        
            if len(notas_estudiante) == r:
                fila_para_agregar = notas_b_m1.iloc[i].to_frame().T
                dfb = pd.concat([dfb, fila_para_agregar], ignore_index=True)
                break    
notas_b_m1.drop(indices_a_eliminar_m1_1, inplace=True)
notas_b_m1 = notas_b_m1.reset_index(drop=True)
                                             
################################################## MATEMATICAS 2 ###############################################################

print('-------------------------------Errores M2-----------------------------')

indices_a_eliminar_m2 = []

materias_especificas_6_7 = ['Animaplanos','Aritmética', 'Geometría', 'Estadística', 'Dibujo técnico', 'Sistemas']
materias_especificas_8_9 = ['Animaplanos','Álgebra', 'Geometría', 'Estadística', 'Dibujo técnico', 'Sistemas']
materias_especificas_10 = ['Animaplanos','Álgebra','Geometría','Trigonometría', 'Matemática financiera', 'Estadística', 'Dibujo técnico', 'Sistemas','Metodología']
materias_especificas_11 = ['Animaplanos','Cálculo', 'Matemática financiera', 'Estadística', 'Dibujo técnico', 'Sistemas','Metodología']

for i in range(len(notas_b_m2)):

    # nombres que no están en el listado general
    
    if notas_b_m2.iloc[i, 2] not in nombres:
        
        print(f"{notas_b_m2.iloc[i, 2]} no está en el listado general se elimina nota del {notas_b_m2.iloc[i, 0]} de la asignatura {notas_b_m2.iloc[i, 5]}")
        print(' ')
        indices_a_eliminar_m2.append(i)
        continue
        

    # asignaturas que no son de acuerdo al grado  
    if notas_b_m2.iloc[i,2] not in excepciones:
        if (notas_b_m2.iloc[i, 3] == 6) or (notas_b_m2.iloc[i, 3] == 7):
            if notas_b_m2.iloc[i, 5] not in materias_especificas_6_7:
                print(f"{notas_b_m2.iloc[i, 5]} no es de grado {int(notas_b_m2.iloc[i, 3])} se elimina nota de {notas_b_m2.iloc[i, 2]} ")
                print(f"del día {notas_b_m2.iloc[i, 0]}")
                print(' ')
                indices_a_eliminar_m2.append(i)
                continue
            

        if (notas_b_m2.iloc[i, 3] == 8) or (notas_b_m2.iloc[i, 3] == 9):
            if notas_b_m2.iloc[i, 5] not in materias_especificas_8_9:
                print(f"{notas_b_m2.iloc[i, 5]} no es de grado {int(notas_b_m2.iloc[i, 3])} se elimina nota de {notas_b_m2.iloc[i, 2]} ")
                print(f"del día {notas_b_m2.iloc[i, 0]}")
                print(' ')
                indices_a_eliminar_m2.append(i)
                continue
            

        if notas_b_m2.iloc[i, 3] == 10:
            if notas_b_m2.iloc[i, 5] not in materias_especificas_10:
                print(f"{notas_b_m2.iloc[i, 5]} no es de grado {int(notas_b_m2.iloc[i, 3])} se elimina nota de {notas_b_m2.iloc[i, 2]} ")
                print(f"del día {notas_b_m2.iloc[i, 0]}")
                print(' ')
                indices_a_eliminar_m2.append(i)
                continue
    
        if notas_b_m2.iloc[i, 3] == 11:
            if notas_b_m2.iloc[i, 5] not in materias_especificas_11:
                print(f"{notas_b_m2.iloc[i, 5]} no es de grado {int(notas_b_m2.iloc[i, 3])} se elimina nota de {notas_b_m2.iloc[i, 2]} ")
                print(f"del día {notas_b_m2.iloc[i, 0]}")
                print(' ')
                indices_a_eliminar_m2.append(i)
                continue
            
     # desempeños duplicados

    notas_estudiante = dfb[(dfb.iloc[:, 2] == notas_b_m2.iloc[i, 2]) &
                       (dfb.iloc[:, 5] == notas_b_m2.iloc[i, 5]) &
                       (dfb.iloc[:, 3] == notas_b_m2.iloc[i, 3])]

    for k in range(len(notas_estudiante)):
        
        if ((notas_b_m2.iloc[i, 6] == notas_estudiante.iloc[k, 6]) &
           (notas_b_m2.iloc[i, 9] == notas_estudiante.iloc[k, 9])):
            
            print(f"{notas_b_m2.iloc[i, 2]}, reportado el día {notas_b_m2.iloc[i, 0]}, de la asignatura {notas_b_m2.iloc[i, 5]}, bloque {notas_b_m2.iloc[i, 6]}, etapa {notas_b_m2.iloc[i, 9]}, ya está reportado, se elimina.")
            print(' ')
            indices_a_eliminar_m2.append(i)
            
            
    fila_actual = notas_b_m2.iloc[i]
    
    for j in range(i + 1, len(notas_b_m2)):
        
        fila_comparar = notas_b_m2.iloc[j]
        
        # Verificar si las columnas 2, 5, 6 y 9 son iguales en ambas filas
        if (fila_actual.iloc[2] == fila_comparar.iloc[2] and
            fila_actual.iloc[5] == fila_comparar.iloc[5] and
            fila_actual.iloc[6] == fila_comparar.iloc[6] and
            fila_actual.iloc[9] == fila_comparar.iloc[9]):
            print(f'{fila_actual.iloc[2]} de la materia {fila_actual.iloc[5]} del bloque {fila_actual.iloc[6]} la etapa {fila_actual.iloc[9]} se reporto dos veces')
            print(f'los dias {fila_actual.iloc[0]} y {fila_comparar.iloc[0]}')
            print(f'se elimina el del dia {fila_comparar.iloc[0]} que tiene nota {fila_comparar.iloc[10]} ')
            print(' ')
            indices_a_eliminar_m2.append(j)

notas_b_m2.drop(indices_a_eliminar_m2, inplace=True)
notas_b_m2 = notas_b_m2.reset_index(drop=True)

###### Desempeños que no sigen el orden de la base de datos ##########

indices_a_eliminar_m2_1 = []

for i in range(len(notas_b_m2)):
    evaluado = False 
    if evaluado:
        continue 
    estudiante = notas_b_m2.iloc[i, 2]
    grado      = notas_b_m2.iloc[i, 3]
    materia    = notas_b_m2.iloc[i, 5]
    dia        = notas_b_m2.iloc[i, 0]
    bloque     = notas_b_m2.iloc[i, 6]
    desempeno  = notas_b_m2.iloc[i, 9]
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
            indices_a_eliminar_m2_1.append(i)
            break
        if ((bloque    == longitud_bloque.iloc[r, 0]) &
            (desempeno == longitud_bloque.iloc[r, 1])):
            if len(notas_estudiante) != r:
                #evaluar cada fila del vector que da longitud de bloques y desempeños del bloque y desempeño siguiente al reportado
                for h in range(r+1, len(longitud_bloque)):
                    #comparar con bloque y etapa de notas del estudiante
                    for p in range(len(bloque_etapa)): 
                        if (longitud_bloque.iloc[h,0] == bloque_etapa.iloc[p,0]) and (longitud_bloque.iloc[h,1] == bloque_etapa.iloc[p,1]):
                            fila_para_agregar = notas_b_m2.iloc[i].to_frame().T
                            dfb = pd.concat([dfb, fila_para_agregar], ignore_index=True)
                            evaluado = True
                            break               
                if evaluado:
                    break    
                print(f'{estudiante} reportado el dia {dia} de la asignatura {materia}, bloque {bloque}, etapa {desempeno}')
                print('no coincide con una nota faltante o que sea el siguiente desempeño a reportar y se elimina.')
                print(' ')
                indices_a_eliminar_m2_1.append(i)
                evaluado = True
                break                        
            if len(notas_estudiante) == r:
                fila_para_agregar = notas_b_m2.iloc[i].to_frame().T
                dfb = pd.concat([dfb, fila_para_agregar], ignore_index=True)
                break    
notas_b_m2.drop(indices_a_eliminar_m2_1, inplace=True)
notas_b_m2 = notas_b_m2.reset_index(drop=True)
            

  

 
####################################################### CIENCIAS 1 ################################################################
                
print('-------------------------------Errores C1-----------------------------')

indices_a_eliminar_c = []

materias_especificas_6_7_8_9_10 = ['Biología', 'Química', 'Medio ambiente', 'Física','Metodología','Animaplanos']
materias_especificas_11 = ['Metodología','Química', 'Medio ambiente', 'Física','Animaplanos']

for i in range(len(notas_b_c)):

    # nombres que no están en el listado general
    
    if notas_b_c.iloc[i, 2] not in nombres:
        
        print(f"{notas_b_c.iloc[i, 2]} no está en el listado general se elimina nota del {notas_b_c.iloc[i, 0]} de la asignatura {notas_b_c.iloc[i, 5]}")
        print(' ')
        indices_a_eliminar_c.append(i)
        continue
        

    # asignaturas que no son de acuerdo al grado
    
    if notas_b_c.iloc[i,2] not in excepciones:
        if notas_b_c.iloc[i, 3] in (6,7,8,9,10):
            if notas_b_c.iloc[i, 5] not in materias_especificas_6_7_8_9_10:
                print(f"{notas_b_c.iloc[i, 5]} no es de grado {int(notas_b_c.iloc[i, 3])} se elimina nota de {notas_b_c.iloc[i, 5]} ")
                print(f"del día {notas_b_c.iloc[i, 0]}")
                print(' ')
                indices_a_eliminar_c.append(i)
                continue
            

        if notas_b_c.iloc[i, 3] == 11:
            if notas_b_c.iloc[i, 5] not in materias_especificas_11:
                print(f"{notas_b_c.iloc[i, 5]} no es de grado {int(notas_b_c.iloc[i, 3])} se elimina nota de {notas_b_c.iloc[i, 5]} ")
                print(f"del día {notas_b_c.iloc[i, 0]}")
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
            print(f'se elimina el del dia {fila_comparar[0]} que tiene nota {fila_comparar.iloc[10]} ')
            print(' ')
            indices_a_eliminar_c.append(j)
    
    
    
notas_b_c.drop(indices_a_eliminar_c, inplace=True)
notas_b_c = notas_b_c.reset_index(drop=True)

###### Desempeños que no sigen el orden de la base de datos ##########

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
            
####################################################### CIENCIAS 2 ################################################################
                
print('-------------------------------Errores C2-----------------------------') 


indices_a_eliminar_c2 = []

materias_especificas_6_7_8_9_10 = ['Biología', 'Química', 'Medio ambiente', 'Física','Metodología','Animaplanos']
materias_especificas_11 = ['Metodología','Química', 'Medio ambiente', 'Física','Animaplanos']

for i in range(len(notas_b_c2)):

    # nombres que no están en el listado general
    
    if notas_b_c2.iloc[i, 2] not in nombres:
        
        print(f"{notas_b_c2.iloc[i, 2]} no está en el listado general se elimina nota del {notas_b_c2.iloc[i, 0]} de la asignatura {notas_b_c2.iloc[i, 5]}")
        print(' ')
        indices_a_eliminar_c2.append(i)
        continue
        

    # asignaturas que no son de acuerdo al grado
    
    if notas_b_c2.iloc[i,2] not in excepciones:
        if notas_b_c2.iloc[i, 3] in (6,7,8,9,10):
            if notas_b_c2.iloc[i, 5] not in materias_especificas_6_7_8_9_10:
                print(f"{notas_b_c2.iloc[i, 5]} no es de grado {int(notas_b_c2.iloc[i, 3])} se elimina nota de {notas_b_c2.iloc[i, 5]} ")
                print(f"del día {notas_b_c2.iloc[i, 0]}")
                print(' ')
                indices_a_eliminar_c2.append(i)
                continue
            

        if notas_b_c2.iloc[i, 3] == 11:
            if notas_b_c2.iloc[i, 5] not in materias_especificas_11:
                print(f"{notas_b_c2.iloc[i, 5]} no es de grado {int(notas_b_c2.iloc[i, 3])} se elimina nota de {notas_b_c2.iloc[i, 5]} ")
                print(f"del día {notas_b_c2.iloc[i, 0]}")
                print(' ')
                indices_a_eliminar_c2.append(i)
                continue
            
    # desempeños duplicados

    notas_estudiante = dfb[(dfb.iloc[:, 2] == notas_b_c2.iloc[i, 2]) &
                       (dfb.iloc[:, 5] == notas_b_c2.iloc[i, 5]) &
                       (dfb.iloc[:, 3] == notas_b_c2.iloc[i, 3])]

    for k in range(len(notas_estudiante)):
    
        if ((notas_b_c2.iloc[i, 6] == notas_estudiante.iloc[k, 6]) &
            (notas_b_c2.iloc[i, 9] == notas_estudiante.iloc[k, 9])):
            
            print(f"{notas_b_c2.iloc[i, 2]}, reportado el día {notas_b_c2.iloc[i, 0]}, de la asignatura {notas_b_c2.iloc[i, 5]}, bloque {notas_b_c2.iloc[i, 6]}, etapa {notas_b_c2.iloc[i, 9]}, ya está reportado, se elimina.")
            print(' ')
            indices_a_eliminar_c2.append(i)
    
    fila_actual = notas_b_c2.iloc[i]
    
    for j in range(i + 1, len(notas_b_c2)):
        
        fila_comparar = notas_b_c2.iloc[j]
        
        # Verificar si las columnas 2, 5, 6 y 9 son iguales en ambas filas
        if (fila_actual.iloc[2] == fila_comparar.iloc[2] and
            fila_actual.iloc[5] == fila_comparar.iloc[5] and
            fila_actual.iloc[6] == fila_comparar.iloc[6] and
            fila_actual.iloc[9] == fila_comparar.iloc[9]):
            print(f'{fila_actual.iloc[2]} de la materia {fila_actual.iloc[5]} del bloque {fila_actual.iloc[6]} la etapa {fila_actual.iloc[9]} se reporto dos veces')
            print(f'los dias {fila_actual.iloc[0]} y {fila_comparar.iloc[0]}')
            print(f'se elimina el del dia {fila_comparar[0]} que tiene nota {fila_comparar.iloc[10]} ')
            print(' ')
            indices_a_eliminar_c2.append(j)
    
    
    
notas_b_c2.drop(indices_a_eliminar_c2, inplace=True)
notas_b_c2 = notas_b_c2.reset_index(drop=True)

###### Desempeños que no sigen el orden de la base de datos ##########

indices_a_eliminar_c2_1 = []

for i in range(len(notas_b_c2)):
    evaluado = False 
    if evaluado:
        continue 
    estudiante = notas_b_c2.iloc[i, 2]
    grado      = notas_b_c2.iloc[i, 3]
    materia    = notas_b_c2.iloc[i, 5]
    dia        = notas_b_c2.iloc[i, 0]
    bloque     = notas_b_c2.iloc[i, 6]
    desempeno  = notas_b_c2.iloc[i, 9]
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
            indices_a_eliminar_c2_1.append(i)
            break
        if ((bloque    == longitud_bloque.iloc[r, 0]) &
            (desempeno == longitud_bloque.iloc[r, 1])):
            if len(notas_estudiante) != r:
                #evaluar cada fila del vector que da longitud de bloques y desempeños del bloque y desempeño siguiente al reportado
                for h in range(r+1, len(longitud_bloque)):
                    #comparar con bloque y etapa de notas del estudiante
                    for p in range(len(bloque_etapa)): 
                        if (longitud_bloque.iloc[h,0] == bloque_etapa.iloc[p,0]) and (longitud_bloque.iloc[h,1] == bloque_etapa.iloc[p,1]):
                            fila_para_agregar = notas_b_c2.iloc[i].to_frame().T 
                            dfb = pd.concat([dfb, fila_para_agregar], ignore_index=True)
                            evaluado = True
                            break               
                    if evaluado:
                        break    
                    print(f'{estudiante} reportado el dia {dia} de la asignatura {materia}, bloque {bloque}, etapa {desempeno}')
                    print('no coincide con una nota faltante o que sea el siguiente desempeño a reportar y se elimina.')
                    print(' ')
                    indices_a_eliminar_c2_1.append(i)
                    evaluado = True
                    break                        
            if len(notas_estudiante) == r:
                fila_para_agregar = notas_b_c2.iloc[i].to_frame().T
                dfb = pd.concat([dfb, fila_para_agregar], ignore_index=True)
                break    
notas_b_c2.drop(indices_a_eliminar_c2_1, inplace=True)
notas_b_c2 = notas_b_c2.reset_index(drop=True)


#################################################### SOCIALES ######################################################################
print('-------------------------------Errores S1-----------------------------')

indices_a_eliminar_s1 = []

materias_especificas_6_7_8_9 = ['Historia', 'Geografía', 'Participación política', 'Filosofía']
materias_especificas_10_11 = ['Metodología', 'Ciencias económicas', 'Ciencias políticas', 'Filosofía']

for i in range(len(notas_b_s1)):

    # nombres que no están en el listado general
    
    if notas_b_s1.iloc[i, 2] not in nombres:
        
        print(f"{notas_b_s2.iloc[i, 2]} no está en el listado general se elimina nota del {notas_b_s2.iloc[i, 0]} de la asignatura {notas_b_s2.iloc[i, 5]}")
        print(' ')
        indices_a_eliminar_s1.append(i)
        continue
        
        # asignaturas que no son de acuerdo al grado
    
    if notas_b_s1.iloc[i,2] not in excepciones:
        if ((notas_b_s1.iloc[i, 3] in (6,7,8,9)) & (notas_b_s1.iloc[i, 2] != 'VALCÁRCEL CASTRO VIOLETA')):
            if notas_b_s1.iloc[i, 5] not in materias_especificas_6_7_8_9:
                print(f"{notas_b_s1.iloc[i, 5]} no es de grado {int(notas_b_s1.iloc[i, 3])} se elimina nota de {notas_b_s1.iloc[i, 2]} ")
                print(f"del día {notas_b_s1.iloc[i, 0]}")
                print(' ')
                indices_a_eliminar_s1.append(i)
                continue
            

        if ((notas_b_s1.iloc[i, 3] in (10,11)) & (notas_b_s1.iloc[i, 2] != 'VALCÁRCEL CASTRO VIOLETA')):
            if notas_b_s1.iloc[i, 5] not in materias_especificas_10_11:
                print(f"{notas_b_s1.iloc[i, 5]} no es de grado {int(notas_b_s1.iloc[i, 3])} se elimina nota de {notas_b_s1.iloc[i, 2]} ")
                print(f"del día {notas_b_s1.iloc[i, 0]}")
                print(' ')
                indices_a_eliminar_s1.append(i)
                continue
            
    # desempeños duplicados
 
    notas_estudiante = dfb[(dfb.iloc[:, 2] == notas_b_s1.iloc[i, 2]) &
                       (dfb.iloc[:, 5] == notas_b_s1.iloc[i, 5]) &
                       (dfb.iloc[:, 3] == notas_b_s1.iloc[i, 3])]

    for k in range(len(notas_estudiante)):
    
        if ((notas_b_s1.iloc[i, 6] == notas_estudiante.iloc[k, 6]) &
            (notas_b_s1.iloc[i, 9] == notas_estudiante.iloc[k, 9])):
            
            print(f"{notas_b_s1.iloc[i, 2]}, reportado el día {notas_b_s1.iloc[i, 0]}, de la asignatura {notas_b_s1.iloc[i, 5]}, bloque {notas_b_s1.iloc[i, 6]}, etapa {notas_b_s1.iloc[i, 9]}, ya está reportado, se elimina.")
            print(' ')
            indices_a_eliminar_s1.append(i)
            
    fila_actual = notas_b_s1.iloc[i]
    
    for j in range(i + 1, len(notas_b_s1)):
        
        fila_comparar = notas_b_s1.iloc[j]
        
        # Verificar si las columnas 2, 5, 6 y 9 son iguales en ambas filas
        if (fila_actual.iloc[2] == fila_comparar.iloc[2] and
            fila_actual.iloc[5] == fila_comparar.iloc[5] and
            fila_actual.iloc[6] == fila_comparar.iloc[6] and
            fila_actual.iloc[9] == fila_comparar.iloc[9]):
            print(f'{fila_actual.iloc[2]} de la materia {fila_actual.iloc[5]} del bloque {fila_actual.iloc[6]} la etapa {fila_actual.iloc[9]} se reporto dos veces')
            print(f'los dias {fila_actual.iloc[0]} y {fila_comparar.iloc[0]}')
            print(f'se elimina el del dia {fila_comparar.iloc[0]} que tiene nota {fila_comparar.iloc[10]} ')
            print(' ')
            indices_a_eliminar_s1.append(j)

notas_b_s1.drop(indices_a_eliminar_s1, inplace=True)
notas_b_s1 = notas_b_s1.reset_index(drop=True)

###### Desempeños que no sigen el orden de la base de datos ##########

indices_a_eliminar_s_1 = []

for i in range(len(notas_b_s1)):
    evaluado = False 
    if evaluado:
        continue 
    estudiante = notas_b_s1.iloc[i, 2]
    grado      = notas_b_s1.iloc[i, 3]
    materia    = notas_b_s1.iloc[i, 5]
    dia        = notas_b_s1.iloc[i, 0]
    bloque     = notas_b_s1.iloc[i, 6]
    desempeno  = notas_b_s1.iloc[i, 9]
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
                            fila_para_agregar = notas_b_s1.iloc[i].to_frame().T 
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
                fila_para_agregar = notas_b_s1.iloc[i].to_frame().T
                dfb = pd.concat([dfb, fila_para_agregar], ignore_index=True)
                break    
notas_b_s1.drop(indices_a_eliminar_s_1, inplace=True)
notas_b_s1 = notas_b_s1.reset_index(drop=True)


print('-------------------------------Errores S2-----------------------------')

indices_a_eliminar_s2 = []

materias_especificas_6_7_8_9 = ['Historia', 'Geografía', 'Participación política', 'Filosofía']
materias_especificas_10_11 = ['Metodología', 'Ciencias económicas', 'Ciencias políticas', 'Filosofía']

for i in range(len(notas_b_s2)):

    # nombres que no están en el listado general
    
    if notas_b_s2.iloc[i, 2] not in nombres:
        
        print(f"{notas_b_s2.iloc[i, 2]} no está en el listado general se elimina nota del {notas_b_s2.iloc[i, 0]} de la asignatura {notas_b_s2.iloc[i, 5]}")
        print(' ')
        indices_a_eliminar_s2.append(i)
        continue
        
    # asignaturas que no son de acuerdo al grado
    
    if notas_b_s2.iloc[i,2] not in excepciones:
        if ((notas_b_s2.iloc[i, 3] in (6,7,8,9)) & (notas_b_s2.iloc[i, 2] != 'VALCÁRCEL CASTRO VIOLETA')):
            if notas_b_s2.iloc[i, 5] not in materias_especificas_6_7_8_9:
                print(f"{notas_b_s2.iloc[i, 5]} no es de grado {int(notas_b_s2.iloc[i, 3])} se elimina nota de {notas_b_s2.iloc[i, 2]} ")
                print(f"del día {notas_b_s2.iloc[i, 0]}")
                print(' ')
                indices_a_eliminar_s2.append(i)
                continue
            

        if ((notas_b_s2.iloc[i, 3] in (10,11)) & (notas_b_s2.iloc[i, 2] != 'VALCÁRCEL CASTRO VIOLETA')):
            if notas_b_s2.iloc[i, 5] not in materias_especificas_10_11:
                print(f"{notas_b_s2.iloc[i, 5]} no es de grado {int(notas_b_s2.iloc[i, 3])} se elimina nota de {notas_b_s2.iloc[i, 2]} ")
                print(f"del día {notas_b_s2.iloc[i, 0]}")
                print(' ')
                indices_a_eliminar_s2.append(i)
                continue
            
    # desempeños duplicados
 
    notas_estudiante = dfb[(dfb.iloc[:, 2] == notas_b_s2.iloc[i, 2]) &
                       (dfb.iloc[:, 5] == notas_b_s2.iloc[i, 5]) &
                       (dfb.iloc[:, 3] == notas_b_s2.iloc[i, 3])]

    for k in range(len(notas_estudiante)):
    
        if ((notas_b_s2.iloc[i, 6] == notas_estudiante.iloc[k, 6]) &
            (notas_b_s2.iloc[i, 9] == notas_estudiante.iloc[k, 9])):
            
            print(f"{notas_b_s2.iloc[i, 2]}, reportado el día {notas_b_s2.iloc[i, 0]}, de la asignatura {notas_b_s2.iloc[i, 5]}, bloque {notas_b_s2.iloc[i, 6]}, etapa {notas_b_s2.iloc[i, 9]}, ya está reportado, se elimina.")
            print(' ')
            indices_a_eliminar_s2.append(i)
            
    fila_actual = notas_b_s2.iloc[i]
    
    for j in range(i + 1, len(notas_b_s2)):
        
        fila_comparar = notas_b_s2.iloc[j]
        
        # Verificar si las columnas 2, 5, 6 y 9 son iguales en ambas filas
        if (fila_actual.iloc[2] == fila_comparar.iloc[2] and
            fila_actual.iloc[5] == fila_comparar.iloc[5] and
            fila_actual.iloc[6] == fila_comparar.iloc[6] and
            fila_actual.iloc[9] == fila_comparar.iloc[9]):
            print(f'{fila_actual.iloc[2]} de la materia {fila_actual.iloc[5]} del bloque {fila_actual.iloc[6]} la etapa {fila_actual.iloc[9]} se reporto dos veces')
            print(f'los dias {fila_actual.iloc[0]} y {fila_comparar.iloc[0]}')
            print(f'se elimina el del dia {fila_comparar.iloc[0]} que tiene nota {fila_comparar.iloc[10]} ')
            print(' ')
            indices_a_eliminar_s2.append(j)

notas_b_s2.drop(indices_a_eliminar_s2, inplace=True)
notas_b_s2 = notas_b_s2.reset_index(drop=True)

###### Desempeños que no sigen el orden de la base de datos ##########

indices_a_eliminar_s_2 = []

for i in range(len(notas_b_s2)):
    evaluado = False 
    if evaluado:
        continue 
    estudiante = notas_b_s2.iloc[i, 2]
    grado      = notas_b_s2.iloc[i, 3]
    materia    = notas_b_s2.iloc[i, 5]
    dia        = notas_b_s2.iloc[i, 0]
    bloque     = notas_b_s2.iloc[i, 6]
    desempeno  = notas_b_s2.iloc[i, 9]
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
            indices_a_eliminar_s_2.append(i)
            break
        if ((bloque    == longitud_bloque.iloc[r, 0]) &
            (desempeno == longitud_bloque.iloc[r, 1])):
            if len(notas_estudiante) != r:
                #evaluar cada fila del vector que da longitud de bloques y desempeños del bloque y desempeño siguiente al reportado
                for h in range(r+1, len(longitud_bloque)):
                    #comparar con bloque y etapa de notas del estudiante
                    for p in range(len(bloque_etapa)): 
                        if (longitud_bloque.iloc[h,0] == bloque_etapa.iloc[p,0]) and (longitud_bloque.iloc[h,1] == bloque_etapa.iloc[p,1]):
                            fila_para_agregar = notas_b_s2.iloc[i].to_frame().T 
                            dfb = pd.concat([dfb, fila_para_agregar], ignore_index=True)
                            evaluado = True
                            break               
                if evaluado:
                    break    
                print(f'{estudiante} reportado el dia {dia} de la asignatura {materia}, bloque {bloque}, etapa {desempeno}')
                print('no coincide con una nota faltante o que sea el siguiente desempeño a reportar y se elimina.')
                print(' ')
                indices_a_eliminar_s_2.append(i)
                evaluado = True
                break                        
            if len(notas_estudiante) == r:
                fila_para_agregar = notas_b_s2.iloc[i].to_frame().T
                dfb = pd.concat([dfb, fila_para_agregar], ignore_index=True)
                break    
notas_b_s2.drop(indices_a_eliminar_s_2, inplace=True)
notas_b_s2 = notas_b_s2.reset_index(drop=True)

######################################################### LENGUAJE ###############################################################

print('-------------------------------Errores L-----------------------------')

indices_a_eliminar_l = []

for i in range(len(notas_b_l)):
    
    asignaturas= ['Metodología','Comunicación y sistemas simbólicos','Producción e interpretación de textos','Pensamiento religioso','Filosofía']
    
    
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

###### Desempeños que no sigen el orden de la base de datos ##########

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


print('-------------------------------Errores E1-----------------------------')

indices_a_eliminar_e1 = []

for i in range(len(notas_b_e1)):

    # nombres que no están en el listado general
    
    if notas_b_e1.iloc[i, 2] not in nombres:
        
        print(f"{notas_b_e1.iloc[i, 2]} no está en el listado general se elimina nota del {notas_b_e1.iloc[i, 0]} de la asignatura {notas_b_e1.iloc[i, 5]}")
        print(' ')
        indices_a_eliminar_e1.append(i)
        continue

    # desempeños duplicados
    
    notas_estudiante = dfb[(dfb.iloc[:, 2] == notas_b_e1.iloc[i, 2]) &
                           (dfb.iloc[:, 5] == notas_b_e1.iloc[i, 5]) &
                           (dfb.iloc[:, 3] == notas_b_e1.iloc[i, 3])]

    for k in range(len(notas_estudiante)):
        
        if ((notas_b_e1.iloc[i, 6] == notas_estudiante.iloc[k, 6]) &
            (notas_b_e1.iloc[i, 9] == notas_estudiante.iloc[k, 9])):
            
            print(f"{notas_b_e1.iloc[i, 2]}, reportado el día {notas_b_e1.iloc[i, 0]}, de la asignatura {notas_b_e1.iloc[i, 5]}, bloque {notas_b_e1.iloc[i, 6]}, etapa {notas_b_e1.iloc[i, 9]}, ya está reportado, se elimina.")
            print(' ')
            indices_a_eliminar_e1.append(i)
            
    fila_actual = notas_b_e1.iloc[i]
    
    for j in range(i + 1, len(notas_b_e1)):
        
        fila_comparar = notas_b_e1.iloc[j]
        
        # Verificar si las columnas 2, 5, 6 y 9 son iguales en ambas filas
        if (fila_actual.iloc[2] == fila_comparar.iloc[2] and
            fila_actual.iloc[5] == fila_comparar.iloc[5] and
            fila_actual.iloc[6] == fila_comparar.iloc[6] and
            fila_actual.iloc[9] == fila_comparar.iloc[9]):
            print(f'{fila_actual.iloc[2]} de la materia {fila_actual.iloc[5]} del bloque {fila_actual.iloc[6]} la etapa {fila_actual.iloc[9]} se reporto dos veces')
            print(f'los dias {fila_actual.iloc[0]} y {fila_comparar.iloc[0]}')
            print(f'se elimina el del dia {fila_comparar.iloc[0]} que tiene nota {fila_comparar.iloc[10]} ')
            print(' ')
            indices_a_eliminar_e1.append(j)

notas_b_e1.drop(indices_a_eliminar_e1, inplace=True)
notas_b_e1 = notas_b_e1.reset_index(drop=True)

###### Desempeños que no sigen el orden de la base de datos ##########

indices_a_eliminar_e1_1 = []

for i in range(len(notas_b_e1)):
    evaluado = False 
    if evaluado:
        continue 
    estudiante = notas_b_e1.iloc[i, 2]
    grado      = notas_b_e1.iloc[i, 3]
    materia    = notas_b_e1.iloc[i, 5]
    dia        = notas_b_e1.iloc[i, 0]
    bloque     = notas_b_e1.iloc[i, 6]
    desempeno  = notas_b_e1.iloc[i, 9]
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
            indices_a_eliminar_e1_1.append(i)
            break
        if ((bloque    == longitud_bloque.iloc[r, 0]) &
            (desempeno == longitud_bloque.iloc[r, 1])):
            if len(notas_estudiante) != r:
                #evaluar cada fila del vector que da longitud de bloques y desempeños del bloque y desempeño siguiente al reportado
                for h in range(r+1, len(longitud_bloque)):
                    #comparar con bloque y etapa de notas del estudiante
                    for p in range(len(bloque_etapa)): 
                        if (longitud_bloque.iloc[h,0] == bloque_etapa.iloc[p,0]) and (longitud_bloque.iloc[h,1] == bloque_etapa.iloc[p,1]):
                            fila_para_agregar = notas_b_e1.iloc[i].to_frame().T 
                            dfb = pd.concat([dfb, fila_para_agregar], ignore_index=True)
                            evaluado = True
                            break               
                if evaluado:
                        break    
                print(f'{estudiante} reportado el dia {dia} de la asignatura {materia}, bloque {bloque}, etapa {desempeno}')
                print('no coincide con una nota faltante o que sea el siguiente desempeño a reportar y se elimina.')
                print(' ')
                indices_a_eliminar_e1_1.append(i)
                evaluado = True
                break                        
            if len(notas_estudiante) == r:
                fila_para_agregar = notas_b_e1.iloc[i].to_frame().T
                dfb = pd.concat([dfb, fila_para_agregar], ignore_index=True)
                break    
notas_b_e1.drop(indices_a_eliminar_e1_1, inplace=True)
notas_b_e1 = notas_b_e1.reset_index(drop=True)

                

######################################################### INGLES 2 ###############################################################

print('-------------------------------Errores E2-----------------------------')

indices_a_eliminar_e2 = []


for i in range(len(notas_b_e2)):

    # nombres que no están en el listado general
    
    if notas_b_e2.iloc[i, 2] not in nombres:
        
        print(f"{notas_b_e2.iloc[i, 2]} no está en el listado general se elimina nota del {notas_b_e2.iloc[i, 0]} de la asignatura {notas_b_e2.iloc[i, 5]}")
        indices_a_eliminar_e2.append(i)
        continue
            

    # desempeños duplicados
    
    notas_estudiante = dfb[(dfb.iloc[:, 2] == notas_b_e2.iloc[i, 2]) &
                           (dfb.iloc[:, 5] == notas_b_e2.iloc[i, 5]) &
                           (dfb.iloc[:, 3] == notas_b_e2.iloc[i, 3])]

    for k in range(len(notas_estudiante)):
        
        if ((notas_b_e2.iloc[i, 6] == notas_estudiante.iloc[k, 6]) &
            (notas_b_e2.iloc[i, 9] == notas_estudiante.iloc[k, 9])):
            
            print(f"{notas_b_e2.iloc[i, 2]}, reportado el día {notas_b_e2.iloc[i, 0]}, de la asignatura {notas_b_e2.iloc[i, 5]}, bloque {notas_b_e2.iloc[i, 6]}, etapa {notas_b_e2.iloc[i, 9]}, ya está reportado, se elimina.")
            print(' ')
            indices_a_eliminar_e2.append(i)
            
    fila_actual = notas_b_e2.iloc[i]
    
    for j in range(i + 1, len(notas_b_e2)):
        
        fila_comparar = notas_b_e2.iloc[j]
        
        # Verificar si las columnas 2, 5, 6 y 9 son iguales en ambas filas
        if (fila_actual.iloc[2] == fila_comparar.iloc[2] and
            fila_actual.iloc[5] == fila_comparar.iloc[5] and
            fila_actual.iloc[6] == fila_comparar.iloc[6] and
            fila_actual.iloc[9] == fila_comparar.iloc[9]):
            print(f'{fila_actual.iloc[2]} de la materia {fila_actual.iloc[5]} del bloque {fila_actual.iloc[6]} la etapa {fila_actual.iloc[9]} se reporto dos veces')
            print(f'los dias {fila_actual.iloc[0]} y {fila_comparar.iloc[0]}')
            print(f'se elimina el del dia {fila_comparar.iloc[0]} que tiene nota {fila_comparar.iloc[10]} ')
            print(' ')
            indices_a_eliminar_e2.append(j)

notas_b_e2.drop(indices_a_eliminar_e2, inplace=True)
notas_b_e2 = notas_b_e2.reset_index(drop=True)

###### Desempeños que no sigen el orden de la base de datos ##########

indices_a_eliminar_e2_1 = []

for i in range(len(notas_b_e2)):
    evaluado = False 
    if evaluado:
        continue 
    estudiante = notas_b_e2.iloc[i, 2]
    grado      = notas_b_e2.iloc[i, 3]
    materia    = notas_b_e2.iloc[i, 5]
    dia        = notas_b_e2.iloc[i, 0]
    bloque     = notas_b_e2.iloc[i, 6]
    desempeno  = notas_b_e2.iloc[i, 9]
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
            indices_a_eliminar_e2_1.append(i)
            break
        if ((bloque    == longitud_bloque.iloc[r, 0]) &
            (desempeno == longitud_bloque.iloc[r, 1])):
            if len(notas_estudiante) != r:
                #evaluar cada fila del vector que da longitud de bloques y desempeños del bloque y desempeño siguiente al reportado
                for h in range(r+1, len(longitud_bloque)):
                    #comparar con bloque y etapa de notas del estudiante
                    for p in range(len(bloque_etapa)): 
                        if (longitud_bloque.iloc[h,0] == bloque_etapa.iloc[p,0]) and (longitud_bloque.iloc[h,1] == bloque_etapa.iloc[p,1]):
                            fila_para_agregar = notas_b_e2.iloc[i].to_frame().T 
                            dfb = pd.concat([dfb, fila_para_agregar], ignore_index=True)
                            evaluado = True
                            break               
                if evaluado:
                    break    
                print(f'{estudiante} reportado el dia {dia} de la asignatura {materia}, bloque {bloque}, etapa {desempeno}')
                print('no coincide con una nota faltante o que sea el siguiente desempeño a reportar y se elimina.')
                print(' ')
                indices_a_eliminar_e2_1.append(i)
                evaluado = True
                break                        
            if len(notas_estudiante) == r:
                fila_para_agregar = notas_b_e2.iloc[i].to_frame().T
                dfb = pd.concat([dfb, fila_para_agregar], ignore_index=True)
                break    
notas_b_e2.drop(indices_a_eliminar_e2_1, inplace=True)
notas_b_e2 = notas_b_e2.reset_index(drop=True)

################################################## STEAM ###############################################################

print('-------------------------------Errores STEAM-----------------------------')

indices_a_eliminar_steam = []

asignaturas_6_7= ['Biología','Química','Medio ambiente','Física',
                  'Historia', 'Geografía', 'Participación política','Filosofía',
                  'Comunicación y sistemas simbólicos','Producción e interpretación de textos',
                  'Aritmética','Animaplanos','Estadística', 'Geometría', 'Dibujo técnico', 'Sistemas']

asignaturas_8_9= ['Biología','Química','Medio ambiente','Física',
                  'Historia', 'Geografía', 'Participación política','Filosofía',
                  'Comunicación y sistemas simbólicos','Producción e interpretación de textos',
                  'Álgebra','Animaplanos', 'Estadística', 'Geometría', 'Dibujo técnico', 'Sistemas']

asignaturas_10=  ['Biología','Química','Medio ambiente','Física',
                  'Metodología','Ciencias económicas', 'Ciencias políticas','Filosofía',
                  'Comunicación y sistemas simbólicos','Producción e interpretación de textos',
                  'Trigonometría','Animaplanos', 'Estadística', 'Matemática financiera', 'Dibujo técnico', 'Sistemas']

asignaturas_11=  ['Química','Medio ambiente','Física',
                  'Metodología','Ciencias económicas', 'Ciencias políticas','Filosofía',
                  'Comunicación y sistemas simbólicos','Producción e interpretación de textos',
                  'Cálculo','Animaplanos', 'Estadística', 'Matemática financiera', 'Dibujo técnico', 'Sistemas']


for i in range(len(notas_b_steam)):

    # nombres que no están en el listado general
    
    if notas_b_steam.iloc[i, 2] not in nombres:
        
        print(f"{notas_b_steam.iloc[i, 2]} no está en el listado general se elimina nota del {notas_b_steam.iloc[i, 0]} de la asignatura {notas_b_steam.iloc[i, 5]}")
        print(' ')
        indices_a_eliminar_steam.append(i)
        continue
        

    # asignaturas que no son de acuerdo al grado
    
    
    if notas_b_steam.iloc[i,2] not in excepciones:
        if (notas_b_steam.iloc[i, 3] == 6) or (notas_b_steam.iloc[i, 3] == 7):
            if notas_b_steam.iloc[i, 5] not in asignaturas_6_7:
                print(f"{notas_b_steam.iloc[i, 5]} no es de grado {int(notas_b_steam.iloc[i, 3])} se elimina nota de {notas_b_steam.iloc[i, 2]} ")
                print(f"del día {notas_b_steam.iloc[i, 0]}")
                print(' ')
                indices_a_eliminar_steam.append(i)
                continue
            

        if (notas_b_steam.iloc[i, 3] == 8) or (notas_b_steam.iloc[i, 3] == 9):
            if notas_b_steam.iloc[i, 5] not in asignaturas_8_9:
                print(f"{notas_b_steam.iloc[i, 5]} no es de grado {int(notas_b_steam.iloc[i, 3])} se elimina nota de {notas_b_steam.iloc[i, 2]} ")
                print(f"del día {notas_b_steam.iloc[i, 0]}")
                print(' ')
                indices_a_eliminar_steam.append(i)
                continue

        if notas_b_steam.iloc[i, 3] == 10:
            if notas_b_steam.iloc[i, 5] not in asignaturas_10:
                print(f"{notas_b_steam.iloc[i, 5]} no es de grado {int(notas_b_steam.iloc[i, 3])} se elimina nota de {notas_b_steam.iloc[i, 2]} ")
                print(f"del día {notas_b_steam.iloc[i, 0]}")
                print(' ')
                indices_a_eliminar_steam.append(i)
                continue
    
        if notas_b_steam.iloc[i, 3] == 11:
            if notas_b_steam.iloc[i, 5] not in asignaturas_11:
                print(f"{notas_b_steam.iloc[i, 5]} no es de grado {int(notas_b_steam.iloc[i, 3])} se elimina nota de {notas_b_steam.iloc[i, 2]} ")
                print(f"del día {notas_b_steam.iloc[i, 0]}")
                print(' ')
                indices_a_eliminar_steam.append(i)
                continue
            
     # desempeños duplicados

    notas_estudiante = dfb[(dfb.iloc[:, 2] == notas_b_steam.iloc[i, 2]) &
                           (dfb.iloc[:, 5] == notas_b_steam.iloc[i, 5]) &
                           (dfb.iloc[:, 3] == notas_b_steam.iloc[i, 3])]

    for k in range(len(notas_estudiante)):
        
        if ((notas_b_steam.iloc[i, 6] == notas_estudiante.iloc[k, 6]) &
            (notas_b_steam.iloc[i, 9] == notas_estudiante.iloc[k, 9])):
            print(f"{notas_b_steam.iloc[i, 2]}, reportado el día {notas_b_steam.iloc[i, 0]}, de la asignatura {notas_b_steam.iloc[i, 5]}, bloque {notas_b_steam.iloc[i, 6]}, etapa {notas_b_steam.iloc[i, 9]}, ya está reportado, se elimina.")
            print(' ')
            indices_a_eliminar_steam.append(i)
            
            
    fila_actual = notas_b_steam.iloc[i]
    
    for j in range(i + 1, len(notas_b_steam)):
        
        fila_comparar = notas_b_steam.iloc[j]
        
        # Verificar si las columnas 2, 5, 6 y 9 son iguales en ambas filas
        if (fila_actual.iloc[2] == fila_comparar.iloc[2] and
            fila_actual.iloc[5] == fila_comparar.iloc[5] and
            fila_actual.iloc[6] == fila_comparar.iloc[6] and
            fila_actual.iloc[9] == fila_comparar.iloc[9]):
            print(f'{fila_actual.iloc[2]} de la materia {fila_actual.iloc[5]} del bloque {fila_actual.iloc[6]} la etapa {fila_actual.iloc[9]} se reporto dos veces')
            print(f'los dias {fila_actual.iloc[0]} y {fila_comparar.iloc[0]}')
            print(f'se elimina el del dia {fila_comparar.iloc[0]} que tiene nota {fila_comparar.iloc[10]} ')
            print(' ')
            indices_a_eliminar_steam.append(j)

notas_b_steam.drop(indices_a_eliminar_steam, inplace=True)
notas_b_steam = notas_b_steam.reset_index(drop=True)

###### Desempeños que no sigen el orden de la base de datos ##########

indices_a_eliminar_steam_1 = []

for i in range(len(notas_b_steam)):
    evaluado = False 
    if evaluado:
        continue 
    estudiante = notas_b_steam.iloc[i, 2]
    grado      = notas_b_steam.iloc[i, 3]
    materia    = notas_b_steam.iloc[i, 5]
    dia        = notas_b_steam.iloc[i, 0]
    bloque     = notas_b_steam.iloc[i, 6]
    desempeno  = notas_b_steam.iloc[i, 9]
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
            indices_a_eliminar_steam_1.append(i)
            break
        if ((bloque    == longitud_bloque.iloc[r, 0]) &
            (desempeno == longitud_bloque.iloc[r, 1])):
            if len(notas_estudiante) != r:
                #evaluar cada fila del vector que da longitud de bloques y desempeños del bloque y desempeño siguiente al reportado
                for h in range(r+1, len(longitud_bloque)):
                    #comparar con bloque y etapa de notas del estudiante
                    for p in range(len(bloque_etapa)): 
                        if (longitud_bloque.iloc[h,0] == bloque_etapa.iloc[p,0]) and (longitud_bloque.iloc[h,1] == bloque_etapa.iloc[p,1]):
                            fila_para_agregar = notas_b_steam.iloc[i].to_frame().T 
                            dfb = pd.concat([dfb, fila_para_agregar], ignore_index=True)
                            evaluado = True
                            break               
                if evaluado:
                    break    
                print(f'{estudiante} reportado el dia {dia} de la asignatura {materia}, bloque {bloque}, etapa {desempeno}')
                print('no coincide con una nota faltante o que sea el siguiente desempeño a reportar y se elimina.')
                print(' ')
                indices_a_eliminar_steam_1.append(i)
                evaluado = True
                break                        
            if len(notas_estudiante) == r:
                fila_para_agregar = notas_b_steam.iloc[i].to_frame().T
                dfb = pd.concat([dfb, fila_para_agregar], ignore_index=True)
                break    
notas_b_steam.drop(indices_a_eliminar_steam_1, inplace=True)
notas_b_steam = notas_b_steam.reset_index(drop=True)
            

notas = pd.concat([notas_b_m1,notas_b_m2,notas_b_c,notas_b_c2,notas_b_s1,notas_b_s2,notas_b_l,notas_b_e1,notas_b_e2,notas_b_steam],ignore_index = True)

notas.to_excel('C:/Users/Admin/Desktop/GK/Notas Para Subir Bachillerato.xlsx', index=False)





