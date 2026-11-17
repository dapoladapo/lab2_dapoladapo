#!/bin/bash
csv_file="grades.csv"
archive_directory="archive"

#If there is nothing to archive
if [ ! -f "$csv_file" ]; then
    echo "Error: '$csv_file' is not found in the current working directory"
    exit 1
fi

#Create an archive directory if it doesn't exist
if [ ! -d "$archive_directory" ]; then
    echo " '$archive_directory' does not exist. Proceeding to create one"
    mkdir "$archive_directory" || { echo "Error: could not create '$archive_directory'"; exit 1; }
fi

timestamp=$(date +%Y%m%d-%H%M%S)
archive_name="grades_${timestamp}.csv"

#Move and rename the file into the archive
if ! mv "$csv_file" "$archive_directory/$archive_name"; then
    echo "Error: '$csv_file' could not move to '$archive_directory'"
    exit 1
fi

#reseting the workspace for next time
touch "$csv_file"

log_file="organizer.log"
#Append to the log 
echo "$timestamp | Original file: $csv_file | Archived file: $archive_directory/$archive_name" >> "$log_file"
echo "At '$timestamp' '$csv_file' is archived as $archive_name in $archive_directory"
echo "Created a new $csv_file and added to logs to $log_file"
