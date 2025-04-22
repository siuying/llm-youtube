import llm
from youtube_transcript_api import YouTubeTranscriptApi


@llm.hookimpl
def register_fragment_loaders(register):
    register("yt", youtube_fragment_loader)

def youtube_fragment_loader(youtube_id):
    """
    Load a YouTube transcript and return it as text.
    Usage: llm -f yt:VIDEO_ID 'prompt'
    """
    try:
        transcript_list = YouTubeTranscriptApi.get_transcript(youtube_id)
        if not transcript_list:
            return f"No transcript found for YouTube video {youtube_id}"
        
        # Combine all transcript segments into a single text
        transcript_text = "\n".join(
            f"{item['start']:.1f} - {item['start'] + item['duration']:.1f}: {item['text']}"
            for item in transcript_list
        )
        
        return f"Transcript of YouTube video https://www.youtube.com/watch?v={youtube_id}:\n\n{transcript_text}"
    except Exception as e:
        return f"Error fetching transcript for YouTube video {youtube_id}: {str(e)}"
