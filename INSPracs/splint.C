#include <stdio.h>
#include <string.h>

#define UP_MAXLEN 20
#define UP_PAIR_COUNT 3
 

int main() 
{ 
int flag;
char termBuf;
char username[UP_MAXLEN]; char cpass[UP_MAXLEN]; char npass[UP_MAXLEN];
char keys[UP_PAIR_COUNT][2][UP_MAXLEN] = {
{"Admin", "pass3693"},
{"Max", "Qqkaif"},
{"Sally","Usfsmfs"}
};
    while (1)
    {
    flag = 0;
    printf("Change Password\n");
    printf("Enter Username: "); 
    gets(username); 
    printf("Enter Current Password: "); 
    gets(cpass); for(int i = 0; i < UP_PAIR_COUNT; i++) {
        if (strcmp(keys[i][0], username) == 0 && strcmp(keys[i][1], cpass) == 0) 
            { printf("Enter New Password: "); 
            gets(npass);
            strcpy(&keys[i][1][0], npass);
            for(int j = 0; j < UP_PAIR_COUNT; j++) 
            printf("%s | %s\n", keys[j][0], keys[j][1]
            );
            printf("Password Changed!\n"); printf("Continue? Y/N: "); gets(&termBuf);
            if (termBuf != 'Y') return 0; else flag = 1;
            
            }
    }
        if (flag == 1) continue;
        printf("Incorrect Username and Password. Enter Y to continue.\n"); gets(&termBuf);
        if (termBuf != 'Y') return 0;
    }
}
