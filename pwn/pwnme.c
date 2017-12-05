#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<sys/socket.h>
#include<arpa/inet.h>
#include<unistd.h>
#include <sys/prctl.h>
#include <linux/seccomp.h>

/*gcc pwnme.c -o pwnme -O0 -fno-pie -fno-pic -fno-stack-protector*/

void shell();

char flag[2048];

/*TODO: Remove legacy code*/
void getname(char *name) {
    puts("Your name is?");
    fflush(stdout);
    gets(name);
}

void run () {
    char name[8192];
    printf("Your lucky number is %p\n",shell);
    getname(name);
    fflush(stdout);
    printf("Hello %.8192s\n",name);
    fflush(stdout);
}

void shell() {
    printf("Yay, you did it, the flag is %s\n",flag);
    fflush(stdout);
    exit(0);
}

inline static void srestrict(){
    prctl(PR_SET_SECCOMP, SECCOMP_MODE_STRICT);
}

#define LPORT 8888



int main(int argc , char *argv[]) {
    int socket_desc , client_sock , c , enable = 1;
    struct sockaddr_in server , client;
    pid_t child;
    FILE * ff = fopen("flag.txt", "r");
    fgets(flag,2048,ff);
    fclose(ff);
    
    socket_desc = socket(AF_INET , SOCK_STREAM , 0);
    if (socket_desc == -1) {
        perror("Could not create socket");
        exit(1);
    }
    
    if (setsockopt(socket_desc, SOL_SOCKET, SO_REUSEADDR, &enable, sizeof(int)) < 0) {
        perror("setsockopt(SO_REUSEADDR) failed");
        exit(1);
    }
    
    server.sin_family = AF_INET;
    server.sin_addr.s_addr = INADDR_ANY;
    server.sin_port = htons( LPORT );
    
    if( bind(socket_desc,(struct sockaddr *)&server , sizeof(server)) < 0) {
        perror("bind failed. Error");
        exit(1);
    }
     
    listen(socket_desc , 128);
     
    while (1) {
        c = sizeof(struct sockaddr_in);
        client_sock = accept(socket_desc, (struct sockaddr *)&client, (socklen_t*)&c);
        if (client_sock < 0) {
            perror("accept failed");
        }
        
        fflush(NULL);
        child = fork();
        if (child == 0) {
            close(socket_desc);
            fflush(NULL);
            dup2(client_sock,STDIN_FILENO);
            dup2(client_sock,STDOUT_FILENO);
            fclose(stderr);
            close(STDERR_FILENO);
            close(client_sock);
            fflush(NULL);
            //Work around bug in srestrict
            rewind(stdin);
            rewind(stdout);
            srestrict();
            run();
            puts("Bye!");
            exit(0);
        } else {
            close(client_sock);
            if (child < 0) {
                perror("fork failed");
            }
        }
    }
    return 0;
}
