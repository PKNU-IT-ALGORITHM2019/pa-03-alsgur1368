#-*- coding: utf-8 -*-
import random
import time

def input_random(size):
	sort_list=[]
	for i in range(0,size):
		sort_list.append(random.randint(1,size))
	return sort_list


def input_reverse(size):
	sort_list=[]
	for i in range(size,0,-1):
		sort_list.append(i)
	return sort_list


def swap(sort_list,i,j):
	tmp=sort_list[i]
	sort_list[i]=sort_list[j]
	sort_list[j]=tmp



def bubble_sort(sort_list,size):
	start_time=time.time()
	for i in range(0,size-1):
		for j in range(0,size-i-1):
			if sort_list[j]>sort_list[j+1]:
				swap(sort_list,j,j+1)
	return time.time()-start_time


def selection_sort(sort_list,size):
	index=-1
	start_time=time.time()
	for i in range(0,size):
		select=sort_list[0]
		for j in ragne(1,size-i):
			if(sort_list[j]>select):
				select=sort_list[j]
				index=j
		swap(sort_list,j,size-i)
	return time.time()-start_time


def insertion_sort(sort_list,size):
	start_time=time.time()
	for i in range(1,size):
		for j in range(i)


def main():
# 	size_list=[1000,10000,100000]
# 	sort_list=[]
# 	time_list=[]
# 	print("		Random1000		Reverse1000 	Random10000 	Reverse10000 	Random100000 	Reverse100000")
# 	print("Bubble",end='')
# 	for size in size_list: 
# 		sort_list=input_random(size)
# 		rand_bubble_1000=bubble_sort(sort_list,size)
# #		print(sort_list)
# #		print("랜덤 버블정렬 실행시간")
# 		print("		%0.3f"%rand_bubble_1000)
		
# 		sort_list=input_reverse(size)
# 		reverse_bubble_1000=bubble_sort(sort_list,size)
# #		print(sort_list)
# 		print("		%0.3f"%reverse_bubble_1000)

# #		print("역순 버블정렬 실행 시간 :%0.2f" % reverse_bubble_1000)
# 		size*=10
main()




