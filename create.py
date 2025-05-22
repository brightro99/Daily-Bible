import os
import sys


def get_next_chapter_number(folder_name):
    folder_path = "쉬운성경/" + folder_name
    md_list = os.listdir(folder_path)
    return len(md_list) + 1


def create_job_chapter_md(folder_name):
    folder_path = "쉬운성경/" + folder_name
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    chapter_number = get_next_chapter_number(folder_name)
    
    if folder_name == "시편":
        if int(chapter_number) < 10:
            filename = os.path.join(
                folder_path, f"{folder_name} 00{chapter_number}편.md"
            )
        elif int(chapter_number) < 100:
            filename = os.path.join(
                folder_path, f"{folder_name} 0{chapter_number}편.md"
            )
        else:
            filename = os.path.join(folder_path, f"{folder_name} {chapter_number}편.md")

    else:
        if int(chapter_number) < 10:
            filename = os.path.join(
                folder_path, f"{folder_name} 0{chapter_number}장.md"
            )
        else:
            filename = os.path.join(folder_path, f"{folder_name} {chapter_number}장.md")

    if os.path.exists(filename):
        print(f"'{filename}' 파일이 이미 존재합니다.")
    else:
        with open(filename, "w", encoding="utf-8", newline="\r\n") as file:
            if folder_name == "시편":
                file.write(
                    "## {} {}편\n\n### \n****\n1\n".format(folder_name, chapter_number)
                )
            else:
                file.write(
                    "## {} {}장\n\n### \n1\n".format(folder_name, chapter_number)
                )
        print(f"'{filename}' 파일이 생성되었습니다.")

if __name__ == "__main__":
    # if len(sys.argv) != 3:
    # print("사용법: python3 create.py <폴더명> <장 번호>")
    # else:
    # folder_name = sys.argv[1]
    # chapter_number = sys.argv[2]
    # create_job_chapter_md(folder_name, chapter_number)
    folder_name = "마태복음"
    create_job_chapter_md(folder_name)
