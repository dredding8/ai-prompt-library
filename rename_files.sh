#!/bin/bash

# Function to clean filename
clean_name() {
    echo "$1" | sed 's/ 1f4b1fbd87d9[a-f0-9]*\.md$/\.md/' | sed 's/[ ()]/-/g' | sed 's/--*/-/g' | tr '[:upper:]' '[:lower:]' | sed 's/^-\|-$//g'
}

# Rename all files
for file in *.md; do
    if [[ "$file" != "index.md" && "$file" != "rename_files.sh" ]]; then
        # Extract the main part before the hash
        clean_file=$(echo "$file" | sed 's/ 1f4b1fbd87d9[a-f0-9]*\.md$/\.md/')
        # Make it web-friendly
        new_name=$(echo "$clean_file" | sed 's/[ ()]/-/g' | sed 's/--*/-/g' | tr '[:upper:]' '[:lower:]' | sed 's/^-\|-$//g')
        
        if [[ "$file" != "$new_name" ]]; then
            echo "Renaming: $file -> $new_name"
            mv "$file" "$new_name"
        fi
    fi
done
