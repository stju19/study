_ROOT = $(shell pwd)/..
_RPM = $(_ROOT)/rpmbuild
_VERSION = $(shell date '+%Y.%m.%d')

all: clean
	cp -r $(_ROOT)/simian-enhanced $(_RPM)/SOURCES/simian-enhanced
	cp -r $(_ROOT)/tools $(_RPM)/SOURCES/simian-enhanced/
	cp simian-enhanced.spec $(_RPM)/SPECS/
	cd $(_RPM)/SOURCES; tar zcvf simian-enhanced-$(_VERSION).tar.gz simian-enhanced
	cd $(_RPM)/SPECS; rpmbuild -bb --define '_topdir $(_RPM)' --define '_version $(_VERSION)' simian-enhanced.spec
	cp $(_RPM)/RPMS/noarch/simian-enhanced-$(_VERSION)-1.el7.noarch.rpm ./

clean:
	rm -rf $(_RPM)/BUILD/*
	rm -rf $(_RPM)/RPMS/*
	rm -rf $(_RPM)/SOURCES/simian-enhanced*

test:
	echo $(_VERSION)
