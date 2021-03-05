_base_ = [
    '../_base_/models/retinanet_r50_fpn.py',
    '../_base_/datasets/phcl_new.py',
    '../_base_/schedules/schedule_1x.py', '../_base_/default_runtime.py'
]
model = dict(
    bbox_head=dict(
        num_classes=4,
    )
)
# optimizer
optimizer = dict(type='SGD', lr=0.001, momentum=0.9, weight_decay=0.0001)
workflow = [('train', 1)]
evaluation = dict(interval=1, metric='mAP')