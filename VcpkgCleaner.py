import os
import os.path
import shutil

vcpkg_home = "D:\\Vcpkg\\vcpkg"

pdb_fix = ".pdb"
log_fix = ".log"
src_dir = "src"
rel_build_temp_dir_fix = "-rel"
dbg_build_temp_dir_fix = "-dbg"

rm_temp = True
rm_log = True
rm_src = True
rm_pdb = True


def is_build_temp_dir(path):
    """
Check is the path for build temp
    :param path:The absolute path witch need check
    :return:bool
    """
    return os.path.isdir(path) and \
           (path.endswith(rel_build_temp_dir_fix) or path.endswith(dbg_build_temp_dir_fix))


def is_log_file(path):
    return path.endswith(log_fix)


def is_src_dir(path):
    """
Check is the path for source code
    :param path: The absolute path witch need check
    :return:bool
    """
    return path.endswith(src_dir)


def clean_build_build_trees(buildtrees):
    """
    Clean buildtrees dir.
    :param buildtrees: The absolute path of buildtrees.
    """
    cnt = 0
    sum = len(os.listdir(buildtrees))
    for path_prj in os.listdir(buildtrees):
        cnt+=1
        print("Clean {}, {}/{}".format(path_prj, cnt, sum))
        path_prj = os.path.join(buildtrees, path_prj)
        if rm_temp and rm_src and rm_log:
            shutil.rmtree(path_prj)
        else:
            for path in os.listdir(path_prj):
                full_path = os.path.join(path_prj, path)
                if is_log_file(full_path) and rm_log:
                    try:
                        os.remove(full_path)
                    except Exception as e:
                        print("Remove {} failed!".format(full_path))
                        print(e)
                elif is_build_temp_dir(full_path) and rm_temp:
                    try:
                        shutil.rmtree(full_path)
                    except Exception as e:
                        print("Remove {} failed!".format(full_path))
                        print(e)
                elif is_src_dir(full_path) and rm_src:
                    try:
                        shutil.rmtree(full_path)
                    except Exception as e:
                        print("Remove {} failed!".format(full_path))
                        print(e)


    print("Clean buildtrees Done!")


def clean_pdb_file(root_dir):

    # get all pdb files
    pdbs = []
    for (root, dirs, files) in os.walk(root_dir):
        pdbs += [os.path.join(root, file) for file in files if file.endswith(pdb_fix)]
    cnt = 0
    sum = len(pdbs)
    if rm_pdb:
        for pdb in pdbs:
            cnt += 1
            print("Clean {}, {}/{}".format(pdb, cnt, sum))
            try:
                os.remove(pdb)
            except Exception as e:
                print("Remove {} failed!".format(pdb))
                print(e)

    print("Clean *.pdf in %s: Done!" % os.path.basename(root_dir))


def clean(home):
    if rm_pdb:
        clean_pdb_file(os.path.join(home, "installed"))
        clean_pdb_file(os.path.join(home, "packages"))
    clean_build_build_trees(os.path.join(home, "buildtrees"))
    print("All clear!")


if __name__ == '__main__':
    clean(vcpkg_home)

