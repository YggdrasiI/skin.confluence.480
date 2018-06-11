s/<bordertexture \([^>]*\)border="\([^{$"]*\)"/<bordertexture \1border="{{ScaleBorder('\2')}}"/g
s/<bordersize>\([0-9]*\)</<bordersize>{{ScaleBorder('\1')}}</g
