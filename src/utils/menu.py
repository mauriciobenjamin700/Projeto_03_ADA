def menu_geral():
    
    print('-'*30,'MENU-GERAL','-'*30)
    print("1 - Adicionar Registro")
    print("2 - Adicionar CSV de Registros")
    print("3 - Buscar Registro")
    print("4 - Editar Registro")
    print("5 - Remover Registro")
    print("0 - Encerrar")
    opc = int(input('\nSua escolha: '))
    print('-'*30,'----------','-'*30)
    
    if opc < 0 or opc > 5:
        opc = -1
    
        
    return opc
            
            
def menu_adicionar():
    print('-'*30,'MENU-ADICIONAR','-'*30)
    print("1 - customers")
    print("2 - stores")
    print("3 - staffs")
    print("4 - orders")
    print("5 - brands")
    print("6 - categories")
    print("7 - products")
    print("8 - order_items")
    print("9 - stocks")
    print("0 - voltar")
    opc = int(input('\nSua escolha: '))
    print('-'*30,'-------------','-'*30)
    
    if opc < 0 or opc > 9:
        opc = -1
        
    return opc

def menu_adicionar_csv():
    print('-'*30,'MENU-CSV','-'*30)
    print("1 - customers")
    print("2 - stores")
    print("3 - staffs")
    print("4 - orders")
    print("5 - brands")
    print("6 - categories")
    print("7 - products")
    print("8 - order_items")
    print("9 - stocks")
    print("0 - voltar")
    opc = int(input('\nSua escolha: '))
    print('-'*30,'-------','-'*30)
    
    if opc < 0 or opc > 9:
        opc = -1
        
    return opc