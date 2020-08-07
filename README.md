# SPARQL-Generate integration in Sublime Text

Edit and run [SPARQL-Generate](https://ci.mines-stetienne.fr/sparql-generate/) projects directly in Sublime text!

### Install:

To use SPARQL-Generate with Sublime Text, follow these steps:

Prerequisites:

- Java SE v8 minimum installed
- java executable available in the path
- Sublime Text v3

1. Browse the latest [package release](https://github.com/sparql-generate/sublime-editor/releases) whose version name ends with `sparql-generate`, and download the file with the suffix `.sublime-package`
  - Note: this file is actually a zip built from the sources with the command `npx emk`

2. In Sublime Text v3, open the `Packages` folder. (Preferences -> Browse Packages...)

3. Navigate to `.../Sublime Text 3/Installed Packages`, and copy the file here as `LinkedData.sublime-package`.

4. Go back to `.../Sublime Text 3/Packages`, create a directory named `LinkedData`, and copy inside this directory the [latest jar of SPARQL-Generate](https://ci.mines-stetienne.fr/sparql-generate/language-cli.html). 

5. Rename this file as `sparql-generate.jar`.


### Test:

To test the installation is fine, follow these steps:

1. Download the [SPARQL-Generate tutorial workspace.](https://eswc2018-sparql-ext.github.io/tutorial/sparql-generate-tutorial.zip)

2. Unzip it, and open one of the folders it contains inside Sublime Text (File -> Open Folder...)

3. Open the project in the left side bar, search and open the main query. You should see the syntax getting colored

4. Build the project (Tools -> Build), check that `sparql-generate.jar` has been found.

5. Check the output (file ending with `.out`).

6. Check the log (file ending with `.rqglog`). Key shortcut CTRL+SHIFT+L opens the log. (SUPER+SHIFT+L on Mac) 

### Configure:

You can configure your SPARQL-Generate project inside a `sparql-generate-conf.json` file. Key shortcut CTRL+SHIFT+O should open this file (SUPER+SHIFT+O on Mac).

The configuration of this file is documented on the [SPARQL-Generate website](https://ci.mines-stetienne.fr/sparql-generate/sublime.html). 


### Documentation:

The playground contains a progressive documentation of [SPARQL-Generate](https://ci.mines-stetienne.fr/sparql-generate/playground.html).  Just load the examples one by one, read the text, and experiment.  

An html documentation of the package is available on the [SPARQL-Generate website](https://ci.mines-stetienne.fr/sparql-generate/sublime.html). 

#### Developed by

Maxime Lefrançois

MINES Saint-Étienne, France

http://maxime-lefrancois.info/


Omar Qawasmeh

MINES Saint-Étienne, France

https://perso.univ-st-etienne.fr/alo09685/



As an extension of the excellent [Sublime Text `LinkedData` package](https://packagecontrol.io/packages/LinkedData) developed by:


Blake Regalia

University of California, Santa Barbara, CA, USA

https://blake-regalia.net/
