#/bin/bash

ld -static /usr/lib/i386-linux-gnu/crt1.o /usr/lib/i386-linux-gnu/crti.o   /usr/lib/gcc/i686-linux-gnu/4.6.3/crtbeginT.o  -L/usr/lib/gcc/i686-linux-gnu/4.6.3/ -L/usr/lib -L/lib hello.o   --start-group -lgcc -lgcc_eh -lc --end-group /usr/lib/gcc/i686-linux-gnu/4.6.3/crtend.o /usr/lib/i386-linux-gnu/crtn.o
