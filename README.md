# Epub Metadata Editor


`epubmeta` is a tool...


## Requirements


* Beautiful Soup -- HTML/XML stream parsing and manipulation for Python
* Calibre (Calibre's `ebook-convert` command is used to manipulate and
  build EPUB package files.)
* pandoc -- all purpose converter to and from Markdown syntax
* Python 2.7
* YAML for Python -- minimal config / serialization syntax
* zip -- command line tool for writing/updating Zip files from the
  InfoZip package

Install Calibre on a Unix box:

    sudo python -c "import sys; py3 = sys.version_info[0] > 2; u = __import__('urllib.request' if py3 else 'urllib', fromlist=1); exec(u.urlopen('http://status.calibre-ebook.com/linux_installer').read()); main()"

Ubuntu packages for the rest of the requirements:

    sudo apt-get install pandoc python-beautifulsoup python-yaml


## Installation


No installation script is provided. The simplest way to install mdepub
is to download the source as a `.zip` or `.tar.gz`, or `git clone`. Put
the package files in `~/Apps/epubmeta` and then do this:

    chmod +x ~/Apps/epubmeta/__main__.py
    ln --symbolic ~/Apps/epubmeta/__main.py__ ~/bin/epubmeta

(Make sure `~/bin` is in your `$PATH` variable when you run `epubmeta`.)


### Windows


`epubmeta` should work in Windows as well. Make sure all your
requirements are installed and make sure you can run `python`, `pandoc`,
and `ebook-convert` by just calling their name from the command line.
(You probably will have to edit your `$PATH` environment variable.)

To invoke `epubmeta`, you can either do

    python -m [path to...]\epubmeta.zip [epubmeta arguments]

Or create a batch file in your `$PATH` that calls Python in this way and
passes command line arguments through to epubmeta.


## Usage


**Backup an epub file as an embedded file within itself**:

    epubmeta backup FILE.EPUB

Copies FILE.EPUB to `./META-INF/source/FILE.EPUB` file within the
FILE.EPUB package. If you screw up the outer FILE.EPUB later on, you can
just extract the backup using a Zip archiving tool.
