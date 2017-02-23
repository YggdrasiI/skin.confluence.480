#!/usr/bin/env python3
""" Script exports files which are required to
share the addon.
"""

import optparse
import os.path
import os
import glob
import errno
import shutil

# See parse_options for help
settings = {
    "dest_folder": "/dev/shm",
    "copy_templates": False,
    "pack_textures": False,
    "zip_addon": False,  # Not implemented
    "force": False,
    "ignored_patterns": [".*", ".git",
                         "screenshots",
                         "media",
                         "720p",
                         "themes",
                         "tmp",
                         "xml",
                         "__pycache__", "*.pyc",
                         ],
    # This files are required to rebuild the skin.
    "template_files": ["templates",
                       "parseTemplates.py",
                       "buildPackage.py"
                       ],
}

if not hasattr(globals()["__builtins__"], "raw_input"):
    """ Python2 raw_input is called input in Python3. """
    raw_input = input


def parse_options():
    p = optparse.OptionParser()
    p.add_option('--dest', '-d', default=settings["dest_folder"],
                 help="Destination folder for package")
    p.add_option('--force', '-f', action="store_true",
                 help="Skip confirm prompt.")
    p.add_option('--pack', '-p', action="store_true",
                 help="Call TexturePacker to create texture bundles.")
    p.add_option('--no-pack', '-n', action="store_true",
                 help="Ignore texture bundles and copy unpacked images.")
    p.add_option('--with-templates', '-t', action="store_true",
                 help="Copy template folder and buildScripts.")
    options, arguments = p.parse_args()
    settings["dest_folder"] = options.dest
    settings["copy_templates"] = bool(options.with_templates)
    settings["pack_textures"] = bool(options.pack)
    settings["ignore_packed"] = bool(options.no_pack)
    settings["force"] = bool(options.force)


def makedirs(path, mode=511, exist_ok=True):
    """ No exist_ok arg in Python2. """
    try:
        os.makedirs(path, mode)
    except OSError as e:
        if e.errno != errno.EEXIST or not exist_ok:
            raise e


def copy(src, dest, ignore_patterns=[]):
    try:
        shutil.copytree(
            src, dest,
            ignore=shutil.ignore_patterns(
                *ignore_patterns))
    except OSError as e:
        # If the error was caused because the source wasn't a directory
        if e.errno == errno.ENOTDIR:
            shutil.copy(src, dest)
        else:
            print(' Directory not copied. Error: %s' % e)


def call_theme_packer(to_pack_folder):
    if to_pack_folder == "media":
        pack_path = "media/{}".format("Textures.xbt")
        arg = "-dupecheck"
    else:
        pack_path = "media/{}{}".format(
            os.path.basename(to_pack_folder), ".xbt")
        arg = ""

    os.system("TexturePacker {0} -input {1} -output {2}".format(
        arg, to_pack_folder, pack_path))


def copy_addon(source_folder, dest_folder):
    if "^"+source_folder in "^"+dest_folder:
        print(""" Bad input arguments?!
              Destination folder will be cleared, but contains
              the source folder. Please check out the path settings..
              """)
        return
    elif os.path.exists(dest_folder):
        # shutil.copytree require nonexistance of destination.
        shutil.rmtree(dest_folder)

    print(" - Create addon structure.")
    to_ignore = settings["ignored_patterns"] + settings["template_files"]
    copy(source_folder, dest_folder, to_ignore)

    if settings["pack_textures"]:
        print(" - Pack default theme")
        call_theme_packer("media")

        theme_folders = list(glob.glob(
            os.path.join(source_folder, "themes", "*")))
        for theme in theme_folders:
            if os.path.isdir(theme):
                print(" - Pack %s" % (theme))
                call_theme_packer(theme)

    copy_textures(source_folder, dest_folder)
    if settings["copy_templates"]:
        copy_templates(source_folder, dest_folder)

    print(" - Build finished.")


def copy_textures(source_folder, dest_folder):
    """ Copy texture pack files if available and
    copy unpacked files otherwise.
    """
    default_texture_file = list(glob.glob(
        os.path.join(source_folder, "media", "Textures.xbt")))
    texture_files = list(glob.glob(
        os.path.join(source_folder, "media", "*.xbt")))
    texture_files = [x for x in texture_files if x not in default_texture_file]

    if len(default_texture_file) > 0:
        f = default_texture_file[0]
        print(" - Copy default theme %s." % (f,))
        makedirs(os.path.join(dest_folder, "media"), exist_ok=True)
        copy(f, os.path.join(dest_folder, "media", os.path.basename(f)))
    else:
        copy(os.path.join(source_folder, "media"),
             os.path.join(dest_folder, "media"))

    if len(texture_files) > 0:
        for f in texture_files:
            print(" - Copy %s " % (f))
            copy(f, os.path.join(dest_folder, "media",
                                 os.path.basename(f)))
    else:
        if os.path.exists(os.path.join(source_folder, "themes")):
            copy(os.path.join(source_folder, "themes"),
                 os.path.join(dest_folder, "themes"))


def copy_templates(source_folder, dest_folder):
    print(" - Copy templates and build files")
    for f_or_d in settings["template_files"]:
        copy(os.path.join(source_folder, f_or_d),
             os.path.join(dest_folder, f_or_d),
             settings["ignored_patterns"])


def main():
    parse_options()

    this_folder_name = os.path.basename(
        os.path.abspath(os.path.curdir))
    dest_folder_name = os.path.join(
        settings["dest_folder"],
        this_folder_name)

    if settings["force"]:
        confirm = True
    else:
        confirm_str = raw_input(" Copy\t'%s'\n to\t%s.\n Continue? (Y/n) " % (
            this_folder_name, dest_folder_name))
        confirm = confirm_str.lower() in ["y", "yes", ""]

    if confirm:
        print(" - Start build.")
        copy_addon(os.path.curdir, dest_folder_name)
    else:
        print(" Build abort by user.")


# ==========================================================
if __name__ == '__main__':
    main()
