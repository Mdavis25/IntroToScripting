#QUESTION 3
#!/bin/bash
clear

#Using a loop and random numbers, I created a list of twenty numbers and sorted them from lowest to highest

for (( num1=0; num1<30; num1++ ))
do
	rand=$RANDOM
	arr1[num1]=$(($rand%100))
done
echo "Unsorted list: ${arr1[*]}"


for (( num1 = 0; num1<${#arr1[@]}; num1++ ))
do
    for(( num2 = 0; num2<${#arr1[@]}-$num1-1; num2++ ))
    do
    
        if [ ${arr1[$num2]} -gt ${arr1[$((num2+1))]} ]
        then
            temp=${arr1[$num2]}
            arr1[$num2]=${arr1[$((num2+1))]}  
            arr1[$((num2+1))]=$temp
        fi
    done
done

echo "Sorted list from lowest to highest: ${arr1[@]}"

#QUESTION 7
#!/bin/bash
clear

#while loop
num=2
while [ $num -le 1000 ]
do
	flag=0
	count=100
	while [ $count -lt $num ]
	do
		check=$((num%count))
		if [ $check -eq 0 ]
		then
			flag=1
			break
		fi
		let count++
	done
	if [ $flag -eq 0 ]
	then
		echo $num
	fi
	let num++
done

#until loop
num=100
until [ $num -gt 1000 ]
do
	flag=0
	count=2
	until [ $count -ge $num ]
	do
		check=$((num%count))
		if [ $check -eq 0 ]
		then
			flag=1
			break
		fi
		let count++
	done
	if [ $flag -eq 0 ]
	then
		echo $num
	fi
	let num++
done

#for loop
for (( num=100; num<=1000; num++))
do
	flag=0
	for(( count=100; count<num; count++))
	do
		check=$((num%count))
		if [ $check -eq 0 ]
		then
			flag=1
			break
		fi
	done
	if [ $flag -eq 0 ]
	then
		echo $num
	fi
done

# #QUESTION 8
#!/bin/bash
clear

#while loop
sum=0
num=50
while [ $num -le 100 ]
do
  if [ 'expr $num % 2' == 0]
  then
	  let sum+=num num++
  fi
done

echo while loop sum: $sum

#until loop
sum=0
num=50
until [ $num -gt 100 ]
do
  if [ 'expr $num % 2' == 0]
  then
	  let sum+=num num++
  fi
done

echo Until loop sum: $sum

#for loop
sum=0
for (( num=50; num<=100; num++ ))
do
  if [ 'expr $num % 2' == 0]
  then
	  let sum+=num num++
  fi
done
echo For loop sum: $sum

#while loop
sum=0
num=51
while [ $num -le 101 ]
do
  if [ 'expr $num % 2' == 0]
  then
  else
	  let sum+=num num++
  fi
done

echo while loop sum: $sum

#until loop
sum=0
num=51
until [ $num -gt 101 ]
do
  if [ 'expr $num % 2' == 0]
  then
  else
	  let sum+=num num++
  fi
done

echo Until loop sum: $sum

#for loop
sum=0
for (( num=51; num<=101; num++ ))
do
  if [ 'expr $num % 2' == 0]
  then
  else
	  let sum+=num num++
  fi
done
echo For loop sum: $sum


# #QUESTION 9
#!/bin/bash
clear

#Using a loop and random numbers, I created a list of twenty numbers and sorted them from lowest to highest

for (( num1=0; num1<20; num1++ ))
do
	rand=$RANDOM
	arr1[num1]=$(($rand%100))
done
echo "Unsorted list: ${arr1[*]}"


for (( num1 = 0; num1<${#arr1[@]}; num1++ ))
do
    for(( num2 = 0; num2<${#arr1[@]}-$num1-1; num2++ ))
    do
    
        if [ ${arr1[$num2]} -gt ${arr1[$((num2+1))]} ]
        then
            temp=${arr1[$num2]}
            arr1[$num2]=${arr1[$((num2+1))]}  
            arr1[$((num2+1))]=$temp
        fi
    done
done

echo "Sorted list from lowest to highest: ${arr1[@]}"

#QUESTION 10
#!/bin/bash
clear

echo - n “Enter a number: “
read n
echo -i “Enter another number: “
read i
echo "Variable one - variable two = $((n-i))”
echo "Variable one + variable two = $((n+i))”
echo "Variable one * variable two = $((n*i))”
echo "Variable one^2 = $((i*i))”
echo "Variable two^2 = $((n*n))”
