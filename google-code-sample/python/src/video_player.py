"""A video player class."""
from random import random

from .video_library import VideoLibrary
is_playing = False
pre_video = False
isit_paused = False
is_vid_playing = None
now_playing = "None"

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.is_Playing = False
        self.vid_play_id = "None"

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        videos = self._video_library.get_all_videos()
        print("Here's a list of all available videos:")
        temp_list = []

        for vid in videos:

            # Display tags in required format
            tags = "["
            for tag in vid.tags:
                tags = tags + tag + " "
            tags = tags + "]"

            if tags != "[]":
                tags = tags[0:len(tags) - 2] + "]"

            # Put all videos in a list for sorting
            temp_list += [f"{vid.title} ({vid.video_id}) {tags}"]

        # Sort the list and display
        sorted_list = sorted(temp_list)
        for x in sorted_list:
            print(x)

    def play_video(self, video_id):
        global is_playing
        global pre_video
        global is_vid_playing
        global isit_paused

        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        is_vid_playing = self._video_library.get_video(video_id)

        # warning message
        if not is_vid_playing:
            print(f"Cannot play video: Video does not exist")

        else:
            # something already playing
            if is_playing is True:
                print(f"Stopping video: {pre_video.title}")
                print(f"Playing video: {is_vid_playing.title}")
                pre_video = is_vid_playing
            # nothing already playing
            else:
                print(f"Playing video: {is_vid_playing.title}")
                is_playing = True
                isit_paused = False
                pre_video = is_vid_playing


    def stop_video(self):
        """Stops the current video."""
        global is_playing
        global pre_video
        global is_vid_playing

        # warning message if nothing is playing
        if is_playing:
            print(f"Stopping video: {is_vid_playing.title}")
            is_playing = False
            pre_video = None

        else:
            if not is_playing:
                # something already playing
                print("Cannot stop video: No video is currently playing")
                pre_video = None

    def play_random_video(self):
        """Plays a random video from the video library."""
        global is_playing
        global isit_paused
        global pre_video
        global now_playing

        # all available vids and random select one
        now_playing = random.choice(self._video_library.get_all_videos())

        # no video, so play random video
        if is_playing is False:
            print(f"Playing video: {now_playing.title}")
            is_playing = True
            isit_paused = False
        # check vid is playing, select random video from list
        else:
            print(f"Stopping video: {pre_video.title}")
            print(f"Playing video: {now_playing.title}")
            is_playing = True
            isit_paused = False
        # changing values of variable
        pre_video = now_playing.title

    def pause_video(self):
        """Pauses the current video."""
        global now_playing
        global is_playing
        global pre_video
        global isit_paused

        if is_playing is True:
            # if video is playing and not paused, pause
            if isit_paused == False:
                print(f"Pausing video: {now_playing.title}")
                is_playing = False
                isit_paused = True
        else:
            # if video is not playing, and paused, Paused.
            if isit_paused == True:
                print(f"Video already paused: {now_playing.title}")
                # if video is not playing, paused, and new video playing. ignore previous video's
                # paused status
                if is_vid_playing:
                    print(f"Stopping video: {now_playing.title}")
                    print(f"Playing video: {is_vid_playing.title}")
                    isit_paused = False
                    is_playing = True
        # nothing playing, so error message
        print(f"Cannot pause video: No video is currently playing")

    def continue_video(self):
        """Resumes playing the current video."""


    def show_playing(self):
        """Displays video currently playing."""
        global is_playing
        global now_playing
        global isit_paused

        # check if video is playing. True? then title and tags
        if now_playing and not isit_paused and is_playing:
            print(f"Currently playing: {now_playing.title} ({now_playing.video_id}) {now_playing.tags}")
        # check if video paused. True? add paused after title and tags
        else:
            if isit_paused and now_playing:
                print(f"Currently playing: {now_playing.title} ({now_playing.video_id}) {now_playing.tags} - PAUSED")
            # if no video playing, display warning
            else:
                print("No video is currently playing")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
