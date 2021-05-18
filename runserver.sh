cust_func(){
  echo "Do something $1 times..."
  ./server.py $i
}
# For loop 3 times
for i in {1..3}
do
	cust_func $i & # Put a function in the background
done
