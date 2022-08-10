/users/jasonnelson/.platformio/packages/toolchain-gccarmnoneeabi/bin/arm-none-eabi-gcc -O0 -Wall -c -g -mcpu=cortex-m3 -mthumb stm32/min.c -o bin/min.o

/users/jasonnelson/.platformio/packages/toolchain-gccarmnoneeabi/bin/arm-none-eabi-ld -o bin/min.elf -T stm32/103.ld bin/min.o 
/users/jasonnelson/.platformio/packages/toolchain-gccarmnoneeabi/bin/arm-none-eabi-objcopy bin/min.elf bin/min.bin -O binary

/users/jasonnelson/.platformio/packages/toolchain-gccarmnoneeabi/bin/arm-none-eabi-nm --numeric-sort bin/min.elf