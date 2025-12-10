from src.database import connect
from src.operations import (
    is_leaf, 
    list_child_departments, 
    list_products, 
    get_product, 
    update_discount
)
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

def run_department_browser(cursor):
    logger.info("\n--- Department Browser ---")
    try:
        user_input = input("Enter a department ID: ")
        if not user_input:
            logger.warning("No department ID entered.")
            return
            
        dept_id = int(user_input)

        if is_leaf(cursor, dept_id):
            logger.info("\nLeaf department. Listing products:\n")
            products = list_products(cursor, dept_id)
            if not products:
                logger.info("No products found.")
            for p in products:
                # p[0]: product_id, p[1]: title, p[2]: discounted_price
                logger.info(f"{p[0]} | {p[1]} | {p[2]:.2f} kr")
        else:
            logger.info("\nNon-leaf department. Listing child departments:\n")
            children = list_child_departments(cursor, dept_id)
            if not children:
                logger.info("No child departments found.")
            for d in children:
                # d[0]: dept_id, d[1]: title
                logger.info(f"{d[0]} | {d[1]}")
                
    except ValueError:
        logger.error("Invalid input. Please enter a numeric department ID.")

def run_discount_manager(conn, cursor):
    logger.info("\n--- Discount Manager ---")
    try:
        user_input = input("Enter a product ID: ")
        if not user_input:
            logger.warning("No product ID entered.")
            return
        product_id = int(user_input)
        
        result = get_product(cursor, product_id)
        
        if not result:
            logger.warning("Product not found.")
            return
            
        logger.info(f"Product: {result[0]}")
        logger.info(f"Current discount: {result[1]}%")
        
        new_discount_input = input("Enter new discount (0-100): ")
        if not new_discount_input:
                logger.warning("No discount entered.")
                return
        new_discount = float(new_discount_input)
        
        if not (0 <= new_discount <= 100):
            logger.warning("Discount must be between 0 and 100.")
            return

        update_discount(cursor, product_id, new_discount)
        conn.commit()
        logger.info("Discount updated successfully.")
        
    except ValueError:
        logger.error("Invalid input. Please enter numeric values.")

def main():
    # Connect to the database
    try:
        conn = connect()
        cursor = conn.cursor()
        
        while True:
            logger.info("\nSelect a program:")
            logger.info("1. Department Browser")
            logger.info("2. Discount Manager")
            logger.info("q. Quit")
            
            choice = input("Enter choice: ")
            
            if choice == '1':
                run_department_browser(cursor)
            elif choice == '2':
                run_discount_manager(conn, cursor)
            elif choice.lower() == 'q':
                break
            else:
                logger.warning("Invalid choice. Please try again.")

        cursor.close()
        conn.close()
            
    except Exception as e:
        logger.error(f"Failed to connect to database: {e}")

if __name__ == "__main__":
    main()
