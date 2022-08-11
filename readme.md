This repo contains some tools I hacked together to let me export symbols from
reverse engineering firmware in Binary Ninja to use in gdb.
After you're done reverse engineering/adding symbols in BN, run symbuild.py, then run the generated command
to execute your copy of objcopy annotate the binary with symbols.
The original firmware will replace the text section. 
This doesn't work correctly with views whose offset is not 0x8000000, but it could easily be edited to do so.