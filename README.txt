Skin based on skin.confluence (currently version 3.0.46).

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
  into ./out. (The 'out'-folder was defined skin directory in `addon.xml`.)

  • Use `./buildPackage.py` to export the data for a release of the skin.
    See ./buildPackage --help for more information.


Workflow for updates on new confluence versions:
 1. Checkout original_skin.
 2. Update static files like addon.xml, changelog.txt
    and folders
    resources, languages, media, colors, fonts, backgrounds
    This changes should be repeat in step 3/4, too.

 3. Replace xml files in /templates with new files of
    orginial confluence skin. And commit changes.

 4. Checkout sedChangesOnly and replace xml files
    in templates directory, too.
    (cd templates ; rm *.xml;  git checkout original_skin *.xml)
    Then, run sed scripts and commit changes.

 4. Checkout unstable branch and apply changes of step 2 and 3. 
   Then run sed scripts (cd templates/sed; ./runSubstitutions.sh *.sed ),
    parse templates ( ./parseTemplates.py ),
    and build new package ( ./buildPackage --dest /dev/shm -t -p -f )

 5. Zip result, .i.e.    
    cd /dev/shm ; zip -r skin.confluence.480.zip skin.confluence.480

 6. Copy skin-zip to media center and resolve errors.
