import os
os.environ["CUDA_VISIBLE_DEVICES"] = "2"
import torch
import numpy as np
import config
import utils


def train():

    # 加载数据

    train_dataset = torch.utils.data.DataLoader(
        utils.Dataset(), batch_size=config.TRAIN_BATCH_SIZE, shuffle=True)
    print("Data Loaders created")
    utils.writelog("Data Loaders created")

    # 加载模型
    model = None
    start_epoch = 0
    optimizer = torch.optim.Adam(model.parameters(), lr=config.LEARNING_RATE)
    lr_scheduler = torch.optim.lr_scheduler.StepLR(optimizer, step_size=5, gamma=0.8)
    if config.IS_CONTINUE:
        model, start_epoch, optimizer, lr_scheduler = utils.get_checkpoint_state(
            model, optimizer, lr_scheduler)

    device = torch.device(
        "cuda") if torch.cuda.is_available() else torch.device("cpu")
    model.to(device)
    print("Model loaded to device")
    utils.writelog("Model loaded to device")

    print("---------------- Training Started --------------")
    utils.writelog("---------------- Training Started --------------")
    min_loss = 10000000
    for epoch in range(start_epoch, config.EPOCHS):
        loss_value = engine.train_fn(
            train_dataset, detector, optimizer, lr_scheduler, device)
        print("epoch = {}, Training_loss = {}".format(epoch, loss_value))
        utils.writelog("epoch = {}, Training_loss = {}".format(
            epoch, loss_value))

        utils.save_checkpoint_state(
            epoch, model, optimizer, lr_scheduler, "models/model_{}.pth".format(epoch))
        # Set the threshold as per needs
        if loss_value < min_loss:
            min_loss = loss_value
            utils.save_checkpoint_state(epoch, model, optimizer, lr_scheduler)
            utils.writelog(
                ">>>>>>>>>>>>>>>>>>>>> save min loss model <<<<<<<<<<<<<<<<<")

    print("-" * 25)
    utils.writelog("-" * 25)
    print("Model Trained and Saved to Disk")
    utils.writelog("Model Trained and Saved to Disk")


if __name__ == "__main__":
    run()
