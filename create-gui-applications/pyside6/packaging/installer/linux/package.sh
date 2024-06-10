#!/bin/sh
# Create folders.
[ -e package ] && rm -r package
mkdir -p package/opt
mkdir -p package/usr/share/applications
mkdir -p package/usr/share/icons/hicolor/scalable/apps

# Copy files (change icon names, add lines for non-scaled icons)
cp -r dist/hello-world package/opt/hello-world
cp icons/penguin.svg package/usr/share/icons/hicolor/scalable/apps/hello-world.svg
cp hello-world.desktop package/usr/share/applications

# Change permissions
find package/opt/hello-world -type f -exec chmod 644 -- {} +
find package/opt/hello-world -type d -exec chmod 755 -- {} +
find package/usr/share -type f -exec chmod 644 -- {} +
chmod +x package/opt/hello-world/hello-world

