#!/bin/bash

echo ""
echo "Copyright (c) 2011-2012 Icelandic Met Office"
echo "CParser 0.1 - Installation script"
echo ""

DIR=$HOME/.config/gpsconfig/
FILE_DIR="data"

echo "copying config file for gps config files under $DIR"

if [ -d "$DIR" ]; then
    :
else
    echo "Creating directory..."
    mkdir -p "$DIR"
fi

if [ -d "$DIR" ]; then
    echo "Copying config file.."
    cp "$FILE_DIR"/"postprocess.cfg" "$DIR/"
    cp "$FILE_DIR"/"stations.cfg" "$DIR/"

    if [ -f "$DIR"/"postprocess.cfg" ] && [ -f "$DIR"/"stations.cfg" ]; then
        echo "All seems to have gone well."
        echo "       > DON'T FORGET TO EDIT THE CONFIG FILES"
    else
        echo ""
        echo "ERROR: Config file failed to copy!"
    fi
else
    echo ""
    echo "ERROR: Directory was not created. User has to have sudo/root privelegs."
fi
