import glob
import os
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("sdmbdf")
args = parser.parse_args()

cwd = os.getcwd().split('/')[-1]
vis      = f'{cwd}.ms'
importasdm(asdm=args.sdmbdf, vis=vis, ocorr_mode='co', with_pointing_correction=True, process_flags=True)
flagdata(vis=vis, mode="shadow")
flagdata(vis=vis, mode="clip", correlation="ABS_ALL", clipzeros=True)
