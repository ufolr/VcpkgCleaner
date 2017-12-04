# VcpkgCleaner
A python script to make vcpkg directory slim by remove the useless buildtrees & packages.

##Usage:

 * Clone or download the VcpkgCleaner.py.
 * Edit it, custom the `vcpkg_home` to the root of vcpkg.
 * Run it.
## What will it do
now there'are 4 flags: `rm_temp`,`rm_log`, `rm_src`,`rm_pdb`:  
rm_temp=True, the intermediate objects in `buildtrees` will be remove.  
rm_log=True, the build log will be remove.  
rm_src=True, the sources of libs in `buildtrees` will be remove.  
rm_pdb=True, the *.pdb in `buildtrees `&` packages` will be remove.  
