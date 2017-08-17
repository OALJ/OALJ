# include <stdio.h>

inline int StrToInt(char str[]) { 
    int k = 0;
    for(int i = 0; str[i]; i++) { 
        k = k * 10 + str[i] - '0';
    }
    return k;
}

int main(int argc, char *argv[]) {
    int n = StrToInt(argv[1]);
    int i = 2;
    while(n--) { 
        int k = StrToInt(argv[i++]);
        printf("%c[1;3%dm%s", 27, k, argv[i++]);
    }
    return 0;
}


/* red gre ylw blu pup bgr wht
    1   2   3   4   5   6   7
 
  printf("%c[1;3%cmHello, world!\n", 27, 1); // red
  printf("%c[1;3%cmHello, world!\n", 27, 2); // green
  printf("%c[1;3%cmHello, world!\n", 27, 3); // yellow
  printf("%c[1;3%cmHello, world!\n", 27, 4); // blue
  printf("%c[1;3%cmHello, world!\n", 27, 5); // purple
  printf("%c[1;3%cmHello, world!\n", 27, 6); // blue green
  printf("%c[1;3%cmHello, world!\n", 27, 7); // white
*/
