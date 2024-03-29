# Kodi skin with big fonts

This skin based on skin.confluence, but scaling most GUI elements up.
An early targeting system was a RPI 1 with CRT TV on composite output, but
it is also useable on modern screens.

## Versions

Newest supported skin version for Kodi 19.x (Matrix): 4.7.14 (=> master branch).  
Newest supported skin version for Kodi 18.x (Leia): 4.5.5 (=> release_4.5.5 branch).  
Newest supported skin version for Kodi 17.x (Krypton): 3.1.6 (=> release_3.1.6 branch)  
Older skin version for Kodi 15.2-16.x: See release_0.8 branch.  

## Changes

The following changes were made:
- General downscaling of GUI from 720p to 480p.
- Increase font size to made text more readable.
- Add VT323 font.
- Increase width of many GUI elements to reflect the
  styling issues due big fonts for the confluence theme.
- Omiting scrolling of text if possible. (Scrolling of text consumes
  a lot of CPU/GPU time.)
- Added theme with opaque background textures. This could reduce
  flickering, see (Settings>Appearance).
- Added color set with better contrast.


## How to build (short)

- `./parseTemplates.py`
- `./buildPackage.py [--pack]`
- `cd /dev/shm ; zip -r skin.confluence.480.zip skin.confluence.480`


## How to build (long)

- Run `./parseTemplates.py` to translate the XML files from ./templates
into ./out. The 'out'-folder was defined as skin directory in `addon.xml`.
- Use `./buildPackage.py` to export the data for a release of the skin.
  Add `--pack` to compress the images with Kodi's TexturePacker.
	If not installed, you could compile the tool with `./TexturePackerBuild.sh`!
  See `./buildPackage.py --help` for more information.


## Notes for developers

- The sed scripts in `./templates/sed` could also be used for other skins. They
  wrap the values of many tags like <width>, <height>, <left>, <top>
	by a function. This is dual to font resizing, but more flexible.
- I was disappointed about the capabilities of
  Kodi's $VAR and $PARAM capabilities (or simply misunderstand how to use them…)
  and attached an own variant for variables.
  .`/templates` contains the normal skin definitions but some values was
  replaced by `{variable}` or `{{Python code}}` token.

- `./templates/config.py` is containing the definition of constants.


### Workflow for updates on new confluence versions (sketch)

1. Checkout branch 'original_skin'.
   This branch holds the used reference of skin.confluence.

2. Update static files like addon.xml, changelog.txt
   and the folders: 720p, resources, languages, media,
   colors, fonts and backgrounds.

   Commit these changes now, to cherry-pick them in step 4/5.

3. Replace xml files in ./templates with new files of
   original confluence skin (./720p) and commit changes again.

4. Checkout branch 'sedChangesOnly' and cherry-pick changes of 2.
   Replace xml files like in 3., and finally run sed scripts.
   ( `cd templates ; rm *.xml;  git checkout original_skin *.xml;
   cd sed; ./runSubstitutions.sh *.sed`)

   Commit changes.

5. Rebase unstable branch on new sedChangesOnly.
   This should lift the manual changes of the templates upon the new
   automated.
   This step required manually work, especially if new xml files was added.
   Run `./parseTemplates.py --force` to check if templates are still valid.

6. Build new package ( `./buildPackage.py --dest /dev/shm -t -p -f` )

7. Zip result, .i.e.  
   `cd /dev/shm ; zip -r skin.confluence.480.zip skin.confluence.480`

8. Copy skin-zip to media center and resolve errors.


### Testing of changes

	```
	./parseTemplates.py -f --out ~/.kodi/addons/skin.confluence.480/out/
	 kodi-send --action="ReloadSkin()"
	```
