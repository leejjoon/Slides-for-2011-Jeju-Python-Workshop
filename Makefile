all: mpl_advanced2.html astropy2.html

mpl_advanced2.html: mpl_advanced.rst
	landslide -d mpl_advanced.html -c mpl_advanced.rst
	cat mpl_advanced.html | sed "s#file://`pwd`#.#g" > mpl_advanced2.html

astropy2.html: astropy.rst
	landslide -d astropy.html -c astropy.rst
	cat astropy.html | sed "s#file://`pwd`#.#g" > astropy2.html

rsync:
	rsync -avz . /home/jjlee/Dropbox/Public/Slides-for-2011-Jeju-Python-Workshop
