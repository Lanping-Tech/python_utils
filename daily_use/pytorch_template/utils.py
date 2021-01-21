import torch
import config

class Dataset(torch.utils.data.Dataset):
    """
    PyTorch wrapper for a numpy dataset.

    @param dataset Numpy array representing the dataset.
    """
    def __init__(self, dataset):
        self.dataset = dataset

    def __len__(self):
        return numpy.shape(self.dataset)[0]

    def __getitem__(self, index):
        return self.dataset[index]

class LabelledDataset(torch.utils.data.Dataset):
    """
    PyTorch wrapper for a numpy dataset and its associated labels.

    @param dataset Numpy array representing the dataset.
    @param labels One-dimensional array of the same length as dataset with
           non-negative int values.
    """
    def __init__(self, dataset, labels):
        self.dataset = dataset
        self.labels = labels

    def __len__(self):
        return numpy.shape(self.dataset)[0]

    def __getitem__(self, index):
        return self.dataset[index], self.labels[index]

def get_checkpoint_state(model, optimizer, scheduler, load_path=config.MODEL_LOAD_PATH):
    checkpoint = torch.load(load_path)
    model.load_state_dict(checkpoint['model_state_dict'])
    epoch = checkpoint['epoch']
    optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
    scheduler.load_state_dict(checkpoint['scheduler_state_dict'])
    return model, epoch, optimizer, scheduler


def save_checkpoint_state(epoch, model, optimizer, scheduler, save_path=config.MODEL_SAVE_PATH):
    checkpoint = {
        'epoch': epoch,
        'model_state_dict': model.state_dict(),
        'optimizer_state_dict': optimizer.state_dict(),
        'scheduler_state_dict': scheduler.state_dict()
    }
    torch.save(checkpoint, save_path)


def writelog(logstr):
    result_file_open = open(config.LOG_FILE_PATH, 'a')
    result_file_open.write(logstr+'\n')
    result_file_open.close()
