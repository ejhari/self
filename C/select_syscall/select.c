/* A DEMO ON SYNCHRONOUS I/O MULTIPLEXING 
 * USING select SYSTEM CALL  
 */

#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <stdlib.h>
#include <sys/select.h> //According to POSIX.1-2001

#define BSIZE 100 // set the buffer size for read
#define TIMEOUT 5 // set the timeout (in seconds)

/* Only two data sources are taken, the keyboard
 * and a named pipe.
 * The named pipe is passed to main() as a 
 * command-line argument.
 */

main(int argc, char *argv[])
{
	int fd, r, length=0;
	char buf[BSIZE]; //declare buffer of size BSIZE

	fd_set rfds; //set of file descriptors
	struct timeval time;
	int ret;
	
	if (!argv[1]) {
		printf("No pipe found ... \n"); 
		exit(0);
	}
	fd = open(argv[1], O_RDWR);

	FD_ZERO(&rfds);
	FD_SET(0, &rfds);
	FD_SET(fd, &rfds);

	time.tv_sec = TIMEOUT; //Timeout (in seconds)
	time.tv_usec = 0;
	
	ret = select(fd+1, &rfds, NULL, NULL, &time);

	if (ret == -1) perror("select() error ... ");
	else if (ret) {
		if (FD_ISSET(0, &rfds)) {
			printf("Data available in stdin ...\n");
			r = 0;
		} 
		if (FD_ISSET(fd, &rfds)) {
			printf("Data available in pipe ...\n");
			r = fd;	
		}
		length = read(r, buf, BSIZE);
		buf[length] = '\0';
		printf("Data is : ");
		printf("%s", buf);
	}
	else printf("No data yet ...\n");
}
