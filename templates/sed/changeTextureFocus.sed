s/<texturefocus \([^>]*\)border="\([^{$"]*\)"/<texturefocus \1border="{{ScaleBorder('\2')}}"/g
s/<alttexturefocus \([^>]*\)border="\([^{$"]*\)"/<alttexturefocus \1border="{{ScaleBorder('\2')}}"/g
s/<texturenofocus \([^>]*\)border="\([^{$"]*\)"/<texturenofocus \1border="{{ScaleBorder('\2')}}"/g
s/<alttexturenofocus \([^>]*\)border="\([^{$"]*\)"/<alttexturenofocus \1border="{{ScaleBorder('\2')}}"/g
