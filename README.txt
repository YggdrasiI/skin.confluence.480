Skin based on skin.confluence of OpenELEC 6.0.1.

The targeting use case is the RPi 1 with a CRT TV on the composite output.
Currently, only the main controls was changed.

The following changes was made:
  • General downscaling of GUI from 720p to 480p.
  • Increase font size to made text more readable. 
  • Add VT323 font. Looks vintage, eh? 
  • Increase width of many GUI elements to reflect the
    styling issues due big fonts for the confluence theme.
    Note that scrolling of text consume a lot of CPU/GPU time.
  • Added theme with opaque background textures. This could reduce
    flickering, see (Settings>Appearance).
  • Added color set with better contrast.



For developers:
  • The sed scripts in `./templates/sed` could also be used for other skins. They
    wrap the values of <width>, <height>, <left>, <top> by a function. This is dual
    to the font resizing but more flexible.
  • I was disappointed about the capabilities of
  Kodi's $VAR and $PARAM capabilities (or simply misunderstand how to use them…)
  and attached an own variant for variables. 
  ./templates contains the normal skin definitions but some values was
  replaced by `{variable}` or `{{Python code}}` token.

  `./templates/config.py` contains the definition of variables.
 
  Run `./parseTemplates.py` to translate the XML files from ./templates
  into ./out. ('out' was defined as skin directory in `addon.xml`.)

  • Use `./buildPackage.py` to export the data for a release of the skin.
    See ./buildPackage --help for more information.

