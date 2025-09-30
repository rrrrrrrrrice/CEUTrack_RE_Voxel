class EnvironmentSettings:
    def __init__(self):
        self.workspace_dir = '/wangx/DATA/Code/chenqiang/PAR/Tracking/CEUTrack/output/checkpoints'    # Base directory for saving network checkpoints.
        self.tensorboard_dir = '/wangx/DATA/Code/chenqiang/PAR/Tracking/CEUTrack/output/tensorboard'    # Directory for tensorboard files.
        self.pretrained_networks = '/wangx/DATA/Code/chenqiang/Attack/CEUTrack/pretrained_models'
        self.coesot_dir = '/wangx/DATA/Dataset/COESOT/train'
        self.coesot_val_dir = '/wangx/DATA/Dataset/COESOT/train'
        # self.fe108_dir = '/media/amax/c08a625b-023d-436f-b33e-9652dc1bc7c0/DATA/chenqiang/COESOT/data/FE108/train'
        # self.fe108_val_dir = '/media/amax/c08a625b-023d-436f-b33e-9652dc1bc7c0/DATA/chenqiang/COESOT/data/FE108/test'
        # self.visevent_dir = '/media/amax/c08a625b-023d-436f-b33e-9652dc1bc7c0/DATA/chenqiang/COESOT/data/VisEvent/train'
        # self.visevent_val_dir = '/media/amax/c08a625b-023d-436f-b33e-9652dc1bc7c0/DATA/chenqiang/COESOT/data/VisEvent/test'
