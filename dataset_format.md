该数据集存储位置为
```python
/datasets/algo-project/BDD100K/
/datasets/algo-project/kitti_data_object_image_2/
/lustre/datasets/5w_phcl/
/lustre/datasets/20w_weather
/datasets/phcl/trainval/
/datasets/phcl/extratest/
/datasets/phcl/capture/
```
其中 `annotations/` 里面包含数据的标注.标注中包含的关键词是`info`, `licences`, `images`, `annotations`, `categories`
以一个数据集为例(***抽取标注中一个json为例***):

```python
info = dataset
licences = None
categories = [{'supercategory': 'person', 'id': 0, 'name': 'person'}, \
        {'supercategory': 'human_head', 'id': 1, 'name': 'human_head'}, \
        {'supercategory': 'car', 'id': 2, 'name': 'car'}, \
        {'supercategory': 'license_plate', 'id': 3, 'name': 'license_plate'}, \
        {'supercategory': 'others', 'id': 7, 'name': 'others'}]
images = {'file_name': './E/6c34f197bf8e5d2e21c2657694da9bcd.jpg', \
        'id': 1, 'height': 720, 'width': 1280}
annotations = {'id': 1, 'image_id': 1, 'category_id': 2, \
        'bbox': [0, 127.6, 382, 250], 'car_type': 'Car', \
        'occluded_rate': 0, 'truncated': 1}
images nums = 194003
annotations nums = 1866073
```

其中`images nums ` 和 `annotations nums`  是抽取出来的一个json里面大小， 并不代表整个数据集的大小
`bbox` 的 数值分别是检测框左上角和右下角的xy值。（**左上角是坐标轴原点**）
