import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """

    path_list = []

    if not os.path.isdir(path):
        return path_list

    for item in os.listdir(path):
        full_path = os.path.join(path, item)

        if os.path.isdir(full_path):
            path_list.extend(find_files(suffix, full_path))
            continue

        if os.path.isfile(full_path) and full_path.endswith(suffix):
            path_list.append(full_path)

    return path_list


def run_test(suffix, path, expected):
    result = find_files(suffix, path)
    result.sort()
    expected.sort()

    assert expected == result


run_test('.c', './testdir/subdir1', ['./testdir/subdir1/a.c'])
run_test('.h', './testdir/subdir1', ['./testdir/subdir1/a.h'])
run_test('', './testdir/subdir1',   ['./testdir/subdir1/a.c', './testdir/subdir1/a.h'])

run_test('.c', './testdir/subdir2', [])
run_test('.gitkeep', './testdir/subdir2', ['./testdir/subdir2/.gitkeep'])

run_test('.c', './testdir/subdir3', ['./testdir/subdir3/subsubdir1/b.c'])

# The full monty
run_test('.c', './testdir', [
    './testdir/subdir1/a.c',
    './testdir/subdir3/subsubdir1/b.c',
    './testdir/subdir5/a.c',
    './testdir/t1.c'
])

run_test('', './nope', [])      # Invalid path returns an empty array
