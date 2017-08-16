gcc overflow.c -o overflow -fno-stack-protector -z execstack -m32 -D_FORTIFY_SOURCE=0
