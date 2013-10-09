RokuRTerm
=========

A very lightweight terminal based [Roku](http://www.roku.com) remote.

Uses [this](http://code.activestate.com/recipes/134892/) recipe to add cross platform ```getch()``` function.

Config
-----

Simply set the ```roku_ip``` variable to the IP address of your Roku player, you can get this by going to "Settings" > "About" on your Roku player.

You may wish to change some of the key mappings if you find my layout isn't working well for you, you can do this by changing the values in the ```case('X')``` statements.

Usage
-----

Start the application using ```python RokuRTerm.py```, you may wish to enclose this is a shell script in your home directory or by adding a new bash alias, this can be done by adding the line ```alias roku='python ~/apps/RokuRTerm.py'``` to ```.bashrc``` (located in your home directory), this will allow the script to be started using the command ```roku```.

Once the app is running the following key functions are assigned:

-	```?``` - Help
-	```/``` - Exit Remote App
-	```w``` - Up
-	```a``` - Left
-	```s``` - Down
-	```d``` - Right
-	```z``` - Select
-	```b``` - Back
-	```k``` - Keyboard Mode
-	```q``` - Quit
-	```p``` - Play/Pause
-	```<``` or ```,``` - Reverse
-	```>``` or ```.``` - Forward
-	```I``` - Info (* on Roku Remote)
-	```R``` - Instant Replay

Keyboard mode allows you to send alphanumerics directly to the Roku,
which is especially helpful for the search box.  You can type text right
into the box without navigating the matrix of letters on the screen.
Use the Escape key to exit keyboard mode.

This list can be obtained within the application by pressing ```?```.
