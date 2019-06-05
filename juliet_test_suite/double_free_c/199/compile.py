#!/usr/bin/python
import os,shutil

option = '-lm -D INCLUDEMAIN'
share_dir = ['../../../shared/104', '../../../shared/108']
share_io = '../../../shared/108/io.o'

def compile_n(cur_dir, file_list, compiler):
	global share_dir
	file_count = len(file_list)
	os.chdir(cur_dir)
	for i in range(file_count):
		src_file = file_list[i]
		
		cmd = compiler + ' '
		cmd += option + ' '
		str_share = ''
		for share in share_dir:
			str_share += '-I ' + share + ' '
		cmd += str_share
		cmd += '-c ' + src_file + ' '
		cmd += '-o ' + str(i) + '.o'
		print cmd
		os.system(cmd + "> /dev/null 2>&1")
	
	cmd = compiler + ' '
	cmd += '-o target '
	cmd += share_io
	str_o = ''
	for i in range(file_count):
		str_o += ' ' + str(i) + '.o'
	cmd += str_o
	print cmd
	os.system(cmd + "> /dev/null 2>&1")

def delete_file(cur_dir):
	os.chdir(cur_dir)
	file_list = os.listdir(cur_dir)
	for f in file_list:
		if '.cpp' not in f and '.c' not in f and '.cc' not in f and '.h' not in f:
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
		try:
			delete_file(cur_dir)
		except OSError:
			print 'cannot delete ' + cur_dir
			continue

		file_list = []
		tmp_list = os.listdir(cur_dir)
		compiler = 'gcc'
		for f in tmp_list:
			if ('.cpp' in f) or ('.c' in f) or ('.cc' in f):
				file_list.append(f)
			if ('.cpp' in f) or ('.cc' in f):
				compiler = 'g++'
		compiler = 'g++'
		compile_n(cur_dir, file_list, compiler)

		if check(cur_dir):
			success_count += 1
			print cur_dir + ': ' + 'successfully!'
		else:
			wrong_count += 1
			print cur_dir + 'something wrong!'
	print 'compile successfully: ' + str(success_count)
	print 'compile wrong: ' + str(wrong_count)

#gcc $(CFLAGS) -I ../../../shared/108 -c $(file_b) -o file_b.o
#gcc $(CFLAGS) -I ../../../shared/108 -c $(file_a) -o file_a.o
#gcc -o target ../../../shared/108/io.o file_a.o file_b.o
			
