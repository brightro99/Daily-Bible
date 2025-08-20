import os
import re

# 상위 성경 폴더명 (고정값)
BASE_DIR = "쉬운성경"
# 현재 작업할 성경 책 이름
FOLDER_NAME = "사도행전"


def get_chapter_number():
    """
    현재 성경 책 폴더 안의 마지막 장/편 번호를 계산합니다.

    Returns:
        int: 마지막 장/편 번호 (0부터 시작)
    """
    folder_path = os.path.join(BASE_DIR, FOLDER_NAME)
    if not os.path.exists(folder_path):
        return 1  # 폴더가 없으면 첫 장

    # .md 파일만 개수 세기
    md_files = [f for f in os.listdir(folder_path) if f.endswith(".md")]
    return len(md_files)


def get_chapter_filename(chapter_number):
    """
    주어진 장/편 번호에 맞는 파일 경로를 생성합니다.

    Args:
        chapter_number (int): 장/편 번호

    Returns:
        str: 생성된 파일의 전체 경로
    """
    folder_path = os.path.join(BASE_DIR, FOLDER_NAME)

    if FOLDER_NAME == "시편":
        filename = f"{FOLDER_NAME} {chapter_number:03d}편.md"
    else:
        filename = f"{FOLDER_NAME} {chapter_number:02d}장.md"

    return os.path.join(folder_path, filename)


def add_dot_after_numbers_inplace(file_path):
    """
    .md 파일에서 각 줄 시작 숫자 뒤에 점(.)을 붙이고,
    같은 파일에 덮어쓰기 저장합니다.

    Args:
        file_path (str): 대상 파일 경로
    """
    try:
        # 파일 읽기
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        new_lines = []
        for line in lines:
            # 줄 끝 줄바꿈 분리
            stripped_line = line.rstrip('\r\n')
            line_ending = line[len(stripped_line):]

            # 줄 시작 숫자(1~3자리) → 숫자 뒤 점(.) 붙이기
            # 예: '1 ' 또는 '12' → '1. ' 또는 '12. '
            if re.match(r'^\d{1,3}(\s|$)', stripped_line):
                new_line = re.sub(r'^(\d{1,3})(\s|$)', r'\1. ', stripped_line).rstrip()
            else:
                new_line = stripped_line

            # 원래 줄바꿈 복원
            new_lines.append(new_line + line_ending)

        # 동일 파일로 덮어쓰기
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(new_lines)

        print(f"✅ 완료: '{file_path}' 파일에 숫자 뒤에 점 추가 완료!")

    except Exception as e:
        print(f"⚠️ 오류 발생: {e}")


if __name__ == "__main__":
    # 현재 성경 폴더에서 다음 처리할 장 번호 가져오기
    chapter_number = get_chapter_number()
    # 해당 장의 파일 경로 생성
    file_path = get_chapter_filename(chapter_number)
    # 파일 내용 처리 (숫자 뒤에 점 추가)
    add_dot_after_numbers_inplace(file_path)