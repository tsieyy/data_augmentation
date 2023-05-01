1.将标注数据集的标签（xml文件）放入./DataAugForObjectDetection/data/Annotations

2.将标注数据集的图片放入./DataAugForObjectDetection/data/images

3.修改./DataAugForObjectDetection/DataAugmentForObejctDetection.py/中的need_aug_num，即每张图片需要扩增的数量，然后运行./DataAugForObjectDetection/DataAugmentForObejctDetection.py

注意：DataAugmentForObejctDetection_pool.py 是多进程增强版本，耗时较少。代码中的process不宜设置过大否则可能会报错，默认即可。