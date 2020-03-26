from pyulog import ulog2kml
import easygui


def main():
    file_path = easygui.fileopenbox("Choose .ulg files to convert.", "AVY", filetypes="*.txt", multiple=True)

    if file_path is None:
        print(f" \n >> No files selected. Exiting program.")
        return 1
        
    for file in file_path:
        ulog2kml.convert_ulog2kml(ulog_file_name=file, output_file_name=file[:-4]+'.kml')
    return 0


if __name__ == '__main__':
    main()
