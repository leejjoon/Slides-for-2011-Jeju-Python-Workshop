all: mpl_advanced.html astropy.html

mpl_advanced.html: mpl_advanced.rst
	landslide -d mpl_advanced_orig.html -c mpl_advanced.rst
	cat mpl_advanced_orig.html | sed "s#file://`pwd`#.#g" > mpl_advanced.html

astropy.html: astropy.rst
	landslide -d astropy_orig.html -c astropy.rst
	cat astropy_orig.html | sed "s#file://`pwd`#.#g" > astropy.html

rsync:
	rsync -avz . /home/jjlee/Dropbox/Public/Slides-for-2011-Jeju-Python-Workshop
