import pytest
from unittest.mock import patch, MagicMock
import llm_youtube


@pytest.fixture
def mock_transcript():
    return [
        {
            'text': 'Hello, this is a test transcript.',
            'start': 0.0,
            'duration': 2.5
        },
        {
            'text': 'It contains multiple segments.',
            'start': 2.5,
            'duration': 3.0
        }
    ]


def test_youtube_fragment_loader(mock_transcript):
    with patch('llm_youtube.YouTubeTranscriptApi.get_transcript', return_value=mock_transcript) as mock_get:
        result = llm_youtube.youtube_fragment_loader('test_video_id')
        mock_get.assert_called_once_with('test_video_id')
        
        # Check if the result contains the transcript text
        assert 'Hello, this is a test transcript.' in result
        assert 'It contains multiple segments.' in result
        assert 'https://www.youtube.com/watch?v=test_video_id' in result


def test_register_fragment_loaders():
    # Create a mock register function
    mock_register = MagicMock()
    
    # Call the register_fragment_loaders function with the mock
    llm_youtube.register_fragment_loaders(mock_register)
    
    # Verify that register was called with the correct arguments
    mock_register.assert_called_once_with('yt', llm_youtube.youtube_fragment_loader)


def test_youtube_fragment_loader_error():
    with patch('llm_youtube.YouTubeTranscriptApi.get_transcript', 
              side_effect=Exception('Test error')):
        result = llm_youtube.youtube_fragment_loader('test_video_id')
        assert 'Error fetching transcript' in result
        assert 'Test error' in result 