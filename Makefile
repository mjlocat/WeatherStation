CC=gcc
CFLAGS=
LDFLAGS=-L/usr/local/lib -lusb-1.0 
DEPS=
OBJ=weatherstation.o

all: weatherstation

%.o: %.c $(DEPS)
	$(CC) -c -o $@ $< $(CFLAGS)

weatherstation: $(OBJ)
	$(CC) -o $@ $^ $(LDFLAGS) $(CFLAGS)

clean:
	rm -f weatherstation *.o
