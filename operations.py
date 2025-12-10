def is_leaf(cursor, dept_id):
    """
    Checks if a department is a leaf department (has no sub-departments).
    """
    cursor.execute("""
        SELECT COUNT(*)
        FROM Department
        WHERE parent_id = ?
    """, (dept_id,))
    return cursor.fetchone()[0] == 0

def list_child_departments(cursor, dept_id):
    """
    Lists all child departments for a given department ID.
    """
    cursor.execute("""
        SELECT dept_id, title
        FROM Department
        WHERE parent_id = ?
    """, (dept_id,))
    return cursor.fetchall()

def list_products(cursor, dept_id):
    """
    Lists all products in a given department, calculating the discounted price.
    """
    cursor.execute("""
        SELECT product_id, title,
        retail_price * (1 - current_discount / 100.0)
        FROM Product
        WHERE dept_id = ?
    """, (dept_id,))
    return cursor.fetchall()
