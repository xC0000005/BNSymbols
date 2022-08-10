# Methodology -
# get target name from get_save_filename_input
# Export the original .bin via save.
# Replace the text section in the min bin with the original.
# Annotate the replaced binary with symbols from BN.
symbol_adds = ""
save_file_name = get_save_filename_input("File to save to")
min_file_name = get_open_filename_input("Skeleton File:", "All Files (*)")
print(save_file_name)
print(min_file_name)
bv.save(save_file_name)
for symbol in bv.get_symbols():
    flags = ",global"
    if symbol.type == SymbolType.FunctionSymbol:
        flags += ",function"
    # need to make this dynamic, as it woudld break ram/other section symbols
    # but for now, since the symbols are relative to the section, subtract
    # 0x8000000
    adjusted_symbol_address = int(symbol.address) - int(0x8000000)
    symbol_adds += f" --add-symbol {symbol.name}=.text:{hex(adjusted_symbol_address)}{flags}"

out_file_name = save_file_name + ".elf"

#still todo: use the save_file_name to replace the .text section
command = f"arm-none-eabi-objcopy \"{min_file_name}\" --update-section .text={save_file_name} {symbol_adds} \"{out_file_name}\"\n"
print(command)


