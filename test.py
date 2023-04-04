from scaper import Scaper
import os

n_soundscapes = 1000
ref_db = -50
duration = 10.0 

min_events = 1
max_events = 9

event_time_dist = 'truncnorm'
event_time_mean = 5.0
event_time_std = 2.0
event_time_min = 0.0
event_time_max = 10.0

source_time_dist = 'const'
source_time = 0.0

event_duration_dist = 'uniform'
event_duration_min = 0.5
event_duration_max = 4.0

snr_dist = 'uniform'
snr_min = 6
snr_max = 30

pitch_dist = 'uniform'
pitch_min = -3.0
pitch_max = 3.0

time_stretch_dist = 'uniform'
time_stretch_min = 0.8
time_stretch_max = 1.2

# create a scaper
sc = Scaper(10.0, "foreground", "background")
sc.protected_labels = []
sc.ref_db = -50

# add background
sc.add_background(label=('const', 'shopping mall'), 
                    source_file=('choose', []), 
                    source_time=('const', 0))

# add random number of foreground events
n_events = 1
for _ in range(n_events):
    sc.add_event(label=('choose', []), 
                    source_file=('choose', []), 
                    source_time=(source_time_dist, source_time), 
                    event_time=(event_time_dist, event_time_mean, event_time_std, event_time_min, event_time_max), 
                    event_duration=(event_duration_dist, event_duration_min, event_duration_max), 
                    snr=(snr_dist, snr_min, snr_max),
                    pitch_shift=(pitch_dist, pitch_min, pitch_max),
                    time_stretch=(time_stretch_dist, time_stretch_min, time_stretch_max),
                    hrir_db=('choose', ['H1', 'H2']),
                    hrir_angle=('choose', [(87,93), (267,273)]))

# generate
audiofile = os.path.join("output", "soundscape_unimodal{:d}.wav".format(1))
jamsfile = os.path.join("output", "soundscape_unimodal{:d}.jams".format(1))
txtfile = os.path.join("output", "soundscape_unimodal{:d}.txt".format(1))

sc.generate(audiofile, jamsfile,
            allow_repeated_label=True,
            allow_repeated_source=False,
            reverb=0.1,
            disable_sox_warnings=True,
            no_audio=False,
            txt_path=txtfile)