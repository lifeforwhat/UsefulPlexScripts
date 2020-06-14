import os
import sys
import sqlite3
import subprocess

# 우분투 사용자용
#
# export LD_LIBRARY_PATH=/usr/lib/plexmediaserver:/usr/lib/plexmediaserver/lib
# 
# export PLEX_MEDIA_SERVER_APPLICATION_SUPPORT_DIR=/var/lib/plexmediaserver/Library/Application\ Support
# 


conn = sqlite3.connect("/var/lib/plexmediaserver/Library/Application Support/Plex Media Server/Plug-in Support/Databases/com.plexapp.plugins.library.db")
c = conn.cursor()
scanner_path = "/usr/lib/plexmediaserver/'Plex Media Scanner'"
db = c.execute("SELECT * FROM media_parts")


for item in db.fetchall():
    # first job to do
    id = item[0]
    duration = item[8]
    filepath = item[5]
    if type(duration) != int :
        print(db)
        print(item)
        media_item_id = item[1]
        a = c.execute("SELECT * FROM media_items WHERE id="+str(media_item_id))
        m = a.fetchall()
        metadata_item_id = m[0][3]
        print(metadata_item_id)
        section_id = m[0][2]
        os.system("./'Plex Media Scanner' --analyze --item %s --section %s" % (str(metadata_item_id) , str(section_id)))

print("Analyze Unanalyzed Media Files Done")
