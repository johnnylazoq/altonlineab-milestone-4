from database import connect
from operations import is_leaf, list_child_departments, list_products

def main():
    # Connect to the database
    try:
        conn = connect()
        cursor = conn.cursor()
        
        try:
            user_input = input("Enter a department ID: ")
            if not user_input:
                print("No department ID entered.")
                return
                
            dept_id = int(user_input)

            if is_leaf(cursor, dept_id):
                print("\nLeaf department. Listing products:\n")
                products = list_products(cursor, dept_id)
                if not products:
                    print("No products found.")
                for p in products:
                    # p[0]: product_id, p[1]: title, p[2]: discounted_price
                    print(f"{p[0]} | {p[1]} | {p[2]:.2f} kr")
            else:
                print("\nNon-leaf department. Listing child departments:\n")
                children = list_child_departments(cursor, dept_id)
                if not children:
                    print("No child departments found.")
                for d in children:
                    # d[0]: dept_id, d[1]: title
                    print(f"{d[0]} | {d[1]}")
                    
        except ValueError:
            print("Invalid input. Please enter a numeric department ID.")
        except Exception as e:
            print(f"An error occurred during execution: {e}")
        finally:
            cursor.close()
            conn.close()
            
    except Exception as e:
        print(f"Failed to connect to database: {e}")

if __name__ == "__main__":
    main()
