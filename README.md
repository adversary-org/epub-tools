# ePUB Tools

Nothing new here, just some additional scripts which help me get from ODF files (primarily ODT files) to ePUB 3.0.1 files which pass the epubchecker validation with zero errors.

Does **not** use either Calibre or Sigil.  Calibre is fine for managing ePUBs as a consumer and getting them on and off devices, but not as a publishing tool.  Sigil is fine for ePUB 2.0.1 and earlier, but does not meet the requirements of the current standard.

Basic process currently consists of converting ODT to generated HTML through LibreOffice and unoconv (or headless LibreOffice).  Then convert that HTML to HTML 5 with Pandoc.  Edit that a little to remove things like footers or other LO relics which made it through.  Write a metadata.xml file which conforms to the Dublin Core framework (I do this in Emacs).  Use Pandoc again to convert the edited HTML 5 files to ePUB 3.0.  Extract the generated ePUB in a temp directory.  Make the OEBPS directory, move and modify files as needed.  Zip it all back up and test again.

Some of this can be automated with shell scripts and/or Python.  Some of it can't.  As my methods evolve, that's what will end up here.  There will be no support, use it at your peril.

