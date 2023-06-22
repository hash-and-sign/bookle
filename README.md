## bookle
Modify a PDF to link to local audio-visual files using Python tools

### What is a bookle?

A bookle is a multimedia virutal book, readable on your own off-line computer using server technology. Reading a bookle is like reading a PDF but with links redirected to locally stored audio-visual files instead of resources on the web, allowing you to read the bookle offline. The instructions below describe how to create a bookle on your computer.

### Step 1: Set up a server on your computer.

1. Install [Python3](https://www.python.org/downloads/), perhaps the easiest way to install a server.
2. Create a folder named `server`, for example.
3. Inside the folder, create an executable file to launch the server. On a Windows system, this could be a batch file such as `server.bat` containing the single line: `python -m http.server 80`. This file can be placed outside the `server` folder if the command `cd path-to-server` is inserted at its beginning. Wherever the python server is invoked becomes the server's document root folder. 
4. Click on `server.bat` to start the server.
5. On Windows, a warning about your computer's firewall will appear. You should enable private network access and disable public network access. This only needs to be done once. On other platforms, follow the appropraite procedure to open your firewall for the Python server.
6. A shell window opens and stays open to log server activity. Closing the shell window stops the Python server.
7. Test the server by opening a browser and typing `localhost` in the URL field. A directory of the server folder is shown, namely the `server.bat` file.

### Step 2: Install PDF file conversion tools.

1. Download the code from this repository into a separate folder named `bookle`, for example.
2. There are two python tools, `extract.py` and `replace.py`, which can be started from a command line in a command window.
3. Each program takes one argument, the pathname of the PDF file to be converted, like so: `python extract.py file.pdf` and `python replace.py file.pdf`
4. The batch command files named `extract.bat` and `replace.bat` are provided to automatically launch these Python programs for those not familiar with running python programs from a shell window.
5. The first program, `extract.py`, creates a file named `urls.txt` with one line for each URL in the specified PDF file.
6. The second program, `replace.py`, reads `urls.txt` after it has been modified, using it to replace URLs in the specified PDF file.
7. There is also a third program, `server.bat`, mentioned in Step 1.3.

### Step 3: Convert a PDF file for local, offline use

1. Move any audio-visual files you are serving locally into the server folder created in Step 1.2, preferably into a subfolder in case you have more than one bookle. These files should be renamed to form proper URLs. I recommend using the character set a-z, A-Z, 0-9, period, underscore and hyphen, but you can also use [urlencoder.org](https://www.urlencoder.org)
2. Extract the URLs from the PDF file as explained in Step 2.5.
3. Edit the created `urls.txt` file, appending to each URL a comma followed by the pathname of an audio-visual file, relative to the server folder.
4. Example line in `urls.txt` (for an mp4 video file stored in the `server/fs` subfolder: `https://youtu.be/Hrowi4hHz8A,fs/Yes-Love_Will_Find_a_Way.mp4`
5. If you do not have a local file for one of the URLs in `urls.txt`, either leave it as is or delete the line it is in.
6. Replace the URLs in the PDF file according to the modified `urls.txt`, as explained in Step 2.6.
7. Move the converted PDF file to the server folder created in Step 1.2.
8. Test the bookle based on the converted PDF by:
   a. starting the server as explained in Step 1.4,
   b. entering `localhost` in the URL field of a browser,
   c. clicking on the filename of your converted PDF file,
   d. then after the PDF opens, clicking on a link to a local audio-visual file.

### Tips

1. Use a browser that can display PDFs and play audio-visual resources such as MP3s and MP4s within its window, such as the Chrome browser.
2. When a link is clicked in a PDF, the target resource loads into the current tab. If you then return to the PDF, you may be at the beginning, having lost your place. To avoid this problem, instead hold down the control key when clicking a link to open the target in a new tab. Holding down both the shift and control keys when clicking shifts focus to the new tab immediately. Alternatively, you can press the mouse wheel (optionally with the shift key held down).
3. Wikipedia articles can easily be downloaded as PDFs using the Tools menu righ on the Wikipedia article page. 
4. Any web page can be downloaded as a PDF using a service such as [Web Page to PDF](https://webtopdf.com)
