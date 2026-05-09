import time
import sys

def type_text(text, delay=0.03):
    """텍스트를 타자 치듯 출력하는 연출 함수"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_line():
    print("-" * 50)
