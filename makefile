CC = cc 
CF = -std=c99 -pedantic -Wall -Wextra \
     -Wmissing-prototypes -Wstrict-prototypes \
     -Wformat-signedness -Wformat-extra-args \
     -Wshadow -Wdouble-promotion -Wconversion -Wformat \
     -Wdeclaration-after-statement -Wmissing-declarations \
     -Wpointer-arith -Wcast-qual -Wimplicit-function-declaration
LF = #libraries
DF = -DDEBUG_MODE
SC = #source
OB = #output

all: $(SC)
	$(CC) -g -O0 $(CF) $(LF) $(DF) $(SC) -o $(OB)
