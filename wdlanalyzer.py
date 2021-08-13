import anvil
# pip intsll anvil-parser
region = anvil.Region.from_file('r.-682.-1229.mca')
chunk = anvil.Chunk.from_region(region, 17, 6)
for z in range(0, 16):
    for y in range(0,128):
        for x in range(0,16):
            block = chunk.get_block(x, y, z)
            if block.id != "air":
                print(block.id, x, y, z)
                