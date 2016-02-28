#!/usr/bin/env python3
import optparse
import os.path
import os
import glob
import re
import importlib
import errno
import time

settings = {
    "template_folder": "templates/",
    "out_folder": "out/",
    "base_resolution": [1280, 720],
    "out_resolution": [720, 480],
    "verbose": False,
    "configModule": "templates.config",
    "ignore_timestamps": False,
}

config = None
MAX_SUBSTITUTIONS_PER_LINE = 100


if not hasattr(globals()["__builtins__"], "xrange"):
    """ Python3 range is Python2 xrange. """
    def xrange(*args):
        return range(*args)


def get_template_paths(folder, extension=".xml"):
    pattern = folder + "*" + extension
    xmlFiles = list(glob.glob(pattern))
    if settings["verbose"]:
        print("Number of templates:\n%d" % len(xmlFiles))
        # print("Founded templates:\n%s" % ("\n".join(xmlFiles),))

    return xmlFiles


def parse_options():
    p = optparse.OptionParser()
    p.add_option('--out', '-o', default=settings["out_folder"])
    p.add_option('--xscale', '-x', default=str(settings["base_resolution"][0]))
    p.add_option('--yscale', '-y', default=str(settings["base_resolution"][1]))
    p.add_option('--templates', '-t', default=settings["template_folder"])
    # default=int(settings["verbose"]))
    p.add_option('--verbose', '-v', action="store_true")
    p.add_option('--config', '-c', default=str(settings["configModule"]))
    p.add_option('--force', '-f',
                 default=settings["ignore_timestamps"],
                 action="store_true")
    options, arguments = p.parse_args()
    settings["base_resolution"] = [int(options.xscale), int(options.yscale)]
    settings["out_folder"] = options.out
    settings["template_folder"] = options.templates  # + os.path.sep
    settings["verbose"] = bool(options.verbose)
    settings["configModule"] = options.config
    settings["ignore_timestamps"] = bool(options.force)


def do_substitutions(line, iLine=-1):
    """ Search for call of function, i.e. to rescale. """
    iLineSub = 0
    while iLineSub < MAX_SUBSTITUTIONS_PER_LINE:
        m = re.search("[{]{1,2}[^{}:]+[}]{1,2}", line)
        iLineSub += 1
        if m is None:
            break
        # print("Match: %s" % line[m.start():m.end()])
        s = m.start()
        e = m.end()

        # Change '{{x}' and '{x}}' cases into '{x}'
        if line[s+1] == "{" and line[e-2] != "}":
            s += 1
        elif line[s+1] != "{" and line[e-2] == "}":
            e -= 1

        # Handle '{{x}}' and '{x}'
        if line[s+1] == "{" and line[e-2] == "}":
            # Eval python code
            pre = line[0:s]
            cmd = line[s+2: e-2]
            post = line[e:len(line)]
            try:
                ret_cmd = eval(cmd)
            except ValueError:
                ret_cmd = cmd
                print("\t(%d) Run of '%s' failed!" % (iLine, cmd,))
            except SyntaxError:
                ret_cmd = cmd
                print("\t(%d) Syntax Error in '%s'" % (iLine, cmd,))
            except NameError:
                ret_cmd = cmd
                print("\t(%d) Run of '%s' failed!" % (iLine, cmd,))
            except TypeError:
                ret_cmd = cmd
                print("\t(%d) Run of '%s' failed!" % (iLine, cmd,))
            else:
                if settings["verbose"]:
                    print("\t(%d) Run '%s'." % (iLine, cmd,))
            line = pre + str(ret_cmd) + post
        else:
            # Variable substitution
            pre = line[0:s]
            var = line[s+1: e-1].strip()
            post = line[e:len(line)]
            if settings["verbose"]:
                print("\tSubstitute %s" % (var,))
            var = config.substitutions.get(var, var)
            line = pre + str(var) + post

    return line


def substitute(file_in, file_out):
    f = open(file_in, 'r')
    f2 = open(file_out, 'w')
    l = f.readline()
    iLine = 1
    while(l):
        l2 = do_substitutions(l, iLine)
        f2.write(l2)
        l = f.readline()
        iLine += 1

    f2.close()
    f.close()


def makedirs(path, mode=511, exist_ok=True):
    """ No exist_ok arg in Python2. """
    try:
        os.makedirs(path, mode)
    except OSError as e:
        if e.errno != errno.EEXIST or not exist_ok:
            raise e


def main():
    parse_options()

    # Load config
    globals()["config"] = importlib.import_module(settings["configModule"])

    # Overwrite main settings
    if(hasattr(config, "overrideSettings") and
       callable(config.overrideSettings)):
        config.overrideSettings(settings)

    makedirs(os.path.join(os.path.curdir,
                          settings["out_folder"]),
             exist_ok=True)

    templates = get_template_paths(settings["template_folder"])
    for file_in in templates:
        file_out = os.path.join(
            settings["out_folder"],
            os.path.basename(file_in))
        # file_in[file_in.find(os.path.sep)+1:]])

        # Check if update is required
        bUpdate = True
        try:
            timestamp_in = os.path.getctime(file_in)
            timestamp_out = os.path.getctime(file_out)
            #  ctime_in = time.ctime(timestamp_in)
            #  ctime_out = time.ctime(timestamp_out)
            if(timestamp_out > timestamp_in and not settings["ignore_timestamps"]):
                bUpdate = False
        except OSError:
            pass

        if not bUpdate:
            continue

        if settings["verbose"] or True:
            print("Handle %s" % (os.path.basename(file_in),))

        substitute(file_in, file_out)


# ==========================================================

""" Helper functions which are used in the templates. """


def ScaleGeneral(sX, base_dim, out_dim):
    """ Scaling of width, height, x-position or y-position.
    Note that inputs handled as string with or without trailing 'r'.

    Input args:
        x - str type with content '%d' or '%dr'.
    Output:
        ret = string
    """
    sX = str(sX).strip()

    if(sX == "auto"
       or sX == "-"
       or sX == ""
       or sX[-1] == "%"):
        return sX

    bRight = sX[-1] == "r"
    if bRight:
        sX = sX[:-1]

    x = int(sX)
    sign = bool(x > 0) - bool(x < 0)
    x = int(x * out_dim / base_dim)

    # Omit return of 0 for non-zero inputs.
    if x is 0 and sign is not 0:
        x = sign

    if bRight:
        return str(x) + "r"
    else:
        return str(x)


def ScaleX(x):
    """ Adapt position or width to other skin resolution.
    Input args:
        x - str type with content '%d' or '%dr'.
    """
    return ScaleGeneral(str(x),
                        settings["base_resolution"][0],
                        settings["out_resolution"][0])


def ScaleY(y):
    """ Adapt position or height to other skin resolution. """
    return ScaleGeneral(str(y),
                        settings["base_resolution"][1],
                        settings["out_resolution"][1])


def ScaleBorder(b):
    """ Input is integer or "a,b,c,d".
    The vertical scaling use ScaleX to conserve the local aspect ratio,
    but not the global one.
    """
    lb = str(b).split(",")
    scaled = [ScaleX(x) for x in lb]
    return ",".join(scaled)


def ScaleBorder2(b):
    """ Input is integer or "a,b,c,d" or "a,b".
    Like ScaleBorder but jump between ScaleX and ScaleY.
    """
    lb = str(b).split(",")
    scaled = []
    fnames = [ScaleX, ScaleY]
    for i in xrange(len(lb)):
        scaled.append(fnames[i % 2](lb[i]))
    return ",".join(scaled)


def iScaleX(x):
    """ Convert to int made evaluations easier but
    could fail for non-integer inputs.
    """
    return int(ScaleX(x))


def iScaleY(y):
    return int(ScaleY(y))


# ==========================================================
if __name__ == '__main__':
    main()
