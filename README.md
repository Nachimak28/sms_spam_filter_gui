# SMS spam filter GUI app built to test DearPyGUI framework


This app is a simple spam filter app built using NLTK for the NLP functions and DearPyGUI for the GUI (obviously!).
It is a replication of the app build in [this](https://www.youtube.com/watch?v=2RocXKPPx4o) video.

Unfortunately, the [original codebase](https://github.com/MariyaSha/SimpleSMSspamFilter_GUI) was built using an older version of the dearpygui app, hence I've replicated the app with the newest API of DearPyGUI.



## Steps to run the app locally

Clone this repository
```
git clone https://github.com/Nachimak28/sms_spam_filter_gui
```

Change directory into the sms_spam_filter_gui
```
cd sms_spam_filter_gui
```

Install the dependencies - preferrably in conda or vitrual env
```
pip install -r requirements.txt
```

Change directory into spam_sms_identifier folder
```
cd spam_sms_identifier
```

Run the code
```
python app.py
```

Feel free to create issues if you face any problems running the app.

## Converting to EXE

Warning: Does not work as expected

### Method 1

* Using py2exe

Install py2exe
```sh
pip install py2exe
```

Change directory into the spam_sms_identifier
```
cd spam_sms_identifier
```

Run the following command
```sh
python setup.py install
```
This should create a dist folder and we can find the app.exe in this folder which can bew distributed along with the dist folder. Not as a single file 

* Problems faced with py2exe: 
    - Even with the right configuration, including necessary packages, files, assets and the python interpreter config, it does not produce a single independently installable EXE to distribute


### Method 2

* Using pyinstaller

Install pyinstaller
```sh
pip install pyinstaller
```

Change directory into the spam_sms_identifier
```
cd spam_sms_identifier
```

Run the following command
```sh
pyinstaller --onefile app.py
```

This produces a build and dist folder where in the dist folder, one could find the exe. 
It does bundle up the whole codebase into a single EXE. 

* Problems faced with pyinstaller: 
    - All right configuration, including necessary packages, files, assets and the python interpreter config, there are some problems with loading of assest like images. I simply ran out of time and patience to search and solve this problem even after a lot of effort. Might come back to this later if felt necessary. 