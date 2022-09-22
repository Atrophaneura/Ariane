install:
	sudo meson builddir --prefix=/usr/local --wipe
	sudo ninja -C builddir install

global:
	sudo meson builddir --prefix=/usr --wipe
	sudo ninja -C builddir install

release:
	sudo meson builddir --prefix=/usr --buildtype=release --wipe
	sudo ninja -C builddir install