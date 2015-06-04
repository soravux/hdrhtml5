import os
import sys
import time
import subprocess

# Usage : batchHDRprocessing.py top_level_folder (ex : ./path/to/20140924)

if __name__ == '__main__':
    for path, dirs, files in os.walk(sys.argv[1]):
        if 'envmap.js' in files:
            continue
        for f in files:
            if not '.exr' in f:
                continue

            newf = f.rsplit(".")[0] + ".js"
            fullpath = os.path.join(path, f)
            fullpathNew = os.path.join(path, newf)

            print("Converting {}...".format(fullpath), end="", flush=True)
            atime = time.time()
            subprocess.check_call(["python", "gethdr.py", fullpath, fullpathNew])
            btime = time.time()
            print(" {} seconds elapsed".format(btime-atime))
