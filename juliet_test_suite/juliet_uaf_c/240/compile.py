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
		src_file = file_list[0]
		
		cmd1 = 'gcc '
		cmd1 += option + ' '
		cmd1 += '-I ../../../shared/108 '
		cmd1 += '-c ' + src_file + ' '
		cmd1 += '-o src_file.o'
		
		cmd2 = 'gcc '
		cmd2 += '-o target '
		cmd2 += '../../../shared/108/io.o src_file.o'
		
		print cmd1
		os.system(cmd1)
		print cmd2
		os.system(cmd2)
#gcc $(CFLAGS) -I ../../../shared/108 -c $(file_b) -o file_b.o
#gcc -o target ../../../shared/108/io.o file_a.o file_b.o
			
