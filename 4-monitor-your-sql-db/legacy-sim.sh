old_select_engineers_query="/*!999999 old_select_engineers */ SELECT * FROM titles WHERE title LIKE 'Engineer';"
new_select_engineers_query="/*!999999 new_select_engineers */ SELECT * FROM titles WHERE title = 'Engineer';"
old_select_employees_query="/*!999999 old_select_employees */ SELECT * FROM employees WHERE first_name LIKE 'Georgi';"
new_select_employees_query="/*!999999 new_select_employees */ SELECT * FROM employees WHERE first_name = 'Georgi';"
# Create an array of queries
queries=("$old_select_engineers_query" "$new_select_engineers_query" "$old_select_employees_query" "$new_select_employees_query")
while true; do
  # Get a random index ranging from 0 to length of the array
  index=$((RANDOM % ${#queries[@]}))
  # Use the randomly selected index to get a query
  query=${queries[$index]}
  mysql -uroot -pcodely employees -e "$query"
  # Wait for 1 second
  sleep 1
done
