import glob
for file in glob.glob('./*.svg'):
     with open(file, 'r+') as f:
         original_svg = f.read()
         f.seek(0)
         f.write(original_svg.replace('<path ', '<path fill="param(fill) #000" fill-opacity="param(fill-opacity)" stroke="param(outline) #fff" stroke-width="param(outline-width) 0" stroke-opacity="param(outline-opacity)" '))
         f.close()
