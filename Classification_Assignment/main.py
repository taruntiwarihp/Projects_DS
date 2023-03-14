from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

# Local files
from models import BaseFeatureExtractor
from utils import create_logger

# Libraries
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from collections import Counter
from tensorboardX import SummaryWriter
from datasets.logo import LogoImageFolder, build_transform

import argparse
from tqdm import tqdm
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, confusion_matrix
import numpy as np
import pprint
import os

def parse_args():
    parser = argparse.ArgumentParser(description='Classification')

    parser.add_argument('--modelDir',
                        help='model directory',
                        type=str,
                        default='weights')
    parser.add_argument('--logDir',
                        help='log directory',
                        type=str,
                        default='logs_temp')
    parser.add_argument('--model_type',
                        help='Types of model',
                        type=str,
                        default='efficientnet_v2_s',
                        choices=['efficientnet_b7', 'efficientnet_b4', 'efficientnet_b0', 'efficientnet_v2_l', 'efficientnet_v2_m', 'efficientnet_v2_s', 'mobilenet', 'vgg', 'alexnet', 'resnet', 'inception', 'conv_trans', 'efficient_att', 'fmnet', 'swin'])
    parser.add_argument('--split_ratio',
                        help='train set valid set ratio',
                        type=float,
                        default=0.9)
    parser.add_argument('--n_class',
                        help='Total Class',
                        type=int,
                        default=28)
    parser.add_argument("--class_weights", 
                        type=int, 
                        default=1, 
                        choices=[0, 1])
    parser.add_argument('--batch_size',
                        help='Total batch',
                        type=int,
                        default=8)
    parser.add_argument('--epochs',
                        help='Total Epochs',
                        type=int,
                        default=200)
    parser.add_argument('--max_lr',
                        help='maximum Learning Rate',
                        type=float,
                        default=3e-5)
    parser.add_argument('--weight_decay',
                        help='Weight Decay',
                        type=float,
                        default=1e-4)

    args = parser.parse_args()

    return args

def main():
    opts = parse_args()

    os.makedirs(opts.modelDir, exist_ok=True)
    os.makedirs(os.path.join(opts.modelDir, opts.model_type), exist_ok=True)

    logger, tb_log_dir = create_logger(opts)
    logger.info(pprint.pformat(opts))

    # cudnn related setting
    torch.backends.cudnn.benchmark = True
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.enabled = True
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    model = BaseFeatureExtractor(config = opts.model_type, n_class = opts.n_class)

    logger.info(pprint.pformat(model))
    writer_dict = {
        'writer': SummaryWriter(log_dir=tb_log_dir),
        'train_global_steps': 0,
        'valid_global_steps': 0,
    }
    model = model.cuda()
    trans = build_transform(input_size=224, is_train=True)
    data = LogoImageFolder('data/train', sampling=1, transform=trans)

    trans_val = build_transform(input_size=224, is_train=False)
    data_val = LogoImageFolder('data/val', sampling=1, transform=trans_val)

    torch.manual_seed(42)
    indices = torch.randperm(len(data)).tolist()
    indices_val = torch.randperm(len(data_val)).tolist()

    trainset = torch.utils.data.Subset(data, indices[:len(data)])
    valset = torch.utils.data.Subset(data_val, indices_val[:len(data_val)])
    print(len(data), len(data_val), len(trainset), len(valset))

    train_loader = DataLoader(trainset, batch_size=opts.batch_size, shuffle=True, pin_memory=True, num_workers=8, drop_last=True)
    val_loader = DataLoader(valset, batch_size=opts.batch_size, shuffle=True, pin_memory=True, drop_last=True, num_workers=8)

    if opts.class_weights:
        class_counts = dict(Counter(data.targets))
        m = max(class_counts.values())
        for c in class_counts:
            class_counts[c] = m / class_counts[c]
        weights = []
        for k in sorted(class_counts.keys()):
            weights.append(class_counts[k])

        print("Weights", weights)

        weights = torch.Tensor(weights)
        loss_fn = nn.CrossEntropyLoss(weight=weights.to(device))
    else:
        loss_fn = torch.nn.CrossEntropyLoss()

    optimizer = torch.optim.Adam(model.parameters(), opts.max_lr, weight_decay=opts.weight_decay)
    sched = torch.optim.lr_scheduler.OneCycleLR(optimizer, opts.max_lr, epochs=opts.epochs, steps_per_epoch=len(train_loader))

    val_acc = 0.0
    for epoch in range(opts.epochs):

        model.train()
        losses = 0
        with tqdm(train_loader, unit="batch") as tepoch:
            for data, target in tepoch:
                tepoch.set_description("Epoch {}".format(epoch))

                optimizer.zero_grad()
                pred = model(data.cuda())

                loss = loss_fn(pred, target.cuda())
                loss.backward()
                optimizer.step()
                sched.step()

                losses += loss.item()

                tepoch.set_postfix(loss=loss.item())

        train_loss = losses/len(train_loader)

        msg = 'Train Epoch : {}\t Training Loss : {}'.format(epoch, train_loss)
        logger.info(msg)

        global_steps = writer_dict['train_global_steps']
        writer_dict['writer'].add_scalar('train_loss', train_loss, global_steps)
        writer_dict['train_global_steps'] = global_steps + 1

        model.eval()
        losses = 0
        pred_list = []
        tar_list = []

        with torch.no_grad():
            with tqdm(val_loader, unit="batch") as tepoch:
                for data, target in tepoch:
                    tepoch.set_description("Epoch {}".format(epoch))
                    pred = model(data.cuda())

                    _, predicted = torch.max(pred.data, 1)

                    tar_list.append(target.numpy())
                    pred_list.append(predicted.cpu().numpy())

                    loss = loss_fn(pred, target.cuda())

                    losses += loss.item()

                    tepoch.set_postfix(loss=loss.item())

        val_loss = losses/len(val_loader)
        tar_list_np = np.concatenate(tar_list)
        pred_list_np = np.concatenate(pred_list)

        cm = 5 * confusion_matrix(tar_list_np, pred_list_np)
        class_acc = cm.diagonal()/cm.sum(axis=1)
        class_precision = precision_score(pred_list_np, tar_list_np, average=None)
        class_f1 = f1_score(pred_list_np, tar_list_np, average=None)
        class_recall = recall_score(pred_list_np, tar_list_np, average=None)

        accuracy = accuracy_score(pred_list_np, tar_list_np)
        precision = precision_score(pred_list_np, tar_list_np, average='macro')
        f1 = f1_score(pred_list_np, tar_list_np, average='macro')
        recall = recall_score(pred_list_np, tar_list_np, average='macro')

        logger.info('Class Accuracy')
        logger.info(pprint.pformat(class_acc))
        logger.info('Class Precision')
        logger.info(pprint.pformat(class_precision))
        logger.info('Class F1 Score')
        logger.info(pprint.pformat(class_f1))
        logger.info('Class Recall')
        logger.info(pprint.pformat(class_recall))

        msg = 'Eval Epoch : {}\t Validation Loss {}\t Accuracy : {}\t Precision : {}\t F1_score : {}\t Recall : {}\t'.format(
            epoch, val_loss, accuracy, precision, f1, recall
        )
        logger.info(msg)


        global_steps = writer_dict['valid_global_steps']
        writer_dict['writer'].add_scalar('val_loss', val_loss, global_steps)
        writer_dict['writer'].add_scalar('accuracy', accuracy, global_steps)
        writer_dict['writer'].add_scalar('precision', precision, global_steps)
        writer_dict['writer'].add_scalar('f1', f1, global_steps)
        writer_dict['writer'].add_scalar('recall', recall, global_steps)
        writer_dict['valid_global_steps'] = global_steps + 1

        if accuracy > val_acc:
            ckpt = {
                'model_dict': model.state_dict(),
                'optim_dict': optimizer.state_dict(),
                'schd_dict': sched.state_dict(),
                'val_loss' : val_loss,
                'epoch': epoch,
            }

            mats = {
                'cm': cm, 
                'accuracy': accuracy,
                'precision' : precision,
                'f1_score' : f1,
                'recall' : recall,
                'class_acc' : class_acc,
                'class_precision' : class_precision,
                'class_f1' : class_f1,
                'class_recall' : class_recall,
            }
            ckpt.update(mats)

            save_path = os.path.join(opts.modelDir, opts.model_type, 'best_model.pt')
            torch.save(ckpt, save_path)

            logger.info('Best Model saved')
            logger.info(pprint.pformat(mats))
            val_acc = accuracy

    logger.info('==>Training done!\nBest accuracy: %.3f' % (val_acc))
    logger.info('Best Evaluation matrix')
    logger.info(pprint.pformat(mats))

if __name__ == '__main__':
    main()