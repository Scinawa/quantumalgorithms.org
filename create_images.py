#!/usr/bin/python
import subprocess
import sys
import os

# due to the power of imagemagic and convert (magick in ImageMagick 7+) command, this python could have been a bash
# kept python in case more power is needed later

def create_images(directory, latex_files):
  for latex_document in latex_files:

    document_name = latex_document.split(".")
    print("\n\n {} \n\n".format(latex_document))
    subprocess.call(["pdflatex", "-output-directory={}".format(directory), latex_document])

    # "-background", "white", "-alpha",  "remove",
    subprocess.call(["convert", "-density", "300", document_name[0]+".pdf", "-trim",  "-colorspace", "RGB", document_name[0]+".png"])


if __name__  == "__main__":
  if len(sys.argv) == 1:
    print("-"*80)
    print("python3 create_images.py path")
    print("This software accepts only one argument as input")
    print("- If path is a .tex file : convert only that tex file into cropped png")
    print("- If path is a directory : convert all .tex file into that directory to cropped png")
    print("-"*80)

  elif len(sys.argv) == 2:

    if str(sys.argv[1]).endswith("tex"):
      # it's a single file
      directory=os.path.dirname(sys.argv[1])
      create_images(directory, [ str(sys.argv[1]) ]  )
    else:
      # it is a directory

      files = [str(sys.argv[1])+"/"+str(file) for file in os.listdir(str(sys.argv[1]))  if file.endswith(".tex")   ]
      create_images(str(sys.argv[1]), files)
      
  else:
    print("Nope")


  
