SELECT unique_id, employee_name
FROM  employeeuni
RIGHT JOIN employees ON employeeuni.id = employees.id;