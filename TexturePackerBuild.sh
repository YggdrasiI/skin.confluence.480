#!/bin/bash
##
# Test of Sparse checkout of TexturePack folder
#git clone --depth=1 "https://github.com/xbmc/xbmc.git" xbmc
# cd xbmc

ROOT_DIR="./"


cd "${ROOT_DIR}" && mkdir TexturePackerBuild; cd TexturePackerBuild

if [ ! -d ".git" ] ; then
  echo "Checkout TexturePacker source..."
  git init
  git config core.sparseCheckout true
  git remote add xbmc "https://github.com/xbmc/xbmc.git" 
  echo "tools/depends/native/TexturePacker" >> .git/info/sparse-checkout
  echo "xbmc/guilib" >> .git/info/sparse-checkout
  echo "xbmc/utils" >> .git/info/sparse-checkout
  echo "xbmc/linux" >> .git/info/sparse-checkout
  git pull --depth=1 xbmc master
fi

echo "Install libs..."
REQUIRED_LIBS="libpng16-dev libgif-dev libjpeg-dev liblzo2-dev"
echo -e "Required dev packges for header files: \n" \
       "${REQUIRED_LIBS} \n\nInstall? y/N"
read INSTALL_LIBS
if [ "x${INSTALL_LIBS}" = "xy" -o "x${INSTALL_LIBS}" = "xY" ] ; then
sudo apt-get install ${REQUIRED_LIBS}
fi

echo "Building..."
mkdir -p tools/depends/native/TexturePacker/native
cd tools/depends/native/TexturePacker/native \
     && cp -a ../src/* . \
     && ./autogen.sh \
     && ./configure \
     && make \
     && cp TexturePacker ../../../../../../. \
     && echo "Done"
