# src/main.py
from parser.sql_parser import parse_sql_query
from parser.query_tree import build_query_tree
from optimizer.cost_estimator import calculate_cost
from utils.constants import TABLE_METADATA

def main():
    query = "SELECT name, course_name FROM Students JOIN Enrollments ON Students.student_id = Enrollments.student_id JOIN Courses ON Enrollments.course_id = Courses.course_id WHERE age > 20"
    query_tree = build_query_tree(query)
    print("Parsed Query Tree:", query_tree)
    total_cost = calculate_cost(query_tree, TABLE_METADATA)
    print("Total Cost:", total_cost)

if __name__ == "__main__":
    main()