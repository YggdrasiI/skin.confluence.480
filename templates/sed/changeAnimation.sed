# Substitute in properties of animation and effect
# for types fade, zoom and rotate.
/<\(animation [^$>]*effect="\(rotation\|zoom\)"\|effect [^$>]*type="\(rotation\|zoom\)\)"/ {
  s/center="\([^$"]*\)"/center="{{ScaleBorder2('\1')}}"/ 

# Note: With zooms you can also specify the coordinates and dimensions of the texture. (ie start="posx,posy,width,height"). 
    /<\(animation [^$>]*effect="\(zoom\)"\|effect [^$>]*type="\(zoom\)\)"/ {
      s/start="\(\([^$",]*,\)\{3\}[^$",]*\)"/start="{{ScaleBorder2('\1')}}"/ 
      s/end="\(\([^$",]*,\)\{3\}[^$",]*\)"/end="{{ScaleBorder2('\1')}}"/ 
    }
}

/<\(animation [^$>]*effect="\(slide\)"\|effect [^$>]*type="\(slide\)"\)/ {
 s/start="\([^$"]*\)"/start="{{ScaleBorder2('\1')}}"/ 
 s/end="\([^$"]*\)"/end="{{ScaleBorder2('\1')}}"/ 
}

