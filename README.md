# 人车模型 Demo

## 1. 测试样例
默认目录为mmdetection

+ phcl_new.py 放到 configs/\_base_/datasets/
+ retinanet_r50_fpn_1x_phcl.py 放到 configs/retinanet/
+ cag.py, phcl.py 放到 mmdet/datasets/

修改  mmdet/datasets/\__init__.py 文件， 添加函数路径
```python
from .cag import CAGDataset, PHCLDataset
__all__ = ['CAGDataset', 'PHCLDataset'] 
```
**(\__all__ 里面其他内容不动)**

## 2. 数据集以及标注

+ `link.sh` 在 mmdetection 目录下运行， 该脚本将**数据集**以及**标注** 软连接到相应目录。

+ `split_dataset.py` 用来切分标注,因为没有提供测试集, 然后demo 自己从训练集中切分一部分出来，当作测试集。总训练集大概40w, 按照9：1 进行切分. 该脚本直接从 phcl_train.json 中进行切分， 按照
clear, cloudy, foggy, rainy 四种天气各1w, 总共4w 当作测试集new_val.json, 其余继续当作训练集 new_train.json. **然后需要将这俩个json, 移动到 data/phcl/annotations**


## 3. 训练 以及测试脚本示例：

+ train_dist.sh： 默认8卡训练， 可以修改GPUS参数来进行调整(***注意调整不同卡数对应的learning rate***)， 训练结果存放在 result_phcl/retinanet_r50_fpn_1x_phcl 下面
+ test_dist.sh： 默认4卡测试， 可以调整config, 以及 checkpoint 路径


