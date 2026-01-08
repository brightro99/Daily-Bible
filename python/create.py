import os

# 상위 성경 폴더
BASE_DIR = "쉬운성경"
# 작업할 성경 책 이름
FOLDER_NAME = "요한일서"


def get_next_chapter_number():
    """
    성경 폴더 안에서 다음 생성할 장/편 번호를 계산합니다.

    Returns:
        int: 다음 장/편 번호 (1부터 시작)
    """
    folder_path = os.path.join(BASE_DIR, FOLDER_NAME)

    if not os.path.exists(folder_path):
        return 1  # 폴더가 없으면 첫 장

    # .md 파일만 세어서 다음 번호 결정
    md_files = [f for f in os.listdir(folder_path) if f.endswith(".md")]
    return len(md_files) + 1


def get_chapter_filename(chapter_number):
    """
    장/편 번호를 받아 해당 성경 파일의 전체 경로를 생성합니다.

    Args:
        chapter_number (int): 생성할 장/편 번호

    Returns:
        str: 생성된 파일의 전체 경로
    """
    folder_path = os.path.join(BASE_DIR, FOLDER_NAME)

    if FOLDER_NAME == "시편":
        filename = f"{FOLDER_NAME} {chapter_number:03d}편.md"
    else:
        filename = f"{FOLDER_NAME} {chapter_number:02d}장.md"

    return os.path.join(folder_path, filename)


def create_chapter_md():
    """
    지정된 성경 폴더에 새 장/편 Markdown 파일을 생성합니다.
    폴더가 없으면 자동으로 생성하고,
    이미 동일 파일이 있으면 생성하지 않습니다.
    """
    folder_path = os.path.join(BASE_DIR, FOLDER_NAME)
    os.makedirs(folder_path, exist_ok=True)

    chapter_number = get_next_chapter_number()
    file_path = get_chapter_filename(chapter_number)

    if os.path.exists(file_path):
        print(f"⚠️ '{file_path}' 파일이 이미 존재합니다.")
        return

    # 파일 생성 및 기본 템플릿 작성
    with open(file_path, "w", encoding="utf-8", newline="\r\n") as file:
        if FOLDER_NAME == "시편":
            file.write(f"## {FOLDER_NAME} {chapter_number}편\n\n### \n****\n1.\n")
        else:
            file.write(f"## {FOLDER_NAME} {chapter_number}장\n\n### \n1.\n")

    print(f"✅ '{file_path}' 파일이 생성되었습니다.")


if __name__ == "__main__":
    create_chapter_md()