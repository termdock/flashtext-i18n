"""Test cases for CJK adjacent keyword extraction."""

from flashtext import KeywordProcessor
import unittest


class TestCJKAdjacentKeywords(unittest.TestCase):
    """Test CJK language support for adjacent keywords."""

    def setUp(self):
        self.kp = KeywordProcessor()

    def test_chinese_adjacent_keywords(self):
        """Test adjacent Chinese keywords are both extracted."""
        self.kp.add_keyword('雅詩蘭黛')
        self.kp.add_keyword('小棕瓶')

        text = '推薦雅詩蘭黛小棕瓶超好用'
        result = self.kp.extract_keywords(text)

        self.assertEqual(len(result), 2)
        self.assertIn('雅詩蘭黛', result)
        self.assertIn('小棕瓶', result)

    def test_chinese_adjacent_with_span(self):
        """Test span info is correct for adjacent Chinese keywords."""
        self.kp.add_keyword('蘋果')
        self.kp.add_keyword('香蕉')

        text = '我喜歡蘋果香蕉'
        result = self.kp.extract_keywords(text, span_info=True)

        self.assertEqual(len(result), 2)
        # Verify span positions
        self.assertEqual(result[0][0], '蘋果')
        self.assertEqual(result[1][0], '香蕉')
        # Check that spans are adjacent (no overlap, no gap)
        self.assertEqual(result[0][2], result[1][1])

    def test_three_adjacent_keywords(self):
        """Test three adjacent keywords are all extracted."""
        self.kp.add_keyword('台北')
        self.kp.add_keyword('台中')
        self.kp.add_keyword('台南')

        text = '台北台中台南都是好城市'
        result = self.kp.extract_keywords(text)

        self.assertEqual(len(result), 3)
        self.assertEqual(result, ['台北', '台中', '台南'])

    def test_japanese_adjacent_keywords(self):
        """Test adjacent Japanese keywords."""
        self.kp.add_keyword('東京')
        self.kp.add_keyword('大阪')

        text = '東京大阪間の新幹線'
        result = self.kp.extract_keywords(text)

        self.assertEqual(len(result), 2)
        self.assertIn('東京', result)
        self.assertIn('大阪', result)

    def test_korean_adjacent_keywords(self):
        """Test adjacent Korean keywords."""
        self.kp.add_keyword('서울')
        self.kp.add_keyword('부산')

        text = '서울부산 기차'
        result = self.kp.extract_keywords(text)

        self.assertEqual(len(result), 2)
        self.assertIn('서울', result)
        self.assertIn('부산', result)

    def test_mixed_cjk_and_english(self):
        """Test mixed CJK and English text."""
        self.kp.add_keyword('Python')
        self.kp.add_keyword('機器學習')
        self.kp.add_keyword('深度學習')

        text = 'I use Python做機器學習深度學習'
        result = self.kp.extract_keywords(text)

        self.assertEqual(len(result), 3)
        self.assertEqual(result, ['Python', '機器學習', '深度學習'])

    def test_non_adjacent_still_works(self):
        """Ensure non-adjacent keywords still work correctly."""
        self.kp.add_keyword('咖啡')
        self.kp.add_keyword('茶')

        text = '我喜歡喝咖啡，也喜歡喝茶'
        result = self.kp.extract_keywords(text)

        self.assertEqual(len(result), 2)
        self.assertIn('咖啡', result)
        self.assertIn('茶', result)


if __name__ == '__main__':
    unittest.main()
