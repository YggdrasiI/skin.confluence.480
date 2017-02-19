s/<texturesliderbackground border="\([^$"]*\)"/<texturesliderbackground border="{{ScaleBorder('\1')}}"/g
s/<texturesliderbar border="\([^$"]*\)"/<texturesliderbar border="{{ScaleBorder('\1')}}"/g
s/<texturesliderbarfocus border="\([^$"]*\)"/<texturesliderbarfocus border="{{ScaleBorder('\1')}}"/g
s/<texturefocus border="\([^$"]*\)"/<texturefocus border="{{ScaleBorder('\1')}}"/g
s/<texturenofocus border="\([^$"]*\)"/<texturenofocus border="{{ScaleBorder('\1')}}"/g

