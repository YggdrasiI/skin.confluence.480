/<animation [^$>]*effect="rotate"/ {
  s/center="\([^$"]*\)"/center="{{ScaleBorder2('\1')}}"/ 
}

