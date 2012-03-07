# Ebook Metadata Editor


`ebmeta` is a tool for editing metadata in an ebook file (Epub,
Mobipocket, or PDF). When the first edit is made, the entire ebook file
is backed up to `./.backup/FILE.backup` under the folder where the
working file is, to allow for safely resetting.

Calibre is used to write metadata changes to the ebook file.

Fields that are available for editing are:

* title; title sort
* authors; author sort
* publication date; publisher
* book producer
* isbn; uuid; language
* tags; rating
* series; series index
* description


## Requirements


* Beautiful Soup -- HTML/XML stream parsing and manipulation for Python
* Calibre (Calibre's `ebook-convert` command is used to manipulate and
  build EPUB package files.)
* pandoc -- all purpose converter to and from Markdown syntax
* Python 2.7
* YAML for Python -- minimal config / serialization syntax
* zenity -- dialog boxes for scripts
* zip -- command line tool for writing/updating Zip files from the
  InfoZip package

Install Calibre on a Unix box:

    sudo python -c "import sys; py3 = sys.version_info[0] > 2; u = __import__('urllib.request' if py3 else 'urllib', fromlist=1); exec(u.urlopen('http://status.calibre-ebook.com/linux_installer').read()); main()"

Ubuntu packages for the rest of the requirements:

    sudo apt-get install pandoc python-beautifulsoup python-yaml zenity


## Installation


No installation script is provided. The simplest way to install ebmeta
is to download the source as a `.zip` or `.tar.gz`, or `git clone`. Put
the package files in `~/Apps/ebmeta` and then do this:

    chmod +x ~/Apps/ebmeta/__main__.py
    ln --symbolic ~/Apps/ebmeta/__main.py__ ~/bin/ebmeta

(Make sure `~/bin` is in your `$PATH` variable when you run `ebmeta`.)


### Windows


`ebmeta` should work in Windows as well. Make sure all your requirements
are installed and make sure you can run `python`, `pandoc`, and
`ebook-convert` by just calling their name from the command line. (You
probably will have to edit your `$PATH` environment variable.)

To invoke `ebmeta`, you can either do

    python -m [path to...]\ebmeta.zip [ebmeta arguments]

Or create a batch file in your `$PATH` that calls Python in this way and
passes command line arguments through to ebmeta.


## Usage


**Backup an ebook file as an embedded file within itself**:

    ebmeta backup FILE

Copies `FILE` to `./.backup/FILE.backup` under the folder containing
`FILE`. If you screw up the outer `FILE` later on, you can just extract
the backup using a Zip archiving tool.

**Display metadata on the command line**:

    ebmeta display FILE

**Edit metadata in a popup dialog box**:

    ebmeta edit FILE

**Reset metadata to state before first edit with this program**:

    ebmeta reset FILE

**Get all command line help**:

    ebmeta --help
