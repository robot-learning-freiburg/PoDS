# -*- coding: utf-8 -*-
# Copyright (c) Facebook, Inc. and its affiliates.

from detectron2.config import CfgNode as CN
from detectron2.projects.deeplab import add_deeplab_config


def add_pods_config(cfg):
    """
    Add config for Panoptic-DeepLab.
    """
    # Reuse DeepLab config.
    add_deeplab_config(cfg)
    # Target generation parameters.
    cfg.INPUT.GAUSSIAN_SIGMA = 10
    cfg.INPUT.IGNORE_STUFF_IN_OFFSET = True
    cfg.INPUT.SMALL_INSTANCE_AREA = 4096
    cfg.INPUT.SMALL_INSTANCE_WEIGHT = 3
    cfg.INPUT.IGNORE_CROWD_IN_SEMANTIC = False
    # Optimizer type.
    cfg.SOLVER.OPTIMIZER = "ADAM"
    # PoDS semantic segmentation head.
    # We add an extra convolution before predictor.
    cfg.MODEL.SEM_SEG_HEAD.HEAD_CHANNELS = 256
    cfg.MODEL.SEM_SEG_HEAD.LOSS_TOP_K = 0.2
    cfg.MODEL.SEM_SEG_HEAD.CROSS_CHANNELS = 0
    cfg.MODEL.SEM_SEG_HEAD.DPC_CHANNELS = 256
    cfg.MODEL.SEM_SEG_HEAD.DPC_DILATIONS = [(1, 6), (1, 1), (6, 21), (18, 15), (6, 3)]
    cfg.MODEL.SEM_SEG_HEAD.PROCESSING_BLOCK_A_CONVS = 2       
    cfg.MODEL.SEM_SEG_HEAD.PROCESSING_BLOCK_B_CONVS = 2
    cfg.MODEL.SEM_SEG_HEAD.NUM_OCC_LEVELS = 3     
    # PoDS instance segmentation head.
    cfg.MODEL.INS_EMBED_HEAD = CN()
    cfg.MODEL.INS_EMBED_HEAD.NAME = "PoDSInsEmbedHead"
    cfg.MODEL.INS_EMBED_HEAD.IN_FEATURES = ["res2", "res3", "res5"]
    cfg.MODEL.INS_EMBED_HEAD.PROJECT_FEATURES = ["res2", "res3"]
    cfg.MODEL.INS_EMBED_HEAD.PROJECT_CHANNELS = [32, 64]
    cfg.MODEL.INS_EMBED_HEAD.CE_CHANNELS = 128
    cfg.MODEL.INS_EMBED_HEAD.CE_DILATIONS = [(1,6), (3,1)]
    cfg.MODEL.INS_EMBED_HEAD.BLOCK_A_CONVS = 2      
    cfg.MODEL.INS_EMBED_HEAD.NUM_THING_CLASSES = 7  
    # We add an extra convolution before predictor.
    cfg.MODEL.INS_EMBED_HEAD.HEAD_CHANNELS = 32
    cfg.MODEL.INS_EMBED_HEAD.CONVS_DIM = 128
    cfg.MODEL.INS_EMBED_HEAD.CROSS_CHANNELS = 0
    cfg.MODEL.INS_EMBED_HEAD.COMMON_STRIDE = 4
    cfg.MODEL.INS_EMBED_HEAD.NORM = "SyncBN"
    cfg.MODEL.INS_EMBED_HEAD.CENTER_LOSS_WEIGHT = 200.0
    cfg.MODEL.INS_EMBED_HEAD.OFFSET_LOSS_WEIGHT = 0.01
    cfg.MODEL.INS_EMBED_HEAD.IGNORE_VALUE = 1920*3
    # Panoptic-DeepLab post-processing setting.
    cfg.MODEL.PoDS = CN()
    # Stuff area limit, ignore stuff region below this number.
    cfg.MODEL.PoDS.MODE = "modal"
    cfg.MODEL.PoDS.STUFF_AREA = 2048
    cfg.MODEL.PoDS.CENTER_THRESHOLD = 0.1
    cfg.MODEL.PoDS.NMS_KERNEL = 7
    cfg.MODEL.PoDS.TOP_K_INSTANCE = 200
    # If set to False, Panoptic-DeepLab will not evaluate instance segmentation.
    cfg.MODEL.PoDS.PREDICT_INSTANCES = True
    cfg.MODEL.PoDS.USE_DEPTHWISE_SEPARABLE_CONV = False
    # This is the padding parameter for images with various sizes. ASPP layers
    # requires input images to be divisible by the average pooling size and we
    # can use `MODEL.PANOPTIC_DEEPLAB.SIZE_DIVISIBILITY` to pad all images to
    # a fixed resolution (e.g. 640x640 for COCO) to avoid having a image size
    # that is not divisible by ASPP average pooling size.
    cfg.MODEL.PoDS.SIZE_DIVISIBILITY = -1
    # Only evaluates network speed (ignores post-processing).
    cfg.MODEL.PoDS.BENCHMARK_NETWORK_SPEED = False
    

