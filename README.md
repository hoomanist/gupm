# gupm
Grand Unified Package Manager

it is a frontend for 3 common package managers in GNU apt,dnf and pacman

you can use a same command line tool to install and manage your packages in these 3 diffrent distro families

### installition

```
git clone https://github.com/hoomanist/gupm.git
cd gupm
chmod +x main.py
sudo cp main.py /usr/bin/gupm
gupm setup
```

### usage

for install a package
```
gupm install pkgname
```
for remove a package
```
gupm remove pkgname
```
for upgrade a specific package
```
gupm up pkgname
```
