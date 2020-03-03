# gupm

## Grand Unified Package Manager

A frontend for 3 common package managers in GNU: APT, DNF and pacman

You can use the same command line tool to install and manage your packages in these 3 different distro families

### Installation

```
git clone https://github.com/hoomanist/gupm.git
cd gupm
chmod +x main.py
sudo cp main.py /usr/bin/gupm
gupm setup
```

### Usage

To install a package
```
gupm install pkgname
```
To remove a package
```
gupm remove pkgname
```
To upgrade a specific package
```
gupm up pkgname
```
### TODO
[ ] make it interactive because of subprocess.run()

[ ] writing helps (thanks Arcush)

### Acknowledgements
Thanks to Reddit user u/SqueamishOssifrage for slogan

Thanks to Reddit user u/AlternativeOstrich7 for the suggestion of using subprocess.run()

Thanks to Arcush from the persian arch forum for help for writing help
