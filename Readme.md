RaspberryPi by default comes with SSH disabled.  For anyone who wants to run a RaspberryPi without a monitor configuring the ability ssh into the Raspbian is a bit of a pain.  This script helps mitigate that.

First if you are running a unix OS that is not OSX simply mount your SD/microSD card. 

If you are running OSX  You will need to install OSXFuse ( https://osxfuse.github.io/ ) , fuse-ext2 (http://sourceforge.net/projects/fuse-ext2/ ).

Once you have installed both of those you need to enabled read/write on fuse-ext2.  Note:  Enabling read/write can sometimes cause issues. Use at your own risk.

```
sudo sed -e 's/OPTIONS="auto_xattr,defer_permissions"/OPTIONS="auto_xattr,defer_permissions,rw+"/' -i .orig /System/Library/Filesystems/fuse-ext2.fs/fuse-ext2.util
```

Once you have successfully mounted the SD/microSD card execute the script as follows.

./pyconfig.py [PATH TO SD CARD]

Example for OSX.

./config /Volumes/Untitled

