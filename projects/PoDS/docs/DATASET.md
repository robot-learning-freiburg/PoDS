# Dataset Preparation

Ensure your datasets are organized correctly for use with the models. Below are the guidelines for preparing your datasets.

```shell
dataset-ood/
├── gtFine/
│   ├── train/
│   ├── dataset_panoptic_train.json
│   └── dataset_panoptic_train/
├── leftImg8bit/
│   └── train/
```

**Setting the Environment Variable**: Set the DETECTRON2_DATASETS environment variable to the path containing your dataset folder. This allows Detectron2 to locate your dataset.
```shell
export DETECTRON2_DATASETS=/path/to/dataset/containing/folder
```
