# Panoptic Out-of-Distribution Segmentation

PoDS is a bottom approach for panoptic out-of-distribution segmentation, where the goal is to predict the semantic segmentation labels of "stuff" classes (e.g., road, sky, and so on), instance segmentation labels of "thing" classes (e.g., car, truck, etc) and out-of-distribution (OOD) objects as a distinct class.

![Overview of Panoptic Out-of-Distribution Segmentation Task](/projects/PoDS/images/overview.png)

This repository contains the **PyTorch implementation** of our RA-L'2024 paper [Panoptic Out-of-Distribution Segmentation](https://arxiv.org/pdf/2310.11797.pdf). The repository builds on [Detectron2](https://github.com/facebookresearch/detectron2).

If you find this code useful for your research, we kindly ask you to consider citing our papers:

```
@article{mohan2024panoptic,
  title={Panoptic Out-of-Distribution Segmentation},
  author={Mohan, Rohit and Kumaraswamy, Kiran and Hurtado, Juana Valeria and Petek, K{\"u}rsat and Valada, Abhinav},
  journal={IEEE Robotics and Automation Letters},
  year={2024},
  publisher={IEEE}
}
```

## System Requirements
* Linux 
* Python 3.9
* PyTorch 1.12.1
* CUDA 11
* GCC 7 or 8

**IMPORTANT NOTE**: These requirements are not necessarily mandatory. However, we have only tested the code under the above settings and cannot provide support for other setups.

##  Installation
Please refer to the [installation documentation](./projects/PoDS/docs/INSTALLATION.md) for detailed instructions.

## Dataset Preparation
Please refer to the [dataset documentation](./projects/PoDS/docs/DATASET.md) for detailed instructions.

## Usage
For detailed instructions on training, evaluation, and inference processes, please refer to the [usage documentation](./projects/PoDS/docs/USAGE.md).


## Pre-Trained Models
Pre-trained models can be found in the [model zoo](./projects/PoDS/docs/MODEL_ZOO.md).

## Acknowledgements
We have used utility functions from other open-source projects. We espeicially thank the authors of:
- [Detectron2](https://github.com/facebookresearch/detectron2)

## Contacts
* [Rohit Mohan](https://rl.uni-freiburg.de/people/mohan)

## License
For academic usage, the code is released under the [GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html) license. For any commercial purpose, please contact the authors.

