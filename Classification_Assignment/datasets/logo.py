from torch.utils.data import Dataset
from torchvision import transforms
from torchvision.datasets import ImageFolder

from timm.data import create_transform
from timm.data.constants import IMAGENET_DEFAULT_MEAN, IMAGENET_DEFAULT_STD

import os
from PIL import Image

class LogoImageFolder(ImageFolder):

    def __init__(self, root, transform=None, sampling=1):

        super().__init__(root)

        self.transform = transform
        self.sampling = sampling

    def __len__(self):
        return self.sampling * len(self.samples)

    def __getitem__(self, index):

        index = index % len(self.samples)
        path, target = self.samples[index]

        img = Image.open(path).convert("RGB")

        # img = img.convert("RGB")

        if self.transform is not None:
            img = self.transform(img)

        return img, target

class LogoDataset(Dataset):

    def __init__(self, root, transform=None, sampling=1):

        classes, class_to_idx = self.find_classes(root)
        samples = self.make_dataset(root, class_to_idx)

        self.classes = classes
        self.class_to_idx = class_to_idx
        self.transform = transform
        self.samples = samples
        self.sampling = sampling


    def find_classes(self, root):

        classes = sorted(entry.name for entry in os.scandir(root) if entry.is_dir())

        class_to_idx = {cls_name: i for i, cls_name in enumerate(classes)}
        return classes, class_to_idx

    def make_dataset(self, root, class_to_idx):

        instances = []
        available_classes = set()

        for target_class in sorted(class_to_idx.keys()):
            class_index = class_to_idx[target_class]
            target_dir = os.path.join(root, target_class)

            if not os.path.isdir(target_dir):
                continue

            for root, _, fnames in sorted(os.walk(target_dir, followlinks=True)):
                for fname in sorted(fnames):
                    path = os.path.join(root, fname)

                    item = path, class_index
                    instances.append(item)
                    if target_class not in available_classes:
                        available_classes.add(target_class)

        return instances

    def __getitem__(self, index):

        index = index % len(self.samples)
        path, target = self.samples[index]

        img = Image.open(path).convert("RGB")

        # img = img.convert("RGB")

        if self.transform is not None:
            img = self.transform(img)

        return img, target

    def __len__(self):
        return self.sampling * len(self.samples)

def build_transform(is_train=True, input_size=256, color_jitter=0.4, auto_augment='rand-m9-mstd0.5-inc1', interpolation='bicubic'):

    if is_train:
        transform = create_transform(
            input_size=input_size,
            is_training=True,
            color_jitter=color_jitter,
            auto_augment=auto_augment,
            interpolation=interpolation,
        )

        return transform
    
    t = []
    t.append(transforms.Resize([224, 224]))
    t.append(transforms.ToTensor())
    t.append(transforms.Normalize(IMAGENET_DEFAULT_MEAN, IMAGENET_DEFAULT_STD))

    return transforms.Compose(t)