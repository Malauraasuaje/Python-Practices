def tetris():

screen = [["🔳","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲"]
["🔳","🔳","🔳","🔲","🔲","🔲","🔲","🔲","🔲","🔲"],
["🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲"],
["🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲"],
["🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲"],
["🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲"],
["🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲"],
["🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲"],
["🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲"],
["🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲","🔲"]]

for row in screen:
        print("".join(map(str, row)))

tetris()