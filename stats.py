import json
from typing import Dict

import requests
from textblob import TextBlob, download_corpora


class MessageBoardAPIWrapper:
    """
    Wrapper around the messageboard API

    http://localhost:8080/api/
    """

    def __init__(self, base_url: str = "http://localhost:8080"):
        self.base_url = base_url

        result = requests.get(f"{self.base_url}/api/messages/")
        messages = []
        if requests.codes.ok == result.status_code:
            messages = [message["content"] for message in result.json()]
        self.messages = messages

        # Make sure the default tokenizers are downloaded for word/sentence analysis
        try:
            download_corpora.nltk.find("tokenizers/punkt")
        except LookupError:
            download_corpora.nltk.download("punkt")

    def num_messages(self) -> int:
        """
        Returns the total number of messages.
        """

        return len(self.messages)

    def most_common_word(self) -> str:
        """
        Returns the most frequently used word in messages.
        """
        words = TextBlob(" ".join(self.messages))
        return sorted(words.word_counts.items(), key=lambda x: x[1], reverse=True)[0][0]

    def avg_num_words_per_sentence(self) -> float:
        """
        Returns the average number of words per sentence.
        """
        words = TextBlob(" ".join(self.messages))
        return round(len(words.words) / len(words.sentences), 2)

    def avg_num_msg_thread_topic(self) -> Dict[str, float]:
        """
        Returns the average number of messages per thread, per topic.
        """
        raise NotImplementedError

    def _as_dict(self) -> dict:
        """
        Returns the entire messageboard as a nested dictionary.
        """
        raise NotImplementedError

    def to_json(self) -> None:
        """
        Dumps the entire messageboard to a JSON file.
        """
        with open("messageboard.json", "w") as f:
            f.write(json.dumps(self._as_dict(), indent=4))


def main():
    """
    Returns information about the messageboard application
    """

    messageboard = MessageBoardAPIWrapper()

    print(f"Total number of messages: {messageboard.num_messages()}")
    print(f"Most common word: {messageboard.most_common_word()}")
    print(
        f"Avg. number of words per sentence:"
        f"{messageboard.avg_num_words_per_sentence()}"
    )
    print(
        f"Avg. number of messages per thread, per topic:"
        f"{messageboard.avg_num_msg_thread_topic()}"
    )

    messageboard.to_json()
    print("Message Board written to `messageboard.json`")
    return


if __name__ == "__main__":
    main()
