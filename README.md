Simple number guesser with threading. Generates new random number every iteration.

Quick start -> Just install requirements.txt

NOTE! 
If you wanna run it using Docker, before building an image comment out lines 5, 19, 20, 22, 23, and remove keyboard module from requirements.txt, because there is a conflict between 'keyboard' Python module and Linux 'uinput' module. Without this keyboard block the pause between rounds is a mess ain't gonna lie.

To run an image use the command -> docker run -p your_free_port:80 -rm image_name 
