_RPM = $(shell pwd)/rpmbuild
_VERSION = $(shell date '+%Y.%m.%d')

all: clean
	cp -r jgq-utils $(_RPM)/SOURCES/jgq-utils
	cd rpmbuild/SOURCES; tar zcvf jgq-utils-$(_VERSION).tar.gz jgq-utils
	cd rpmbuild/SPECS; rpmbuild -bb --define '_topdir $(_RPM)' --define '_version $(_VERSION)' jgq-utils.spec
	cp rpmbuild/RPMS/noarch/jgq-utils-$(_VERSION)-1.el7.noarch.rpm ./

clean:
	rm -rf rpmbuild/BUILD/*
	rm -rf rpmbuild/RPMS/*
	rm -rf rpmbuild/SOURCES/jgq-utils*

test:
	echo $(_VERSION)
