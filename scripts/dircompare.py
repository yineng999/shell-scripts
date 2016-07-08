import filecmp
dir1='/home/script/python/filecmp'
dir2='/home/script/python/filecmp1'
dircompare=filecmp.dircmp(dir1,dir2)
print('*'*30+'report'+'*'*30)
dircompare.report()
print('*'*30+'partial report'+'*'*30)
dircompare.report_partial_closure()
print('*'*30+'full report'+'*'*30)
dircompare.report_full_closure()
print('*'*30+'left list'+'*'*30)
print(str(dircompare.left_list))
print('*'*30+'right list'+'*'*30)
print(str(dircompare.right_list))
print('*'*30+'common'+'*'*30)
print(str(dircompare.common))
print('*'*30+'leftonly'+'*'*30)
print(dircompare.left_only)
print('*'*30+'rightonly'+'*'*30)
print(dircompare.right_only)
print('*'*30+'common_files'+'*'*30)
print(dircompare.common_files)
print('*'*30+'common_dirs'+'*'*30)
print(dircompare.common_dirs)
print('*'*30+'common_funny'+'*'*30)
print(dircompare.common_funny)
print('*'*30+'same_files'+'*'*30)
print(dircompare.same_files)
print('*'*30+'diff_files'+'*'*30)
print(dircompare.diff_files)
print('*'*30+'funny_files'+'*'*30)
print(dircompare.funny_files)
