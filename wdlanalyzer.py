import anvil
# pip intsll anvil-parser
region = anvil.Region.from_file('write file here')
chunk = anvil.Chunk.from_region(region, 1, 2)
for z in range(0, 16):
    for y in range(0,128):
        for x in range(0,16):
            block = chunk.get_block(x, y, z)
            if block.id != "air":
                print(block.id, x, y, z)
                
