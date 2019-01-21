from codec.vid_data import VidData

vid_obj = VidData(dataset="Weizmann")

print(vid_obj._files)

vid_obj.load_data(1)