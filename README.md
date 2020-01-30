# Memorecon #

This set of python tools allows you to explore the memory of processes within linux. Using a PID, you can discover lies behind every proess and find wher ecertain values are stored within memory if they are defined as integers, or chars. I am looking to expand this repository in the future as well as iron out the spaghetti code.

## Workshop ##

If you're seeing this, it is very likely that you are using this tool as a part of my workshop on anti-cheat software and memory reconnaissance and manipulation. You can find a simple sample application under examples called game.c

Compile the program using gcc and see what you can find in the game. You can also try opening your other favorite games and see whether or not you can find the correlation between values inside memory and how they relate to those visible on the applications surface.

Start by opening a terminal (use tmux if you know how) and navigating to the directory into which you have cloned this repository and then enter:

`cd example && gcc game.c -o game && ./game`

Open another new terminal window or tmux pane and enter the following:

`ps -aux | grep ./game`

Now take the PID number, typically found in the 2nd column of your game process and copy it or remember it. Then enter the following command, entering your PID number as indicated (without the brackets around it):

`cd .. && python3 read_mem.py <PID> memory.txt`

Follow any further prompts that are given and have fun! If you made a mistake you can always rerun the second part of the above command. And if you're feeling really adventurous, enter some of the other PIDs for processes running on your system.

## Regarding Responsibility ##

I take no responsibility for any user's use of the software, the software is provided as is.