import os
import shutil
import random

def count_files(path):
    # 3458
    files = os.listdir(path)
    count = 0
    for file in files:
        if os.path.isfile(os.path.join(path, file)):
            count += 1
    return count

def build_files(image_dir, label_dir, train_images_dir, valid_images_dir, \
                train_labels_dir, valid_labels_dir):

    # 创建训练和验证目录
    os.makedirs(train_images_dir, exist_ok=True)
    os.makedirs(valid_images_dir, exist_ok=True)
    os.makedirs(train_labels_dir, exist_ok=True)
    os.makedirs(valid_labels_dir, exist_ok=True)

    # 获取所有图像文件和标签文件
    # image_files = [f for f in os.listdir(image_dir) if f.endswith('.jpg')]
    # label_files = [f for f in os.listdir(label_dir) if f.endswith('.txt')]
    files = [os.path.splitext(f)[0] for f in os.listdir(image_dir)]
    random.shuffle(files)



    # 划分训练和验证集
    split_ratio = 0.8
    split_index = int(len(files) * split_ratio)

    train_image_files = [f+'.jpg' for f in files[:split_index]]
    valid_image_files = [f+'.jpg' for f in files[split_index:]]
    train_label_files = [f+'.txt' for f in files[:split_index]]
    valid_label_files = [f+'.txt' for f in files[split_index:]]

    # print(valid_image_files[:5])
    # print(valid_label_files[:5])

    # 将图像文件和标签文件移动到训练和验证目录
    for image_file, label_file in zip(train_image_files, train_label_files):
        shutil.copy(os.path.join(image_dir, image_file), os.path.join(train_images_dir, image_file))
        shutil.copy(os.path.join(label_dir, label_file), os.path.join(train_labels_dir, label_file))

    for image_file, label_file in zip(valid_image_files, valid_label_files):
        shutil.copy(os.path.join(image_dir, image_file), os.path.join(valid_images_dir, image_file))
        shutil.copy(os.path.join(label_dir, label_file), os.path.join(valid_labels_dir, label_file))

    return

if __name__ == '__main__':
    image_dir = './bdd100/images-mini'
    label_dir = './bdd100/labels-mini-txt'
    train_images_dir = './mydata/train/images'
    valid_images_dir = './mydata/valid/images'
    train_labels_dir = './mydata/train/labels'
    valid_labels_dir = './mydata/valid/labels'

    build_files(
        image_dir=image_dir,
        label_dir=label_dir,
        train_images_dir=train_labels_dir,
        valid_images_dir=valid_images_dir,
        train_labels_dir=train_labels_dir,
        valid_labels_dir=valid_labels_dir,
    )
  
    image_count = count_files(image_dir)
    label_count = count_files(label_dir)
    train_images_count = count_files(train_images_dir)
    valid_images_count = count_files(valid_images_dir)
    train_labels_count = count_files(train_labels_dir)
    valid_labels_count = count_files(valid_labels_dir)

    print("image_count: {}, label_count: {}".format(image_count, label_count))
    print("train_images_count: {}, train_labels_count: {}".format(train_images_count, train_labels_count))
    print("valid_images_count: {}, valid_labels_count: {}".format(valid_images_count, valid_labels_count))


