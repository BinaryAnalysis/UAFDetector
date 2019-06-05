#!/usr/bin/python
import os,shutil

option = '-D INCLUDEMAIN'
share_dir = '../../../shared/108'

def get_dir_list(dir_list):
	parent_path = os.getcwd()
	list = os.listdir(parent_path)
	for i in range(0,len(list)):
		cur_dir = os.path.join(parent_path,list[i])
		if os.path.isdir(cur_dir):
			dir_list.append(cur_dir)
	return dir_list

def remove_file(dir_list):
	for cur_dir in dir_list:
		os.chdir(cur_dir)
		file_list = os.listdir(cur_dir)
		for i in range(0,len(file_list)):
			cur_file = file_list[i]
			if not cur_file[-2:] == '.c':
				print 'remove ' + cur_file				
				os.remove(cur_file)

def compile_file(dir_list):
	for cur_dir in dir_list:
		print cur_dir
		os.chdir(cur_dir)
		file_list = os.listdir(cur_dir)
		src_file = file_list[0]
		cmd = 'gcc '
		cmd += src_file + ' '
		cmd += '-o target'
		os.system(cmd)
		

if __name__ == "__main__":
	dir_list = []
	dir_list = get_dir_list(dir_list)

	# remove_file(dir_list)

	compile_file(dir_list)
