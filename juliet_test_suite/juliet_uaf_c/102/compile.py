#!/usr/bin/python
import os,shutil

option = '-D INCLUDEMAIN'
share_dir = '../../../shared/108'

if __name__ == "__main__":
	parent_path = os.getcwd()
	dir_list = []
	list = os.listdir(parent_path)
	for i in range(0,len(list)):
		cur_dir = os.path.join(parent_path,list[i])
		if os.path.isdir(cur_dir):
			dir_list.append(cur_dir)

	for cur_dir in dir_list:
		print cur_dir
		os.chdir(cur_dir)
		file_list = os.listdir(cur_dir)
		for i in range(0,len(file_list)):
			cur_file = file_list[i]
			#if not cur_file[-2:] == '.c':
			#	os.remove(cur_file)
			if cur_file[-3] == 'a':
				file_a = cur_file
			if cur_file[-3] == 'b':
				file_b = cur_file
		
		cmd1 = 'gcc '
		cmd1 += option + ' '
		cmd1 += '-I ../../../shared/108 '
		cmd1 += '-c ' + file_a + ' '
		cmd1 += '-o file_a.o'
		
		cmd2 = 'gcc '
		cmd2 += option + ' '
		cmd2 += '-I ../../../shared/108 '
		cmd2 += '-c ' + file_b + ' '
		cmd2 += '-o file_b.o'
		
		cmd3 = 'gcc '
		cmd3 += '-o target '
		cmd3 += '../../../shared/108/io.o file_a.o file_b.o'
		
		print cmd1
		os.system(cmd1)
		print cmd2
		os.system(cmd2)
		print cmd3
		os.system(cmd3)
#gcc $(CFLAGS) -I ../../../shared/108 -c $(file_b) -o file_b.o
#gcc $(CFLAGS) -I ../../../shared/108 -c $(file_a) -o file_a.o
#gcc -o target ../../../shared/108/io.o file_a.o file_b.o
			
