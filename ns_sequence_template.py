import hiero


def sequence_template_tracks():
	sequence = hiero.ui.activeSequence()
	log_plates_track_1 = hiero.core.VideoTrack("log plates 1")
	log_plates_track_2 = hiero.core.VideoTrack("log plates 2")
	lin_plates_track_1 = hiero.core.VideoTrack("lin plates 1")
	lin_plates_track_2 = hiero.core.VideoTrack("lin plates 2")
	log_comps_track_1 = hiero.core.VideoTrack("log comps 1")
	log_comps_track_2 = hiero.core.VideoTrack("log comps 2")
	lin_comps_track_1 = hiero.core.VideoTrack("lin comps 1")
	lin_comps_track_2 = hiero.core.VideoTrack("lin comps 2")
	lin_paint_track_1 = hiero.core.VideoTrack("lin paint 1")
	slate_track = hiero.core.VideoTrack("slate")
	spacer_track_1 = hiero.core.VideoTrack("--------")
	spacer_track_2 = hiero.core.VideoTrack("--------")
	spacer_track_3 = hiero.core.VideoTrack("--------")
	spacer_track_4 = hiero.core.VideoTrack("--------")
	spacer_track_5 = hiero.core.VideoTrack("--------")
	sequence.addTrack(spacer_track_1)
	sequence.addTrack(log_plates_track_1)
	sequence.addTrack(log_plates_track_2)
	sequence.addTrack(spacer_track_2)
	sequence.addTrack(lin_plates_track_1)
	sequence.addTrack(lin_plates_track_2)
	sequence.addTrack(spacer_track_3)
	sequence.addTrack(lin_paint_track_1)
	sequence.addTrack(lin_comps_track_1)
	sequence.addTrack(lin_comps_track_2)
	sequence.addTrack(spacer_track_4)
	sequence.addTrack(log_comps_track_1)
	sequence.addTrack(log_comps_track_2)
	sequence.addTrack(spacer_track_5)
	sequence.addTrack(slate_track)



def remove_all_audio_tracks():
	sequence = hiero.ui.activeSequence()
	audio_tracks = [track for track in sequence.audioTracks()]
	for audio_track in audio_tracks:
		sequence.removeTrack(audio_track)
	audio_track = hiero.core.AudioTrack("Audio 1")
	sequence.addTrack(audio_track)

