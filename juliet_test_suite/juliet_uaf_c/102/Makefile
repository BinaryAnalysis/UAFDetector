CFLAGS += -D INCLUDEMAIN
file_a = CWE416_Use_After_Free__malloc_free_int_63a.c
file_b = CWE416_Use_After_Free__malloc_free_int_63b.c
target:../../../shared/108/io.o file_a.o file_b.o
	gcc -o target ../../../shared/108/io.o file_a.o file_b.o
file_a.o:../../../shared/108/std_testcase.h ../../../shared/108/std_testcase_io.h $(file_a)
	gcc $(CFLAGS) -I ../../../shared/108 -c $(file_a) -o file_a.o
file_b.o:../../../shared/108/std_testcase.h ../../../shared/108/std_testcase_io.h $(file_b)
	gcc $(CFLAGS) -I ../../../shared/108 -c $(file_b) -o file_b.o
clean:
	rm -f target *.o
