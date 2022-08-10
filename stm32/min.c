/* 
 * minimal start file 
 * Jason Nelson, 2022
 * 
*/

// The startup function, address was provided in the vector table	
void startup()
{
	while(1);
}

unsigned int * nvic[2] __attribute__ ((section(".vectors"))) = 
{
    (unsigned int *)	0x20001000,  	// Address of top of stack. 20kB = 1024 x 20 = 20480 bytes = 0x5000 
    (unsigned int *)    startup     	// Address of the reset handler which is also our startup function
};
