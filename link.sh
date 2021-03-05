
if [ ! -d "data/phcl/" ]; then
  mkdir -p data/phcl/
fi

# link dataset and anotations

# ln -s data/phcl/annotations/
# ln -s data/phcl/A
# ln -s data/phcl/B
# ln -s /datasets/algo-project/BDD100K/ data/phcl/C
# ln -s /datasets/algo-project/BDD100K/ data/phcl/D
# ln -s /datasets/algo-project/BDD100K/ data/phcl/E
# ln -s /datasets/algo-project/BDD100K/ data/phcl/F
# ln -s /datasets/algo-project/kitti_data_object_image_2/ data/phcl/G
# ln -s /datasets/algo-project/kitti_data_object_image_2/ data/phcl/H

ln -s /datasets/phcl/* data/phcl/
rm data/phcl/annotations

cp -r /datasets/phcl/annotations data/phcl

# if [ ! -d "data/phcl/capture" ]; then
#   mkdir data/phcl/capture
# fi
# ln -s /lustre/datasets/5w_phcl/* data/phcl/capture
# ln -s /lustre/datasets/20w_weather/* data/phcl/capture
