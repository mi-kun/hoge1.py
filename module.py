# coding: UTF-8

#module.py

import random

def gamemode_challenge(correct_count,x,variable,q_and_a,problem_count):
	while True:
		problem_count += 1
		print("\n問題",problem_count)

		variable = random.randint(0,99)
		print(q_and_a[variable][0])

		x = input("答え : ")
		if x == q_and_a[variable][1]:
			print("正解\n")

			correct_count += 1

		else:
			print("不正解\n")
			print("\n正解数 : ",correct_count,"\n")
			break

		print("今までの正解数 : ",correct_count,"\n")

def gamemode_normal(correct_count,x,variable,q_and_a,problem_count,time):
	for turn in range(1,time):
		problem_count += 1
		print("\n問題",problem_count)

		variable = random.randint(0,99)
		print(q_and_a[variable][0])

		x = input("答え : ")
		if x == q_and_a[variable][1]:
			print("正解\n")

			correct_count += 1

		print("今までの正解数 : ",correct_count,"\n")

	print("\n正解数 : ",correct_count,"\n")
