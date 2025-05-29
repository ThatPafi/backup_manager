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

  
By default runs ```rsync -a --delete``` and logs backup timestamp, source, destination, and ```rsync --stats``` to ```~/.config/backup.log``` (careful of log size).  

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

## Exemples  
Using [command output widget](https://github.com/Zren/plasma-applet-commandoutput/tree/master):  
On timer : ```sh -c '/usr/local/bin/backup_checker.py -x 7'``` (check if backup is older than a week)  
On Hover :  ```echo -e "Click on widget to backup:  \nSOURCE \nto \nDESTINATION"```  
On Click : ```sh -c "konsole --hold -e rsync_backup_manager.py SOURCE DESTINATION"``` (opens new terminal to check view rsync progress or error - replace ```konsole``` with your terminal)  
