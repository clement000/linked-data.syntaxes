inotify-hookable -w src -c 'rm -r build/sublime/assets/
rm build/sublime/LinkedData.sublime-package
npx emk
#cp build/sublime/LinkedData.sublime-package "/home/omar/.config/sublime-text-3/Installed Packages/LinkedData.sublime-package"
#chmod 777 "/home/omar/.config/sublime-text-3/Installed Packages/LinkedData.sublime-package"'

#cp build/sublime/assets/sparql-generate.sublime-syntax "/home/omar/.config/sublime-text-3/Packages/LinkedData/"
cp build/sublime/assets/sparql-generate.* "/home/omar/.config/sublime-text-3/Packages/LinkedData/"
