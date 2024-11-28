# Prompt the user for a prefix
echo "Enter the prefix to add to files."
read prefix

#Check if the user provided a prefix
if [[ -z "$prefix" ]]; then
        echo "No prefix provided. Exiting script."
        exit 1
fi

# Loop through all files in the current directory
for file in *; do
        # Skip the script file itself
        if [[ "$file" == "${0##*/}" ]]; then
                continue
        fi

        # Rename the file by adding the prefix
        mv "$file" "${prefix}_$file"
done

echo "All files have been renamed with the prefix '$prefix'."
