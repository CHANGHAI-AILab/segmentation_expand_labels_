import os
import sys

move_imgs = sys.argv[1]
fixed_imgs = sys.argv[2]

move_masks = move_imgs.replace('_image', '_mask')
fixed_masks = fixed_imgs + 'mask'
if not os.path.exists(fixed_masks):
    os.mkdir(fixed_masks)
print(move_masks)

all_img = os.listdir(move_imgs)
all_mask = os.listdir(move_masks)
all_fixed = os.listdir(fixed_imgs)

for i in all_img:
    if i in all_mask and i in all_fixed:
        move_img = os.path.join(move_imgs, i)
        move_mask = os.path.join(move_masks, i)
        fixed_img = os.path.join(fixed_imgs, i)
        fixed_mask = os.path.join(fixed_masks, i)
        os.system(f'/data/deedsBCV/deedsBCV -F {fixed_img} -M {move_img}  -O {fixed_mask} -S {move_masks}')
    else:
        print(f'not found {i}')