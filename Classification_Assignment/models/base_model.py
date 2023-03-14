from .efficientnet import efficientnet_v2_s
from .resnet import ResNet
from .mobilenet import MobileNetV2
from .efficient_att import EfficientFormer
from .swin import SwinTransformer

from torch import nn
from torch.nn import functional as F

class LayerNorm2d(nn.LayerNorm):
    def forward(self, x):
        x = x.permute(0, 2, 3, 1)
        x = F.layer_norm(x, self.normalized_shape, self.weight, self.bias, self.eps)
        x = x.permute(0, 3, 1, 2)
        return x

class BaseFeatureExtractor(nn.Module):
    def __init__(self, config='efficientnet_v2_s', img_dim=(256, 256), n_class=28):
        super().__init__()


        if config.lower() == 'efficientnet_v2_s':
            self.backbone = efficientnet_v2_s(pretrained=False)

            self.backbone.classifier = nn.Sequential(
                nn.Dropout(p=0.4, inplace=True),
                nn.Linear(in_features=1280, out_features=n_class, bias=True)
            )

        elif config.lower() == 'resnet':
            self.backbone = ResNet(num_classes=n_class)

        elif config.lower() == 'mobilenet':
            self.backbone = MobileNetV2(num_classes=n_class)


        elif config.lower() == 'efficient_att':
            self.backbone = EfficientFormer(
                layers=[3, 2, 6, 4],
                embed_dims=[48, 96, 224, 448],
                downsamples=[True, True, True, True],
                vit_num=1,
                num_classes=n_class,
                distillation=False
            )

        elif config.lower() == 'swin':
            self.backbone = SwinTransformer(num_classes=n_class)

        else:
            raise ValueError('Not supported')



    def forward(self, x):
        return self.backbone(x)
