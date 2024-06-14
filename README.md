# BeReal Exif Batch

This script writes the capture date of each exported BeReal photo into the Exif data. The date and time are automatically extracted from the filename.

## Usage

1. `pip install -r requirements.txt`
2. Create a folder named **photos**
3. Export all BeReals using an auto-clicker app and copy them into the **photos** folder.
4. Run main.py

Now all images should have the correct capture date.

## Additional info

> ℹ️ Note: The time may be shifted by 12 hours. BeReal does not indicate in the filename whether it is AM or PM. The script assumes that all times before 8 AM are actually in the afternoon and adds 12 hours to them (02:50 becomes 14:50). However, this is only a rough correction and can introduce many errors.

> ⚠️ Warning: There is little to no error handling in this script. As soon as BeReal changes anything on the export function, the script might stop working or even destroy your files. So **make sure you have a backup of your photos** before runnning the script.
