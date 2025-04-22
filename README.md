# llm-youtube

LLM plugin for fetching YouTube video transcripts.

## Installation

Install this plugin in the same environment as [LLM](https://llm.datasette.io/en/stable/).

```bash
llm install git+https://github.com/siuying/llm-youtube
```

## Usage

You can fetch a YouTube video transcript and feed it into LLM using the `yt:` fragment with the video ID. For example:

```bash
llm -f yt:dQw4w9WgXcQ 'summary with illustrative direct quotes'
```

The video ID can be found in the URL of the YouTube video. For example, in the URL `https://www.youtube.com/watch?v=dQw4w9WgXcQ`, the video ID is `dQw4w9WgXcQ`.

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:

```bash
cd llm-youtube
python -m venv venv
source venv/bin/activate
```

Now install the dependencies and test dependencies:

```bash
pip install -e '.[test]'
```

To run the tests:

```bash
python -m pytest
```

## License

Apache License 2.0 