from pycocotools.coco import COCO
import os
import mmcv
import json
import pdb
import random


class ImgFilterWeahter:
    def __init__(self):
        self.max_weather = {'snowy': 0, 'clear': 10000, 'cloudy': 10000, 'foggy': 10000, 'rainy': 10000}

    def filter(self, info):
        if info.get('weather', "unknown").lower() in self.max_weather and self.max_weather[info['weather'].lower()] > 0:
            self.max_weather[info['weather'].lower()] -= 1
            return True
        else:
            return False


class AnnFilter:
    def __init__(self):
        self.drop_keys = {'eletric BicycleEletric Bicycle',
                         'bicycle',
                         'motorbike',
                         'tricycle',
                         'Eletric Bicycle'}

    def filter(self, ann):
        if ann.get('car_type', None) in self.drop_keys:
            return False
        else:
            return True


def split_with_annotations(img_list, ImgFilter, AnnFilter):
    train_imgs, val_imgs, train_anns, val_anns = list(), list(), list(), list()
    train_img_id = val_img_id = train_ann_id = val_ann_id = 1
    for img_id, data in img_list:
        img_info = data.load_imgs([img_id])[0]
        new_info = img_info.copy()
        if ImgFilter.filter(img_info):
            # new_info['id'] = val_img_id
            val_imgs.append(new_info)
            for ann in data.load_anns(data.get_ann_ids(img_ids=[img_id])):
                ann = ann.copy()
                if AnnFilter.filter(ann):
                    # ann['image_id'] = val_img_id
                    # ann['id'] = val_ann_id
                    val_anns.append(ann)
                    # val_ann_id += 1
            # val_img_id += 1
        else:
            # new_info['id'] = train_img_id
            train_imgs.append(new_info)
            for ann in data.load_anns(data.get_ann_ids(img_ids=[img_id])):
                ann = ann.copy()
                if AnnFilter.filter(ann):
                    # ann['image_id'] = train_img_id
                    # ann['id'] = train_ann_id
                    train_anns.append(ann)
                    # train_ann_id += 1
            # train_img_id += 1
    return train_imgs, val_imgs, train_anns, val_anns


def save_json(data, file_name):
    with open(file_name, 'w') as f:
        json.dump(data, f)
    print(f"{file_name} save successfully!")


if __name__ == '__main__':
    imgs_list = []
    data = COCO('data/phcl/annotations/phcl_train.json')
    imgs_list.extend([(img_id, data) for img_id in data.get_img_ids()])
    img_filter = ImgFilterWeahter()
    ann_filter = AnnFilter()

    json_data = mmcv.load('data/phcl/annotations/phcl_train.json')

    random.seed(166)
    random.shuffle(imgs_list)
    train_imgs, val_imgs, train_anns, val_anns = split_with_annotations(imgs_list, img_filter, ann_filter)
    print(f'train set: {len(train_imgs)} ; test set: {len(val_imgs)}')

    # save data for train
    json_data['images'] = train_imgs
    json_data['annotations'] = train_anns
    save_json(json_data, 'new_train.json')

    # save data for val
    json_data['images'] = val_imgs
    json_data['annotations'] = val_anns
    save_json(json_data, 'new_val.json')
