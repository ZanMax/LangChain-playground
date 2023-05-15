#!/bin/sh

# Check if both parameters are provided
if [ $# -ne 2 ]; then
  echo "Usage: $0 <folder_name> <url>"
  exit 1
fi

folder_name="$1"
url="$2"

# Create the folder if it doesn't exist
mkdir -p "$folder_name"

# Download files using wget
wget -r -A.html -P "$folder_name" "$url"
