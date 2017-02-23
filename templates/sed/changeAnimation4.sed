# Similar to  changeAnimation.sed, but with 'reversible="false"' substring.
# Example line <animation reversible="false" effect="zoom" start="-2,36,222,318" end="-28,0,284,390"
/<animation reversible="false" [^$>]*effect="\(zoom\)"/ {
  s/start="\([^$"]*\)"/start="{{ScaleBorder2('\1')}}"/ 
    s/end="\([^$"]*\)"/end="{{ScaleBorder2('\1')}}"/ 
}
