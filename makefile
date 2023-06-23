CC = cc 
CF = -std=c99 -pedantic -Wall -Wextra \
     -Wmissing-prototypes -Wstrict-prototypes \
     -Wdeclaration-after-statement -Wmissing-declarations \
     -Wimplicit-function-declaration  \
     -Wshadow -Wdouble-promotion -Wconversion -Wformat \
     -Wformat-signedness -Wformat-extra-args \
     -Wpointer-arith -Wcast-qual
LF = #libraries
DF = -DDEBUG_MODE
SC = #source
OB = #output

all: $(SC)
	$(CC) -g -O0 $(CF) $(SC) $(LF) -o $(OB) $(DF)
