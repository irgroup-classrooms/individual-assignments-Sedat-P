# Shell Lesson
Git Bash mit einem bash script
```
cd /c/Benutzer/palao/Desktop/test
git init

echo "*.log" >> .gitignore
echo "node_modules/" >> .gitignore
echo "temp/" >> .gitignore

git add .gitignore
git commit -m "Add .gitignore to exclude unnecessary files"
git push -u origin main

git checkout -b create-script
nano script.sh
```
### Task 1
```
echo "head -n 3 2014-01_JA.tsv" >> script.sh
```
### Task 2
```
echo "wc -l *.tsv" >> script.sh
```
### Task 3
```
echo "wc -l *.tsv | sort -nr | head -n 1" >> script.sh
```
### Script Datei Ausführen mit allen 3 Aufgaben
```
chmod +x script.sh
./script.sh
```
## Lösung:

### Task 1
```
File    Creator Issue   Volume  Journal ISSN    ID      Citation        Title  Place Labe       Language        Publisher       Date
History_1a-rdf.tsv      Doolittle, W. E.        1       59      KIVA -ARIZONA- 0023-1940        (Uk)RN001571862 KIVA -ARIZONA- 59(1), 7-26. (1993)      A Method for Distinguishing between Prehistoric and Recent Water and Soil Control Features      xxu     eng     ARIZONA ARCHAEOLOGICAL AND HISTORICAL SOCIETY   1993
History_1a-rdf.tsv      Nelson, M. C.   1       59      KIVA -ARIZONA-  0023-1940       (Uk)RN001571874 KIVA -ARIZONA- 59(1), 27-48. (1993)     Classic Mimbres Land Use in the Eastern Mimbres Region, Southwestern New Mexico xxu     eng    ARIZONA ARCHAEOLOGICAL AND HISTORICAL SOCIETY    1993
```
### Task 2
```
13712 2014-01-31_JA-africa.tsv
27392 2014-01-31_JA-america.tsv
507732 2014-01_JA.tsv
5375 2014-02-02_JA-britain.tsv
```
### Task 3
```
554211 total
554211 total
```
