RokuRTerm
=========

A very lightweight terminal based [Roku](http://www.roku.com) remote.

Uses [this](http://code.activestate.com/recipes/134892/) recipe to add cross platform ```getch()``` function.

Config
-----

Simply set the ```roku_ip``` variable to the IP address of your Roku player, you can get this by ging to "Setings" > "About" on your Roku player.

You may wish to change some of the key mappings if you find my layout isn't working well for you, you can do this by changing the values in the ```case('X')``` statements.

Usage
-----

Start the application using ```python RokuRTerm.py```, you may wish to enclose this is a shell script in your home directory allowing you to type something like ```./roku``` into a new terminal to launch the app.

Once the app is running the following key functions are assigned:

-	```?``` - Help
-	```/``` - Exit Remote App
-	```w``` - Up
-	```a``` - Left
-	```s``` - Down
-	```d``` - Right
-	```z``` - Select
-	```q``` - Back
-	```p``` - Play/Pause
-	```<``` or ```,``` - Reverse
-	```>``` or ```.``` - Forward
-	```I``` - Info (* on Roku Remote)
-	```R``` - Instant Replay

This list can be obtained within the application by pressing ```?```.
