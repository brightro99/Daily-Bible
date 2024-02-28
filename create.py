import os
import sys


def create_job_chapter_md(folder_name, chapter_number):
    folder_path = "쉬운성경/" + folder_name
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    filename = os.path.join(folder_path, f"{folder_name} {chapter_number}장.md")
    if os.path.exists(filename):
        print(f"'{filename}' 파일이 이미 존재합니다.")
    else:
        with open(filename, "w") as file:
            file.write("## {} {}장\n\n### \n".format(folder_name, chapter_number))
        print(f"'{filename}' 파일이 생성되었습니다.")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("사용법: python3 create.py <폴더명> <장 번호>")
    else:
        folder_name = sys.argv[1]
        chapter_number = sys.argv[2]
        create_job_chapter_md(folder_name, chapter_number)
