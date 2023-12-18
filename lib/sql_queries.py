# Query 1
select_all_female_bears_return_name_and_age = """
    SELECT
        bears.name,
        bears.age
    FROM bears
    WHERE sex='F';
"""

# Query 2
select_all_brown_bears_return_name_and_sex = """
    SELECT
        bears.name,
        bears.sex
    FROM bears
    WHERE color='Brown';
"""

# Query 3
select_all_alive_bears_ordered_by_age = """
    SELECT
        bears.name,
        bears.age
    FROM bears
    WHERE alive=1
    ORDER BY age;
"""
