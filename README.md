# android_adb_smsbackup_to_spreadsheet

I needed to pull the text messages off an android phone with a broken screen that I had adb access too. Keeping the scripts here in case myself/others find it useful in future

Steps

Connect phone to adb 

Run
adb backup -f backup.ab -noapk com.android.providers.telephony

The phone will prompt for a password - I used scrcpy to mirror the screen to the computer and enter one

Place the backup.ab in the root folder of this repo download

Edit smsToCsv.sh - change the value of PASSWORD from 1 to whatever password was used.

cd to the repo directory and run ./smsToCsv.sh - a messages.csv file should be generated
