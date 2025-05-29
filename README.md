# backup_manager
rsync wrapper and last backup time manager

Tested on :
```
Arch Linux x86_64
kernel 6.14.6-2-cachyos
KDE Plasma 6.3.5 - Wayland
```

## Usage
create backup by running ```rsync_backup_manager.py [SOURCE_PATH] [DESTINATION_PATH]```  

  
By default runs ```rsync -a --delete``` and logs backup timestamp, source, destination, and ```rsync --stats``` to ```~/.config/backup_script/backup.log``` (careful of log size).  

```
usage: rsync_backup_manager.py [-h] [--dry-run] SOURCE DESTINATION

Rsync backup script with stats logging.

positional arguments:
  SOURCE       Source folder to back up
  DESTINATION  Destination folder

options:
  -h, --help   show this help message and exit
  --dry-run    Perform a dry run (no changes made)

```
