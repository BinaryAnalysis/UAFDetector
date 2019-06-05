#!/usr/bin/python
import os,shutil

option = '-D INCLUDEMAIN'
share_dir = '../../../shared/108'

def compile_1(cur_dir,file_list):
	os.chdir(cur_dir)
	src_file = file_list[0]
		
	cmd1 = 'g++ '
	cmd1 += option + ' '
	cmd1 += '-I ../../../shared/108 '
	cmd1 += '-c ' + src_file + ' '
	cmd1 += '-o src_file.o'
	
	cmd2 = 'g++ '
	cmd2 += '-o target '
	cmd2 += '../../../shared/108/io.o src_file.o'
	
	# print cmd1
	os.system(cmd1 + "> /dev/null 2>&1")
	# print cmd2
	os.system(cmd2 + "> /dev/null 2>&1")

def compile_2(cur_dir,file_list):
	os.chdir(cur_dir)
	file_a = file_list[0]
	file_b = file_list[1]
		
	cmd1 = 'g++ '
	cmd1 += option + ' '
	cmd1 += '-I ../../../shared/108 '
	cmd1 += '-c ' + file_a + ' '
	cmd1 += '-o file_a.o'
		
	cmd2 = 'g++ '
	cmd2 += option + ' '
	cmd2 += '-I ../../../shared/108 '
	cmd2 += '-c ' + file_b + ' '
	cmd2 += '-o file_b.o'
		
	cmd3 = 'g++ '
	cmd3 += '-o target '
	cmd3 += '../../../shared/108/io.o file_a.o file_b.o'
	
	# print cmd1
	os.system(cmd1 + "> /dev/null 2>&1")
	# print cmd2
	os.system(cmd2 + "> /dev/null 2>&1")
	# print cmd3
	os.system(cmd3 + "> /dev/null 2>&1")

def delete_file(cur_dir):
	os.chdir(cur_dir)
	file_list = os.listdir(cur_dir)
	for f in file_list:
		if '.cpp' not in f:
			os.remove(f)

def check(cur_dir):
	os.chdir(cur_dir)
	file_list = os.listdir(cur_dir)
	for f in file_list:
		if f == 'target':
			return True
	return False

if __name__ == "__main__":
	success_count = 0
	wrong_count = 0
	parent_path = os.getcwd()
	dir_list = []
	list = os.listdir(parent_path)
	for i in range(0,len(list)):
		cur_dir = os.path.join(parent_path,list[i])
		if os.path.isdir(cur_dir):
			dir_list.append(cur_dir)

	for cur_dir in dir_list:
		delete_file(cur_dir)

		file_list = os.listdir(cur_dir)		
		if len(file_list) == 1:
			compile_1(cur_dir, file_list)
		elif len(file_list) == 2:
			compile_2(cur_dir, file_list)
		if check(cur_dir):
			success_count += 1
			print cur_dir + ': ' + 'successfully!'
		else:
			wrong_count += 1
			print cur_dir + 'something wrong!'
	print 'compile successfully: ' + str(success_count)
	print 'compile wrong: ' + str(wrong_count)

#g++ $(CFLAGS) -I ../../../shared/108 -c $(file_b) -o file_b.o
#g++ $(CFLAGS) -I ../../../shared/108 -c $(file_a) -o file_a.o
#g++ -o target ../../../shared/108/io.o file_a.o file_b.o
			
