import sys
import pandas as pd
import ezdxf



def help():
    print("Text file format:  id,x,y,H")
    print("e.g:\n1,500650.590,4204238.460,351.234\n2,500650.920,4204252.530,350.582")
    print("\nExecution:\npython coordsTable.py coords_filename")
    print("e.g:\npython coordsTable.py coords.txt")


def add_head(msp, block, block2, layer_name, rows, min_x, min_y, width_id, width_x, width_y, width_h, row_height):
    row_inv = rows + 1

    corners_id = [(min_x, row_height * row_inv + min_y), 
                  (min_x, row_height * row_inv + min_y + row_height + 0.1), 
                  (min_x + width_id, row_height * row_inv + min_y + row_height + 0.1),
                  (min_x + width_id, row_height * row_inv + min_y),
                  (min_x, row_height * row_inv + min_y)
                  ]

    block.add_lwpolyline(corners_id)

    msp.add_text("α/α", dxfattribs= {
            "layer": layer_name,
            "style": "Arial",
            "height": 0.3 }).set_pos((min_x + 0.1, row_height * row_inv + min_y + 0.15), align= "LEFT")


    corners_x = [(min_x + width_id, row_height * row_inv + min_y), 
                  (min_x + width_id, row_height * row_inv + min_y + row_height + 0.1), 
                  (min_x + width_id + width_x, row_height * row_inv + min_y + row_height + 0.1),
                  (min_x + width_id + width_x, row_height * row_inv + min_y),
                  (min_x + width_id, row_height * row_inv + min_y)
                  ]

    block.add_lwpolyline(corners_x)

    msp.add_text("x (m)", dxfattribs= {
            "layer": layer_name,
            "style": "Arial",
            "height": 0.3 }).set_pos((min_x + width_id + 0.1, row_height * row_inv + min_y + 0.15), align= "LEFT")


    corners_y = [(min_x + width_id + width_x, row_height * row_inv + min_y), 
                  (min_x + width_id + width_x, row_height * row_inv + min_y + row_height + 0.1), 
                  (min_x + width_id + width_x + width_y, row_height * row_inv + min_y + row_height + 0.1),
                  (min_x + width_id + width_x + width_y, row_height * row_inv + min_y),
                  (min_x + width_id + width_x, row_height * row_inv + min_y)
                  ]

    block.add_lwpolyline(corners_y)

    msp.add_text("y (m)", dxfattribs= {
            "layer": layer_name,
            "style": "Arial",
            "height": 0.3 }).set_pos((min_x + width_id + width_x + 0.1, row_height * row_inv + min_y + 0.15), align= "LEFT")
    

    corners_h = [(min_x + width_id + width_x + width_y, row_height * row_inv + min_y), 
                  (min_x + width_id + width_x + width_y, row_height * row_inv + min_y + row_height + 0.1), 
                  (min_x + width_id + width_x + width_y + width_h, row_height * row_inv + min_y + row_height + 0.1),
                  (min_x + width_id + width_x + width_y + width_h, row_height * row_inv + min_y),
                  (min_x + width_id + width_x + width_y, row_height * row_inv + min_y)
                  ]

    block2.add_lwpolyline(corners_h)

    msp.add_text("H (m)", dxfattribs= {
            "layer": layer_name,
            "style": "Arial",
            "height": 0.3 }).set_pos((min_x + width_id + width_x + width_y + 0.1, row_height * row_inv + min_y + 0.15), align= "LEFT")



def add_row(df, msp, block, block2, layer_name, rows, min_x, min_y, width_id, width_x, width_y, width_h, row_height):
    index = df.name
    row_inv = rows - index

    corners_id = [(min_x, row_height * row_inv + min_y), 
                  (min_x, row_height * row_inv + min_y + row_height), 
                  (min_x + width_id, row_height * row_inv + min_y + row_height),
                  (min_x + width_id, row_height * row_inv + min_y),
                  (min_x, row_height * row_inv + min_y)
                  ]

    block.add_lwpolyline(corners_id)

    msp.add_text(df['id'], dxfattribs= {
            "layer": layer_name,
            "style": "Arial",
            "height": 0.3 }).set_pos((min_x + 0.1, row_height * row_inv + min_y + 0.05), align= "LEFT")


    corners_x = [(min_x + width_id, row_height * row_inv + min_y), 
                  (min_x + width_id, row_height * row_inv + min_y + row_height), 
                  (min_x + width_id + width_x, row_height * row_inv + min_y + row_height),
                  (min_x + width_id + width_x, row_height * row_inv + min_y),
                  (min_x + width_id, row_height * row_inv + min_y)
                  ]

    block.add_lwpolyline(corners_x)

    msp.add_text(df['x'], dxfattribs= {
            "layer": layer_name,
            "style": "Arial",
            "height": 0.3 }).set_pos((min_x + width_id + 0.1, row_height * row_inv + min_y + 0.05), align= "LEFT")


    corners_y = [(min_x + width_id + width_x, row_height * row_inv + min_y), 
                  (min_x + width_id + width_x, row_height * row_inv + min_y + row_height), 
                  (min_x + width_id + width_x + width_y, row_height * row_inv + min_y + row_height),
                  (min_x + width_id + width_x + width_y, row_height * row_inv + min_y),
                  (min_x + width_id + width_x, row_height * row_inv + min_y)
                  ]

    block.add_lwpolyline(corners_y)

    msp.add_text(df['y'], dxfattribs= {
            "layer": layer_name,
            "style": "Arial",
            "height": 0.3 }).set_pos((min_x + width_id + width_x + 0.1, row_height * row_inv + min_y + 0.05), align= "LEFT")
    

    corners_h = [(min_x + width_id + width_x + width_y, row_height * row_inv + min_y), 
                  (min_x + width_id + width_x + width_y, row_height * row_inv + min_y + row_height), 
                  (min_x + width_id + width_x + width_y + width_h, row_height * row_inv + min_y + row_height),
                  (min_x + width_id + width_x + width_y + width_h, row_height * row_inv + min_y),
                  (min_x + width_id + width_x + width_y, row_height * row_inv + min_y)
                  ]

    block2.add_lwpolyline(corners_h)

    msp.add_text(df['h'], dxfattribs= {
            "layer": layer_name,
            "style": "Arial",
            "height": 0.3 }).set_pos((min_x + width_id + width_x + width_y + 0.1, row_height * row_inv + min_y + 0.05), align= "LEFT")


def create_table(input_filename):
    doc = ezdxf.new(dxfversion= "R2010")    
    doc.styles.new("Arial", dxfattribs={"font": "arial.ttf"})
    layer_name = "coord_table"

    doc.layers.new(layer_name, dxfattribs={"color": 7}) 
    msp = doc.modelspace()

    min_x = 0
    min_y = 0

    blockname = "table_block"
    blockname2 = "table_block_height"
    block = doc.blocks.new(name= blockname, base_point= (min_x, min_y))
    block2 = doc.blocks.new(name= blockname2, base_point= (min_x + 1, min_y + 1))
    msp.add_blockref(blockname, (min_x, min_y), dxfattribs= {"layer": layer_name})
    msp.add_blockref(blockname2, (min_x + 1, min_y + 1), dxfattribs= {"layer": layer_name})

    df = pd.read_csv(input_filename, header= None, names= ["id", "x", "y", "h"])
    df['id'] = df['id'].astype(str)
    df['lens'] = df['id'].str.len()

    rows = len(df)
    len_id = 2 if df['lens'].max() < 2 else df['lens'].max()
    len_x = 8
    len_y = 9
    len_h = 6

    factor = 0.35
    width_id = factor * (1 + len_id)
    width_x = factor * (1 + len_x)
    width_y = factor * (1 + len_y)
    width_h = factor * (1 + len_h)
    row_height = 0.5

    add_head(msp, block, block2, layer_name, rows, min_x, min_y, width_id, width_x, width_y, width_h, row_height)
    df.apply(add_row, axis= 1, args= [msp, block, block2, layer_name, rows, min_x, min_y, width_id, width_x, width_y, width_h, row_height])

    doc.saveas(f"coord_table.dxf", encoding="utf-8")
    print("Table done!")


def main():
    arg1 = sys.argv[1]

    if arg1 == "help" or arg1 == "--h" or arg1 == "-h":
        help()
    else:
        input_filename = arg1
        create_table(input_filename)

if __name__ == "__main__":
    main()

