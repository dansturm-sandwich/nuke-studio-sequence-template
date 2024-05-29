import hiero


def sequence_template_tracks():
	sequence = hiero.ui.activeSequence()
	plates_track_1 = hiero.core.VideoTrack("plates 1")
	plates_track_2 = hiero.core.VideoTrack("plates 2")
	comps_track_1 = hiero.core.VideoTrack("comps 1")
	comps_track_2 = hiero.core.VideoTrack("comps 2")
	slate_track = hiero.core.VideoTrack("slate")
	spacer_track = hiero.core.VideoTrack("--------")
	sequence.addTrack(spacer_track)
	sequence.addTrack(plates_track_1)
	sequence.addTrack(plates_track_2)
	sequence.addTrack(spacer_track)
	sequence.addTrack(comps_track_1)
	sequence.addTrack(comps_track_2)
	sequence.addTrack(spacer_track)
	sequence.addTrack(slate_track)



def remove_all_audio_tracks():
	sequence = hiero.ui.activeSequence()
	audio_tracks = [track for track in sequence.audioTracks()]
	for audio_track in audio_tracks:
		sequence.removeTrack(audio_track)
	audio_track = hiero.core.AudioTrack("Audio 1")
	sequence.addTrack(audio_track)

