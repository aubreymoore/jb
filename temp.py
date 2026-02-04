def get_txt(txt_path):
    with open(txt_path) as f:
        s = f.read()
    return s

# Example usage:

# txt_path = 'images/images_for_sam3_post/20251129_152106.jpg-02.jpg.txt'
# txt = get_txt(txt_path)
# print(txt)

# MAIN 

s = ''
for i in range(2, 27):
    txt = get_txt(f'images/images_for_sam3_post/20251129_152106.jpg-{i:02d}.jpg.txt')
    s += f'## Detected object {i:02d}\n'
    s += f'{txt}/n'
    s += f'![](images/images_for_sam3_post/20251129_152106.jpg-{i:02d}.jpg)\n\n'
    s += f'![](images/images_for_sam3_post/roi-20251129_152106.jpg-{i:02d}.jpg)\n\n'
print(s)
    