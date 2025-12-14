# src/optimizer/cost_estimator.py
import math
from utils.constants import TABLE_METADATA

def cost_linear_search(num_rows):
    """Calculate the cost of a linear search."""
    return num_rows

def cost_binary_search(num_rows):
    """Calculate the cost of a binary search."""
    return math.log2(num_rows)

def selectivity_factor(predicate, table_name):
    """Estimate the selectivity factor based on a predicate."""
    cardinality = TABLE_METADATA[table_name]['cardinality']
    # Simple heuristic: 10% of rows match the predicate
    return cardinality * 0.1

def cost_selection(selectivity_factor):
    """Calculate the cost of a selection operation."""
    return 10 * selectivity_factor

def cost_join(num_rows):
    """Calculate the cost of a join operation."""
    return num_rows * 100

def cost_projection(num_columns):
    """Calculate the cost of a projection operation."""
    return num_columns * 5
def calculate_cost(query_tree, table_metadata):
    """Calculate the total cost of a query tree."""
    cost = 0
    if isinstance(query_tree, ProjectionNode):
        num_columns = len(query_tree.value.split(', '))
        cost += cost_projection(num_columns)
        cost += calculate_cost(query_tree.children[0], table_metadata)
    elif isinstance(query_tree, SelectionNode):
        selectivity = selectivity_factor(query_tree.value, query_tree.children[0].value)
        cost += cost_selection(selectivity)
        cost += calculate_cost(query_tree.children[0], table_metadata)
    elif isinstance(query_tree, JoinNode):
        left_cost = calculate_cost(query_tree.children[0], table_metadata)
        right_cost = calculate_cost(query_tree.children[1], table_metadata)
        total_rows = left_cost + right_cost
        cost += cost_join(total_rows)
        cost += calculate_cost(query_tree.children[2], table_metadata)
    elif isinstance(query_tree, TableNode):
        cardinality = table_metadata[query_tree.value]['cardinality']
        cost += cardinality
    return cost