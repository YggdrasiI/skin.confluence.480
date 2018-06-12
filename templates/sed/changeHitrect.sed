# $  to skip lines with $PARAM
s/<hitrect x="\([^"{]\+\)" y="\([^"{]\+\)" w="\([^"{]\+\)" h="\([^"{]\+\)"/<hitrect x="{{ScaleX('\1')}}" y="{{ScaleY('\2')}}" w="{{ScaleX('\3')}}" h="{{ScaleY('\4')}}"/g
