# Substitute in properties of animation and effect
# for types fade, zoom and rotate.
/<\(focusedlayout\|itemlayout\) / {
  s/width="\([^$"]*\)"/width="{{ScaleX('\1')}}"/ 
  s/height="\([^$"]*\)"/height="{{ScaleY('\1')}}"/ 
}

