#!/bin/sh
test -f "Hello World.dmg" && rm "Hello World.dmg"
test -d "dist/dmg" && rm -rf "dist/dmg"
# Make the dmg folder & copy our .app bundle in.
mkdir -p "dist/dmg"
cp -r "dist/Hello World.app" "dist/dmg"
# Create the dmg.
create-dmg \
  --volname "Hello World" \
  --volicon "icons/icon.icns" \
  --window-pos 200 120 \
  --window-size 800 400 \
  --icon-size 100 \
  --icon "Hello World.app" 200 190 \
  --hide-extension "Hello World.app" \
  --app-drop-link 600 185 \
  "Hello World.dmg" \
  "dist/dmg/"
