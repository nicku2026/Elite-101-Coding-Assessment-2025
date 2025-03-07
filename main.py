
# This code is a STARTER scaffold for the E101 Coding assessment


def get_free_tables(tables):
    """
    Level 1
    Returns a list of table IDs (or entire objects) that are currently free.
    """
    # TODO: Implement your logic here
    # HINT: Loop through each 'table' dict, check 'occupied' status.
    #       If table["occupied"] is False, it is free.
    #       Append table["table_id"] (or the entire table dict) to the result list.
    pass


def find_one_table_for_size(tables, party_size):
    """
    Level 2
    Returns the first table ID that can seat 'party_size' and is free,
    or None if none found.
    """
    # TODO: Implement your logic here
    # HINT: Loop through tables and check two conditions:
    #       1) table["occupied"] == False
    #       2) table["capacity"] >= party_size
    #       Return the table_id of the first match you find, otherwise return None.
    pass


def find_all_tables_for_size(tables, party_size):
    """
    Level 3
    Returns a list of all table IDs that can seat 'party_size' and are free.
    """
    # TODO: Implement your logic here
    # HINT: Similar to Level 2, but collect ALL matching tables instead of stopping at the first.
    pass


def find_tables_including_combos(tables, party_size):
    """
    Level 4
    Returns a list of table or table combinations that can seat 'party_size'.
    Adjacent combos are determined via the table's "neighbors" list.
    
    Example output structure:
    [(1,), (3,), (1,2), (3,5)]  # Each tuple is a single table or a pair.
    """
    # TODO: Implement your logic here
    # HINT: 
    #  1) If a single table has enough capacity, add (table_id,) to your results.
    #  2) Otherwise, try pairing with each of its neighbors (if they're free)
    #     and check combined capacity.
    #  3) Sort or otherwise avoid duplicate combos, e.g. (1,2) vs (2,1).
    pass


def friendly_output(tables, combos):
    """
    Bonus (Optional):
    Takes the combos from Level 4 (like [(1,), (2,), (1,2)]) and
    prints a more user-friendly message about each result.
    """
    # TODO: Implement your logic here (optional)
    # HINT: 
    #  1) For single-table tuples (like (1,)), find that table's capacity and print a message.
    #  2) For pairs, combine their capacities and print a message about the total.
    pass


# -----------------------------------------------------------------------------
# Example usage / testing:
if __name__ == "__main__":
    # This example data shows how a list of dictionaries might look.
    # You can modify or replace it with your own tests.
    tables_data = [
        {"table_id": 1, "capacity": 2, "occupied": False, "neighbors": [2]},
        {"table_id": 2, "capacity": 4, "occupied": True,  "neighbors": [1, 3]},
        {"table_id": 3, "capacity": 2, "occupied": False, "neighbors": [2, 4]},
        {"table_id": 4, "capacity": 6, "occupied": False, "neighbors": [3]}
    ]

    # LEVEL 1
    print("LEVEL 1: Free Tables =", get_free_tables(tables_data))

    # LEVEL 2
    print("LEVEL 2: One table for party size 2 =", find_one_table_for_size(tables_data, 2))

    # LEVEL 3
    print("LEVEL 3: All tables for party size 2 =", find_all_tables_for_size(tables_data, 2))

    # LEVEL 4
    combos = find_tables_including_combos(tables_data, 5)
    print("LEVEL 4: Single or combined tables for party size 5 =", combos)

    # BONUS
    print("\nBONUS: Friendly output for the combos above")
    friendly_output(tables_data, combos)
