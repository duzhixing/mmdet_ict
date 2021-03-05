
export CONFIG_FILE=./configs/retinanet/retinanet_r50_fpn_1x_phcl.py
export CHECKPOINT_FILE=./result_phcl/retinanet_r50_fpn_1x_phcl/epoch_12.pth

export GPU_NUM=4
# export CUDA_VISIBLE_DEVICES=0,1,3
bash tools/dist_test.sh \
    ${CONFIG_FILE} \
    ${CHECKPOINT_FILE} \
    ${GPU_NUM} \
    --eval mAP\
