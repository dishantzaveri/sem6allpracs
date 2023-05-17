#include <stdio.h>
#include <stdlib.h>
#include <string.h>
// #include <unistd.h>

char *gets(char *);

int main(int argc, char **argv) {
  struct {
    char buffer[5];
    volatile int changeme;
  } locals;

  locals.changeme = 0;
  gets(locals.buffer);

  if (locals.changeme != 0) {
    puts("Well done, the 'changeme' variable has been changed!");
  } else {
    puts(
        "Uh oh, 'changeme' has not yet been changed. Would you like to try "
        "again?");
  }

  exit(0);
}