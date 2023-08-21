import os, shutil
import sys

def clear_folder(path:str):
    """Clears all files from `path`"""
    count = 0
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
                count+=1
            elif os.path.isdir(file_path):
                count+=1
                shutil.rmtree(file_path)
        except Exception as _e:
            print(f"Failed to delete {file_path}. Reason: {_e}")

    return count
if __name__ == "__main__":
    
    try:
        files_removed = clear_folder(sys.argv[1])
        print(f"removed {files_removed} files")

    except IndexError:
        print("please provide path to folder.\n\nExample:\n\tpython clear_html_out.py path/to/folder")
