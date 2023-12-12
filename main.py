from src.database.conection import bike_db
from src.management.add import *
from src.management.edit import *
from src.management.remove import *
from src.management.search import *
from src.utils.menu import *
from src.utils.presentation import *

def main():
    #tabelas = ('customers','stores','staffs','orders','brands','categories','products','order_items','stocks',)
    #conexão com o banco de dados
    conn = bike_db()
    opc = 1
    add_opc = None
    
    while opc != 0:
        opc = menu_geral()
        
        match opc:
            case -1:
                print("\n\nOpção invalida!!!!")
            case 1:
                add_opc = menu_adicionar()
                
                match add_opc:
                    case 1:
                        first_name = input("\nNome do Cliente: ")
                        last_name = input("\nSobrenome do Cliente: ")
                        phone = input("\nTelefone do Cliente: ")
                        email = input("\nEmail do Cliente: ")
                        street = input("\nRua do Cliente: ")
                        city = input("\nCidade do Cliente: ")
                        state = input("\nEstado que reside o Cliente: ")
                        zip_code = input("\nCódigo postal do Cliente: ")
                        
                        add_customers(conn,first_name,last_name,phone,email,street,city,state,zip_code)
                    case 2:
                        
                        store_name = input("\nNome da Loja: ")
                        phone = input("\nTelefone da Loja: ")
                        email = input("\nEmail da Loja: ")
                        street = input("\nRua da Loja: ")
                        city = input("\nCidade da Loja: ")
                        state = input("\nEstado que reside a Loja: ")
                        zip_code = input("\nCódigo postal da Loja: ")
                        
                        add_stores(conn,store_name, phone, email, street, city, state, zip_code)
                    case 3:
                        store_id = input("\nID da Loja: ")
                        email = input("\nEmail do Funcionário: ")
                        active = input("\nFuncionário ativo [0][1]: ")
                        phone = input("\nTelefone do Funcionário: ")
                        first_name = input("\nNome do Funcionário: ")
                        last_name = input("\nSobrenome do Funcionário: ")
                        
                        add_staffs(conn,store_id, email, active, phone, first_name, last_name)
                    case 4:
                        customer_id = input("\ncustomer_id: ")
                        staff_id = input("\nstaff_id: ")
                        order_status = input("\norder_status: ")
                        order_date = input("\norder_date: ")
                        required_date = input("\nrequired_date: ")
                        shipped_date = input("\nshipped_date: ")
                        
                        add_orders(conn,customer_id, staff_id, order_status, order_date, required_date, shipped_date)
                    case 5:
                        brand_name = input("\nbrand_name: ")
                        add_brands(conn,brand_name)
                    case 6:
                        category_name = input("\ncategory_name: ")
                        add_categories(conn,category_name)
                    case 7:
                        brand_id = input("\nbrand_id: ")
                        category_id = input("\ncategory_id: ")
                        product_name = input("\nproduct_name: ")
                        model_year = input("\nmodel_year: ")
                        list_price = input("\nlist_price: ")
                        
                        add_products(conn,brand_id,category_id,product_name,model_year,list_price)
                    case 8:
                        order_id = input("\norder_id: ")
                        product_id = input("\nproduct_id: ")
                        quantity = input("\nquantity: ")
                        model_year = input("\nmodel_year: ")
                        list_price = input("\nlist_price: ")
                        discount = input("\nlist_price: ")
                        
                        add_order_items(conn,order_id,product_id,quantity,list_price,discount)
                    case 9:
                        store_id = input("\nstore_id: ")
                        product_id = input("\nproduct_id: ")
                        quantity = input("\nquantity: ")
                        add_stocks(conn,store_id,product_id,quantity)
                
            case 2:
                add_opc = menu_adicionar_csv()
                
                match add_opc:
                    case 1:
                        print("\n\nNão fiz ainda")
                    case 2:
                        print("\n\nNão fiz ainda")
                    case 3:
                        print("\n\nNão fiz ainda")
                    case 4:
                        print("\n\nNão fiz ainda")
                    case 5:
                        print("\n\nNão fiz ainda")
                    case 6:
                        print("\n\nNão fiz ainda")
                    case 7:
                        print("\n\nNão fiz ainda")
                    case 8:
                        print("\n\nNão fiz ainda")
                    case 9:
                        print("\n\nNão fiz ainda")
            case 3:
                print("\n\nNão fiz ainda")
            case 4:
                print("\n\nNão fiz ainda")
            case 5:
                print("\n\nNão fiz ainda")
            

    conn.close()
main()