from lib.test.evaluation.environment import EnvSettings

def local_env_settings():
    settings = EnvSettings()

    # Set your local paths here.

    settings.coesot_path = '/wangx/DATA/Dataset/COESOT'
    #settings.fe108_path = '/media/amax/c08a625b-023d-436f-b33e-9652dc1bc7c0/DATA/chenqiang/COESOT/data/FE108'
    settings.network_path = '/wangx/DATA/Code/chenqiang/PAR/Tracking/CEUTrack/output/test'    # Where tracking networks are stored.
    settings.prj_dir = '/wangx/DATA/Code/chenqiang/Attack/CEUTrack'
    settings.result_plot_path = '/wangx/DATA/Code/chenqiang/PAR/Tracking/CEUTrack/output/test/result_plots'
    settings.results_path = '/wangx/DATA/Code/chenqiang/PAR/Tracking/CEUTrack/output/test/tracking_results'    # Where to store tracking results
    settings.save_dir = '/wangx/DATA/Code/chenqiang/PAR/Tracking/CEUTrack/output'
    settings.segmentation_path = '/wangx/DATA/Code/chenqiang/PAR/Tracking/CEUTrack/output/test/segmentation_results'
    #settings.visevent_path = '/media/amax/c08a625b-023d-436f-b33e-9652dc1bc7c0/DATA/chenqiang/COESOT/data/VisEvent'

    return settings

