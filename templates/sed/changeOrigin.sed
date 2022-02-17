# $ to skip lines with $PARAM
s/<origin x="\([^"{]\+\)" y="\([^"{]\+\)"/<origin x="{{ScaleX('\1')}}" y="{{ScaleY('\2')}}"/g
