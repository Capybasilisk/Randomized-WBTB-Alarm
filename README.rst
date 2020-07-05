This is a quick Python script I wrote to aid with the CANWILD [0] lucid 
dreaming technique. The program is an alarm clock with a randomized snooze 
function that prevents the sleeper subconsciously learning the snooze 
schedule. 

The alarms automatically turn themselves off so the sleeper doesn't have to 
move after being awakened. Snooze time is fully random, and can be anywhere 
from a few seconds to 90 minutes. 

It's run from the command line in one of two modes:


1) python sleep.py block 

This mode allows four hours of sleep before setting off an initial alarm, then
it begins the randomized snooze schedule. It is designed to be run at the
begining of the night, when first going to bed.


2) python sleep.py wbtb

This mode is for when you wake up for whatever reason, and you want to
immediately go into the randomized snooze schedule. It's basically the first 
mode without the initial four hour sleep allowance. "wbtb" stands for 
"wake-back-to-bed."


There are two alarm wav files included in the repo. One is a full length alarm 
for waking the sleeper after four hours. The other is a truncated alarm to be
played during the snooze schedule.

If you still don't get what this is all about, please read the linked article
to learn about CANWILD and lucid dreaming in general.


[0] https://lucid.fandom.com/wiki/CANWILD 
