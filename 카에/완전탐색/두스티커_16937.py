import sys
sys.stdin=open("input.txt", "r")

h, w = map(int, input().split())
sticker_count = int(input())
stickers = [tuple(map(int, input().split())) for _ in range(sticker_count)]

max_area = 0

# 모든 스티커의 조합을 고려
for i in range(sticker_count):
    for j in range(i + 1, sticker_count):
        for (height1, width1) in [(stickers[i][0], stickers[i][1]), (stickers[i][1], stickers[i][0])]:
            for (height2, width2) in [(stickers[j][0], stickers[j][1]), (stickers[j][1], stickers[j][0])]:
                # 수직으로 배치
                if height1 + height2 <= h and max(width1, width2) <= w:
                    max_area = max(max_area, height1 * width1 + height2 * width2)
                # 수평으로 배치
                if max(height1, height2) <= h and width1 + width2 <= w:
                    max_area = max(max_area, height1 * width1 + height2 * width2)

print(max_area)