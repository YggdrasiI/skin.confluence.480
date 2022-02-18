# Matches for scaling by ScaleX
/<param name="DialogBackgroundWidth"/ { bx }
/<param name="DialogHeaderWidth"/ { bx }
/<param name="CloseButtonLeft"/ { bx }
/<param name="panel-left"/ { bx }
/<param name="panel-width"/ { bx }
/<param name="item-left"/ { bx }
/<param name="label-width"/ { bx }

# Matches for scaling by ScaleY
/<param name="DialogBackgroundHeight"/ { by }
/<param name="DialogHeaderHeight"/ { by }
/<param name="CloseButtonTop"/ { by }

# Go to end if no match
b

# ScaleX
 {
	:x ;
	s|value="\([^$"]\+\)"|value="{{ScaleX('\1')}}"|
	b
}

# ScaleY
 {
	:y ;
	s|value="\([^$"]\+\)"|value="{{ScaleY('\1')}}"|
	b
}
