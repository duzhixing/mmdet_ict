
export FILE=retinanet_r50_fpn_1x_phcl
export FILE_PATH=./configs/retinanet/

export CONFIG_FILE=$FILE_PATH$FILE.py

export GPUS=8

PORT=29503 bash tools/dist_train.sh \
    ${CONFIG_FILE} \
    ${GPUS} \
    --work-dir result_phcl/$FILE \
