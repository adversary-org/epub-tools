#!/bin/bash4

# Must run from the same directory as the epub

tsuri=`date "+tmp-%Y%m%d%H%M%S"`

mkdir $tsuri
mv "$@" $tsuri
cd $tsuri
unzip "$@"
mv "$@" ../
mkdir OEBPS
mv *.xhtml OEBPS/
mv media/ OEBPS/
mv *.opf OEBPS/
mv *.css OEBPS/
mv *.ncx OEBPS/
cd META-INF/
mv container.xml container.xml.old
cp $HOME/tmp/container.xml.new container.xml
cd ../OEBPS/
