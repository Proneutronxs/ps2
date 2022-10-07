from ps.conexion import ps_Permisos

####Permissions Data Base


def user_General(user):
    permisos = ps_Permisos()
    try:
        cursor = permisos.cursor()
        c_user = ("SELECT id, usr, usr_administracion, usr_calidad, usr_cargas, usr_empaque, usr_chacras, usr_sistemas FROM `Usuarios` WHERE usr = '"+str(user)+"'")
        cursor.execute(c_user)
        j = cursor.fetchall()
        for i in j:
            permissions = {'id':i[0],'user':i[1],'admin':i[2], 'calidad':i[3], 'cargas':i[4], 'empaque':i[5], 'chacras':i[6], 'sistemas': i[7]}
            return permissions
    except Exception as e:
        print("except")
        print(e)

def p_admin(id):
    permisos = ps_Permisos()
    try:
        cursor = permisos.cursor()
        consulta_area = ("SELECT moduloAD1, moduloAD2, moduloAD3 FROM `Administracion` WHERE id = '"+str(id)+"'")
        cursor.execute(consulta_area)
        j = cursor.fetchall()
        for i in j:
            Area_permissions = {'moduloAD1':i[0],'moduloAD2':i[1],'moduloAD3':i[2]}
            return Area_permissions
    except Exception as e:
        print("except")
        print(e)

def p_calidad(id):
    permisos = ps_Permisos()
    try:
        cursor = permisos.cursor()
        consulta_area = ("SELECT moduloCL1, moduloCL2, moduloCL3 FROM `Calidad` WHERE id = '"+str(id)+"'")
        cursor.execute(consulta_area)
        j = cursor.fetchall()
        for i in j:
            Area_permissions = {'moduloCL1':i[0],'moduloCL2':i[1],'moduloCL3':i[2]}
            return Area_permissions
    except Exception as e:
        print("except")
        print(e)

def p_cargas(id):
    permisos = ps_Permisos()
    try:
        cursor = permisos.cursor()
        consulta_area = ("SELECT moduloCG1, moduloCG2, moduloCG3 FROM `Cargas` WHERE id = '"+str(id)+"'")
        cursor.execute(consulta_area)
        j = cursor.fetchall()
        for i in j:
            Area_permissions = {'moduloCG1':i[0],'moduloCG2':i[1],'moduloCG3':i[2]}
            return Area_permissions
    except Exception as e:
        print("except")
        print(e)

def p_empaque(id):
    permisos = ps_Permisos()
    try:
        cursor = permisos.cursor()
        consulta_area = ("SELECT moduloEM1, moduloEM2, moduloEM3 FROM `Empaque` WHERE id = '"+str(id)+"'")
        cursor.execute(consulta_area)
        j = cursor.fetchall()
        for i in j:
            Area_permissions = {'moduloEM1':i[0],'moduloEM2':i[1],'moduloEM3':i[2]}
            return Area_permissions
    except Exception as e:
        print("except")
        print(e)

def p_chacras(id):
    permisos = ps_Permisos()
    try:
        cursor = permisos.cursor()
        consulta_area = ("SELECT moduloCH1, moduloCH2, moduloCH3 FROM `Chacras` WHERE id = '"+str(id)+"'")
        cursor.execute(consulta_area)
        j = cursor.fetchall()
        for i in j:
            Area_permissions = {'moduloCH1':i[0],'moduloCH2':i[1],'moduloCH3':i[2]}
            return Area_permissions
    except Exception as e:
        print("except")
        print(e)

def p_sistemas(id):
    permisos = ps_Permisos()
    try:
        cursor = permisos.cursor()
        consulta_area = ("SELECT moduloSYS1, moduloSYS2, moduloSYS3 FROM `Sistemas` WHERE id = '"+str(id)+"'")
        cursor.execute(consulta_area)
        j = cursor.fetchall()
        for i in j:
            Area_permissions = {'moduloSYS1':i[0],'moduloSYS2':i[1],'moduloSYS3':i[2]}
            return Area_permissions
    except Exception as e:
        print("except")
        print(e)