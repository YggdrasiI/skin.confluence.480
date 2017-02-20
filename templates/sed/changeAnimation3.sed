/<animation [^$>]*effect="rotatex"/ {
  s/center="\([^$"]*\)"/center="{{ScaleBorder2('\1')}}"/ 
}

